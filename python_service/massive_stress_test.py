import asyncio
import httpx
import logging
import time
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s: %(message)s')
logger = logging.getLogger("MassiveStressTest")

SERVICE_URL = "http://localhost:8000"
ENDPOINT = "/video/render"

AUDIO_PATH = "/data_midia/audio/edge_c732a392ce8947f699042cda043d8c11.mp3"

# Dados de teste para 5 vídeos simultâneos
TEST_PAYLOADS = [
    {
        "title": f"Stress Test {i+1} - Renderização Simultânea",
        "audio_path": AUDIO_PATH,
        "assets": [
            {"type": "video", "path": "/data_midia/temp/vid1.mp4", "duration": 3.0},
            {"type": "image", "path": "/data_midia/temp/img1.jpg", "duration": 3.0}
        ],
        "format": "9:16",
        "style": "shorts_viral"
    } for i in range(5)
]

async def trigger_rendering(payload):
    video_title = payload["title"]
    logger.info(f"Disparando renderização: {video_title}")
    
    start_time = time.time()
    try:
        async with httpx.AsyncClient(timeout=600) as client:
            response = await client.post(f"{SERVICE_URL}{ENDPOINT}", json=payload)
            duration = time.time() - start_time
            
            if response.status_code == 200:
                logger.info(f"SUCESSO [{video_title}]: Renderizado em {duration:.2f}s")
                return response.json()
            else:
                logger.error(f"FALHA [{video_title}]: Status {response.status_code} - {response.text}")
                return None
    except Exception as e:
        logger.error(f"ERRO CRÍTICO [{video_title}]: {str(e)}")
        return None

async def run_massive_test():
    logger.info("=== INICIANDO MASSIVE STRESS TEST - 5 VÍDEOS SIMULTÂNEOS ===")
    start_total = time.time()
    
    tasks = [trigger_rendering(p) for p in TEST_PAYLOADS]
    results = await asyncio.gather(*tasks)
    
    total_duration = time.time() - start_total
    success_count = sum(1 for r in results if r is not None)
    
    logger.info("=== RESUMO DO STRESS TEST ===")
    logger.info(f"Total de Vídeos: {len(TEST_PAYLOADS)}")
    logger.info(f"Sucesso: {success_count}")
    logger.info(f"Tempo Total Decorrido: {total_duration:.2f}s")
    logger.info("==============================")

if __name__ == "__main__":
    asyncio.run(run_massive_test())
