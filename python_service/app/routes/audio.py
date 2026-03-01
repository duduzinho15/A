# =============================================================================
# app/routes/audio.py — Endpoint de geração de áudio v2.0 (SSML + Auto-Trim)
# =============================================================================
# MELHORIAS v2.0:
#   - SSML no edge-tts: <emphasis>, <break>, <prosody> para ênfase emocional
#   - Auto-trim de silêncios: detecta e corta dead air via pydub
#   - Vozes múltiplas: pt-BR-AntonioNeural (narrador) | pt-BR-FranciscaNeural (reporter)
#   - Logging estruturado substituindo todos os print()
# =============================================================================
import os
import re
import uuid
import asyncio
import logging
from typing import Optional, List
from fastapi import APIRouter
from pydantic import BaseModel
import edge_tts
import httpx
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
from app.config import settings
from app.utils.errors import ServicoExterno
from io import BytesIO

router = APIRouter(prefix="/audio", tags=["áudio"])
logger = logging.getLogger("audio_routes")

OUTPUT_DIR = os.path.join(settings.DATA_MIDIA, "audio")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Mapa de vozes por estilo (todas gratuitas no edge-tts)
VOICE_MAP = {
    "pt-BR": {
        "news": "pt-BR-AntonioNeural",       # Narrador principal: voz masculina séria
        "shorts": "pt-BR-AntonioNeural",
        "urgent": "pt-BR-FranciscaNeural",   # Urgente: feminina, mais energética
        "analítico": "pt-BR-FranciscaNeural"
    },
    "en-US": {
        "news": "en-US-GuyNeural",
        "shorts": "en-US-AriaNeural",
        "urgent": "en-US-TonyNeural"
    }
}


class AudioRequest(BaseModel):
    text: str
    lang: str = "pt-BR"
    voice: Optional[str] = None
    priority: str = "normal"
    style: str = "news"  # news, shorts, urgent, analítico


class AudioResponse(BaseModel):
    status: str
    audio_path: str
    provider_used: str
    duration_seconds: float = 0.0


# ---------------------------------------------------------------------------
# SSML BUILDER — Ênfase Emocional para edge-tts
# ---------------------------------------------------------------------------

def build_ssml(text: str, style: str = "news", lang: str = "pt-BR") -> str:
    """
    Converte texto simples em SSML com marcadores de ênfase emocional.

    Tags SSML geradas automaticamente:
    - <emphasis level="strong"> em palavras em CAPS (ex: ABSURDO, HISTÓRICO)
    - <break time="400ms"/> após cada ponto final
    - <break time="200ms"/> após vírgulas e ponto-e-vírgula
    - <prosody rate="fast"> nos blocos de CTA/shorts para ritmo dinâmico

    Args:
        text: Texto do roteiro
        style: "news" | "shorts" | "urgent"
        lang: Código de idioma ("pt-BR" | "en-US")

    Returns:
        String SSML válida para edge-tts.
    """
    # Limpa tags SSML existentes para evitar duplicação
    text = re.sub(r"<[^>]+>", "", text)

    # Determina parâmetros de prosody
    rate_map = {"shorts": "fast", "urgent": "+15%", "news": "+0%"}
    rate = rate_map.get(style, "+0%")
    pitch_map = {"shorts": "+5%", "urgent": "+8%", "news": "+0%"}
    pitch = pitch_map.get(style, "+0%")

    # Processa texto linha por linha para adicionar ênfase
    processed_lines = []
    for line in text.split("\n"):
        if not line.strip():
            continue

        # Adiciona <emphasis> em palavras toda-em-CAPS (≥ 3 letras)
        def emphasize_caps(match):
            word = match.group(0)
            return f'<emphasis level="strong">{word}</emphasis>'

        line = re.sub(r"\b[A-ZÁÉÍÓÚÂÊÔÃÕÇ]{3,}\b", emphasize_caps, line)

        # Adiciona <break> após pontos finais
        line = re.sub(r"\.", '.<break time="350ms"/>', line)

        # Adiciona <break> após vírgulas e ponto-e-vírgula
        line = re.sub(r",", ',<break time="150ms"/>', line)
        line = re.sub(r";", ';<break time="200ms"/>', line)

        # Adiciona <break> após reticências
        line = re.sub(r"\.\.\.", '...<break time="500ms"/>', line)

        processed_lines.append(line)

    body = "\n".join(processed_lines)

    # Monta o envelope SSML
    ssml = (
        f'<speak xmlns="http://www.w3.org/2001/10/synthesis" '
        f'xml:lang="{lang}">\n'
        f'  <prosody rate="{rate}" pitch="{pitch}">\n'
        f"    {body}\n"
        f"  </prosody>\n"
        f"</speak>"
    )
    return ssml


