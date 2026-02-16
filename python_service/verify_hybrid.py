import requests
import json

URL = "http://localhost:8000/jobs/"

payload = {
  "title": "Teste de Vídeo Híbrido",
  "script": "Nesta simulação, vamos testar a inserção de um clipe de vídeo real no meio das imagens.",
  "type": "Highlight",
  "assets": {
    "all_images": [
        "https://via.placeholder.com/1080x1920?text=Capa+Cutout",
        "https://via.placeholder.com/1080x1920?text=Slide+3"
    ],
    "all_videos": [
        "https://www.w3schools.com/html/mov_bbb.mp4" # Vídeo de teste público
    ],
    "all_news": []
  },
  "config": {
    "slide1": "cutout",
    "slide2": "video_4s_zoom",
    "slide3": "static"
  }
}

try:
    print("Enviando payload para o serviço...")
    response = requests.post(URL, json=payload)
    print(f"Status: {response.status_code}")
    print(f"Resposta: {json.dumps(response.json(), indent=2)}")
except Exception as e:
    print(f"Erro ao conectar: {e}")
