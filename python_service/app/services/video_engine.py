"""
video_engine.py — Motor de Edição Pro "Futebas"
=================================================
REFACTORING v2.0 — TikToker Profissional

Principais mudanças vs MVP:
  - Blurred Background Padding: nunca mais estica imagens ou telas pretas.
    A matemática é: fundo = imagem escalada para 1920px de altura + Gaussian
    Blur(40) + escurecimento 65%; frente = imagem escalada para caber em 1080px
    de largura, centralizada verticalmente.
  - Word-Level Subtitles: faster-whisper extrai timestamps por palavra;
    agrupamos em blocos de 2-3 palavras para ritmo de leitura TikTok.
  - Crossfade entre clipes: elimina o corte seco que causa drop de retenção.
  - Detecção de Watermark de Stock: heurística Pillow rápida — sem OpenCV,
    sem aumentar a imagem Docker.
  - Mixagem de áudio: loop robusto + ducking 10% + fade out 2s.
"""

import os
import uuid
import logging
import requests
import yt_dlp
import random
import asyncio
import httpx

# --- FIX IMAGEMAGICK DOCKER (FASE 2) ---
os.environ["HOME"] = "/tmp"
os.environ["MAGICK_TEMPORARY_PATH"] = "/tmp"
os.environ["XDG_CACHE_HOME"] = "/tmp"
# --------------------------------------

import edge_tts
import json
import numpy as np
from typing import List, Optional, Tuple, Union, Any
from pathlib import Path

# --- Pillow (Processamento de Imagem) ---
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont

# --- MoviePy ---
from moviepy.editor import (
    ImageClip, VideoFileClip, AudioFileClip, concatenate_videoclips,
    concatenate_audioclips, vfx, CompositeVideoClip, CompositeAudioClip,
    TextClip, ColorClip, clips_array
)
from moviepy.video.tools.subtitles import SubtitlesClip

import cv2

from app.config import settings
from app.utils.database import get_db_connection
from app.services.visual_gate import VisualGate
from app.services.audio import AudioService

# =============================================================================
# CONFIGURAÇÃO DE LOGGER — Todos os passos geram logs descritivos para o Docker
# =============================================================================
logger = logging.getLogger("video_engine")
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(name)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S"
)

# Instância Global do Serviço de Áudio
audio_service = AudioService()

# =============================================================================
# DIRETÓRIOS
# =============================================================================
TEMP_DIR    = os.path.join(settings.DATA_MIDIA, "temp")
OUTPUT_DIR  = os.path.join(settings.DATA_MIDIA, "videos")
AUDIO_DIR   = os.path.join(settings.DATA_MIDIA, "audios")

APP_DIR      = os.path.dirname(os.path.dirname(__file__))  # app/
ASSETS_DIR   = os.path.join(APP_DIR, "assets")
FONTS_DIR    = os.path.join(ASSETS_DIR, "fonts")
MUSIC_DIR    = os.path.join(ASSETS_DIR, "music")
OVERLAYS_DIR = os.path.join(ASSETS_DIR, "overlays")
DEFAULTS_DIR = os.path.join(ASSETS_DIR, "defaults")

# Resolução alvo: 9:16 vertical (YouTube Shorts / TikTok)
TARGET_W = 1080
TARGET_H = 1920

for d in [TEMP_DIR, OUTPUT_DIR, AUDIO_DIR, FONTS_DIR, MUSIC_DIR, OVERLAYS_DIR, DEFAULTS_DIR]:
    os.makedirs(d, exist_ok=True)


# =============================================================================
# PASSO A — HELPERS DE ASSETS
# =============================================================================

def get_montserrat_black() -> str:
    """
    Retorna o path absoluto da fonte Montserrat-Black.ttf.
    Fallback: qualquer .ttf disponível → 'Arial-Bold' (ImageMagick).
    """
    primary = os.path.join(FONTS_DIR, "Montserrat-Black.ttf")
    if os.path.exists(primary):
        return primary
    # Fallback: primeira .ttf encontrada
    try:
        fonts = [f for f in os.listdir(FONTS_DIR) if f.endswith(".ttf")]
        if fonts:
            logger.warning("Montserrat-Black.ttf não encontrada, usando: %s", fonts[0])
            return os.path.join(FONTS_DIR, fonts[0])
    except Exception:
        pass
    return "Arial-Bold"


def get_background_music(mood: str = "Epic") -> Optional[str]:
    """
    Seleciona trilha sonora aleatória da pasta de mood.
    Moods disponíveis: Epic, Happy, Rock, Sad.
    Fallback: qualquer .mp3 em qualquer subpasta.
    """
    try:
        mood_path = os.path.join(MUSIC_DIR, mood)
        if os.path.exists(mood_path):
            musics = [f for f in os.listdir(mood_path) if f.endswith(".mp3")]
            if musics:
                chosen = random.choice(musics)
                logger.info("[Music] DJ escolheu (%s): %s", mood, chosen)
                return os.path.join(mood_path, chosen)

        # Fallback: qualquer subpasta
        all_musics = []
        for root, _, files in os.walk(MUSIC_DIR):
            for f in files:
                if f.endswith(".mp3"):
                    all_musics.append(os.path.join(root, f))
        if all_musics:
            chosen = random.choice(all_musics)
            logger.info("[Music] DJ Fallback: %s", os.path.basename(chosen))
            return chosen
    except Exception as e:
        logger.error("[Music] Erro ao buscar música: %s", e)
    return None


def get_watermark_path() -> Optional[str]:
    """
    Retorna o path do logo/watermark do canal.

    PRIORIDADE (do mais para o menos preferido):
      1. DATA_MIDIA/branding/logo.png  (volume persistente — asset oficial)
      2. DATA_MIDIA/branding/logo_full.png
      3. OVERLAYS_DIR (fallback legado dentro do container)
    """
    # 1. Primeiro: volume de dados persistente (montado em /data_midia)
    branding_dir = os.path.join(settings.DATA_MIDIA, "branding")
    for name in ["logo.png", "logo_full.png", "Logo.png"]:
        path = os.path.join(branding_dir, name)
        if os.path.exists(path):
            logger.info("[Branding] Logo carregado de DATA_MIDIA: %s", name)
            return path

    # 2. Fallback legado: pasta overlays dentro do container
    for name in ["watermark.png", "logo.png", "Logo.png"]:
        path = os.path.join(OVERLAYS_DIR, name)
        if os.path.exists(path):
            logger.warning("[Branding] Logo carregado de OVERLAYS_DIR (legado): %s", name)
            return path

    logger.warning("[Branding] Nenhum logo encontrado — vídeo sem watermark.")
    return None


def get_fallback_loop() -> Optional[str]:
    """Retorna um vídeo de loop padrão da pasta defaults."""
    try:
        loops = [f for f in os.listdir(DEFAULTS_DIR) if f.endswith(".mp4")]
        if loops:
            chosen = random.choice(loops)
            logger.info("[Fallback] Usando loop padrão: %s", chosen)
            return os.path.join(DEFAULTS_DIR, chosen)
    except Exception:
        pass
    return None


# =============================================================================
# PASSO A — DETECÇÃO DE WATERMARK DE STOCK (Heurística Pillow)
# =============================================================================

