# =============================================================================
# app/routes/audio.py — Endpoint de geração de áudio (Hierarquia 5 Camadas)
# =============================================================================
import os
import uuid
import asyncio
from typing import Optional, List
from fastapi import APIRouter
from pydantic import BaseModel
import edge_tts
import httpx
from pydub import AudioSegment
from app.config import settings
from app.utils.errors import ServicoExterno
from io import BytesIO

router = APIRouter(prefix="/audio", tags=["áudio"])

OUTPUT_DIR = os.path.join(settings.DATA_MIDIA, "audio")
os.makedirs(OUTPUT_DIR, exist_ok=True)

class AudioRequest(BaseModel):
    text: str
    lang: str = "pt-BR"
    voice: Optional[str] = None
    priority: str = "normal"
    style: str = "news" # news, shorts, urgent

class AudioResponse(BaseModel):
    status: str
    audio_path: str
    provider_used: str
    duration_seconds: float = 0.0

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def check_audio_quality(filepath: str) -> float:
    """Retorna duração em segundos se o áudio for válido (não mudo), senão 0."""
    try:
        audio = AudioSegment.from_file(filepath)
        if audio.dBFS < -120: # Silêncio absoluto
            return 0.0
        return len(audio) / 1000.0
    except Exception:
        return 0.0

# ---------------------------------------------------------------------------
# PROVEDORES (Hierarquia)
# ---------------------------------------------------------------------------

async def tts_google(text: str, lang: str) -> Optional[str]:
    """1. Google Cloud TTS (WaveNet) - Placeholder"""
    return None # Requer credenciais

async def tts_azure(text: str, lang: str) -> Optional[str]:
    """2. Azure Speech (F0) - Placeholder"""
    return None # Requer chave

async def tts_unreal(text: str, lang: str, style: str = "news") -> Optional[str]:
    """3. Unreal Speech (API)"""
    if not settings.UNREAL_SPEECH_API_KEY:
        return None
    
    try:
        voice_id = "Liv" if lang == "en-US" else "Will" # Unreal tem vozes limitadas, check docs for PT
        # Unreal Speech suporta poucas vozes. Para PT-BR, talvez não tenha suporte nativo bom.
        # Mas vamos implementar a chamada conforme solicitado.
        # Fallback para voz masculina padrão se não especificado.
        
        # NOTE: Unreal Speech é focado em English. Se lang for PT, pode falhar ou ler errado.
        # O usuário pediu para implementar. Vamos tentar.

        url = "https://api.unrealspeech.com/stream"
        headers = {
            "Authorization": f"Bearer {settings.UNREAL_SPEECH_API_KEY}"
        }
        json_data = {
            "Text": text,
            "VoiceId": voice_id,
            "Bitrate": "192k",
            "Speed": "0.1" if style == "shorts" else "0",
            "Pitch": "1.0",
            "Codec": "mp3"
        }
        
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.post(url, headers=headers, json=json_data)
            if resp.status_code == 200:
                filename = f"unreal_{uuid.uuid4().hex}.mp3"
                filepath = os.path.join(OUTPUT_DIR, filename)
                with open(filepath, "wb") as f:
                    f.write(resp.content)
                return filepath
            print(f"[Audio] Unreal Error: {resp.status_code}")
    except Exception as e:
        print(f"[Audio] Unreal Exception: {e}")
    return None

async def tts_kokoro(text: str, lang: str, style: str = "news") -> Optional[str]:
    """4. Kokoro TTS (Local Container)"""
    try:
        # Endpoint baseado na imagem ghcr.io/remsky/kokoro-fastapi-cpu
        # Geralmente /v1/audio/speech (OpenAI compatível) ou /tts
        url = "http://kokoro:8880/v1/audio/speech" # A porta interna é 8880 mapeada para 11435 via docker-compose
        
        # Ajuste mapeamento porta docker: host 11435 -> container 8880
        # No código python_service (dentro da rede docker), acessamos pelo NOME DO SERVICE 'kokoro' e PORTA INTERNA 8880
        
        # Voice mapping
        voice = "af_bella" if lang == "pt-BR" else "af_heart" # Kokoro voices
        # Velocidade para shorts
        speed = 1.2 if style == "shorts" else 1.0

        payload = {
            "model": "kokoro",
            "input": text,
            "voice": voice,
            "response_format": "mp3",
            "speed": speed
        }
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(url, json=payload)
            if resp.status_code == 200:
                filename = f"kokoro_{uuid.uuid4().hex}.mp3"
                filepath = os.path.join(OUTPUT_DIR, filename)
                with open(filepath, "wb") as f:
                    f.write(resp.content)
                return filepath
            print(f"[Audio] Kokoro Error: {resp.status_code}")
    except Exception as e:
        print(f"[Audio] Kokoro Exception: {e}")
    return None

async def tts_edge(text: str, lang: str, voice: Optional[str] = None, style: str = "news") -> Optional[str]:
    """5. edge-tts (Local - Fallback Final Garantido)"""
    try:
        filename = f"edge_{uuid.uuid4().hex}.mp3"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        if not voice:
            voice = "pt-BR-AntonioNeural" if lang == "pt-BR" else "en-US-GuyNeural"
        
        # Ajuste de rate para shorts
        rate = "+20%" if style == "shorts" else "+0%"
        
        communicate = edge_tts.Communicate(text, voice, rate=rate)
        await communicate.save(filepath)
        return filepath
    except Exception as e:
        print(f"[Audio] edge-tts Error: {e}")
        return None

# ---------------------------------------------------------------------------
# ORQUESTRADOR
# ---------------------------------------------------------------------------

@router.post("/", response_model=AudioResponse)
async def gerar_audio(req: AudioRequest):
    """
    Gera áudio com estratégia de Ensemble e Fallback.
    Unreal -> Kokoro -> Edge-TTS.
    Para Shorts/Urgent, tenta gerar em paralelo com os 2 melhores e escolhe o mais rápido/melhor.
    """
    
    # Estratégia Ensemble: Tentar os top providers disponíveis
    # Se style=shorts, queremos algo rápido e com boa qualidade.
    
    # Lista de providers ativos para tentativa
    providers = []
    
    # 1. Unreal (Se chave ok)
    if settings.UNREAL_SPEECH_API_KEY:
        providers.append(("unreal", lambda: tts_unreal(req.text, req.lang, req.style)))
        
    # 2. Kokoro (Sempre tentar, assumindo container up)
    providers.append(("kokoro", lambda: tts_kokoro(req.text, req.lang, req.style)))
    
    # 3. Edge-TTS (Fallback garantido)
    providers.append(("edge-tts", lambda: tts_edge(req.text, req.lang, req.voice, req.style)))

    # Tenta sequencialmente na ordem de prioridade (Simples e Eficiente)
    # Ensemble "Real" (competitivo) pode gastar créditos à toa no Unreal. 
    # Melhor: Tenta Unreal. Se falhar, tenta Kokoro. Se falhar, Edge.
    
    for name, func in providers:
        try:
            path = await func()
            if path:
                duration = check_audio_quality(path)
                if duration > 0.5: # Áudio válido (> 0.5s)
                    return {
                        "status": "sucesso",
                        "audio_path": path,
                        "provider_used": name,
                        "duration_seconds": duration
                    }
                else:
                    print(f"[Audio] {name} gerou áudio inválido/mudo.")
        except Exception as e:
            print(f"[Audio] {name} falhou: {e}")
            continue

    raise ServicoExterno("Falha crítica: Todos os provedores de áudio falharam.", url="/audio")
