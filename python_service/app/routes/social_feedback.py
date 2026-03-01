from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
import logging
from typing import List, Dict, Optional
import json

from app.utils.ollama import generate_ollama

router = APIRouter()
logger = logging.getLogger(__name__)

class CommentInput(BaseModel):
    id: str
    text: str
    likes: int
    data_publicacao: str

class FeedbackRequest(BaseModel):
    video_id: str
    platform: str
    comments: List[CommentInput]

class FeedbackResponse(BaseModel):
    video_id: str
    audience_insight: str
    sentiment_score: float  # -1.0 a 1.0
    suggested_themes: List[str]

@router.post("/", response_model=FeedbackResponse)
async def process_feedback(req: FeedbackRequest):
    """
    Processa comentários e gera insights qualitativos do público
    """
    logger.info(f"[Feedback] Processando {len(req.comments)} comentários do {req.platform} (Video: {req.video_id})")

    if not req.comments:
        return FeedbackResponse(
            video_id=req.video_id,
            audience_insight=(
                "Sem comentários suficientes no último vídeo para extrair um insight direto. "
                "Continue com a linha editorial principal, mas engaje o público chamando para a discussão."
            ),
            sentiment_score=0.0,
            suggested_themes=[]
        )

    # Ordena comentários por relevância (likes) e pega os 15 melhores para limitar context window
    sorted_comments = sorted(req.comments, key=lambda c: c.likes, reverse=True)[:15]
    comments_text = "\n".join([f"- {c.text} ({c.likes} likes)" for c in sorted_comments])

    prompt = f"""
Você é o Analista Master de Audiência do canal 'Real Futebas'.
Abaixo estão os comentários de maior engajamento do nosso último vídeo sobre futebol.

COMENTÁRIOS:
{comments_text}

Sua tarefa é extrair um 'Audience Insight' acionável para guiar O PRÓXIMO ROTEIRO.
O que nosso público gostou? Do que discordou? Que tipo de pauta eles querem ver mais?

Responda OBRIGATORIAMENTE em JSON válido com esta exata estrutura e chaves curtas:
{{
  "insight": "Resumo de 2 linhas do sentimento da galera e o que abordar no próximo vídeo.",
  "score": 0.8, // -1.0 (ódio generalizado) a 1.0 (sucesso absoluto)
  "temas": ["Nome do jogador 1", "Tática", "Polêmica do jogo"]
}}

Não envie blocos de código markdown nem explicações fora do JSON. Apenas o JSON puro.
"""

    try:
        response_text = await generate_ollama(prompt, model="qwen2.5-coder:7b", fallback_model="llama3")
        # Limpar blocos markdown
        clean_json = response_text.replace("```json", "").replace("```", "").strip()
        data = json.loads(clean_json)

        return FeedbackResponse(
            video_id=req.video_id,
            audience_insight=data.get("insight", "Insight não extraído."),
            sentiment_score=float(data.get("score", 0.0)),
            suggested_themes=data.get("temas", [])
        )
    except json.JSONDecodeError as je:
         logger.error(f"[Feedback] JSON Invalido recebido: {response_text}")
         raise HTTPException(status_code=500, detail="Erro ao parsear output da IA")
    except Exception as e:
        logger.error(f"[Feedback] Erro processando insight: {e}")
        raise HTTPException(status_code=500, detail=str(e))
