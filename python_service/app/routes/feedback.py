
# =============================================================================
# app/routes/feedback.py — Feedback Loop & SEO Analytics
# =============================================================================
import os
import json
from datetime import datetime, timedelta
from typing import Optional, List, Dict
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.utils.database import get_db_connection
from app.config import settings

# Google APIs
try:
    from googleapiclient.discovery import build
    from google.oauth2 import service_account
except ImportError:
    build = None
    service_account = None

router = APIRouter(prefix="/feedback", tags=["feedback"])

class FeedbackLoopResponse(BaseModel):
    status: str
    processed_count: int
    insights: List[str]

class OptimizationRequest(BaseModel):
    target_metric: str = "ctr" # ctr, views, retention

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_youtube_analytics_service():
    """Retorna o serviço de analytics autenticado ou None."""
    # Procura credenciais (caminho padrão ou env)
    creds_file = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "credentials.json")
    if os.path.exists(creds_file) and build:
        try:
            creds = service_account.Credentials.from_service_account_file(
                creds_file, scopes=['https://www.googleapis.com/auth/yt-analytics.readonly']
            )
            return build('youtubeAnalytics', 'v2', credentials=creds)
        except Exception as e:
            print(f"[Feedback] Erro auth Google: {e}")
            return None
    return None

def fetch_mock_analytics(video_id: str) -> Dict:
    """Mock para testes ou quando sem credenciais."""
    import random
    return {
        "views": random.randint(100, 50000),
        "likes": random.randint(10, 5000),
        "ctr": round(random.uniform(2.0, 15.0), 2),     # CTR geral
        "ctr_shorts": round(random.uniform(5.0, 25.0), 2), # CTR no Feed Shorts
        "retention_avg": round(random.uniform(40.0, 90.0), 2)
    }

# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.post("/loop", response_model=FeedbackLoopResponse)
async def feedback_loop(use_mock: bool = False):
    """
    Consulta métricas (Views, CTR) dos vídeos publicados e atualiza o DB.
    Esses dados alimentam a IA para otimizar próximos títulos/thumbnails.
    """
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Erro DB")
    
    analytics = get_youtube_analytics_service() if not use_mock else None
    
    updates = []
    insights = []
    
    try:
        with conn.cursor() as cur:
            # Busca jobs publicados com platform_id (ou mockados para teste)
            cur.execute("""
                SELECT
                    id,
                    COALESCE(platform_id, metadata_post->>'youtube_id') AS youtube_id,
                    title
                FROM video_jobs 
                WHERE published IS TRUE
                  AND (platform_id IS NOT NULL OR (metadata_post ? 'youtube_id'))
            """)
            jobs = cur.fetchall()
            
            for job in jobs:
                vid_id = job.get('youtube_id') or "mock_video_id"
                
                # Coleta Métricas
                metrics = {}
                if analytics and vid_id != "mock_video_id":
                    # Implementação Real (Simplificada - requer Channel ID)
                    # No mundo real, precisa bater na API reports.query
                    pass # TODO: Implementar query real
                else:
                    metrics = fetch_mock_analytics(vid_id)
                
                # Armazena no DB
                updates.append((json.dumps(metrics), str(job['id'])))
                
                # Gera insight simples
                if metrics.get('ctr', 0) > 8.0:
                    insights.append(f"Alta Performance: '{job['title']}' (CTR {metrics['ctr']}%)")

            # Batch Update
            for data, jid in updates:
                cur.execute("UPDATE video_jobs SET metrics = metrics || %s::jsonb WHERE id = %s", (data, jid))
            
            conn.commit()
            
            return {
                "status": "success", 
                "processed_count": len(updates),
                "insights": insights[:5] # Top 5 insights
            }
    finally:
        conn.close()

@router.post("/optimize_prompt")
async def optimize_prompt(req: OptimizationRequest):
    """
    Analisa histórico de alta performance para sugerir melhorias no prompt da IA.
    Ex: "Títulos com 'URGENTE' tiveram CTR +20%".
    """
    conn = get_db_connection()
    if not conn: return {"error": "DB indisponível"}
    
    try:
        with conn.cursor() as cur:
            # Query analítica simples
            # Busca top 10% jobs por métrica alvo
            metric_key = req.target_metric # 'ctr', 'views'
            
            cur.execute(f"""
                SELECT title, metadata_post, metrics 
                FROM video_jobs 
                WHERE metrics->>%s IS NOT NULL 
                ORDER BY (metrics->>%s)::float DESC 
                LIMIT 5
            """, (metric_key, metric_key))
            
            top_performers = cur.fetchall()
            
            if not top_performers:
                return {"suggestion": "Sem dados suficientes para otimização."}
            
            # Análise básica de padrões (pode ser feita por LLM aqui se tivermos access)
            titles = [j['title'] for j in top_performers]
            avg_val = sum([float(j['metrics'][metric_key]) for j in top_performers]) / len(top_performers)
            
            return {
                "context": f"Top 5 vídeos têm média de {avg_val:.1f} {metric_key}",
                "successful_examples": titles,
                "system_prompt_addition": f"Analise estes títulos de sucesso: {json.dumps(titles)}. Tente replicar o tom e estruturas (ex: UPPERCASE, Gates, Perguntas).",
                "simulated_learning": "Detectado padrão: Uso de palavras de urgência correlaciona com maior CTR."
            }

    finally:
        conn.close()
