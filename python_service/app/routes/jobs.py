# =============================================================================
# app/routes/jobs.py — Gestão de Estado e Fila de Produção
# =============================================================================
from fastapi import APIRouter, HTTPException, Query, BackgroundTasks
from pydantic import BaseModel, HttpUrl
from typing import Optional, List, Union, Any
from app.utils.database import get_db_connection
from app.services import video_engine
from psycopg2.errors import UniqueViolation
import uuid

router = APIRouter(prefix="/jobs", tags=["jobs"])

class AssetsModel(BaseModel):
    all_images: List[str] = []
    all_videos: List[str] = []
    all_news: List[dict] = []

class ConfigModel(BaseModel):
    slide1: Optional[str] = "cutout"
    slide2: Optional[str] = "video_4s_zoom"
    slide3: Optional[str] = "static"

class JobCreate(BaseModel):
    title: str
    script: Union[str, dict, Any]
    type: str  # "Highlight" ou "Noticia"
    assets: AssetsModel
    config: ConfigModel
    # Novos campos opcionais na criação
    formato: Optional[str] = None
    regiao: Optional[str] = None
    agregacao: Optional[str] = None
    pub_date: Optional[str] = None # ISO format str
    source_url: Optional[str] = None # Para idempotência (URL do RSS)

class JobUpdate(BaseModel):
    status: Optional[str] = None
    title: Optional[str] = None
    audio_path: Optional[str] = None
    video_path: Optional[str] = None
    thumbnail_path: Optional[str] = None
    metadata: Optional[dict] = None
    error_message: Optional[str] = None
    # Updates SEO
    formato: Optional[str] = None
    regiao: Optional[str] = None
    metadata_post: Optional[dict] = None
    published: Optional[bool] = None

# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.post("/", status_code=201)
async def create_job(job: JobCreate, background_tasks: BackgroundTasks):
    """Cria um novo job de vídeo e inicia o processamento híbrido."""
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Erro de conexão com o banco.")
    
    # 1. Filtro de Notícias Antigas (48h)
    if job.pub_date:
        try:
            from datetime import datetime, timedelta, timezone
            # Assuming ISO format from n8n
            pub_dt = datetime.fromisoformat(job.pub_date.replace('Z', '+00:00'))
            now = datetime.now(timezone.utc)
            if (now - pub_dt) > timedelta(hours=48):
                return {"status": "skipped", "reason": "Content too old (>48h)", "job_id": None}
        except Exception as e:
            print(f"[Jobs] Erro ao validar data: {e}")

    # 2. Idempotência: Verifica se source_url já existe
    # Se o cliente enviou um source_url (do RSS), usamos ele. Senão, geramos um.
    final_source_url = job.source_url if hasattr(job, 'source_url') and job.source_url else f"hybrid://{uuid.uuid4().hex[:12]}"
    
    # Check DB existence
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, status FROM video_jobs WHERE source_url = %s", (final_source_url,))
            existing = cur.fetchone()
            if existing:
                print(f"[Jobs] Idempotência: Job {existing['id']} já existe (Status: {existing['status']}). Retornando existente.")
                return {"status": "existing", "job_id": str(existing['id']), "job_status": existing['status']}
    except Exception as e:
        print(f"[Jobs] Erro ao checar existência: {e}")

    try:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO video_jobs (
                    source_url, title, status, metadata, 
                    formato, regiao, agregacao, pub_date
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (
                final_source_url, 
                job.title, 
                "processing", 
                job.model_dump_json(),
                job.formato or "shorts", # Default to shorts if None
                job.regiao,
                job.agregacao,
                job.pub_date,
            ))
            new_id = cur.fetchone()['id']
            conn.commit()
            
            # Inicia o motor de vídeo em background (passa ID como string)
            background_tasks.add_task(video_engine.generate_video, str(new_id), job.model_dump())
            
            return {"status": "created", "job_id": str(new_id)}
    except UniqueViolation:
        # Race condition catch
        conn.rollback()
        return {"status": "existing", "msg": "Race condition detected, job likely created."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar job: {str(e)}")
    finally:
        conn.close()



@router.patch("/{job_id}")
async def update_job(job_id: str, update: JobUpdate):
    """Atualiza o estado de um job."""
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Erro de conexão com o banco.")
    
    try:
        with conn.cursor() as cur:
            # Montagem dinâmica da query
            fields = []
            values = []
            
            for k, v in update.model_dump(exclude_unset=True).items():
                if k in ['metadata', 'metadata_post']:
                    import json
                    fields.append(f"{k} = {k} || %s::jsonb") # Merge JSONB
                    values.append(json.dumps(v))
                else:
                    fields.append(f"{k} = %s")
                    values.append(v)
            
            if not fields:
                return {"status": "no_changes"}

            fields.append("updated_at = CURRENT_TIMESTAMP")
            if update.status == 'error':
                fields.append("retry_count = retry_count + 1")

            query = f"UPDATE video_jobs SET {', '.join(fields)} WHERE id = %s"
            values.append(job_id)
            
            cur.execute(query, tuple(values))
            conn.commit()
            return {"status": "updated"}
    finally:
        conn.close()

@router.get("/")
async def list_jobs(status: Optional[str] = None, limit: int = 20):
    """Lista os jobs recentes."""
    conn = get_db_connection()
    if not conn: return []
    try:
        with conn.cursor() as cur:
            query = "SELECT * FROM video_jobs"
            params = []
            if status:
                query += " WHERE status = %s"
                params.append(status)
            query += " ORDER BY created_at DESC LIMIT %s"
            params.append(limit)
            
            cur.execute(query, tuple(params))
            return cur.fetchall()
    finally:
        conn.close()

@router.get("/check")
async def check_url(url: str):
    """Verifica se uma URL já foi processada/está em processamento."""
    conn = get_db_connection()
    if not conn: return {"exists": False}
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, status, created_at FROM video_jobs WHERE source_url = %s", (url,))
            job = cur.fetchone()
            return {"exists": bool(job), "job": job}
    finally:
        conn.close()

@router.get("/{job_id}")
async def get_job(job_id: str):
    """Retorna os detalhes de um job específico."""
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Erro de conexão com o banco.")
    
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM video_jobs WHERE id = %s", (job_id,))
            job = cur.fetchone()
            
            if not job:
                raise HTTPException(status_code=404, detail="Job não encontrado.")
                
            return job
    finally:
        conn.close()


