import os
import uuid
import requests
import yt_dlp
import random
import asyncio
import edge_tts
import json
from typing import List, Optional, Tuple, Union
from moviepy.editor import (
    ImageClip, VideoFileClip, AudioFileClip, concatenate_videoclips, concatenate_audioclips,
    vfx, CompositeVideoClip, CompositeAudioClip, TextClip, ColorClip
)
from app.config import settings
from app.utils.database import get_db_connection
from app.services.audio import AudioService
from app.services.subtitles import SubtitleService

# Instância Global do Serviço de Áudio e Legendas
audio_service = AudioService()
subtitle_service = SubtitleService()

# Diretórios
TEMP_DIR = os.path.join(settings.DATA_MIDIA, "temp")
OUTPUT_DIR = os.path.join(settings.DATA_MIDIA, "videos")
AUDIO_DIR = os.path.join(settings.DATA_MIDIA, "audios")

# Assets do Canal
APP_DIR = os.path.dirname(os.path.dirname(__file__)) # app/
ASSETS_DIR = os.path.join(APP_DIR, "assets")

FONTS_DIR = os.path.join(ASSETS_DIR, "fonts")
MUSIC_DIR = os.path.join(ASSETS_DIR, "music")
OVERLAYS_DIR = os.path.join(ASSETS_DIR, "overlays")
DEFAULTS_DIR = os.path.join(ASSETS_DIR, "defaults")

# Garantir existência
for d in [TEMP_DIR, OUTPUT_DIR, AUDIO_DIR, FONTS_DIR, MUSIC_DIR, OVERLAYS_DIR, DEFAULTS_DIR]:
    os.makedirs(d, exist_ok=True)

# --- Helpers de Assets ---

def get_custom_font() -> str:
    """Retorna o path da primeira fonte .ttf encontrada ou 'Arial-Bold'."""
    try:
        fonts = [f for f in os.listdir(FONTS_DIR) if f.endswith(".ttf")]
        if fonts:
            return os.path.join(FONTS_DIR, fonts[0])
    except:
        pass
    return 'Arial-Bold' # Fallback sistema (ImageMagick)

def get_background_music(mood: str = "Tension") -> Optional[str]:
    """
    Retorna music baseada no Mood (Epic, Sad, Rock, Happy).
    Fallback: Tenta pasta raiz ou outras categorias.
    """
    try:
        # 1. Tenta pasta específica do mood
        mood_path = os.path.join(MUSIC_DIR, mood)
        if os.path.exists(mood_path):
            musics = [f for f in os.listdir(mood_path) if f.endswith(".mp3")]
            if musics:
                print(f"[VideoEngine] DJ Selecionou ({mood}): {random.choice(musics)}")
                return os.path.join(mood_path, random.choice(musics))
        
        # 2. Fallback: Procura em qualquer subpasta
        all_musics = []
        for root, dirs, files in os.walk(MUSIC_DIR):
            for f in files:
                if f.endswith(".mp3"):
                     all_musics.append(os.path.join(root, f))
        
        if all_musics:
            selected = random.choice(all_musics)
            print(f"[VideoEngine] DJ Fallback (Aleatório): {os.path.basename(selected)}")
            return selected
            
    except Exception as e:
        print(f"[VideoEngine] Erro no DJ: {e}")
    return None

def get_watermark_path() -> Optional[str]:
    """Retorna path da marca d'água."""
    # Prioridade: watermark.png > logo.png
    w_path = os.path.join(OVERLAYS_DIR, "watermark.png")
    if os.path.exists(w_path): return w_path
    
    l_path = os.path.join(OVERLAYS_DIR, "logo.png")
    if os.path.exists(l_path): return l_path
    
    return None

def get_fallback_loop() -> Optional[str]:
    """Retorna vídeo de loop padrão."""
    try:
        loops = [f for f in os.listdir(DEFAULTS_DIR) if f.endswith(".mp4")]
        if loops:
            return os.path.join(DEFAULTS_DIR, loops[0])
    except:
        pass
    return None

