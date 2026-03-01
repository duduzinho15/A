
import requests
import json
import time

URL = "http://ollama:11434/api/chat"

SYSTEM_PROMPT = """
Você é um torcedor fanático de futebol brasileiro — apaixonado, emotivo, usa gírias como 'rapaziada', 'é nóis', 'que absurdo', 'meu'.
Linguagem direta, coloquial, como um fã falaria no grupo do WhatsApp.

🎬 TIPO DE VÍDEO: Noticia
📋 INSTRUÇÃO DE ESTILO: Factual e direto.

📦 SAÍDA: APENAS JSON válido:
{
  "title": "Título IMPACTANTE",
  "blocks": [{"text": "fala do narrador", "type": "speech"}],
  "thumbnail_text": "Texto da capa",
  "hook": "Frase do gancho",
  "cta": "Pergunta para comentários"
}
"""

PROMPT = "📰 NOTÍCIA:\nBi brasileiro, campeão continental e vice mundial: por que Lucas Piccinato caiu no Corinthians? - Bolavip"

def test_model(model_name):
    print(f"\n--- Testando Modelo: {model_name} ---")
    payload = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": PROMPT}
        ],
        "stream": False,
        "format": "json"
    }
    start = time.time()
    try:
        resp = requests.post(URL, json=payload, timeout=60)
        end = time.time()
        if resp.status_code == 200:
            data = resp.json()
            response_text = data.get("message", {}).get("content", "")
            print(f"Tempo: {end - start:.2f}s")
            print("Resposta (Preview):", response_text[:200] + "...")
            return response_text
        else:
            print(f"Erro {resp.status_code}: {resp.text}")
    except Exception as e:
        print(f"Exception: {e}")
    return None

def run_comparison():
    models_to_test = [
        "qwen2.5-coder:7b",
        "llama3.2:latest"
    ]
    results = {}
    for m in models_to_test:
        res = test_model(m)
        if res:
            print(f"\n[RESULTADO COMPLETO - {m}]")
            print(res)
            results[m] = res
    
    print("\n--- RESUMO FINAL ---")
    for m, res in results.items():
        status = "OK ✅" if res else "FALHA ❌"
        print(f"{m}: {status}")

if __name__ == "__main__":
    run_comparison()

if __name__ == "__main__":
    run_comparison()
