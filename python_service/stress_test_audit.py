import asyncio
import logging
import sys
from pathlib import Path

# Adicionar root ao path para encontrar os módulos
sys.path.append(str(Path(__file__).parent))

from app.services.quality_auditor import quality_auditor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("StressTest")

async def test_single_notion_log():
    logger.info("Iniciando teste de log único no Notion...")
    
    # Simulação de dados de auditoria
    video_url = "https://www.youtube.com/shorts/stress_test_123"
    local_path = "tests/mock_video.mp4"
    transcript = "Este é um vídeo de teste de stress para validar a integração com o painel do Notion."
    title = "Stress Test - Notion Dashboard Integration"
    
    # Como audit_video_quality depende de API real, vamos mockar ou usar run_full_audit direto
    # se a chave do Gemini estiver configurada.
    try:
        results = await quality_auditor.run_full_audit(
            video_url=video_url,
            local_video_path=local_path,
            transcript=transcript,
            title=title
        )
        logger.info(f"Auditoria concluída e enviada ao Notion: {results}")
    except Exception as e:
        logger.error(f"Falha no teste de stress: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_single_notion_log())