def fetch_google_images(query: str, limit: int = 3) -> List[str]:
    """
    Busca imagens no Google (via Serper, Custom Search ou Brave).
    Útil para encontrar fotos específicas de notícias recentes.
    """
    assets = []
    
    # 1. Serper Dev (Melhor para automação)
    if settings.SERPER_API_KEY:
        try:
            print(f"[VideoEngine] Buscando Google Images (Serper): {query}")
            url = "https://google.serper.dev/images"
            payload = json.dumps({"q": query, "num": limit})
            headers = {
                'X-API-KEY': settings.SERPER_API_KEY,
                'Content-Type': 'application/json'
            }
            r = requests.post(url, headers=headers, data=payload, timeout=10)
            data = r.json()
            if "images" in data:
                for img in data["images"]:
                     path = download_file(img["imageUrl"], ext="jpg")
                     if path: assets.append(path)
                     if len(assets) >= limit: return assets
        except Exception as e:
            print(f"[VideoEngine] Erro Serper: {e}")

    # 2. Google Custom Search (Fallback)
    if not assets and settings.GOOGLE_CUSTOM_SEARCH_KEY and settings.GOOGLE_CUSTOM_SEARCH_CX:
        try:
            print(f"[VideoEngine] Buscando Google Images (CSE): {query}")
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                "q": query,
                "cx": settings.GOOGLE_CUSTOM_SEARCH_CX,
                "key": settings.GOOGLE_CUSTOM_SEARCH_KEY,
                "searchType": "image",
                "num": limit
            }
            r = requests.get(url, params=params, timeout=10)
            data = r.json()
            if "items" in data:
                for item in data["items"]:
                    path = download_file(item["link"], ext="jpg")
                    if path: assets.append(path)
                    if len(assets) >= limit: return assets
        except Exception as e:
            print(f"[VideoEngine] Erro Google CSE: {e}")

    # 3. Brave Search (Fallback Final)
    if not assets and settings.BRAVE_API_KEY:
        try:
             print(f"[VideoEngine] Buscando Brave Images: {query}")
             headers = {"Accept": "application/json", "X-Subscription-Token": settings.BRAVE_API_KEY}
             # Brave Image Search endpoint
             url = "https://api.search.brave.com/res/v1/images/search"
             params = {"q": query, "count": limit}
             r = requests.get(url, headers=headers, params=params, timeout=10)
             data = r.json()
             if "results" in data:
                 for res in data["results"]:
                     path = download_file(res["properties"]["url"], ext="jpg")
                     if path: assets.append(path)
                     if len(assets) >= limit: return assets
        except Exception as e:
            print(f"[VideoEngine] Erro Brave: {e}")

    return assets

def fetch_external_assets(query: str, limit: int = 3) -> List[str]:
    """
    Busca assets externos (Panic Search).
    Prioridade: Google Images (Notícia) -> Stock (Genérico)
    """
    all_assets = []
    
    # 1. Tenta Google Images Primeiro (Contexto Real)
    web_images = fetch_google_images(query, limit)
    all_assets.extend(web_images)
    
    # Se já temos o suficiente, retorna (mas idealmente queremos misturar)
    if len(all_assets) >= limit:
        return all_assets

    # 2. Pexels Video (Melhor qualidade visual)
    if settings.PEXELS_API_KEY:
        try:
            print(f"[VideoEngine] Buscando vídeos no Pexels: {query}")
            headers = {"Authorization": settings.PEXELS_API_KEY}
            url = f"https://api.pexels.com/videos/search?query={query}&orientation=portrait&per_page={limit}"
            r = requests.get(url, headers=headers, timeout=10)
            data = r.json()
            if "videos" in data:
                for v in data["videos"]:
                    # Pega melhor file (HD)
                    files = sorted([f for f in v["video_files"] if f["width"] >= 720], key=lambda x: x["width"])
                    if files:
                        v_url = files[-1]["link"]
                        path = download_file(v_url, ext="mp4")
                        if path: all_assets.append(path)
        except Exception as e:
            print(f"[VideoEngine] Erro Pexels: {e}")

    # 3. Pixabay Images (Fallback rápido)
    if len(all_assets) < limit and settings.PIXABAY_API_KEY:
        try:
             print(f"[VideoEngine] Buscando imagens no Pixabay: {query}")
             url = f"https://pixabay.com/api/?key={settings.PIXABAY_API_KEY}&q={query}&image_type=photo&per_page={limit}"
             r = requests.get(url, timeout=10)
             data = r.json()
             if "hits" in data:
                 for h in data["hits"]:
                     path = download_file(h["largeImageURL"], ext="jpg")
                     if path: all_assets.append(path)
        except Exception as e:
            print(f"[VideoEngine] Erro Pixabay: {e}")
            
    return all_assets

