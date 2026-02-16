# =============================================================================
# app/routes/download.py — Endpoint de download de vídeos
# =============================================================================
# Substitui o uso de yt-dlp dentro do n8n.
# Baixa vídeos para /data_midia para serem usados na montagem.
# =============================================================================

from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl
import yt_dlp
import os
import uuid
from app.utils.errors import ServicoExterno

router = APIRouter(prefix="/download", tags=["download"])

# Diretório onde os vídeos serão salvos (volume compartilhado)
OUTPUT_DIR = "/data_midia"

class DownloadRequest(BaseModel):
    url: HttpUrl
    qualidade: str = "best"  # best, worst, 720p, etc.

class DownloadResponse(BaseModel):
    status: str
    arquivo: str
    titulo: str
    duracao: int
    meta: dict

@router.post("/", response_model=DownloadResponse, summary="Baixa vídeo do YouTube/Redes Sociais")
async def baixar_video(dados: DownloadRequest):
    url = str(dados.url)
    video_id = str(uuid.uuid4())[:8]
    template_saida = os.path.join(OUTPUT_DIR, f"video_{video_id}.%(ext)s")

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Tenta melhor qualidade
        'outtmpl': template_saida,
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
        # 'cookiefile': '/app/cookies.txt' # Futuro: se precisar de cookies
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # 1. Extrair info primeiro
            info = ydl.extract_info(url, download=True)
            
            # Pega o nome do arquivo gerado
            # yt-dlp pode mudar a extensão (mkv, mp4), então precisamos achar o arquivo
            filename = ydl.prepare_filename(info)
            
            # Se o arquivo não existir com o nome exato (as vezes merge muda), tenta achar
            if not os.path.exists(filename):
                # Fallback simples: lista diretório e acha o arquivo com ID
                for f in os.listdir(OUTPUT_DIR):
                    if video_id in f:
                        filename = os.path.join(OUTPUT_DIR, f)
                        break

            return {
                "status": "sucesso",
                "arquivo": filename,
                "titulo": info.get('title', 'Sem titulo'),
                "duracao": info.get('duration', 0),
                "meta": {
                    "uploader": info.get('uploader'),
                    "views": info.get('view_count')
                }
            }

    except Exception as e:
        raise ServicoExterno(f"Erro ao baixar vídeo: {str(e)}", url=url)
