# =============================================================================
# app/routes/media.py — Fallback de Vídeos e Imagens
# =============================================================================
# - ScoreBat: Thumbnails de alta qualidade e Vídeos.
# - Reddit: Scraper de Gols (r/soccer).
# =============================================================================

from fastapi import APIRouter
from pydantic import BaseModel
import requests
from typing import List, Optional
from app.services.youtube_transcript import get_transcript

router = APIRouter(prefix="/media", tags=["media"])

# ---------------------------------------------------------------------------
# Configuração
# ---------------------------------------------------------------------------
SCOREBAT_TOKEN = "Mjc1OTAwXzE3NzA2MTI3MDNfMjI1ZTIyNzk3YWY1YTI0MmVhMTAwNmY0ZGE4Yjk4ZGMwNWM0N2Y4Yw=="
HEADERS_REDDIT = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------
class ScoreBatRequest(BaseModel):
    team1: str
    team2: str

class ScoreBatResponse(BaseModel):
    title: str
    thumbnail: str
    video_embed: str
    match_url: str
    found: bool

class RedditRequest(BaseModel):
    query: str # Ex: "Chelsea vs Manchester"

class RedditResponse(BaseModel):
    videos: list[dict] # [{title:..., url:...}]

class YouTubeTranscriptRequest(BaseModel):
    url: str
    languages: list[str] = ["pt", "en"]

class YouTubeTranscriptResponse(BaseModel):
    status: str
    transcript: Optional[str] = None
    error: Optional[str] = None

class MediaProcessRequest(BaseModel):
    action: str
    original_msg: str

@router.post("/process")
async def process_media(payload: MediaProcessRequest):
    """
    Acionado pelo Telegram Callback Handler para iniciar o processamento de um conteúdo aprovado.
    """
    print(f"[Media] Iniciando processamento: {payload.action} para {payload.original_msg[:50]}...")
    
    # Aqui dispararíamos o fluxo de roteirização/renderização.
    # Por enquanto, retornamos sucesso para validar a integração do n8n.
    return {
        "status": "sucesso",
        "message": f"Ação {payload.action} recebida e em processamento.",
        "original_msg_preview": payload.original_msg[:100]
    }

@router.post("/scorebat", response_model=ScoreBatResponse)
async def get_scorebat_media(payload: ScoreBatRequest):
    """
    Busca highlights no ScoreBat API (Free Feed).
    """
    url = f"https://www.scorebat.com/video-api/v3/free-feed/?token={SCOREBAT_TOKEN}"
    
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            data = r.json()
            matches = data.get('response', [])
            
            t1 = payload.team1.lower()
            t2 = payload.team2.lower()
            
            for match in matches:
                title = match['title'].lower()
                # Verifica se ambos os times estao no titulo (busca simples)
                if t1 in title and t2 in title:
                    videos = match.get('videos', [])
                    embed = videos[0].get('embed', '') if videos else ''
                    
                    return ScoreBatResponse(
                        title=match['title'],
                        thumbnail=match['thumbnail'],
                        video_embed=embed,
                        match_url=match.get('matchviewUrl', ''),
                        found=True
                    )
            
            # Fallback: Tenta encontrar qualquer jogo que envolva um dos times
            # (Para nao retornar vazio em jogos futuros ou sem highlight especifico)
            for match in matches:
                title = match['title'].lower()
                # Verifica se pelo menos UM time esta no titulo
                if t1 in title or t2 in title:
                     videos = match.get('videos', [])
                     embed = videos[0].get('embed', '') if videos else ''
                     return ScoreBatResponse(
                        title=match['title'],
                        thumbnail=match['thumbnail'],
                        video_embed=embed,
                        match_url=match.get('matchviewUrl', ''),
                        found=True
                    )
            
    except Exception as e:
        print(f"[ScoreBat] Erro: {e}")
        
    return ScoreBatResponse(title="", thumbnail="", video_embed="", match_url="", found=False)


@router.post("/reddit", response_model=RedditResponse)
async def get_reddit_goals(payload: RedditRequest):
    """
    Busca gols no Reddit (r/soccer).
    """
    # Clean query and make it specific
    # Ex: "Girona x Barcelona" -> "Girona" "Barcelona" (para evitar match parcial de "Barcelona" em "Barcelona SC")
    terms = payload.query.replace(' x ', ' ').replace(' vs ', ' ').replace(' - ', ' ').split(' ')
    refined_query = ""
    for term in terms:
        if len(term) > 3:
            refined_query += f'"{term}" '
            
    if not refined_query:
        refined_query = payload.query
        
    url = f"https://www.reddit.com/r/soccer/search.json?q={refined_query}+flair:Media&restrict_sr=1&sort=new&limit=10"
    
    found_videos = []
    
    try:
        r = requests.get(url, headers=HEADERS_REDDIT, timeout=10)
        if r.status_code == 200:
            data = r.json()
            posts = data.get('data', {}).get('children', [])
            
            for post in posts:
                p_data = post['data']
                title = p_data.get('title', '')
                url_video = p_data.get('url', '')
                
                # Basic domain filter
                if any(x in url_video for x in ['streambug', 'dubz', 'streamin', 'twitter', 'vpa.qq', 'youtube', 'youtu.be']):
                     found_videos.append({'title': title, 'url': url_video})
                     
        return RedditResponse(videos=found_videos)

    except Exception as e:
        print(f"[Reddit] Erro: {e}")
        return RedditResponse(videos=[])

@router.post("/youtube-transcript", response_model=YouTubeTranscriptResponse)
async def youtube_transcript(payload: YouTubeTranscriptRequest):
    """
    Extrai a transcrição de um vídeo do YouTube.
    """
    transcript = get_transcript(payload.url, languages=payload.languages)
    if transcript:
        return YouTubeTranscriptResponse(status="sucesso", transcript=transcript)
    return YouTubeTranscriptResponse(status="erro", error="Não foi possível obter a transcrição.")