# ---------------------------------------------------------------------------
# AUTO-TRIM DE SILÊNCIOS (pydub)
# ---------------------------------------------------------------------------

def auto_trim_silence(filepath: str, min_silence_ms: int = 500, silence_thresh_db: int = -40) -> str:
    """
    Remove silêncios iniciais, finais e internos longos do áudio gerado.
    Retorna o path do arquivo trimado (substitui o original).

    Args:
        filepath: Path do arquivo de áudio a trimmar
        min_silence_ms: Silêncios menores que isso são mantidos (naturalidade)
        silence_thresh_db: Threshold abaixo do qual considera silêncio
    """
    try:
        audio = AudioSegment.from_file(filepath)
        original_duration = len(audio) / 1000.0

        # Detecta partes não-silenciosas
        nonsilent_ranges = detect_nonsilent(
            audio,
            min_silence_len=min_silence_ms,
            silence_thresh=silence_thresh_db
        )

        if not nonsilent_ranges:
            logger.warning("[AudioTrim] Áudio completamente mudo: %s", filepath)
            return filepath

        # Montagem: une os chunks não-silenciosos com 100ms de padding
        padding = 100  # ms de buffer entre os chunks
        chunks = []
        for start, end in nonsilent_ranges:
            start = max(0, start - padding)
            end = min(len(audio), end + padding)
            chunks.append(audio[start:end])

        if not chunks:
            return filepath

        trimmed = chunks[0]
        for chunk in chunks[1:]:
            trimmed = trimmed + chunk

        # Salva sobre o arquivo original
        trimmed.export(filepath, format="mp3", bitrate="192k")

        new_duration = len(trimmed) / 1000.0
        saved = original_duration - new_duration
        if saved > 0.1:
            logger.info(
                "[AudioTrim] Silêncios removidos: %.1fs → %.1fs (economizou %.1fs)",
                original_duration, new_duration, saved
            )

    except Exception as e:
        logger.warning("[AudioTrim] Erro ao trimmar silêncios de '%s': %s", filepath, e)

    return filepath


# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

def check_audio_quality(filepath: str) -> float:
    """Retorna duração em segundos se o áudio for válido (não mudo), senão 0."""
    try:
        audio = AudioSegment.from_file(filepath)
        if audio.dBFS < -120:  # Silêncio absoluto
            return 0.0
        return len(audio) / 1000.0
    except Exception:
        return 0.0


# ---------------------------------------------------------------------------
# PROVEDORES (Hierarquia)
# ---------------------------------------------------------------------------

async def tts_google(text: str, lang: str) -> Optional[str]:
    """1. Google Cloud TTS (WaveNet) - Placeholder (requer credenciais pagas)"""
    return None


async def tts_azure(text: str, lang: str) -> Optional[str]:
    """2. Azure Speech F0 - Placeholder (requer chave Azure)"""
    return None


async def tts_unreal(text: str, lang: str, style: str = "news") -> Optional[str]:
    """3. Unreal Speech (API — chave necessária)"""
    if not settings.UNREAL_SPEECH_API_KEY:
        return None
    try:
        voice_id = "Liv" if lang == "en-US" else "Will"
        url = "https://api.unrealspeech.com/stream"
        headers = {"Authorization": f"Bearer {settings.UNREAL_SPEECH_API_KEY}"}
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
            logger.warning("[Audio] Unreal Error: %d", resp.status_code)
    except Exception as e:
        logger.error("[Audio] Unreal Exception: %s", e)
    return None