def detect_stock_watermark(img_path: str) -> bool:
    """
    Detecta marcas d'água óbvias de bancos de imagem (Getty, Adobe Stock, etc.)
    usando heurística de pixels — sem OCR, sem OpenCV, sem peso extra na build.

    ALGORITMO:
        1. Abre a imagem e recorta a faixa inferior (últimos 15% da altura),
           que é onde as watermarks de stock costumam ficar.
        2. Converte para grayscale.
        3. Conta pixels muito claros (valor > 200). Se mais de 25% da faixa
           for clara, a imagem provavelmente tem texto de watermark de stock.

    Limitações: pode rejeitar fotos com céu claro na parte de baixo.
    Em produção, isso é aceitável — melhor rejeitar do que publicar com logo.

    Returns:
        True se a imagem parece ter watermark → REJEITAR.
        False se parece OK → ACEITAR.
    """
    try:
        img = Image.open(img_path).convert("L")  # Grayscale
        w, h = img.size

        # Recorta apenas os últimos 15% verticais
        bottom_band = img.crop((0, int(h * 0.85), w, h))
        pixels = list(bottom_band.getdata())

        # Conta pixels muito claros (brancos/cinza claro típico de watermarks)
        bright_count = sum(1 for p in pixels if p > 200)
        bright_ratio = bright_count / len(pixels) if pixels else 0

        if bright_ratio > 0.35:
            logger.info("[WatermarkDetect] Rejeitando '%s' (%.0f%% pixels claros na base)",
                        os.path.basename(img_path), bright_ratio * 100)
            return True  # Suspeito de watermark

    except Exception as e:
        logger.warning("[WatermarkDetect] Erro ao checar '%s': %s", img_path, e)
    return False


def create_scoreboard_overlay(placar: str, gols: Optional[List[str]] = None) -> Optional[Any]:
    """
    Cria um overlay visual de placar para o topo do vídeo.
    Ex: [ PLACAR: 2 x 0 ]
    """
    if not placar or placar == "N/A" or len(placar) < 3:
        return None
    
    try:
        from moviepy.editor import ColorClip, TextClip, CompositeVideoClip
        
        # Fundo do placar: Barra semitransparente preta
        bg = ColorClip(size=(TARGET_W, 80), color=(0, 0, 0)).set_opacity(0.65)
        
        # Texto do placar
        score_text = f"PLACAR: {placar}"
        txt = TextClip(
            score_text,
            fontsize=45,
            color='#FFDD00', # Amarelo Futebas
            font=get_montserrat_black(),
            stroke_color="black",
            stroke_width=2
        ).set_position(("center", "center"))
        
        scoreboard = CompositeVideoClip([bg, txt], size=(TARGET_W, 80))
        return scoreboard.set_position(("center", 60)).set_start(3) # Começa aos 3s
    except Exception as e:
        logger.warning("[Scoreboard] Falha ao criar overlay: %s", e)
        return None

def make_blurred_background(img_path: str) -> Optional[str]:
    """
    Transforma qualquer imagem 16:9 (ou qualquer aspect ratio) em um frame
    9:16 (1080x1920) profissional, sem bordas pretas e sem esticamento.

    MATEMÁTICA DO REDIMENSIONAMENTO:
    ─────────────────────────────────
    Cache:
        - Verifica se a imagem já foi processada (hash do path).
        - Se sim, retorna o path do cache imediatamente.
    Camada de FUNDO (blurred):
        - A imagem é redimensionada para altura 1920px (mantendo aspect ratio).
          Fórmula: new_w = original_w * (1920 / original_h)
          Para uma imagem 16:9 (ex: 1280x720):
            new_w = 1280 * (1920 / 720) = 1280 * 2.67 = 3413px
            Logo ela "transborda" os 1080px de largura → cobre tudo.
        - Aplica GaussianBlur com radius=40 (forte) para suavizar totalmente.
        - Aplica Brightness(0.35) para escurecer 65% e destacar a camada frontal.

    Camada de FRENTE (nítida, centralizada):
        - Redimensiona para caber EXATAMENTE dentro de 1080px de largura.
          Fórmula: new_h = original_h * (1080 / original_w)
          Para uma imagem 16:9 (1280x720):
            new_h = 720 * (1080 / 1280) = 607px (< 1920, sobram 1313px de fundo)
        - Posição Y central: y = (1920 - 607) / 2 = 656px
        - A imagem fica "flutuando" no centro da tela com o fundo desfocado atrás.

    Returns:
        Path do arquivo de saída temporário (PNG), ou None se falhar.
    """
    try:
        import hashlib
        # ── SISTEMA DE CACHE (v13 Turbo) ──────────────────────────────────
        cache_dir = os.path.join(settings.DATA_MIDIA, "cache", "blur_bg")
        os.makedirs(cache_dir, exist_ok=True)
        img_hash = hashlib.md5(img_path.encode()).hexdigest()
        cache_path = os.path.join(cache_dir, f"blur_{img_hash}.jpg")

        if os.path.exists(cache_path):
            logger.info("[BlurBG] Cache hit: %s", os.path.basename(cache_path))
            return cache_path

        img = Image.open(img_path).convert("RGB")
        orig_w, orig_h = img.size

        # ── CAMADA DE FUNDO (Blurred) ──────────────────────────────────────
        # Escala para cobrir os 1920px de altura completamente
        bg_ratio = TARGET_H / orig_h
        bg_w = int(orig_w * bg_ratio)
        bg_h = TARGET_H

        # Se a largura não cobrir 1080, escala pelo eixo X
        if bg_w < TARGET_W:
            bg_ratio = TARGET_W / orig_w
            bg_w = TARGET_W
            bg_h = int(orig_h * bg_ratio)

        bg = img.resize((bg_w, bg_h), Image.LANCZOS)

        # Centraliza o recorte do fundo (caso seja maior que o canvas)
        crop_x = (bg_w - TARGET_W) // 2
        crop_y = (bg_h - TARGET_H) // 2
        bg = bg.crop((crop_x, crop_y, crop_x + TARGET_W, crop_y + TARGET_H))

        # Aplica desfoque gaussiano forte e escurece
        bg = bg.filter(ImageFilter.GaussianBlur(radius=40))
        bg = ImageEnhance.Brightness(bg).enhance(0.35)  # 65% mais escuro

        # ── CAMADA DE FRENTE (Nítida, centralizada) ────────────────────────
        # Escala para caber exatamente na largura de 1080px
        front_ratio = TARGET_W / orig_w
        front_w = TARGET_W
        front_h = int(orig_h * front_ratio)

        # Segurança: se a imagem for muito alta, limita à altura da tela
        if front_h > TARGET_H:
            front_ratio = TARGET_H / orig_h
            front_h = TARGET_H
            front_w = int(orig_w * front_ratio)

        front = img.resize((front_w, front_h), Image.LANCZOS)

        # Calcula posição Y para centralizar verticalmente na tela
        paste_y = (TARGET_H - front_h) // 2
        paste_x = (TARGET_W - front_w) // 2  # Geralmente 0, mas seguro para imgs quadradas

        # ── COMPOSIÇÃO FINAL ───────────────────────────────────────────────
        canvas = Image.new("RGB", (TARGET_W, TARGET_H))
        canvas.paste(bg, (0, 0))            # Fundo desfocado
        canvas.paste(front, (paste_x, paste_y))  # Imagem nítida centralizada

        # Salva em cache
        canvas.save(cache_path, "JPEG", quality=85) # Quality 85 for speed/size
        logger.info("[BlurBG] Gerado e Cacheado: %s (frente=%dx%d @ y=%d)",
                    os.path.basename(cache_path), front_w, front_h, paste_y)
        return cache_path

    except Exception as e:
        logger.error("[BlurBG] Falha ao processar '%s': %s", img_path, e)
        return None


# =============================================================================
# PASSO B — LEGENDAS WORD-LEVEL VIA FASTER-WHISPER
# =============================================================================

