import os
import uuid
import requests
import yt_dlp
import random
import asyncio
import edge_tts
from typing import List, Optional
from moviepy.editor import ImageClip, VideoFileClip, AudioFileClip, concatenate_videoclips, vfx, CompositeVideoClip
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
AUDIO_DIR = os.path.join(settings.DATA_MIDIA, "audios") # Garante que existe

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)


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
        response = requests.get(url, timeout=10)
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
        'duration_limit': 60, # Não baixa vídeos gigantescos
        'socket_timeout': 15,
        'retries': 3,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Se for Reddit, yt-dlp resolve bem
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

async def generate_audio_file(text: str, output_path: str, voice: str = "pt-BR-FranciscaNeural"):
    """Gera áudio usando Edge-TTS (Azure Neural Voice clone)."""
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_path)
    except Exception as e:
        print(f"Erro ao gerar TTS: {e}")
        raise e

def generate_video(job_id: str, payload: dict):
    """Lógica principal de renderização híbrida."""
    conn = get_db_connection()
    try:
        print(f"[VideoEngine] Iniciando job {job_id}")
        title = payload.get("title", "Sem Título")
        script = payload.get("script", "")
        assets = payload.get("assets", {})
        config = payload.get("config", {})
        video_type = payload.get("type", "Noticia")
        
        # 1. Download de Assets
        downloaded_images = []
        # Priorizar imagens que parecem ser cutouts (TheSportsDB costuma ter 'cutout' na URL)
        all_imgs = assets.get("all_images", [])
        cutouts = [img for img in all_imgs if "cutout" in img.lower() or img.endswith(".png")]
        others = [img for img in all_imgs if img not in cutouts]
        
        print(f"[VideoEngine] Baixando {len(all_imgs)} imagens...")
        for url in (cutouts + others):
            path = download_file(url, "png" if url.endswith(".png") else "jpg")
            if path: downloaded_images.append(path)
            if len(downloaded_images) >= 5: break

        # 2. Lógica de Vídeo (Highlight)
        highlight_clip = None
        if video_type == "Highlight":
            video_urls = assets.get("all_videos", [])
            print(f"[VideoEngine] Buscando videos highlight: {len(video_urls)} encontrados.")
            if video_urls:
                for vid_url in video_urls:
                    print(f"[VideoEngine] Tentando baixar: {vid_url}")
                    vid_path = download_video_clip(vid_url)
                    if vid_path and os.path.exists(vid_path):
                        try:
                            clip = VideoFileClip(vid_path).without_audio()
                            # Corta 4 segundos (tenta do meio se for longo)
                            duration = 4
                            if clip.duration > duration:
                                start_t = min(max(0, clip.duration / 2 - 2), max(0, clip.duration - duration))
                                highlight_clip = clip.subclip(start_t, start_t + duration)
                            else:
                                highlight_clip = clip
                            
                            # Aplica Zoom 1.1x
                            highlight_clip = highlight_clip.fx(vfx.resize, 1.1)
                            highlight_clip = highlight_clip.set_duration(duration)
                            print("[VideoEngine] Clip de highlight processado com sucesso.")
                            break # Sucesso
                        except Exception as e:
                            print(f"[VideoEngine] Erro ao processar clipe: {e}")
                            continue
            else:
                 print("[VideoEngine] Nenhum URL de vídeo encontrado para Highlight.")

        # 3. Montagem da Timeline
        final_clips = []
        target_res = (1080, 1920) # Shorts/TikTok/Vertical
        
        # 3.1 Geração de Áudio (TTS) se não existir
        audio_path = os.path.join(AUDIO_DIR, f"{job_id}.mp3")
        if not os.path.exists(audio_path):
            if script and len(script) > 5:
                print(f"[VideoEngine] Gerando áudio pipeline (Unreal/Kokoro/Edge) para job {job_id}...")
                # Chama o serviço de áudio (async) dentro de contexto sync
                generated_audio = asyncio.run(audio_service.generate(script, job_id))
                
                if generated_audio and os.path.exists(generated_audio):
                    print(f"[VideoEngine] Áudio gerado com sucesso: {generated_audio}")
                    
                    # Verifica duração para debug
                    try:
                        temp_clip = AudioFileClip(generated_audio)
                        if temp_clip.duration < 25:
                            print(f"[VideoEngine] ⚠️ AVISO: Áudio curto ({temp_clip.duration}s). Vídeo pode ficar <25s. Aumente o roteiro!")
                        temp_clip.close()
                    except Exception as e:
                        print(f"[VideoEngine] Erro ao verificar duração áudio: {e}")

                    # O serviço já salva no path correto ou retorna o path
                    if generated_audio != audio_path:
                        # Se por acaso o nome for diferente, garante symlink ou rename?
                        # O service salva como {job_id}.mp3, então deve bater.
                        pass
                else:
                     print("[VideoEngine] Falha total na geração de áudio.")
            else:
                print("[VideoEngine] Aviso: Script vazio ou inexistente. Vídeo ficará mudo.")

        # Construção Visual
        # Slide 1: Capa (Idealmente um Cutout)
        if downloaded_images:
            clip1 = ImageClip(downloaded_images[0]).set_duration(3).set_fps(24)
            clip1 = clip1.resize(height=target_res[1]).crop(width=target_res[0], height=target_res[1], x_center=target_res[0]/2, y_center=target_res[1]/2)
            clip1 = apply_ken_burns(clip1, 3)
            final_clips.append(clip1)
        
        # Slide 2: Vídeo ou Imagem
        if highlight_clip:
            highlight_clip = highlight_clip.resize(height=target_res[1]).crop(width=target_res[0], height=target_res[1], x_center=target_res[0]/2, y_center=target_res[1]/2)
            final_clips.append(highlight_clip)
        elif len(downloaded_images) > 1:
            clip2 = ImageClip(downloaded_images[1]).set_duration(4).set_fps(24)
            clip2 = clip2.resize(height=target_res[1]).crop(width=target_res[0], height=target_res[1], x_center=target_res[0]/2, y_center=target_res[1]/2)
            clip2 = apply_ken_burns(clip2, 4)
            final_clips.append(clip2)
            
        # Slide 3 em diante: Restante das imagens
        for img in downloaded_images[2:]:
            clip_img = ImageClip(img).set_duration(4).set_fps(24)
            clip_img = clip_img.resize(height=target_res[1]).crop(width=target_res[0], height=target_res[1], x_center=target_res[0]/2, y_center=target_res[1]/2)
            clip_img = apply_ken_burns(clip_img, 4)
            final_clips.append(clip_img)
            if len(final_clips) >= 6: break

        if not final_clips:
            raise Exception("Nenhum asset visual disponível para gerar o vídeo.")

        # 4. Combinação Final
        print(f"[VideoEngine] Concatenando {len(final_clips)} clipes...")
        video = concatenate_videoclips(final_clips, method="compose")
        
        # Tenta aplicar o áudio se ele existir
        if os.path.exists(audio_path):
            audio = AudioFileClip(audio_path)
            # Ajusta duração do vídeo para bater com o áudio (loop ou corte)
            if video.duration < audio.duration:
                # Loop video to match audio
                video = video.set_audio(audio)
                loops = int(audio.duration / video.duration) + 1
                video = concatenate_videoclips([video] * loops).subclip(0, audio.duration)
                video = video.set_audio(audio)
            else:
                video = video.set_audio(audio)
                video = video.set_duration(audio.duration)
            
            # --- LEGENDAS (Subtitles) ---
            # Gera SRT via Whisper
            srt_path = os.path.join(TEMP_DIR, f"{job_id}.srt")
            if not os.path.exists(srt_path):
                print(f"[VideoEngine] Gerando legendas para {audio_path}...")
                subtitle_service.generate_srt(audio_path, srt_path)
            
            if os.path.exists(srt_path):
                try:
                    from moviepy.video.tools.subtitles import SubtitlesClip
                    from moviepy.editor import TextClip

                    # Estilo Shorts/TikTok: Fonte Grande, Amarelo, Borda Preta
                    # Nota: Posição relativa ('center', 0.70) = 70% da altura (parte de baixo)
                    def generator(txt):
                        return TextClip(
                            txt, 
                            font='Arial-Bold', 
                            fontsize=70, 
                            color='yellow', 
                            stroke_color='black', 
                            stroke_width=3, 
                            method='caption', 
                            size=(target_res[0]*0.9, None), # Quebra de linha automatica (90% largura)
                            align='center'
                        )

                    print("[VideoEngine] Queimando legendas no vídeo...")
                    subtitles = SubtitlesClip(srt_path, generator)
                    # Ajusta posição das legendas
                    subtitles = subtitles.set_pos(('center', 0.75)) 
                    
                    video = CompositeVideoClip([video, subtitles])
                except Exception as e:
                    print(f"[VideoEngine] Falha ao adicionar legendas: {e}")
            else:
                print("[VideoEngine] SRT não gerado, vídeo sem legenda.")

        else:
            print("[VideoEngine] Vídeo gerado sem áudio.")

        output_filename = f"video_{job_id}.mp4"
        output_path = os.path.join(OUTPUT_DIR, output_filename)
        
        print(f"[VideoEngine] Renderizando para {output_path}...")
        _write_videofile_with_fallback(video, output_path)
        
        # 5. Atualiza DB
        if conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE video_jobs SET status = 'completed', video_path = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s",
                    (output_path, job_id)
                )
                conn.commit()
        print(f"[VideoEngine] Job {job_id} concluído com sucesso.")

    except Exception as e:
        print(f"Erro na geração do vídeo: {e}")
        if conn:
            with conn.cursor() as cur:
                cur.execute(
                    "UPDATE video_jobs SET status = 'error', error_message = %s, updated_at = CURRENT_TIMESTAMP WHERE id = %s",
                    (str(e), job_id)
                )
                conn.commit()
    finally:
        if conn: conn.close()
        # Limpar temporários
        # for img in downloaded_images: try: os.remove(img) except: pass