async def tts_kokoro(text: str, lang: str, style: str = "news") -> Optional[str]:
    """4. Kokoro TTS (Container Local — gratuito se rodando)"""
    try:
        url = "http://kokoro:8880/v1/audio/speech"
        voice = "af_bella" if lang == "pt-BR" else "af_heart"
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
            logger.warning("[Audio] Kokoro Error: %d", resp.status_code)
    except Exception as e:
        logger.warning("[Audio] Kokoro Exception: %s", e)
    return None


async def tts_edge(
    text: str,
    lang: str,
    voice: Optional[str] = None,
    style: str = "news",
    use_ssml: bool = True
) -> Optional[str]:
    """
    5. edge-tts (Local - Fallback Final Garantido — 100% gratuito)
    Com SSML para ênfase emocional e auto-trim de silêncios.
    """
    try:
        filename = f"edge_{uuid.uuid4().hex}.mp3"
        filepath = os.path.join(OUTPUT_DIR, filename)

        # Seleciona voz pelo estilo
        if not voice:
            voice = VOICE_MAP.get(lang, VOICE_MAP["pt-BR"]).get(style, "pt-BR-AntonioNeural")

        # Ajuste de rate para shorts (além do SSML, o Communicate também aceita rate)
        rate = "+20%" if style == "shorts" else "+0%"
        volume = "+10%" if style == "urgent" else "+0%"

        if use_ssml:
            # Usa SSML para ênfase emocional máxima
            ssml_text = build_ssml(text, style=style, lang=lang)
            communicate = edge_tts.Communicate(ssml_text, voice, rate=rate, volume=volume)
        else:
            communicate = edge_tts.Communicate(text, voice, rate=rate, volume=volume)

        await communicate.save(filepath)

        # Auto-trim de silêncios após geração
        filepath = auto_trim_silence(filepath)

        logger.info("[Audio] edge-tts OK: %s (voice=%s, style=%s, ssml=%s)",
                    os.path.basename(filepath), voice, style, use_ssml)
        return filepath

    except Exception as e:
        logger.error("[Audio] edge-tts Error: %s", e)
        # Tenta sem SSML como fallback
        if use_ssml:
            logger.info("[Audio] Retentando edge-tts sem SSML...")
            return await tts_edge(text, lang, voice, style, use_ssml=False)
    return None


# ---------------------------------------------------------------------------
# ORQUESTRADOR
# ---------------------------------------------------------------------------

@router.post("/", response_model=AudioResponse)
async def gerar_audio(req: AudioRequest):
    """
    Gera áudio com hierarquia de provedores e fallback garantido.
    Unreal Speech → Kokoro → edge-tts (SSML + auto-trim).
    """
    providers = []

    # 1. Unreal (apenas se chave configurada)
    if settings.UNREAL_SPEECH_API_KEY:
        providers.append(("unreal", lambda: tts_unreal(req.text, req.lang, req.style)))

    # 2. Kokoro (container local — gratuito)
    providers.append(("kokoro", lambda: tts_kokoro(req.text, req.lang, req.style)))

    # 3. edge-tts (Fallback garantido — 100% gratuito, com SSML)
    providers.append(("edge-tts", lambda: tts_edge(req.text, req.lang, req.voice, req.style)))

    for name, func in providers:
        try:
            path = await func()
            if path:
                duration = check_audio_quality(path)
                if duration > 0.5:
                    logger.info("[Audio] Provedor '%s' OK: %.1fs", name, duration)
                    return {
                        "status": "sucesso",
                        "audio_path": path,
                        "provider_used": name,
                        "duration_seconds": duration
                    }
                else:
                    logger.warning("[Audio] %s gerou áudio inválido/mudo (%.1fs)", name, duration)
        except Exception as e:
            logger.error("[Audio] %s falhou: %s", name, e)
            continue

    raise ServicoExterno("Falha crítica: Todos os provedores de áudio falharam.", url="/audio")
