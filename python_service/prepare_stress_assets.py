import asyncio
import httpx
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AssetPrep")

SERVICE_URL = "http://localhost:8000"

async def prepare_assets():
    logger.info("Preparando assets para o Stress Test...")
    
    # 1. Gerar Áudio de Teste
    audio_payload = {
        "text": "Este é um áudio de teste para o massive stress test do sistema auto content factory.",
        "style": "shorts"
    }
    
    async with httpx.AsyncClient(timeout=60.0) as client:
        logger.info("Gerando áudio via API...")
        resp = await client.post(f"{SERVICE_URL}/audio/", json=audio_payload)
        if resp.status_code == 200:
            audio_path = resp.json()["audio_path"]
            logger.info(f"Áudio gerado em: {audio_path}")
        else:
            logger.error(f"Falha ao gerar áudio: {resp.text}")
            return

    # 2. Criar um clipe de B-roll fake (Vídeo preto de 5s) se não houver Pexels
    # Mas como queremos stress real, vamos tentar baixar um clipe via yt-dlp ou similar
    # Para simplificar e garantir, criaremos um script que baixa um vídeo curto do Pexels
    
    logger.info("Pronto para o Stress Test.")

if __name__ == "__main__":
    asyncio.run(prepare_assets())