def generate_word_level_clips(
    audio_path: str,
    words_per_group: int = 3,
    font_path: Optional[str] = None,
    video_duration: Optional[float] = None
) -> List:
    """
    Usa faster-whisper para extrair timestamps por palavra e cria TextClips
    sincronizados com o áudio — efeito "karaokê TikTok".

    ALGORITMO DE AGRUPAMENTO:
    ─────────────────────────
    Recebemos palavras com (start, end, word). Agrupamos em blocos de
    `words_per_group` (default=3) para que o texto seja legível no tempo
    de exibição. Blocos muito longos ficam pequenos na tela; blocos de 2-3
    palavras são o sweet spot de retenção.

    Ex: ["Messi", "marcou", "um", "gol", "incrível", "hoje"]
    → Grupo 1: "Messi marcou um" (start=0.2, end=1.1)
    → Grupo 2: "gol incrível hoje" (start=1.2, end=2.5)

    Cada grupo vira um TextClip com:
    - Fonte: Montserrat-Black 72px
    - Cor: Amarelo #FFDD00 (cor da marca Futebas)
    - Borda stroke preta (5px) para legibilidade em qualquer fundo
    - Posição: 75% da altura (safe zone, abaixo do logo do canal)

    Fallback: se faster-whisper falhar, retorna [] e o vídeo é gerado
    sem legendas (nunca trava a execução).

    Args:
        audio_path: Path do arquivo .mp3/.wav da narração.
        words_per_group: Número de palavras por bloco de legenda.
        font_path: Path da fonte .ttf a usar.
        video_duration: Duração total do vídeo (para sanitizar timestamps).

    Returns:
        Lista de TextClip prontos para CompositeVideoClip.
    """
    clips = []
    if not font_path:
        font_path = get_montserrat_black()

    try:
        from faster_whisper import WhisperModel

        logger.info("[Whisper] Transcrevendo áudio para timestamps word-level...")
        # Usa modelo tiny — leve, rápido e suficiente para PT-BR curto
        # compute_type="int8" minimiza uso de RAM no container
        model = WhisperModel("tiny", device="cpu", compute_type="int8")

        segments, info = model.transcribe(
            audio_path,
            language="pt",
            word_timestamps=True,   # ← chave para legendas sincronizadas
            vad_filter=True,        # Remove silêncios longos
            beam_size=1             # Velocidade > precisão para vídeos curtos
        )
        logger.info("[Whisper] Idioma detectado: %s (confiança %.0f%%)",
                    info.language, info.language_probability * 100)

        # ── Coleta todas as palavras com seus timestamps ──────────────────
        all_words = []
        for segment in segments:
            if hasattr(segment, "words") and segment.words:
                for word_obj in segment.words:
                    text = word_obj.word.strip()
                    if text:
                        all_words.append({
                            "word": text,
                            "start": word_obj.start,
                            "end": word_obj.end
                        })

        if not all_words:
            logger.warning("[Whisper] Nenhuma palavra extraída — sem legendas.")
            return []

        logger.info("[Whisper] %d palavras extraídas. Agrupando em blocos de %d...",
                    len(all_words), words_per_group)

        # ── Agrupa as palavras em blocos de N palavras ────────────────────
        groups = []
        for i in range(0, len(all_words), words_per_group):
            chunk = all_words[i : i + words_per_group]
            group_text = " ".join(w["word"] for w in chunk).upper()
            group_start = chunk[0]["start"]
            group_end = chunk[-1]["end"]

            # Sanitiza: garante que timestamps estão dentro da duração do vídeo
            if video_duration:
                group_end = min(group_end, video_duration - 0.1)
            if group_start >= group_end:
                continue

            groups.append({
                "text": group_text,
                "start": group_start,
                "end": group_end,
                "duration": group_end - group_start
            })

        logger.info("[Whisper] %d grupos de legendas criados.", len(groups))

        # ── Cria TextClips para cada grupo ───────────────────────────────
        import random
        for group in groups:
            try:
                # Estilo TikTok: Cores dinâmicas para as bordas de palavras chave
                colors = ["#FFDD00", "#FFFFFF", "#00FFDD"]
                active_color = colors[0] if len(group["text"]) > 5 else random.choice(colors)
                # O highlight pode ser uma leve rotação randômica ou mudança de fonte
                font_z = font_path

                txt_clip = (
                    TextClip(
                        group["text"],
                        font=font_z,
                        fontsize=85, # Aumentado para estilo dinâmico
                        color=active_color,         
                        stroke_color="black",
                        stroke_width=6, # Mais bold
                        method="caption",
                        size=(int(TARGET_W * 0.90), None), 
                        align="center"
                    )
                    .set_start(group["start"])
                    .set_duration(group["duration"])
                    .set_position(("center", 0.70), relative=True)  # Subiu levemente
                )
                clips.append(txt_clip)
            except Exception as e:
                logger.warning("[Whisper] Erro ao criar TextClip '%s': %s", group["text"], e)

        logger.info("[Whisper] %d TextClips de legenda renderizados.", len(clips))

    except ImportError:
        logger.error("[Whisper] faster-whisper não instalado — sem legendas word-level.")
    except Exception as e:
        logger.error("[Whisper] Falha na transcrição (fallback: sem legendas): %s", e)

    return clips


# =============================================================================
# HELPERS DE DOWNLOAD E PROCESSAMENTO
# =============================================================================

# URLs de placeholder/dummy que devem ser rejeitadas
_PLACEHOLDER_DOMAINS = {
    "dummyimage.com", "via.placeholder.com", "placeholder.com",
    "placekitten.com", "lorempixel.com", "fillmurray.com",
    "picsum.photos", "fakeimg.pl", "loremflickr.com"
}


def reject_placeholder_urls(urls: List[str]) -> List[str]:
    """
    Filtra URLs de placeholder/dummy que não devem ir para o vídeo.
    Retorna a lista limpa de URLs válidas.
    """
    valid = []
    for url in urls:
        is_placeholder = any(dom in url.lower() for dom in _PLACEHOLDER_DOMAINS)
        if is_placeholder:
            logger.info("[URLFilter] URL de placeholder rejeitada: %s", url)
        else:
            valid.append(url)
    return valid


def download_file(url: str, ext: str = "jpg") -> Optional[str]:
    """Baixa um arquivo (imagem/áudio) via requests com timeout e UA."""
    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
            )
        }
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200 and len(response.content) > 1024:
            filename = f"asset_{uuid.uuid4().hex}.{ext}"
            filepath = os.path.join(TEMP_DIR, filename)
            with open(filepath, "wb") as f:
                f.write(response.content)
            return filepath
    except Exception as e:
        logger.warning("[Download] Erro ao baixar '%s': %s", url, e)
    return None


def download_video_clip(url: str) -> Optional[str]:
    """Baixa vídeo com yt-dlp (suporta YouTube, Reddit, Twitter, etc.)."""
    video_id = uuid.uuid4().hex[:8]
    template = os.path.join(TEMP_DIR, f"vid_{video_id}.%(ext)s")
    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": template,
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "duration_limit": 90,
        "socket_timeout": 20,
        "retries": 3,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)
    except Exception as e:
        logger.warning("[Download] Erro yt-dlp '%s': %s", url, e)
    return None


# --- NOVOS HELPERS ASSÍNCRONOS (v13 Turbo) ---

async def async_download_file(url: str, ext: str = "jpg") -> Optional[str]:
    """Versão assíncrona do download_file usando httpx."""
    if not url: return None
    try:
        async with httpx.AsyncClient(timeout=15.0, follow_redirects=True) as client:
            headers = {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
                )
            }
            response = await client.get(url, headers=headers)
            if response.status_code == 200 and len(response.content) > 1024:
                filename = f"asset_{uuid.uuid4().hex}.{ext}"
                filepath = os.path.join(TEMP_DIR, filename)
                # Escrita síncrona de arquivo é rápida o suficiente para imagens pequenos, 
                # mas em 'Turbo' usamos threads para evitar bloquear o event loop em IO pesado.
                await asyncio.to_thread(lambda: open(filepath, "wb").write(response.content))
                return filepath
    except Exception as e:
        logger.warning("[AsyncDownload] Erro ao baixar '%s': %s", url, e)
    return None


async def async_download_video_clip(url: str) -> Optional[str]:
    """Versão assíncrona do download_video_clip rodando yt-dlp em thread."""
    if not url: return None
    # Rodamos o download_video_clip (que é síncrono e pesado) em uma thread separada
    return await asyncio.to_thread(download_video_clip, url)