# --- Helpers de Render ---

def create_stinger(duration: float = 0.6) -> Optional[VideoFileClip]:
    """
    Cria uma transição Stinger simples:
    Logo Zoom In (0.3s) + Logo Zoom Out (0.3s) sobre fundo transparente (ou preto).
    """
    logo_path = get_watermark_path()
    if not logo_path: return None
    
    try:
        # Usa resolução alvo
        w, h = 1080, 1920
        
        # Logo base
        logo = ImageClip(logo_path).resize(width=400).set_duration(duration)
        
        # Animação de escala (Keyframes simulados com lambda)
        # t=0 -> 0.5x, t=center -> 1.5x, t=end -> 0.5x
        def scale_effect(t):
            if t < duration / 2:
                # Zoom In: 0.1 -> 1.5
                progress = t / (duration / 2)
                return 0.1 + (1.4 * progress)
            else:
                # Zoom Out: 1.5 -> 0.1
                progress = (t - duration/2) / (duration / 2)
                return 1.5 - (1.4 * progress)

        stinger = logo.resize(scale_effect).set_position('center')
        
        # Fundo (opcional, ou apenas o logo sobreposto)
        # Para stinger real, idealmente cobre tudo. Vamos por um flash branco ou cor da marca?
        # Vamos usar apenas o logo crescendo muito para cobrir a tela?
        # Melhor: Logo + Fundo Laranja/Azul rápido
        bg = ColorClip(size=(w, h), color=(0,0,0), duration=duration).set_opacity(0.3) # Leve dim
        
        return CompositeVideoClip([bg, stinger]).set_duration(duration)
    except Exception as e:
        print(f"[VideoEngine] Erro ao criar Stinger: {e}")
        return None

def apply_copyright_protection(clip):
    """
    Aplica filtros para evitar Copyright:
    1. Espelhamento Horizontal (Mirror X)
    2. Zoom Leve (1.05x)
    """
    try:
        clip = clip.fx(vfx.mirror_x)
        clip = clip.resize(1.05) # Zoom leve para mudar hash visual
        return clip
    except:
        return clip

def _write_videofile_with_fallback(video, output_path: str):
    """
    Tenta NVENC primeiro para acelerar render em GPU NVIDIA.
    Se NVENC nao estiver disponivel no runtime, faz fallback para libx264.
    """
    try:
        print("[VideoEngine] Tentando render com NVENC (h264_nvenc)...")
        video.write_videofile(
            output_path,
            fps=24,
            codec="h264_nvenc",
            audio_codec="aac",
            threads=4,
            preset="p5",
            ffmpeg_params=[
                "-gpu", "0",
                "-rc:v", "vbr",
                "-cq", "23",
                "-b:v", "6M",
                "-maxrate", "10M",
                "-bufsize", "12M",
                "-pix_fmt", "yuv420p",
                "-profile:v", "high",
            ],
        )
        print("[VideoEngine] Render finalizado com NVENC.")
    except Exception as gpu_exc:
        print(f"[VideoEngine] NVENC indisponivel, fallback para CPU (libx264): {gpu_exc}")
        video.write_videofile(
            output_path,
            fps=24,
            codec="libx264",
            audio_codec="aac",
            threads=4,
            preset="ultrafast",
        )
        print("[VideoEngine] Render finalizado com libx264.")

