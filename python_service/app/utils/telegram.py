# =============================================================================
# app/utils/telegram.py - Telegram Bot Integration (Notifications & Fallback)
# =============================================================================
import os
import logging
import requests
from typing import Optional

logger = logging.getLogger("telegram_util")

from app.config import settings

logger = logging.getLogger("telegram_util")

TELEGRAM_TOKEN = settings.TELEGRAM_TOKEN
TELEGRAM_CHAT_ID = settings.TELEGRAM_CHAT_ID

def send_telegram_message(text: str) -> bool:
    """Envia uma mensagem de texto simples para o Telegram."""
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        logger.warning("[Telegram] Token ou Chat ID não configurados no .env")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }

    try:
        resp = requests.post(url, json=payload, timeout=15)
        resp.raise_for_status()
        return True
    except Exception as e:
        logger.error(f"[Telegram] Erro ao enviar mensagem: {e}")
        return False

def send_telegram_video(video_path: str, caption: Optional[str] = None) -> bool:
    """Envia um arquivo de vídeo para o Telegram."""
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        logger.warning("[Telegram] Token ou Chat ID não configurados no .env")
        return False

    if not os.path.exists(video_path):
        logger.error(f"[Telegram] Arquivo de vídeo não encontrado: {video_path}")
        return False

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendVideo"
    
    try:
        with open(video_path, "rb") as video_file:
            files = {"video": video_file}
            data = {
                "chat_id": TELEGRAM_CHAT_ID,
                "caption": caption or "",
                "parse_mode": "Markdown"
            }
            resp = requests.post(url, data=data, files=files, timeout=60)
            resp.raise_for_status()
            logger.info(f"[Telegram] Vídeo enviado com sucesso: {video_path}")
            return True
    except Exception as e:
        logger.error(f"[Telegram] Erro ao enviar vídeo: {e}")
        return False
