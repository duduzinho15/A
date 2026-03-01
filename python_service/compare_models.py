
import requests
import json
import time

URL = "http://ollama:11434/api/generate"

SYSTEM_PROMPT = """
Você é um torcedor fanático de futebol brasileiro — apaixonado, emotivo, usa gírias como 'rapaziada', 'é nóis', 'que absurdo', 'meu'.
Linguagem direta, coloquial, como um fã falaria no grupo do WhatsApp.

🎬 TIPO DE VÍDEO: Noticia
📋 INSTRUÇÃO DE ESTILO: Factual e direto.

📐 ESTRUTURA OBRIGATÓRIA (AIDA — DURAÇÃO 60s):
  Parte 1 — GANCHO EXPLOSIVO (0-5s): Pergunta retórica OU fato chocante.
  Parte 2 — CONTEXTO E DADOS (5-45s): Fatos reais, placar e estatísticas.
  Parte 3 — IMPACTO E CALLBACK (45-55s): O que isso muda? Feche o Open Loop.
  Parte 4 — CTA (55-65s): Pergunta para comentários + 'siga o Futebas'

📦 SAÍDA: APENAS JSON válido:
{
  "title": "Título IMPACTANTE",
  "blocks": [{"text": "fala do narrador", "type": "speech"}],
  "thumbnail_text": "Texto da capa",
  "hook": "Frase do gancho",
  "cta": "Pergunta para comentários"
}
"""

PROMPT = "📰 NOTÍCIA:\nBi brasileiro, campeão continental e vice mundial: por que Lucas Piccinato caiu no Corinthians? - Bolavip\n\nGere o roteiro seguindo RIGOROSAMENTE a estrutura AIDA acima."

def test_model(model_name):
    print(f"\n--- Testando Modelo: {model_name} ---")
    payload = {
        "model": model_name,
        "prompt": PROMPT,
        "system": SYSTEM_PROMPT,
        "stream": False,
        "format": "json"
    }
    start = time.time()
    try:
        resp = requests.post(URL, json=payload, timeout=120)
        end = time.time()
        if resp.status_code == 200:
            data = resp.json()
            response_text = data.get("response", "")
            print(f"Tempo: {end - start:.2f}s")
            print("Resposta:")
            print(response_text)
            return response_text
        else:
            print(f"Erro {resp.status_code}: {resp.text}")
    except Exception as e:
        print(f"Exception: {e}")
    return None

def run_comparison():
    # Testar Qwen 32b
    qwen_res = test_model("qwen2.5-coder:32b")
    
    # Tentar Mistral-Nemo
    mistral_res = test_model("mistral-nemo")

if __name__ == "__main__":
    run_comparison()