def download_file(url: str, ext: str = "jpg") -> Optional[str]:
    """Baixa um arquivo via requests (para imagens)."""
    try:
        # User Agent para evitar bloqueios (Pixabay/Google)
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            filename = f"asset_{uuid.uuid4().hex}.{ext}"
            filepath = os.path.join(TEMP_DIR, filename)
            with open(filepath, "wb") as f:
                f.write(response.content)
            return filepath
    except Exception as e:
        print(f"Erro ao baixar imagem {url}: {e}")
    return None

def download_video_clip(url: str) -> Optional[str]:
    """Baixa um vídeo usando yt-dlp."""
    video_id = uuid.uuid4().hex[:8]
    template = os.path.join(TEMP_DIR, f"vid_{video_id}.%(ext)s")
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': template,
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
        'duration_limit': 60, 
        'socket_timeout': 15,
        'retries': 3,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Se for Reddit/Twitter, yt-dlp resolve bem
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)
    except Exception as e:
        print(f"Erro ao baixar vídeo {url}: {e}")
    return None

def apply_ken_burns(clip, duration, zoom_ratio=0.1):
    """Aplica efeito de zoom suave (Ken Burns)."""
    def zoom(t):
        return 1 + zoom_ratio * (t / duration)
    return clip.resize(zoom)

