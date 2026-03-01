import re
import logging
from typing import Optional, List
from youtube_transcript_api import YouTubeTranscriptApi

logger = logging.getLogger("youtube_transcript")

def extract_video_id(url: str) -> Optional[str]:
    """Extrai o ID do vídeo de uma URL do YouTube."""
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11}).*",
        r"youtu\.be\/([0-9A-Za-z_-]{11})",
        r"youtube\.com\/embed\/([0-9A-Za-z_-]{11})",
        r"youtube\.com\/shorts\/([0-9A-Za-z_-]{11})"
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

def get_transcript(video_id_or_url: str, languages: List[str] = ["pt", "en"]) -> Optional[str]:
    """
    Obtém a transcrição de um vídeo do YouTube.
    
    Args:
        video_id_or_url: ID do vídeo ou URL completa.
        languages: Lista de idiomas preferenciais.
        
    Returns:
        String com a transcrição completa ou None se falhar.
    """
    video_id = extract_video_id(video_id_or_url) or video_id_or_url
    
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        full_text = " ".join([t['text'] for t in transcript_list])
        logger.info("[YouTube Transcript] Transcrição obtida para vídeo %s (%d chars)", video_id, len(full_text))
        return full_text
    except Exception as e:
        logger.warning("[YouTube Transcript] Falha ao obter transcrição para %s: %s", video_id, e)
        return None
