# =============================================================================
# app/routes/comments.py — Análise de Feedback Social (v13 Sensorial)
# =============================================================================
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional
from app.routes.ai import call_ollama, extract_json

router = APIRouter(prefix="/social", tags=["social"])

class CommentAnalysisRequest(BaseModel):
    comments: List[str]
    current_topic: Optional[str] = "futebol"

@router.post("/analyze-feedback")
async def analyze_social_feedback(req: CommentAnalysisRequest):
    """
    Analisa comentários do YouTube para extrair sentimento e sugestões.
    """
    system = (
        "Você é um Social Media Manager especializado em engajamento de futebol. "
        "Analise os comentários e identifique: 1. Sentimento Geral, 2. Pedidos de novos temas, 3. Críticas construtivas. "
        "JSON: "
        '{"sentiment": "positivo"|"negativo"|"misto", "trending_requests": ["tema 1", "tema 2"], "feedback": "resumo"}'
    )
    prompt = f"Tema Atual: {req.current_topic}\n\nComentários:\n" + "\n".join(req.comments[:20])

    resp = await call_ollama(prompt, system)
    data = extract_json(resp or "{}")
    
    return {
        "status": "sucesso",
        "analysis": data
    }