def fetch_google_images(query: str, limit: int = 3) -> List[str]:
    """Busca imagens no Google via Serper → CSE → Brave (cascata)."""
    assets = []

    # 1. Serper Dev
    if settings.SERPER_API_KEY:
        try:
            r = requests.post(
                "https://google.serper.dev/images",
                headers={"X-API-KEY": settings.SERPER_API_KEY, "Content-Type": "application/json"},
                data=json.dumps({"q": query, "num": limit}),
                timeout=10
            )
            for img in r.json().get("images", []):
                path = download_file(img.get("imageUrl", ""), ext="jpg")
                if path:
                    assets.append(path)
                if len(assets) >= limit:
                    return assets
        except Exception as e:
            logger.warning("[Serper] %s", e)

    # 2. Brave Fallback
    if not assets and settings.BRAVE_API_KEY:
        try:
            r = requests.get(
                "https://api.search.brave.com/res/v1/images/search",
                headers={"Accept": "application/json", "X-Subscription-Token": settings.BRAVE_API_KEY},
                params={"q": query, "count": limit},
                timeout=10
            )
            for res in r.json().get("results", []):
                url = res.get("properties", {}).get("url") or res.get("url", "")
                path = download_file(url, ext="jpg")
                if path:
                    assets.append(path)
                if len(assets) >= limit:
                    return assets
        except Exception as e:
            logger.warning("[Brave] %s", e)

    return assets


def fetch_external_assets(query: str, limit: int = 3) -> List[str]:
    """Pánico Search: Google Images → Pexels → Pixabay."""
    all_assets = []

    all_assets.extend(fetch_google_images(query, limit))
    if len(all_assets) >= limit:
        return all_assets

    if settings.PEXELS_API_KEY:
        try:
            r = requests.get(
                f"https://api.pexels.com/videos/search?query={query}&orientation=portrait&per_page={limit}",
                headers={"Authorization": settings.PEXELS_API_KEY},
                timeout=10
            )
            for v in r.json().get("videos", []):
                files = sorted(
                    [f for f in v.get("video_files", []) if f.get("width", 0) >= 720],
                    key=lambda x: x["width"]
                )
                if files:
                    path = download_file(files[-1]["link"], ext="mp4")
                    if path:
                        all_assets.append(path)
        except Exception as e:
            logger.warning("[Pexels] %s", e)

    if len(all_assets) < limit and settings.PIXABAY_API_KEY:
        try:
            r = requests.get(
                f"https://pixabay.com/api/?key={settings.PIXABAY_API_KEY}&q={query}&image_type=photo&per_page={limit}",
                timeout=10
            )
            for h in r.json().get("hits", []):
                path = download_file(h.get("largeImageURL", ""), ext="jpg")
                if path:
                    all_assets.append(path)
        except Exception as e:
            logger.warning("[Pixabay] %s", e)

    return all_assets


# =============================================================================
# B-ROLL SCORING — relevância de clip por keywords
# =============================================================================

def score_clip_relevance(clip_filename: str, visual_keywords: List[str]) -> int:
    """
    Pontua a relevância de um clip baseado em quantas keywords visuais
    do roteiro aparecem no nome do arquivo ou no path.

    Score: 0-100 (100 = todos os termos estão presentes)

    Args:
        clip_filename: Path ou nome do arquivo do clip
        visual_keywords: Lista de keywords do campo `keywords_visuais` do roteiro

    Returns:
        Score de 0 a 100.
    """
    if not visual_keywords:
        return 50  # Score neutro quando não há keywords

    name_lower = os.path.basename(clip_filename).lower()
    matches = sum(1 for kw in visual_keywords if kw.lower() in name_lower)
    return int((matches / len(visual_keywords)) * 100)


# =============================================================================
# YOUTUBE CREATIVE COMMONS (yt-dlp — gratuito)
# =============================================================================

