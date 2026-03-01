from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
import logging
import json
import os
import httpx
import requests
from app.services.quality_auditor import quality_auditor
from app.utils.database import get_db_connection

router = APIRouter(prefix="/analytics", tags=["Analytics & E2E"])
logger = logging.getLogger("analytics_routes")

# Webhook Oficial de Produção
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "http://n8n:5678/webhook/buffer-news")

class AuditRequest(BaseModel):
    video_url: str
    job_id: str

@router.post("/test-e2e")
async def trigger_e2e_test():
    """
    Dispara o Workflow Oficial enviando payload JSON MOCK. 
    Ideal para testes de regressão do Agent.
    """
    logger.info(f"Disparando n8n E2E Execution no endpoint: {N8N_WEBHOOK_URL}")
    
    sample_news = {
        "title": "Notícia Urgente Mockada para E2E Testing (Fase 4)",
        "link": "https://example.com/noticia-mock",
        "description": "Uma quebra brutal nos mercados gerou este teste automatizado pelo AntiGravity-kit.",
        "author": "Mock Author",
        "pubDate": "2026-02-24T12:00:00Z"
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                N8N_WEBHOOK_URL,
                json=sample_news,
                timeout=30.0
            )

        if response.status_code >= 400:
            raise HTTPException(status_code=response.status_code, detail=f"Erro no n8n: {response.text}")

        n8n_data = "OK"
        try:
            n8n_data = response.json()
        except Exception:
            n8n_data = response.text

        return {
            "status": "success",
            "message": "Workflow E2E disparado com sucesso!",
            "n8n_response": n8n_data
        }

    except Exception as e:
        logger.error(f"Falha ao iniciar Pipeline n8n E2E: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/audit")
async def run_quality_audit(req: AuditRequest):
    """
    Dispara o Quality Auditor (yt-dlp + LLM Multimodal) 
    num vídeo recém-publicado usando a URL e metadados no DB.
    """
    # Busca Metadados do DB (transcrição e título) baseados no Job ID.
    conn = get_db_connection()
    if not conn:
         raise HTTPException(status_code=500, detail="Database indisponível para Auditoria de Qualidade.")
    
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT ai_log, generated_title 
                FROM video_jobs 
                WHERE id = %s
            """, (req.job_id,))
            
            row = cur.fetchone()
            if not row:
                raise HTTPException(status_code=404, detail=f"Job {req.job_id} não encontrado no banco de dados.")
                
            ai_log_db = row[0] or {}
            title = row[1] or "Video Title Placeholder"
            
            # Tentar achar a transcrição bruta do Script se houver
            transcript = "N/A"
            try:
                if "/ai/script" in ai_log_db:
                    # Parse AI response_preview if available
                    import re
                    match = re.search(r"\{.*\}", ai_log_db["/ai/script"]["response_preview"], re.DOTALL)
                    if match:
                        script_json = json.loads(match.group())
                        transcript = " ".join([b["text"] for b in script_json.get("blocks", [])])
            except:
                 pass
            
            # Passa para o AI Auditor Service
            audit_result = await quality_auditor.audit_video_quality(
                local_video_path="N/A_using_remote_url",
                transcript=transcript, 
                title=title
            )
            
            perf_metrics = quality_auditor.fetch_metrics(req.video_url)
            
            return {
                "status": "success",
                "performance_metrics": perf_metrics,
                "bot_review": audit_result
            }
    finally:
        conn.close()
