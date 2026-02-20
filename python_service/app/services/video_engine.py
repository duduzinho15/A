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
import edge_tts
import json
import numpy as np
from typing import List, Optional, Tuple, Union
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

from app.config import settings
from app.utils.database import get_db_connection
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
    """Retorna o path do logo/watermark do canal."""
    for name in ["watermark.png", "logo.png", "Logo.png"]:
        path = os.path.join(OVERLAYS_DIR, name)
        if os.path.exists(path):
            return path
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


# =============================================================================
# PASSO A — BLURRED BACKGROUND PADDING (O coração do refactoring visual)
# =============================================================================

def make_blurred_background(img_path: str) -> Optional[str]:
    """
    Transforma qualquer imagem 16:9 (ou qualquer aspect ratio) em um frame
    9:16 (1080x1920) profissional, sem bordas pretas e sem esticamento.

    MATEMÁTICA DO REDIMENSIONAMENTO:
    ─────────────────────────────────
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

        # Salva em temp
        out_path = os.path.join(TEMP_DIR, f"blur_bg_{uuid.uuid4().hex}.jpg")
        canvas.save(out_path, "JPEG", quality=90)
        logger.info("[BlurBG] Gerado: %s (frente=%dx%d @ y=%d)",
                    os.path.basename(out_path), front_w, front_h, paste_y)
        return out_path

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
        for group in groups:
            try:
                txt_clip = (
                    TextClip(
                        group["text"],
                        font=font_path,
                        fontsize=72,
                        color="#FFDD00",          # Amarelo da marca Futebas
                        stroke_color="black",
                        stroke_width=5,           # Borda preta grossa para legibilidade
                        method="caption",
                        size=(int(TARGET_W * 0.88), None),  # 88% da largura → margens laterais
                        align="center"
                    )
                    .set_start(group["start"])
                    .set_duration(group["duration"])
                    .set_position(("center", 0.75), relative=True)  # Safe zone inferior
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
    O ultrafast preset é necessário para CPU — velocidade > qualidade perfeita.
    """
    try:
        logger.info("[Render] Tentando NVENC (GPU)...")
        video.write_videofile(
            output_path, fps=24, codec="h264_nvenc", audio_codec="aac",
            threads=4, preset="p5",
            ffmpeg_params=["-gpu", "0", "-rc:v", "vbr", "-cq", "23",
                           "-b:v", "6M", "-maxrate", "10M", "-bufsize", "12M",
                           "-pix_fmt", "yuv420p", "-profile:v", "high"],
        )
        logger.info("[Render] Finalizado com NVENC.")
    except Exception as gpu_exc:
        logger.warning("[Render] NVENC indisponível (%s), usando CPU (libx264)...", gpu_exc)
        video.write_videofile(
            output_path, fps=24, codec="libx264", audio_codec="aac",
            threads=4, preset="ultrafast",
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
            # 0 → 0.1, meio → 1.5, fim → 0.1
            if t < duration / 2:
                return 0.1 + 1.4 * (t / (duration / 2))
            return 1.5 - 1.4 * ((t - duration / 2) / (duration / 2))

        stinger = logo.resize(scale_effect).set_position("center")
        bg = ColorClip(size=(TARGET_W, TARGET_H), color=(0, 0, 0), duration=duration).set_opacity(0.3)
        return CompositeVideoClip([bg, stinger]).set_duration(duration)
    except Exception as e:
        logger.warning("[Stinger] Erro: %s", e)
        return None


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
                logger.info("[Audio] Gerando narração com edge-tts...")
                asyncio.run(audio_service.generate(script_text, job_id))

        if not os.path.exists(audio_path):
            raise RuntimeError("Falha crítica: áudio não gerado ou script vazio.")

        main_audio = AudioFileClip(audio_path)
        total_duration = main_audio.duration + 1.5  # Buffer de fim
        logger.info("[Audio] Duração da narração: %.2fs | Total do vídeo: %.2fs",
                    main_audio.duration, total_duration)

        # ── 1. DOWNLOAD E FILTRAGEM DE IMAGENS ──────────────────────────
        raw_images = assets.get("all_images", [])
        logger.info("[Assets] Processando %d imagens do payload...", len(raw_images))

        image_clips = []
        for url in raw_images[:12]:  # Limite de 12 imagens para não travar
            # Ignora URLs de placeholder genéricas
            if "dummyimage" in url or "placeholder" in url:
                logger.info("[Assets] URL de placeholder ignorada: %s", url)
                continue

            ext = "png" if url.lower().endswith(".png") else "jpg"
            raw_path = download_file(url, ext=ext)
            if not raw_path:
                continue

            clip = process_image_asset(raw_path, duration=4.0)
            if clip:
                image_clips.append({"type": "image", "clip": clip})

        logger.info("[Assets] %d imagens aceitas após filtragem.", len(image_clips))

        # ── 2. DOWNLOAD DE VÍDEOS HIGHLIGHT ─────────────────────────────
        video_clips = []
        video_urls = assets.get("all_videos", [])
        for vid_url in video_urls[:3]:  # Máximo 3 highlights
            vid_path = download_video_clip(vid_url)
            if vid_path and os.path.exists(vid_path):
                try:
                    clip = VideoFileClip(vid_path).without_audio()
                    clip = apply_copyright_protection(clip)

                    # Recorta 5 segundos do meio do vídeo (parte mais dinâmica)
                    dur = 5.0
                    if clip.duration > dur:
                        # Começa a 40% do vídeo para pegar o "melhor momento"
                        start = max(0, clip.duration * 0.4 - dur / 2)
                        start = min(start, clip.duration - dur)
                        clip = clip.subclip(start, start + dur)

                    # Redimensiona para 9:16 sem esticar: crop central
                    clip = (clip
                           .resize(height=TARGET_H)
                           .crop(width=TARGET_W, height=TARGET_H,
                                 x_center=clip.w / 2, y_center=TARGET_H / 2))
                    video_clips.append({"type": "video", "clip": clip})
                    logger.info("[Highlight] Vídeo processado: %s", os.path.basename(vid_path))
                    break  # Um highlight é suficiente para o primeiro slot
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
                            c = (VideoFileClip(fpath).without_audio()
                                 .resize(height=TARGET_H)
                                 .crop(width=TARGET_W, height=TARGET_H,
                                       x_center=TARGET_W / 2, y_center=TARGET_H / 2))
                            if c.duration > 5:
                                c = c.subclip(0, 5)
                            downloaded_assets.append({"type": "video", "clip": c})
                            current_coverage += c.duration
                        except Exception:
                            pass
                    else:
                        clip = process_image_asset(fpath, duration=4.0)
                        if clip:
                            downloaded_assets.append({"type": "image", "clip": clip})
                            current_coverage += 4.0

        # ── 4. MONTAGEM DO TIMELINE COM CROSSFADE ────────────────────────
        stinger = create_stinger(0.6)
        fallback_loop = get_fallback_loop()
        visual_clips = []
        curr_time = 0.0
        asset_idx = 0

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
                        loop_clip = (VideoFileClip(fallback_loop)
                                     .resize(height=TARGET_H)
                                     .crop(width=TARGET_W, height=TARGET_H,
                                           x_center=TARGET_W / 2, y_center=TARGET_H / 2)
                                     .without_audio()
                                     .loop(duration=rem))
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

                visual_clips.append(clip)
                curr_time += clip.duration

            if curr_time >= total_duration:
                break

        if not visual_clips:
            raise RuntimeError("Nenhum clip visual foi gerado — abortando job.")

        logger.info("[Timeline] Concatenando %d clipes...", len(visual_clips))
        video = concatenate_videoclips(visual_clips, method="compose", padding=-0.5)
        video = video.subclip(0, min(total_duration, video.duration))

        # ── 5. MIXAGEM DE ÁUDIO (narração + trilha sonora) ───────────────
        bg_music_path = get_background_music(mood)
        if bg_music_path:
            try:
                bg_music = AudioFileClip(bg_music_path)

                # Loop robusto: calcula quantas repetições são necessárias
                # e concatena para cobrir toda a duração do vídeo.
                # Motivo: audio_loop() pode ter bugs em versões antigas do moviepy.
                if bg_music.duration < total_duration:
                    loops_needed = int(total_duration / bg_music.duration) + 2
                    bg_music = concatenate_audioclips([bg_music] * loops_needed)

                bg_music = (bg_music
                            .subclip(0, total_duration)
                            .volumex(0.10)          # Ducking: 10% do volume original
                            .audio_fadeout(2.0))    # Fade out nos últimos 2s

                final_audio = CompositeAudioClip([main_audio, bg_music])
                video = video.set_audio(final_audio)
                logger.info("[Audio] Trilha mixada: %s @10%% volume", os.path.basename(bg_music_path))
            except Exception as e:
                logger.error("[Audio] Erro ao mixar trilha, usando só narração: %s", e)
                video = video.set_audio(main_audio)
        else:
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
            video = CompositeVideoClip([video] + subtitle_clips)
        else:
            logger.warning("[Subtitles] Nenhuma legenda gerada — vídeo sem legenda word-level.")

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

        # ── 8. RENDER FINAL ───────────────────────────────────────────────
        output_filename = f"video_{job_id}.mp4"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        logger.info("[Render] Iniciando render final → %s", output_path)
        _write_videofile_with_fallback(video, output_path)

        # ── 9. ATUALIZAÇÃO DO BANCO ──────────────────────────────────────
        if conn:
            with conn.cursor() as cur:
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
        logger.info("[JobDone] Job %s concluído com sucesso! Vídeo: %s", job_id, output_path)

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
            except Exception:
                pass
    finally:
        if conn:
            conn.close()