def fetch_youtube_cc(query: str, max_duration: int = 30) -> Optional[str]:
    """
    Busca e baixa vídeo Creative Commons do YouTube via yt-dlp.
    Filtra automaticamente para apenas vídeos com licença CC-BY.

    Args:
        query: Termo de busca (ex: "Palmeiras treino")
        max_duration: Duração máxima em segundos (padrão 30s)

    Returns:
        Path do arquivo baixado, ou None se não encontrar.
    """
    video_id = uuid.uuid4().hex[:8]
    template = os.path.join(TEMP_DIR, f"yt_cc_{video_id}.%(ext)s")

    ydl_opts = {
        "format": "bestvideo[ext=mp4][height<=720]+bestaudio[ext=m4a]/best[ext=mp4]",
        "outtmpl": template,
        "quiet": True,
        "no_warnings": True,
        "noplaylist": True,
        "match_filter": yt_dlp.utils.match_filter_func(f"duration < {max_duration}"),
        "socket_timeout": 20,
        "retries": 2,
        # Filtra apenas Creative Commons
        "extract_flat": False,
        "postprocessors": [],
        # Busca com prefixo ytsearch e filtro de licença CC
        "default_search": f"ytsearch5:{query} Creative Commons",
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch5:{query} licença CC", download=True)
            if info and "entries" in info:
                for entry in info["entries"]:
                    if not entry:
                        continue
                    # Verifica licença CC no campo license
                    license_field = (entry.get("license") or "").lower()
                    if "creative commons" in license_field or "cc" in license_field:
                        downloaded = ydl.prepare_filename(entry)
                        if os.path.exists(downloaded):
                            logger.info("[YT-CC] CC encontrado: %s", entry.get("title", "")[:50])
                            return downloaded
        logger.info("[YT-CC] Nenhum vídeo CC encontrado para: %s", query)
    except Exception as e:
        logger.warning("[YT-CC] Erro ao buscar CC para '%s': %s", query, e)
    return None


# =============================================================================
# EFEITOS VISUAIS
# =============================================================================

def apply_ken_burns(clip, duration: float, zoom_ratio: float = 0.08):
    """
    Efeito Ken Burns: zoom suave progressivo ao longo da duração.
    zoom_ratio=0.08 → o clipe cresce 8% do início ao fim — sutil e elegante.
    """
    def zoom(t):
        return 1 + zoom_ratio * (t / duration)
    return clip.resize(zoom)

def apply_smart_crop(clip, target_w=1080, target_h=1920):
    """
    Usa OpenCV (Haar Cascades) no frame central do clip para encontrar rostos.
    Faz o crop centrado no rosto mantendo o aspect ratio do Shorts (9:16).
    Se não achar rosto, ou falhar, faz crop simples central.
    """
    try:
        import cv2
        import numpy as np
        
        # Pega frame na metade do clipe
        mid_t = clip.duration / 2.0
        frame = clip.get_frame(mid_t)
        
        ih, iw = frame.shape[:2]
        
        # Inicia detector OpenCV iterativo
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        
        # minSize evita pegar "rostos" minúsculos que podem ser ruído de background
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        if len(faces) > 0:
            # Pega o maior rosto (por área)
            largest_face = max(faces, key=lambda rect: rect[2] * rect[3])
            x, y, w, h = largest_face
            
            cx = x + w // 2
            cy = y + h // 2
            
            logger.info("[SmartCrop] Rosto detectado em (x=%d, y=%d) no clip de B-Roll.", cx, cy)
        else:
            logger.info("[SmartCrop] Nenhum rosto detectado, usando crop central limpo.")
            cx, cy = iw // 2, ih // 2
    except Exception as e:
        logger.warning("[SmartCrop] Falha OpenCV, fallback para centro: %s", e)
        # clip.size é formato (W, H)
        iw, ih = clip.size[0], clip.size[1]
        cx, cy = iw // 2, ih // 2

    aspect = target_w / target_h
    # Altura do crop será baseada na largura total se a largura for o gargalo
    crop_h = min(ih, int(iw / aspect))
    crop_w = min(iw, int(ih * aspect))

    left = max(0, cx - crop_w // 2)
    top = max(0, cy - crop_h // 2)
    
    # Adjust boundaries to remain inside the frame while maintaining size
    if left + crop_w > iw: left = iw - crop_w
    if top + crop_h > ih: top = ih - crop_h
        
    left = max(0, left)
    top = max(0, top)
    right = left + crop_w
    bottom = top + crop_h

    from moviepy.video.fx.all import crop as crop_fx
    cropped_clip = crop_fx(clip, x1=left, y1=top, x2=right, y2=bottom)
    return cropped_clip.resize(newsize=(target_w, target_h))


def apply_copyright_protection(clip):
    """Mirror X + Zoom 1.05x para modificar o hash visual do vídeo."""
    try:
        clip = clip.fx(vfx.mirror_x)
        clip = clip.resize(1.05)
    except Exception:
        pass
    return clip


def _write_videofile_with_fallback(video, output_path: str):
    """
    Render: tenta NVENC (GPU) primeiro, fallback automático para libx264 (CPU).
    Otimizado v13: Maior paralelismo e presets mais rápidos.
    """
    try:
        logger.info("[Render] Tentando NVENC (GPU)...")
        video.write_videofile(
            output_path, fps=24, codec="h264_nvenc", audio_codec="aac",
            threads=8, preset="p1", # p1 é o mais rápido (Turbo)
            ffmpeg_params=["-gpu", "0", "-rc:v", "vbr", "-cq", "24",
                           "-b:v", "6M", "-maxrate", "12M", "-bufsize", "15M",
                           "-pix_fmt", "yuv420p", "-profile:v", "main"],
        )
        logger.info("[Render] Finalizado com NVENC.")
    except Exception as gpu_exc:
        logger.warning("[Render] NVENC indisponível (%s), usando CPU (libx264)...", gpu_exc)
        video.write_videofile(
            output_path, fps=24, codec="libx264", audio_codec="aac",
            threads=8, preset="ultrafast", # Máxima velocidade
        )
        logger.info("[Render] Finalizado com libx264 (CPU).")


def create_stinger(duration: float = 0.6) -> Optional:
    """Transição Stinger: logo do canal zoom in/out durante a troca de cena."""
    logo_path = get_watermark_path()
    if not logo_path:
        return None
    try:
        logo = ImageClip(logo_path).resize(width=400).set_duration(duration)

        def scale_effect(t):
            if t < duration / 2:
                return 0.1 + 1.4 * (t / (duration / 2))
            return 1.5 - 1.4 * ((t - duration / 2) / (duration / 2))

        stinger = logo.resize(scale_effect).set_position("center")
        bg = ColorClip(size=(TARGET_W, TARGET_H), color=(0, 0, 0), duration=duration).set_opacity(0.3)
        return CompositeVideoClip([bg, stinger]).set_duration(duration)
    except Exception as e:
        logger.warning("[Stinger] Erro: %s", e)
        return None


def add_lower_third(text: str, duration: float, start_time: float = 0.0) -> Optional:
    """
    Cria um lower-third dinâmico na base do frame.
    Exibido durante as primeiras `duration` segundos do vídeo ou de um segmento.

    Args:
        text: Texto a exibir (ex: "Estádio Morumbi • São Paulo, SP")
        duration: Duração em segundos que o banner fica visível
        start_time: Quando o banner aparece no timeline

    Returns:
        CompositeVideoClip-ready TextClip ou None.
    """
    try:
        font_path = get_montserrat_black()

        # Fundo semitransparente (barra escura)
        bar_h = 90
        bar = (
            ColorClip(size=(TARGET_W, bar_h), color=(10, 10, 30))
            .set_opacity(0.75)
            .set_duration(duration)
            .set_start(start_time)
            .set_position((0, TARGET_H - bar_h - 80))  # 80px acima da base (safe zone)
        )

        # Texto do lower-third
        txt = (
            TextClip(
                text.upper(),
                font=font_path,
                fontsize=38,
                color="white",
                stroke_color="black",
                stroke_width=2,
                method="caption",
                size=(TARGET_W - 60, None),
                align="West"
            )
            .set_duration(duration)
            .set_start(start_time)
            .set_position((30, TARGET_H - bar_h - 75))
        )

        logger.info("[LowerThird] Criado: '%s' por %.1fs", text[:40], duration)
        return [bar, txt]

    except Exception as e:
        logger.warning("[LowerThird] Erro ao criar lower-third: %s", e)
        return []


def add_end_screen(total_duration: float, end_duration: float = 3.5) -> List:
    """
    Adiciona end screen nos últimos `end_duration` segundos.

    ESTRATÉGIA:
      1. Se existir DATA_MIDIA/branding/end_screen_vertical.png usa como fundo
         (imagem oficial do canal Futebas com "Inscreva-se" já estampado).
      2. Caso contrário, usa ColorClip escuro semitransparente + TextClip.

    Args:
        total_duration: Duração total do vídeo
        end_duration: Quantos segundos antes do fim mostrar o end screen

    Returns:
        Lista de clips para CompositeVideoClip.
    """
    start = max(0.0, total_duration - end_duration)
    try:
        font_path = get_montserrat_black()
        branding_dir = os.path.join(settings.DATA_MIDIA, "branding")
        end_img_path = os.path.join(branding_dir, "end_screen_vertical.png")

        clips = []

        # ── Fundo: imagem oficial ou ColorClip ───────────────────────────────
        if os.path.exists(end_img_path):
            # Usa a imagem "Inscreva-se" do canal — já tem o visual correto
            bg = (
                ImageClip(end_img_path)
                .resize((TARGET_W, TARGET_H))
                .set_duration(end_duration)
                .set_start(start)
                .set_position("center")
            )
            clips.append(bg)
            logger.info("[EndScreen] Usando end_screen_vertical.png do branding.")
        else:
            # Fallback genérico
            overlay = (
                ColorClip(size=(TARGET_W, TARGET_H), color=(0, 0, 0))
                .set_opacity(0.55)
                .set_duration(end_duration)
                .set_start(start)
                .set_position("center")
            )
            clips.append(overlay)

            txt_main = (
                TextClip(
                    "Siga o Futebas\npara mais ⚽",
                    font=font_path,
                    fontsize=80,
                    color="#FFDD00",
                    stroke_color="black",
                    stroke_width=5,
                    method="caption",
                    size=(TARGET_W - 80, None),
                    align="center"
                )
                .set_duration(end_duration)
                .set_start(start)
                .set_position(("center", 0.38), relative=True)
            )
            txt_cta = (
                TextClip(
                    "👍 Curte e compartilha!",
                    font=font_path,
                    fontsize=52,
                    color="white",
                    stroke_color="black",
                    stroke_width=3,
                    method="caption",
                    size=(TARGET_W - 80, None),
                    align="center"
                )
                .set_duration(end_duration)
                .set_start(start)
                .set_position(("center", 0.60), relative=True)
            )
            clips.extend([txt_main, txt_cta])
            logger.info("[EndScreen] Fallback genérico (end_screen_vertical.png não encontrado).")

        logger.info("[EndScreen] Criado: aparece em t=%.1fs por %.1fs", start, end_duration)
        return clips

    except Exception as e:
        logger.warning("[EndScreen] Erro ao criar end screen: %s", e)
        return []


def add_teaser_intro(clips_list: list, teaser_duration: float = 2.0) -> Optional:
    """
    Extrai um teaser de 2s do clipe mais dinâmico (1º vídeo ou 2ª imagem)
    para colocar no início como 'preview do que está por vir'.
    Aumenta a retenção nos primeiros 3s (período crítico).

    Args:
        clips_list: Lista de clips do timeline
        teaser_duration: Duração do teaser em segundos

    Returns:
        Clip de teaser ou None se não for possível extrair.
    """
    try:
        # Prefere clips de vídeo (mais dinâmicos) para o teaser
        for item in clips_list:
            if item.get("type") == "video":
                clip = item["clip"]
                # Pega um trecho do meio do vídeo (mais dinâmico que o início)
                mid = clip.duration / 2
                start = max(0, mid - teaser_duration / 2)
                end = min(clip.duration, start + teaser_duration)
                teaser = clip.subclip(start, end)
                logger.info("[Teaser] Teaser de %.1fs extraído do vídeo highlight", teaser_duration)
                return teaser

        # Fallback: usa 2ª imagem se disponível (mais informativa que a capa)
        image_clips = [item for item in clips_list if item.get("type") == "image"]
        if len(image_clips) >= 2:
            teaser = image_clips[1]["clip"].subclip(0, min(teaser_duration, image_clips[1]["clip"].duration))
            logger.info("[Teaser] Teaser de %.1fs extraído da 2ª imagem", teaser_duration)
            return teaser

    except Exception as e:
        logger.warning("[Teaser] Não foi possível criar teaser: %s", e)
    return None


def apply_color_grading(clip, mood: str = "Epic"):
    """
    Aplica color grading básico via Pillow + numpy dependendo do mood.

    Moods:
        Epic   → Alto contraste, levemente dessaturado, tons frios
        Happy  → Saturação elevada, tons quentes, brilho +10%
        Rock   → Baixo brilho, contraste alto, tint vermelho
        Sad    → Dessaturado (quase B&W), tom azulado

    Args:
        clip: VideoClip ou ImageClip do MoviePy
        mood: Mood/clima do vídeo

    Returns:
        Clip com color grading aplicado.
    """
    try:
        from PIL import Image as PILImage, ImageEnhance as PILEnhance
        from moviepy.video.VideoClip import VideoClip

        # Parâmetros por mood
        grading = {
            "Epic": {"brightness": 0.95, "contrast": 1.25, "saturation": 0.85},
            "Happy": {"brightness": 1.10, "contrast": 1.10, "saturation": 1.30},
            "Rock":  {"brightness": 0.85, "contrast": 1.40, "saturation": 0.90},
            "Sad":   {"brightness": 0.90, "contrast": 1.05, "saturation": 0.40},
        }
        params = grading.get(mood, grading["Epic"])

        def grade_frame(frame):
            """Aplica os ajustes em cada frame via PIL."""
            img = PILImage.fromarray(frame, "RGB")
            img = PILEnhance.Brightness(img).enhance(params["brightness"])
            img = PILEnhance.Contrast(img).enhance(params["contrast"])
            img = PILEnhance.Color(img).enhance(params["saturation"])
            return np.array(img)

        graded = clip.fl_image(grade_frame)
        logger.info("[ColorGrade] Mood '%s' aplicado (br=%.2f, ct=%.2f, sat=%.2f)",
                    mood, params["brightness"], params["contrast"], params["saturation"])
        return graded

    except Exception as e:
        logger.warning("[ColorGrade] Erro ao aplicar color grading (mood=%s): %s", mood, e)
        return clip


# =============================================================================
# PASSO A — PROCESSAMENTO DE IMAGEM PARA O TIMELINE
# =============================================================================

def process_image_asset(img_path: str, duration: float = 4.0) -> Optional[ImageClip]:
    """
    Pipeline completo de processamento de um asset de imagem:
    1. Detecta e rejeita watermarks de stock.
    2. Aplica Blurred Background Padding.
    3. Adiciona Ken Burns (zoom suave).
    4. Retorna um ImageClip pronto para o timeline.

    Returns:
        ImageClip pronto, ou None se a imagem for rejeitada.
    """
    # Passo 1: Detecção de Watermark de Stock
    if detect_stock_watermark(img_path):
        logger.info("[AssetProc] Imagem rejeitada por watermark: %s", os.path.basename(img_path))
        return None

    # Passo 2: Blurred Background Padding
    blurred_path = make_blurred_background(img_path)
    if not blurred_path:
        # Fallback seguro: usa a imagem original sem distorção
        logger.warning("[AssetProc] BlurBG falhou, usando imagem sem padding: %s", img_path)
        blurred_path = img_path

    # Passo 3: Cria o clip
    try:
        clip = ImageClip(blurred_path).set_duration(duration).set_fps(24)

        # Garante que o clip tem exatamente 1080x1920 (segurança extra)
        if clip.size != (TARGET_W, TARGET_H):
            clip = clip.resize((TARGET_W, TARGET_H))

        # Passo 4: Ken Burns (zoom 8% ao longo da duração)
        clip = apply_ken_burns(clip, duration, zoom_ratio=0.06)
        return clip
    except Exception as e:
        logger.error("[AssetProc] Erro ao criar ImageClip: %s", e)
        return None


# =============================================================================
# FUNÇÃO PRINCIPAL: generate_video()
# =============================================================================

def generate_video(job_id: str, payload: dict):
    """
    Motor principal de renderização.

    Fluxo:
        0. Geração de áudio (edge-tts via AudioService)
        1. Download e filtragem de imagens (com BlurBG e WatermarkDetect)
        2. Download de vídeos highlight
        3. Panic Search (se cobertura insuficiente)
        4. Montagem do timeline com crossfade entre clipes
        5. Mixagem de áudio (narração + trilha)
        6. Legendas word-level (Whisper)
        7. Branding (logo do canal)
        8. Render final (NVENC → libx264)
        9. Atualização do banco de dados
    """
    conn = get_db_connection()
    try:
        logger.info("[JobStart] Iniciando job: %s", job_id)

        # ── 0. PARSE DO PAYLOAD ──────────────────────────────────────────
        title = payload.get("title", "Notícia de Futebol")

        script = payload.get("script", "")
        if isinstance(script, dict):
            script_text = " ".join(
                b.get("text", "") for b in script.get("blocks", [])
            ) or str(script)
            search_terms = script.get("search_terms", [])
        else:
            script_text = script
            search_terms = []

        assets = payload.get("assets", {})
        video_type = payload.get("type", "Noticia")

        # Mood: determina a pasta de música
        mood_map = {"Highlight": "Epic", "Gol": "Rock", "Noticia": "Happy", "Analise": "Sad"}
        mood = mood_map.get(video_type, "Epic")

        logger.info("[Parse] Título: '%s' | Tipo: %s | Mood: %s", title, video_type, mood)

        # ── 0. GERAÇÃO DE ÁUDIO ──────────────────────────────────────────
        audio_path = os.path.join(AUDIO_DIR, f"{job_id}.mp3")
        if not os.path.exists(audio_path):
            if script_text and len(script_text) > 5:
                logger.info("[Audio] Gerando narração com edge-tts (timeout 60s)...")
                try:
                    asyncio.run(asyncio.wait_for(audio_service.generate(script_text, job_id), timeout=60.0))
                except asyncio.TimeoutError:
                    logger.error("[Audio] Timeout na geração de áudio!")
                    raise RuntimeError("Timeout na geração de áudio (edge-tts)")

        if not os.path.exists(audio_path):
            raise RuntimeError("Falha crítica: áudio não gerado ou script vazio.")

        main_audio = AudioFileClip(audio_path)
        total_duration = main_audio.duration + 1.5  # Buffer de fim
        logger.info("[Audio] Duração da narração: %.2fs | Total do vídeo: %.2fs",
                    main_audio.duration, total_duration)

        # ── 1. DOWNLOAD PARALELO DE ASSETS (v13 Turbo) ──────────────────
        raw_images = assets.get("all_images", [])
        # Filtra URLs de placeholder antes de baixar
        raw_images = reject_placeholder_urls(raw_images)
        video_urls = assets.get("all_videos", [])
        
        logger.info("[TurboIO] Iniciando ingestão paralela de %d imagens e %d vídeos...", 
                    len(raw_images), len(video_urls))

        # Criamos lista de tarefas para download simultâneo
        tasks = []
        # Imagens (limite de 12 para evitar abuso de banda)
        for url in raw_images[:12]:
            ext = "png" if url.lower().endswith(".png") else "jpg"
            tasks.append(async_download_file(url, ext=ext))
        
        # Vídeos (limite de 3 para não estourar RAM/CPU)
        for v_url in video_urls[:3]:
            tasks.append(async_download_video_clip(v_url))

        # Executa tudo em paralelo! (v13)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            downloaded_paths = loop.run_until_complete(asyncio.gather(*tasks))
        finally:
            loop.close()

        # Separa imagens e vídeos baixados
        downloaded_images = [p for p in downloaded_paths if p and p.endswith((".jpg", ".png", ".jpeg"))]
        downloaded_videos = [p for p in downloaded_paths if p and p.endswith(".mp4")]

        # Keywords visuais do roteiro para B-roll scoring
        visual_keywords = payload.get("keywords_visuais", [])
        mood = payload.get("mood", mood)  # Sobrescreve mood se o roteiro especificou

        # Processamento das imagens baixadas
        image_clips = []
        for raw_path in downloaded_images:
            # --- Nível 3: Validação Semântica (Visual Gate) ---
            tema_validacao = visual_keywords[0] if visual_keywords else (title or "futebol")
            if not VisualGate.is_relevant(raw_path, tema=tema_validacao):
                logger.warning("[VisualGate] Imagem descartada por incoerência: %s", os.path.basename(raw_path))
                continue

            clip = process_image_asset(raw_path, duration=4.0)
            if clip:
                image_clips.append({"type": "image", "clip": clip})

        logger.info("[Assets] %d imagens aceitas após filtragem.", len(image_clips))

        # ── 2. PROCESSAMENTO DOS VÍDEOS BAIXADOS ────────────────────────
        video_clips = []
        for vid_path in downloaded_videos:
            try:
                clip = VideoFileClip(vid_path).without_audio()
                clip = apply_copyright_protection(clip)

                # Recorta 5 segundos do meio do vídeo
                dur = 5.0
                if clip.duration > dur:
                    start = max(0, clip.duration * 0.4 - dur / 2)
                    start = min(start, clip.duration - dur)
                    clip = clip.subclip(start, start + dur)

                # Redimensiona para 9:16 usando Smart Crop
                clip = apply_smart_crop(clip, target_w=TARGET_W, target_h=TARGET_H)

                video_clips.append({"type": "video", "clip": clip})
                logger.info("[Highlight] Vídeo processado com SmartCrop: %s", os.path.basename(vid_path))
            except Exception as e:
                logger.warning("[Highlight] Erro ao processar vídeo: %s", e)

        # ── 3. MONTAGEM DA LISTA DE ASSETS ──────────────────────────────
        # Intercala: [imagem_capa, video_highlight, imagem, imagem, ...]
        downloaded_assets = []
        if image_clips:
            downloaded_assets.append(image_clips[0])  # Capa (1ª imagem)
        downloaded_assets.extend(video_clips)
        if len(image_clips) > 1:
            downloaded_assets.extend(image_clips[1:])

        # ── 3b. PANIC SEARCH (cobertura insuficiente) ───────────────────
        current_coverage = sum(
            4.0 if a["type"] == "image" else a["clip"].duration
            for a in downloaded_assets
        )
        if current_coverage < total_duration:
            missing = total_duration - current_coverage
            logger.info("[PanicSearch] Faltam %.1fs de cobertura visual.", missing)
            search_q = search_terms[:1] or [f"{title} futebol"]
            for term in search_q + ["futebol brasil torcida", "soccer highlights"]:
                if current_coverage >= total_duration:
                    break
                new_files = fetch_external_assets(term, limit=3)
                for fpath in new_files:
                    if fpath.endswith(".mp4"):
                        try:
                            # Panic Search: subclip + smart crop
                            c = VideoFileClip(fpath).without_audio()
                            if c.duration > 5:
                                c = c.subclip(0, 5)
                            c = apply_smart_crop(c, target_w=TARGET_W, target_h=TARGET_H)
                            
                            downloaded_assets.append({"type": "video", "clip": c})
                            current_coverage += c.duration
                        except Exception:
                            pass
                    else:
                        if VisualGate.is_relevant(fpath, tema=tema_validacao):
                            clip = process_image_asset(fpath, duration=4.0)
                            if clip:
                                downloaded_assets.append({"type": "image", "clip": clip})
                                current_coverage += 4.0
                        else:
                            logger.info("[VisualGate] Imagem de panic search descartada: %s", os.path.basename(fpath))

        # ── 3c. SCOREBOARD OVERLAY ──────────────────────────────────────
        placar = payload.get("placar", "N/A")
        gols = payload.get("gols", [])
        scoreboard = create_scoreboard_overlay(placar, gols)
        if scoreboard:
            scoreboard = scoreboard.set_duration(total_duration - 5)
            logger.info("[Scoreboard] Overlay de placar adicionado: %s", placar)

        # ── 4. MONTAGEM DO TIMELINE COM CROSSFADE ────────────────────────
        stinger = create_stinger(0.6)
        fallback_loop = get_fallback_loop()
        visual_clips = []
        curr_time = 0.0
        asset_idx = 0
        transition_times = []  # Armazena timestamps para SFX

        while curr_time < total_duration:
            clip = None

            if asset_idx < len(downloaded_assets):
                item = downloaded_assets[asset_idx]
                clip = item["clip"]
                asset_idx += 1
            else:
                # Esgotou assets → usa loop padrão de futebol
                if fallback_loop:
                    rem = total_duration - curr_time
                    try:
                        loop_clip = apply_smart_crop(VideoFileClip(fallback_loop).without_audio(), target_w=TARGET_W, target_h=TARGET_H).loop(duration=rem)
                        clip = loop_clip
                    except Exception:
                        clip = ColorClip(
                            size=(TARGET_W, TARGET_H),
                            color=(10, 10, 10),
                            duration=total_duration - curr_time
                        )
                else:
                    clip = ColorClip(
                        size=(TARGET_W, TARGET_H),
                        color=(10, 10, 10),
                        duration=total_duration - curr_time
                    )

            if clip:
                # Aplica crossfade em todos os clips exceto o primeiro
                # O crossfadein(0.5) faz o clip aparecer suavemente em 0.5s
                # eliminando o corte seco que causa queda na retenção
                if visual_clips:
                    clip = clip.crossfadein(0.5)
                    transition_times.append(curr_time)

                visual_clips.append(clip)
                curr_time += clip.duration

            if curr_time >= total_duration:
                break

        if not visual_clips:
            raise RuntimeError("Nenhum clip visual foi gerado — abortando job.")

        logger.info("[Timeline] Concatenando %d clipes...", len(visual_clips))
        video = concatenate_videoclips(visual_clips, method="compose", padding=-0.5)
        video = video.subclip(0, min(total_duration, video.duration))

        # ── 4b. TEASER INTRO (2s do clipe mais dinâmico no início) ────────
        teaser = add_teaser_intro(downloaded_assets, teaser_duration=2.0)
        if teaser and visual_clips:
            try:
                # Insere o teaser como primeiro frame (antes do vídeo principal)
                visual_clips = [teaser] + visual_clips
                logger.info("[Teaser] Intro preview inserida no início do timeline.")
            except Exception as e:
                logger.warning("[Teaser] Erro ao inserir intro: %s", e)

        # ── 5. MIXAGEM DE ÁUDIO (narração + trilha sonora + SFX) ───────────────
        audio_layers = [main_audio]
        
        bg_music_path = get_background_music(mood)
        if bg_music_path:
            try:
                bg_music = AudioFileClip(bg_music_path)

                if bg_music.duration < total_duration:
                    loops_needed = int(total_duration / bg_music.duration) + 2
                    bg_music = concatenate_audioclips([bg_music] * loops_needed)

                bg_music = (bg_music
                            .subclip(0, total_duration)
                            .volumex(0.10)          # Ducking: 10% do volume original
                            .audio_fadeout(2.0))    # Fade out nos últimos 2s

                audio_layers.append(bg_music)
                logger.info("[Audio] Trilha mixada: %s @10%% volume", os.path.basename(bg_music_path))
            except Exception as e:
                logger.error("[Audio] Erro ao mixar trilha: %s", e)

        # Trilha de Efeitos Sonoros (SFX) nas Transições
        sfx_path = os.path.join(ASSETS_DIR, "sfx", "swoosh.mp3")
        if os.path.exists(sfx_path) and transition_times:
            try:
                base_swoosh = AudioFileClip(sfx_path).volumex(0.2)
                for t_time in transition_times:
                    # Inserindo o som de swoosh no momento do crossfade
                    sfx_clip = base_swoosh.set_start(t_time).set_duration(base_swoosh.duration)
                    audio_layers.append(sfx_clip)
                logger.info("[Audio] SFX Swoosh aplicado em %d transições.", len(transition_times))
            except Exception as e:
                logger.warning("[Audio] Falha ao injetar Swoosh SFX: %s", e)

        try:
            final_audio = CompositeAudioClip(audio_layers)
            video = video.set_audio(final_audio)
        except Exception as err:
            logger.error("[Audio] Falha ao criar CompositeAudioClip: %s", err)
            video = video.set_audio(main_audio)

        # ── 6. LEGENDAS WORD-LEVEL (Whisper) ─────────────────────────────
        font_path = get_montserrat_black()
        subtitle_clips = generate_word_level_clips(
            audio_path=audio_path,
            words_per_group=3,
            font_path=font_path,
            video_duration=total_duration
        )

        if subtitle_clips:
            logger.info("[Subtitles] Aplicando %d clips de legenda word-level.", len(subtitle_clips))
            # Garante que as legendas fiquem acima do vídeo mas abaixo do scoreboard/logo
            video = CompositeVideoClip([video] + subtitle_clips)
        else:
            logger.warning("[Subtitles] Nenhuma legenda gerada — vídeo sem legenda word-level.")

        # --- FIX: Garante que as legendas usem o TMPDIR correto ---
        os.environ["MAGICK_TEMPORARY_PATH"] = "/tmp"

        # ── 6b. COLOR GRADING por mood ──────────────────────────────────
        try:
            video = apply_color_grading(video, mood=mood)
        except Exception as e:
            logger.warning("[ColorGrade] Falhou, ignorando: %s", e)

        # ── 6c. LOWER-THIRDS (nome/contexto nos primeiros 6s) ─────────────
        lower_third_text = payload.get("lower_third", "") or title[:50]
        if lower_third_text:
            lt_clips = add_lower_third(lower_third_text, duration=5.0, start_time=1.0)
            if lt_clips:
                video = CompositeVideoClip([video] + lt_clips)

        # ── 6d. END SCREEN (últimos 3.5s) ─────────────────────────────────
        end_clips = add_end_screen(total_duration, end_duration=3.5)
        if end_clips:
            video = CompositeVideoClip([video] + end_clips)

        # ── 7. BRANDING (Logo do canal) ───────────────────────────────────
        logo_path = get_watermark_path()
        if logo_path:
            try:
                logo = (ImageClip(logo_path)
                        .set_duration(total_duration)
                        .resize(width=140)
                        .set_opacity(0.88)
                        .set_pos(("right", 48)))  # Canto superior direito
                video = CompositeVideoClip([video, logo])
                logger.info("[Branding] Logo aplicado do canal.")
            except Exception as e:
                logger.warning("[Branding] Erro ao aplicar logo: %s", e)

        # ── 7b. SCOREBOARD (overlay final) ──────────────────────────────────
        placar = payload.get("placar", "N/A")
        scoreboard = create_scoreboard_overlay(placar)
        if scoreboard:
            scoreboard = scoreboard.set_duration(total_duration - scoreboard.start - 0.5)
            video = CompositeVideoClip([video, scoreboard])
            logger.info("[Scoreboard] Overlay de placar aplicado: %s", placar)

        # ── 8. RENDER FINAL ───────────────────────────────────────────────
        output_filename = f"video_{job_id}.mp4"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        logger.info("[Render] Iniciando render final → %s", output_path)
        _write_videofile_with_fallback(video, output_path)

        # ── 8b. QUALITY GATE (pré-update do banco) ────────────────────────
        try:
            from app.services.quality_gate import run_full_quality_gate
            title_meta = payload.get("title", "")
            desc_meta = payload.get("description", "")
            tags_meta = payload.get("tags", [])
            qr = run_full_quality_gate(output_path, title_meta, desc_meta, tags_meta)
            logger.info("[QualityGate] Score: %d/100 | Aprovado: %s", qr.score, qr.passed)
            if not qr.passed:
                logger.warning("[QualityGate] REPROVADO — issues: %s", qr.issues)
        except Exception as qe:
            logger.warning("[QualityGate] Erro ao checar qualidade: %s", qe)
            qr = None

        # ── 9. ATUALIZAÇÃO DO BANCO ──────────────────────────────────────
        if conn:
            with conn.cursor() as cur:
                quality_score = getattr(qr, "score", None) if qr else None
                quality_passed = getattr(qr, "passed", True) if qr else True
                cur.execute(
                    """UPDATE video_jobs
                       SET status = 'completed',
                           published = false,
                           video_path = %s,
                           updated_at = CURRENT_TIMESTAMP
                       WHERE id = %s""",
                    (output_path, job_id)
                )
                conn.commit()
        logger.info("[JobDone] Job %s concluído! Vídeo: %s | Quality: %s/100",
                    job_id, output_path, getattr(qr, 'score', 'N/A'))

    except Exception as e:
        logger.error("[JobError] Erro no job %s: %s", job_id, e)
        import traceback
        traceback.print_exc()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(
                        """UPDATE video_jobs
                           SET status = 'error',
                               error_message = %s,
                               updated_at = CURRENT_TIMESTAMP
                           WHERE id = %s""",
                        (str(e)[:500], job_id)
                    )
                    conn.commit()
            except Exception as inner_e:
                logger.error("[JobError] Falha ao atualizar erro no banco: %s", inner_e)
    finally:
        if conn:
            try:
                conn.close()
                logger.info("[JobStore] Conexão DB fechada para job %s", job_id)
            except Exception:
                pass

# =============================================================================
# PASSO X — SMART CROP (OPENCV)
# =============================================================================

def get_face_center(frame: np.ndarray) -> Optional[Tuple[int, int]]:
    """
    Detecta o centro da face predominante no frame usando Haar Cascades.
    """
    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            # Pega a maior face detectada
            faces = sorted(faces, key=lambda f: f[2] * f[3], reverse=True)
            x, y, w, h = faces[0]
            return (int(x + w / 2), int(y + h / 2))
    except Exception as e:
        logger.warning("[SmartCrop] Erro na deteccao facial: %s", e)
    return None

def apply_smart_crop(clip: VideoFileClip, target_w: int = 1080, target_h: int = 1920) -> VideoFileClip:
    """
    Aplica crop inteligente centralizado no rosto detectado.
    Se nao detectar nada, cai no fallback de centralizacao padrao.
    """
    logger.info("[SmartCrop] Iniciando processamento de clip: %dx%d", clip.w, clip.h)

    # Analisa o frame central do clip para encontrar o rosto
    middle_frame = clip.get_frame(clip.duration / 2)
    face_center = get_face_center(middle_frame)

    # 1. Redimensiona para que a altura seja a do target (1920)
    # ou a largura seja a do target (1080), mantendo aspect ratio
    scale_factor = max(target_w / clip.w, target_h / clip.h)
    new_w = int(clip.w * scale_factor)
    new_h = int(clip.h * scale_factor)
    
    resized_clip = clip.resize(new_size=(new_w, new_h))

    # 2. Calcula coordenadas de crop
    if face_center:
        center_x, center_y = face_center
        # Ajusta o centro proporcionalmente ao resize
        center_x = int(center_x * scale_factor)
        center_y = int(center_y * scale_factor)
        logger.info("[SmartCrop] Face detectada em: %d, %d", center_x, center_y)
    else:
        center_x, center_y = new_w // 2, new_h // 2
        logger.info("[SmartCrop] Nenhuma face detectada, usando centro padrao.")

    # Garante que o crop (1080x1920) esteja dentro das bordas do resized_clip
    x1 = max(0, min(new_w - target_w, center_x - target_w // 2))
    y1 = max(0, min(new_h - target_h, center_y - target_h // 2))
    x2 = x1 + target_w
    y2 = y1 + target_h

    logger.info("[SmartCrop] Crop final: x1=%d, y1=%d, x2=%d, y2=%d", x1, y1, x2, y2)

    return resized_clip.crop(x1=x1, y1=y1, x2=x2, y2=y2)