def generate_video(job_id: str, payload: dict):
    """Lógica principal de renderização híbrida Profissional."""
    conn = get_db_connection()
    try:
        print(f"[VideoEngine] Iniciando job {job_id}")
        title = payload.get("title", "Sem Título")
        
        # Parse Script
        script = payload.get("script", "")
        if isinstance(script, dict):
             blocks = script.get("blocks", [])
             if blocks:
                 script_text = " ".join([b.get("text", "") for b in blocks])
             else:
                 script_text = str(script)
             # Extrair Search Terms do roteiro
             search_terms = script.get("search_terms", [])
        else:
             script_text = script
             search_terms = []

        assets = payload.get("assets", {})
        config = payload.get("config", {})
        video_type = payload.get("type", "Noticia")
        
        # 0. Preparar Áudio (Necessário para saber duração)
        audio_path = os.path.join(AUDIO_DIR, f"{job_id}.mp3")
        if not os.path.exists(audio_path):
            if script_text and len(script_text) > 5:
                # O serviço de áudio agora normaliza o texto internamente
                asyncio.run(audio_service.generate(script_text, job_id))
        
        if not os.path.exists(audio_path):
             raise Exception("Falha crítica: Áudio não gerado ou script vazio.")
        
        main_audio = AudioFileClip(audio_path)
        total_duration = main_audio.duration + 1.5 # Buffer fim
        print(f"[VideoEngine] Duração alvo: {total_duration:.2f}s")

        # 1. Agregação Inicial de Assets (N8n Payload)
        downloaded_assets = [] # Pode conter paths de img ou vid
        all_imgs = assets.get("all_images", [])
        
        # Priorizar cutouts (fundo transparente)
        cutouts = [img for img in all_imgs if "cutout" in img.lower() or img.endswith(".png")]
        others = [img for img in all_imgs if img not in cutouts]
        
        print(f"[VideoEngine] Baixando {len(all_imgs)} imagens do payload...")
        for url in (cutouts + others):
            path = download_file(url, "png" if url.endswith(".png") else "jpg")
            if path: downloaded_assets.append({"type": "image", "path": path})
            if len(downloaded_assets) >= 8: break
            
        # 2. Highlight Video (Se disponível)
        highlight_clip = None
        video_urls = assets.get("all_videos", [])
        if video_urls:
            print(f"[VideoEngine] Processando highlights: {len(video_urls)} URLs.")
            for vid_url in video_urls:
                vid_path = download_video_clip(vid_url)
                if vid_path and os.path.exists(vid_path):
                    try:
                        clip = VideoFileClip(vid_path).without_audio()
                        # Proteção de Copyright
                        clip = apply_copyright_protection(clip)
                        
                        duration = 5 # Padrao highlight
                        if clip.duration > duration:
                            start_t = min(max(0, clip.duration / 2 - 2), max(0, clip.duration - duration))
                            highlight_clip = clip.subclip(start_t, start_t + duration)
                        else:
                            highlight_clip = clip
                        
                        highlight_clip = highlight_clip.resize(height=1920).crop(width=1080, height=1920, x_center=1080/2, y_center=1920/2)
                        # Adiciona ao pool de assets
                        downloaded_assets.insert(1, {"type": "video", "clip": highlight_clip}) # Logo depois da capa
                        break 
                    except Exception as e: 
                        print(f"[VideoEngine] Erro clip highlight: {e}") 
        
        # 3. Verificação de Cobertura & Busca Contextual (Panic Search)
        # Estimativa: cada imagem cobre 4s, video cobre sua duracao
        current_coverage = 0
        for item in downloaded_assets:
            if item["type"] == "image": current_coverage += 4
            elif item["type"] == "video": current_coverage += item["clip"].duration
        
        if current_coverage < total_duration:
            missing_time = total_duration - current_coverage
            print(f"[VideoEngine] Faltam {missing_time:.1f}s de cobertura. Iniciando Busca Contextual...")
            
            # Tentar termos específicos primeiro, depois genéricos
            search_queue = search_terms[:] if search_terms else []
            search_queue.append("soccer match close up") 
            search_queue.append("football stadium crowds")
            
            for term in search_queue:
                if current_coverage >= total_duration: break
                
                # Garante contexto "Futebol" se nao tiver
                query = term if "futebol" in term.lower() or "soccer" in term.lower() or "football" in term.lower() else f"{term} soccer"
                
                new_files = fetch_external_assets(query, limit=3)
                for fpath in new_files:
                    if fpath.endswith(".mp4"):
                        # Video externo
                        try:
                            c = VideoFileClip(fpath).without_audio().resize(height=1920)
                            c = c.crop(width=1080, height=1920, x_center=540, y_center=960)
                            if c.duration > 5: c = c.subclip(0, 5)
                            downloaded_assets.append({"type": "video", "clip": c})
                            current_coverage += c.duration
                        except: pass
                    else:
                        # Imagem externa
                        downloaded_assets.append({"type": "image", "path": fpath})
                        current_coverage += 4
        
        # 4. Fallback Final (Local Loop)
        fallback_loop = get_fallback_loop()
        
        # 5. Montagem Timeline
        visual_clips = []
        target_res = (1080, 1920)
        curr_time = 0.0
        
        # Define Stinger
        stinger = create_stinger(0.6)
        
        asset_idx = 0
        while curr_time < total_duration:
            clip = None
            
            if asset_idx < len(downloaded_assets):
                item = downloaded_assets[asset_idx]
                if item["type"] == "image":
                    dur = 4.0
                    clip = ImageClip(item["path"]).set_duration(dur).set_fps(24)
                    clip = clip.resize(height=target_res[1]).crop(width=target_res[0], height=target_res[1], x_center=target_res[0]/2, y_center=target_res[1]/2)
                    clip = apply_ken_burns(clip, dur)
                elif item["type"] == "video":
                    clip = item["clip"] # Já processado
            else:
                # Esgotou assets, usar Loop
                if fallback_loop:
                    rem = total_duration - curr_time
                    clip = VideoFileClip(fallback_loop).resize(height=target_res[1]).crop(width=target_res[0], height=target_res[1], x_center=target_res[0]/2, y_center=target_res[1]/2)
                    clip = clip.loop(duration=rem)
                else:
                    # Color fallback
                    clip = ColorClip(size=target_res, color=(0,0,0), duration=total_duration - curr_time)
            
            if clip:
                # Adiciona Stinger antes (exceto no primeiro)
                if visual_clips and stinger:
                    visual_clips.append(stinger)
                    curr_time += stinger.duration
                
                visual_clips.append(clip)
                curr_time += clip.duration
                asset_idx += 1
                
            if curr_time >= total_duration: break

        print(f"[VideoEngine] Concatenando {len(visual_clips)} clipes...")
        video = concatenate_videoclips(visual_clips, method="compose")
        video = video.subclip(0, total_duration)

        # --- ÁUDIO DUCKING (Mixagem) ---
        # Mood vem do script (AI) ou default "Rock"
        mood = "Rock"
        if isinstance(payload.get("script"), dict):
            mood = payload.get("script", {}).get("mood", "Rock")
            
        bg_music_path = get_background_music(mood)
        if bg_music_path:
            print(f"[VideoEngine] Adicionando música de fundo: {bg_music_path}")
            bg_music = AudioFileClip(bg_music_path)
            
            # Loopa música
            if bg_music.duration < total_duration:
                 loops = int(total_duration / bg_music.duration) + 1
                 bg_music = concatenate_audioclips([bg_music] * loops)
            
            bg_music = bg_music.subclip(0, total_duration)
            
            # Ducking: Volume 12%
            bg_music = bg_music.volumex(0.12)
            
            # Fade out
            bg_music = bg_music.audio_fadeout(2.0)
            
            # Mixagem
            final_audio = CompositeAudioClip([main_audio, bg_music])
            video = video.set_audio(final_audio)
        else:
            video = video.set_audio(main_audio)

        # --- BRANDING (Logo) ---
        watermark_path = get_watermark_path()
        if watermark_path:
            # Logo menor, canto superior direito
            logo = ImageClip(watermark_path).set_duration(total_duration).resize(width=150).set_opacity(0.85)
            # Position: right=20, top=50
            logo = logo.set_pos(('right', 50)) 
            video = CompositeVideoClip([video, logo])

        # --- LEGENDAS (Burned-in) ---
        srt_path = os.path.join(TEMP_DIR, f"{job_id}.srt")
        if not os.path.exists(srt_path):
             print("[VideoEngine] Gerando legendas...")
             subtitle_service.generate_srt(audio_path, srt_path)
        
        if os.path.exists(srt_path):
            try:
                from moviepy.video.tools.subtitles import SubtitlesClip
                
                custom_font = get_custom_font()
                print(f"[VideoEngine] Renderizando legendas com fonte: {custom_font}")

                def generator(txt):
                    return TextClip(
                        txt, 
                        font=custom_font, 
                        fontsize=65, 
                        color='#FFDD00', # Dourado/Laranja da marca
                        stroke_color='black', 
                        stroke_width=4, 
                        method='caption', 
                        size=(target_res[0]*0.85, None), 
                        align='center'
                    )

                subtitles = SubtitlesClip(srt_path, generator)
                # Safe Zone: Bottom 250px
                # Relative Position: 0.75 (3/4 da tela)
                subtitles = subtitles.set_pos(('center', 0.78))
                
                video = CompositeVideoClip([video, subtitles])
            except Exception as e:
                print(f"[VideoEngine] Erro ao queimar legendas: {e}")

        # Final Render
        output_filename = f"video_{job_id}.mp4"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        
        print(f"[VideoEngine] Renderizando para {output_path}...")
        _write_videofile_with_fallback(video, output_path)

        # Atualiza DB
        if conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE video_jobs SET status = 'completed', published = false, video_path = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s",
                    (output_path, job_id)
                )
                conn.commit()
        print(f"[VideoEngine] Job {job_id} concluído com sucesso.")

    except Exception as e:
        print(f"Erro na geração do vídeo: {e}")
        import traceback
        traceback.print_exc()
        if conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE video_jobs SET status = 'error', error_message = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s",
                    (str(e), job_id)
                )
                conn.commit()
    finally:
        if conn: conn.close()
