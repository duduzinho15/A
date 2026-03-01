from fastapi import APIRouter, HTTPException
import uuid
from pydantic import BaseModel
from typing import List, Optional
from app.utils.database import get_db_connection
import logging
import json

router = APIRouter(prefix="/leads", tags=["leads"])
logger = logging.getLogger("leads")

class LeadCreate(BaseModel):
    title: str
    url: str
    content: Optional[str] = ""
    source: Optional[str] = "freshrss"
    language: Optional[str] = "pt"
    metadata: Optional[dict] = {}

class LeadUpdate(BaseModel):
    status: str
    metadata: Optional[dict] = None

@router.post("/", response_model=dict)
def create_lead(lead: LeadCreate):
    """
    Cria um novo lead de notícia. 
    Garante idempotência pela URL (não permite duplicatas).
    """
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    try:
        with conn.cursor() as cur:
            # Tenta inserir, se a URL já existir apenas retorna o ID existente
            cur.execute("""
                INSERT INTO news_leads (title, url, content, source, language, metadata)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (url) DO UPDATE SET updated_at = CURRENT_TIMESTAMP
                RETURNING id;
            """, (lead.title, lead.url, lead.content, lead.source, lead.language, json.dumps(lead.metadata)))
            
            row = cur.fetchone()
            conn.commit()
            return {"id": str(row['id']), "message": "Lead sync successful"}
    except Exception as e:
        logger.error("Erro ao criar lead: %s", e)
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        conn.close()

@router.get("/pending", response_model=List[dict])
def get_pending_leads(limit: int = 10):
    """Retorna os leads que ainda não foram processados."""
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, title, url, content, source, language, metadata, created_at
                FROM news_leads
                WHERE status = 'pending'
                ORDER BY created_at DESC
                LIMIT %s
            """, (limit,))
            rows = cur.fetchall()
            results = []
            for row in rows:
                r = dict(row)
                # Aliasing para compatibilidade com n8n v13
                r["metadata_assets"] = r["metadata"]
                results.append(r)
            return results
    finally:
        conn.close()

@router.patch("/{lead_id}")
def update_lead_status(lead_id: str, update: LeadUpdate):
    """Atualiza o status de um lead (ex: 'processed', 'rejected')."""
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    try:
        # Validação de UUID para evitar que o banco exploda com "undefined"
        try:
            uuid.UUID(lead_id)
        except (ValueError, AttributeError):
            logger.warning(f"ID de lead inválido recebido: {lead_id}")
            raise HTTPException(status_code=400, detail="ID de lead inválido. Deve ser um UUID.")

        with conn.cursor() as cur:
            if update.metadata:
                cur.execute("""
                    UPDATE news_leads 
                    SET status = %s, metadata = metadata || %s::jsonb, updated_at = CURRENT_TIMESTAMP
                    WHERE id = %s
                """, (update.status, json.dumps(update.metadata), lead_id))
            else:
                cur.execute("""
                    UPDATE news_leads 
                    SET status = %s, updated_at = CURRENT_TIMESTAMP
                    WHERE id = %s
                """, (update.status, lead_id))
            
            conn.commit()
            return {"message": "Status updated"}
    finally:
        conn.close()
@router.get("/{lead_id}", response_model=dict)
def get_lead_detail(lead_id: str):
    """Retorna os detalhes de um lead específico."""
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    
    try:
        # Validação de UUID
        try:
            uuid.UUID(lead_id)
        except (ValueError, AttributeError):
            logger.warning(f"ID de lead inválido solicitado: {lead_id}")
            raise HTTPException(status_code=400, detail="ID de lead inválido. Deve ser um UUID.")

        with conn.cursor() as cur:
            cur.execute("""
                SELECT id, title, url, content, status, source, language, metadata, created_at
                FROM news_leads
                WHERE id = %s
            """, (lead_id,))
            row = cur.fetchone()
            if not row:
                raise HTTPException(status_code=404, detail="Lead not found")
            
            r = dict(row)
            r["metadata_assets"] = r["metadata"]
            return r
    finally:
        conn.close()
