import os
import requests
import json
import logging
from dotenv import load_dotenv

# Configura o Logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("n8n_executor")

# Carrega variáveis de ambiente (para URL do Webhook do n8n, se necessário)
load_dotenv()

# Ajuste conforme o Webhook Oficial do seu n8n
# EX: http://localhost:5678/webhook/sua-url-aqui
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "http://localhost:5678/webhook/buffer-news")

def trigger_workflow(sample_data: dict) -> dict:
    """
    Dispara o Workflow Oficial enviando payload JSON. 
    Permite rodar o n8n via Agente sem clicar na UI.
    """
    logger.info(f"Disparando n8n E2E Execution no endpoint: {N8N_WEBHOOK_URL}")
    
    try:
        response = requests.post(
            N8N_WEBHOOK_URL, 
            json=sample_data,
            headers={"Content-Type": "application/json"}
        )
        response.raise_for_status()
        logger.info(f"Pipeline n8n iniciada! Status Code: {response.status_code}")
        
        # Tenta devolver o Job ID se o n8n tiver um node "Respond to Webhook" mapeado
        try:
            return response.json()
        except Exception:
            return {"status_code": response.status_code, "text": response.text}

    except Exception as e:
        logger.error(f"Falha ao iniciar Pipeline n8n: {e}")
        return {"error": str(e)}

if __name__ == "__main__":
    # Exemplo Mock Data (Simula a entrega RSS do FreshRSS)
    sample_news = {
        "title": "Notícia Urgente Mockada para E2E Testing",
        "link": "https://example.com/noticia-mock",
        "description": "Uma quebra brutal nos mercados gerou este teste automatizado pelo AntiGravity-kit.",
        "author": "Mock Author",
        "pubDate": "2026-02-24T12:00:00Z"
    }

    result = trigger_workflow(sample_news)
    print("\n[Resultado do Disparo]")
    print(json.dumps(result, indent=2))
