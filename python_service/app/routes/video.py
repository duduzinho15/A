# =============================================================================
# app/routes/video.py — Motor de Renderização de Vídeo (Fase 5 - B-roll & SEO)
# =============================================================================
import os
import uuid
import random
import numpy as np
from typing import Optional, List
from fastapi import APIRouter
from pydantic import BaseModel
from moviepy.editor import ImageClip, AudioFileClip, VideoFileClip, CompositeVideoClip, TextClip, concatenate_videoclips, ColorClip
import moviepy.video.fx.all as vfx
import asyncio
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from PIL import Image
try:
    if not hasattr(Image, 'ANTIALIAS'):
        Image.ANTIALIAS = Image.LANCZOS
except:
    pass # Pillow 10+ fixes
from app.config import settings
from app.utils.errors import ServicoExterno

router = APIRouter(prefix="/video", tags=["vídeo"])

# Diretórios
OUTPUT_DIR = os.path.join(settings.DATA_MIDIA, "videos")
BROLL_DIR = os.path.join(settings.DATA_MIDIA, "broll")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(BROLL_DIR, exist_ok=True)

class Subtitle(BaseModel):
    text: str
    start: float
    end: float
    highlight: bool = False # Se true, texto maior/cor diferente

class Asset(BaseModel):
    type: str  # "image", "video", "broll"
    path: Optional[str] = None
    category: Optional[str] = "geral" # usado para busca em broll
    duration: float
    text_overlay: Optional[str] = None # Texto de impacto para este clip (SEO)

class VideoRenderRequest(BaseModel):
    audio_path: str
    assets: List[Asset] # Lista de clipes sequenciais
    subtitles: Optional[List[Subtitle]] = None
    title: Optional[str] = "Video Gerado"
    format: str = "16:9" # "16:9" (Youtube) ou "9:16" (Shorts/TikTok)
    style: str = "news" # "news", "shorts_viral", "documentary"

class VideoResponse(BaseModel):
    status: str
    video_path: str
    duration_seconds: float
    file_size_mb: float

# ---------------------------------------------------------------------------
# Helpers de Composição
# ---------------------------------------------------------------------------

def apply_zoom_pan(clip, duration, zoom_ratio=0.15):
    """Efeito Ken Burns (Zoom in)."""
    def zoom(t):
        return 1 + zoom_ratio * (t / duration)
    return clip.resize(zoom)

def get_local_broll(category: str, duration: float, target_res: tuple) -> VideoFileClip:
    """Busca um clipe de vídeo aleatório na pasta da categoria."""
    # Busca recursiva ou direta
    search_paths = [os.path.join(BROLL_DIR, category), BROLL_DIR]
    files = []
    
    for p in search_paths:
        if os.path.exists(p):
            files.extend([os.path.join(p, f) for f in os.listdir(p) if f.lower().endswith(('.mp4', '.mov', '.avi'))])
    
    if not files:
        # Fallback para cor sólida se não achar
        return ColorClip(size=target_res, color=(20, 20, 25), duration=duration)
    
    chosen = random.choice(files)
    try:
        clip = VideoFileClip(chosen).without_audio()
        
        # Lógica de loop ou corte
        if clip.duration < duration:
            clip = vfx.loop(clip, duration=duration)
        else:
            # Pega trecho aleatório
            max_start = max(0, clip.duration - duration)
            start_t = random.uniform(0, max_start)
            clip = clip.subclip(start_t, start_t + duration)
            
        # Resize e Crop central (Fill)
        # Calcula ratio
        clip_ratio = clip.w / clip.h
        target_ratio = target_res[0] / target_res[1]
        
        if clip_ratio > target_ratio:
            # Clip mais largo que alvo, ajusta altura e corta laterais
            clip = clip.resize(height=target_res[1])
            clip = clip.crop(x_center=clip.w/2, width=target_res[0])
        else:
            # Clip mais alto/estreito, ajusta largura e corta topo/base
            clip = clip.resize(width=target_res[0])
            clip = clip.crop(y_center=clip.h/2, height=target_res[1])
            
        return clip
    except Exception as e:
        print(f"[Video] Erro processando broll {chosen}: {e}")
        return ColorClip(size=target_res, color=(30, 0, 0), duration=duration)

