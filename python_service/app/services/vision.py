# =============================================================================
# app/services/vision.py — Sensorial e Detecção de Destaques (v13 IA Vision)
# =============================================================================
import re
import logging
from typing import List, Dict, Any
from app.routes.ai import call_ollama, extract_json

logger = logging.getLogger("vision_service")

class HighlightDetector:
    """
    Motor que 'enxerga' momentos de alta intensidade no conteúdo.
    Focado em transcrições (NLP Vision) e metadados visuais.
    """

    # Termos que indicam alta intensidade emocional/visual em futebol
    INTENSITY_KEYWORDS = [
        r"gooo+l", r"golasso", r"golaço", r"espetacular", r"inacreditável",
        r"falhou", r"frango", r"expulso", r"cartão vermelho", r"var",
        r"pênalti", r"penalidade", r"mão na bola", r"mordeu"
    ]

    @staticmethod
    async def find_intense_moments(transcript: str) -> List[Dict[str, Any]]:
        """
        Analisa a transcrição para encontrar timestamps de alta intensidade.
        Útil para selecionar clips de B-roll ou highlights.
        """
        highlights = []
        
        # 1. Heurística de Expressões Regulares
        for pattern in HighlightDetector.INTENSITY_KEYWORDS:
            matches = re.finditer(pattern, transcript, re.IGNORECASE)
            for m in matches:
                highlights.append({
                    "type": "emotion",
                    "term": m.group(),
                    "position": m.start() / len(transcript) # Posição relativa 0-1
                })

        # 2. Análise via LLM (opcional se transcript for curto)
        if len(transcript) > 100 and len(transcript) < 5000:
            system = (
                "Você é um editor de vídeo esportivo. "
                "Dada a transcrição, identifique os 3 momentos mais 'visuais' ou 'emocionantes'. "
                "Responda APENAS JSON: [{\"moment\": \"desc\", \"reason\": \"...\"}]"
            )
            resp = await call_ollama(transcript[:2000], system)
            llm_moments = extract_json(resp or "[]")
            if isinstance(llm_moments, list):
                for m in llm_moments:
                    highlights.append({
                        "type": "llm_detected",
                        "moment": m.get("moment"),
                        "reason": m.get("reason")
                    })

        logger.info("[Vision] %d momentos de destaque detectados.", len(highlights))
        return highlights

    @staticmethod
    def rank_images_by_vibrancy(image_paths: List[str]) -> List[str]:
        """
        (Futuro) Ordena imagens por 'vibração' visual (brilho, saturação, rostos).
        Por enquanto remove caminhos inválidos.
        """
        import os
        return [p for p in image_paths if os.path.exists(p)]

# Instância Global
vision_engine = HighlightDetector()