def create_impact_text(text: str, duration: float, resolution: tuple) -> TextClip:
    """Cria overlay de texto impactante (Estilo Shorts)."""
    # Tenta usar fonte do sistema ou default
    font = 'Arial-Bold'
    if os.path.exists("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        font = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        
    fontsize = 90 if resolution[0] < resolution[1] else 110 # Maior em vertical
    
    txt_clip = TextClip(
        text.upper(),
        fontsize=fontsize,
        color='yellow',
        font=font,
        stroke_color='black',
        stroke_width=4,
        size=(resolution[0]*0.9, None), # Wrap width
        method='caption',
        align='center'
    ).set_duration(duration).set_position(('center', 'center'))
    
    return txt_clip

# ---------------------------------------------------------------------------
# Helper de Timeout
# ---------------------------------------------------------------------------

async def render_with_timeout(func, *args):
    """Executa função bloqueante em thread separada com timeout."""
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        return await loop.run_in_executor(pool, func, *args)


# ---------------------------------------------------------------------------
# Endpoint Principal
# ---------------------------------------------------------------------------

def _render_logic_internal(req: VideoRenderRequest):
    try:
        if not os.path.exists(req.audio_path):
            raise ServicoExterno(f"Áudio não encontrado: {req.audio_path}", url="/video/render")
            raise ServicoExterno(f"Áudio não encontrado: {req.audio_path}", url="/video/render")

        filename = f"video_{req.style}_{uuid.uuid4().hex[:8]}.mp4"
        filepath = os.path.join(OUTPUT_DIR, filename)

        audio_clip = AudioFileClip(req.audio_path)
        
        # Definição de Resolução
        width, height = (1080, 1920) if req.format == "9:16" else (1920, 1080)
        resolution = (width, height)
        
        # SEO Shorts: Cortes mais rápidos? 
        # A request já traz assets com durações. Se style="shorts_viral", poderiamos forçar max duration.
        # Mas vamos respeitar o request do n8n/planner.

        # 1. Processa a lista de Assets (Video Track)
        clips = []
        current_time = 0.0
        
        # Ordenação inteligente (Ensemble simples de Thumb/Intro)
        # Se tiver style="shorts", garantir que o primeiro clip seja impactante (ex: imagem com texto ou broll forte)
        # Por enquanto, confiamos na ordem da request.

        for i, asset in enumerate(req.assets):
            # Se duração não definida, calcula baseada no audio full / num assets (fallback)
            duration = asset.duration if asset.duration > 0 else 3.0
            
            # Limita duração apenas se for excessiva e o estilo for shorts
            if req.style == "shorts_viral" and duration > 3.0 and asset.type == "broll":
                 duration = 2.0 # Cortes rápidos em B-roll
            
            clip = None
            
            # TIPO: VÍDEO PRÓPRIO
            if asset.type == "video" and asset.path and os.path.exists(asset.path):
                clip = VideoFileClip(asset.path).without_audio()
                # Ajuste de tempo
                if clip.duration < duration:
                    clip = vfx.loop(clip, duration=duration)
                else:
                    clip = clip.subclip(0, duration)
                
                # Resize/Crop to fill
                clip_ratio = clip.w / clip.h
                target_ratio = width / height
                if clip_ratio > target_ratio:
                    clip = clip.resize(height=height).crop(x_center=clip.w/2, width=width)
                else:
                    clip = clip.resize(width=width).crop(y_center=clip.h/2, height=height)

            # TIPO: IMAGEM
            elif asset.type == "image" and asset.path and os.path.exists(asset.path):
                clip = ImageClip(asset.path).set_duration(duration)
                # Resize/Crop
                clip_ratio = clip.w / clip.h
                target_ratio = width / height
                if clip_ratio > target_ratio:
                    clip = clip.resize(height=height).crop(x_center=clip.w/2, width=width)
                else:
                    clip = clip.resize(width=width).crop(y_center=clip.h/2, height=height)
                
                # Ken Burns Effect (Zoom lento)
                clip = apply_zoom_pan(clip, duration)
            
            # TIPO: BROLL / FALLBACK
            else:
                cat = asset.category or "futebol"
                clip = get_local_broll(cat, duration, resolution)
            
            # TEXT OVERLAY (Para cada clip individual - HOOK VISUAL)
            if asset.text_overlay:
                txt = create_impact_text(asset.text_overlay, duration, resolution)
                clip = CompositeVideoClip([clip, txt]).set_duration(duration)

            clips.append(clip)
            current_time += duration
            
            # Se já passamos do áudio, paramos (opcional, ou fazemos loop audio)
            if current_time >= audio_clip.duration + 2: 
                break 

        # 2. Concatena base visual
        if not clips:
             raise ServicoExterno("Nenhum clip válido gerado.", url="/video/render")
             
        visual_track = concatenate_videoclips(clips, method="compose")
        
        # Ajusta duração exata ao áudio (Fade out no final se vídeo for maior)
        if visual_track.duration > audio_clip.duration:
            visual_track = visual_track.subclip(0, audio_clip.duration)
            visual_track = visual_track.fadeout(0.5)
        # Se vídeo for menor, loopa ou não (deixa tela preta? Melhor não. User garante assets suficientes)
        
        # 3. Legendas Globais (Sync com Áudio)
        final_layers = [visual_track]
        
        if req.subtitles:
            for sub in req.subtitles:
                # Estilo de legenda SEO (Palavra por palavra seria ideal, mas frase é ok)
                # Fundo semi-transparente para legibilidade
                font_size = 60 if req.format == "9:16" else 50
                
                # Check for highlight
                color = 'yellow' if sub.highlight else 'white'
                
                txt_c = TextClip(
                    sub.text,
                    fontsize=font_size,
                    color=color,
                    font='Arial-Bold', # Tenta usar fonte padrão do imagemagick
                    stroke_color='black',
                    stroke_width=2,
                    size=(width*0.8, None),
                    method='caption',
                    align='center'
                ).set_start(sub.start).set_end(sub.end).set_position(('center', height*0.75 if req.format == "9:16" else height*0.85))
                
                final_layers.append(txt_c)

        final_comp = CompositeVideoClip(final_layers)

        # 4. Exportação
        final_video = final_comp.set_audio(audio_clip)
        
        # Parametros otimizados com fallback automatico para CPU.
        try:
            final_video.write_videofile(
                filepath,
                fps=30,
                codec="h264_nvenc",
                audio_codec="aac",
                threads=4, # Multithreading
                preset="p4", # GPU efficient preset
                ffmpeg_params=[
                    "-gpu", "0",
                    "-rc:v", "vbr",
                    "-cq", "23",
                    "-b:v", "6000k",
                    "-maxrate", "10000k",
                    "-bufsize", "12000k",
                    "-pix_fmt", "yuv420p",
                    "-profile:v", "high"
                ],
                verbose=True,
                logger='bar' # Barra de progresso visivel nos logs
            )
        except Exception as gpu_exc:
            print(f"[Video] NVENC indisponivel, fallback para libx264: {gpu_exc}")
            final_video.write_videofile(
                filepath,
                fps=30,
                codec="libx264",
                audio_codec="aac",
                threads=4,
                preset="veryfast",
                ffmpeg_params=[
                    "-pix_fmt", "yuv420p",
                    "-profile:v", "high"
                ],
                verbose=True,
                logger='bar'
            )

        # Cleanup
        audio_clip.close()
        for c in clips: 
            try: c.close()
            except: pass

        file_size = os.path.getsize(filepath) / (1024 * 1024)

        return {
            "status": "sucesso",
            "video_path": filepath,
            "duration_seconds": audio_clip.duration,
            "file_size_mb": round(file_size, 2)
        }

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise ServicoExterno(f"Erro renderização: {str(e)}", url="/video/render")

@router.post("/render", response_model=VideoResponse)
async def renderizar_video(req: VideoRenderRequest):
    """Endpoint Wrapper com Timeout."""
    try:
        return await asyncio.wait_for(
            render_with_timeout(_render_logic_internal, req), 
            timeout=300.0
        )
    except asyncio.TimeoutError:
        print(f"[Timeout] Renderização abortada após 300s: {req.title}")
        raise ServicoExterno("Render timeout após 300s (limite de segurança)", timeout=True)
