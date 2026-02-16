
import os
import asyncio
import yt_dlp
from app.config import settings

# URLs ou Queries para B-roll inicial
# Usando busca do yt-dlp para garantir que sempre ache algo
INITIAL_ASSETS = [
    {"category": "torcida", "query": "ytsearch1:football crowd atmosphere no copyright"},
    {"category": "torcida", "query": "ytsearch1:soccer fans chanting stock footage"},
    {"category": "futebol", "query": "ytsearch1:soccer cinematic skills 4k no copyright"},
    {"category": "futebol", "query": "ytsearch1:football training b-roll no copyright"},
    {"category": "futebol", "query": "ytsearch1:soccer slow motion goal celebration no copyright"},
]

def download_initial_assets():
    """
    Baixa assets iniciais se a pasta estiver vazia.
    Roda de forma síncrona/blocking no startup para garantir disponibilidade,
    ou pode ser chamado em background.
    """
    base_dir = os.path.join(settings.DATA_MIDIA, "broll")
    
    print("[Assets] Verificando assets iniciais...")
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'outtmpl': f'{base_dir}/%(info.category)s/%(id)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
        'ignoreerrors': True,
        'noplaylist': True,
        # 'max_filesize': 50 * 1024 * 1024 # 50MB max por clip
    }

    for item in INITIAL_ASSETS:
        category = item["category"]
        cat_dir = os.path.join(base_dir, category)
        os.makedirs(cat_dir, exist_ok=True)
        
        # Verifica se já tem vídeos na pasta
        existing = [f for f in os.listdir(cat_dir) if f.endswith(".mp4")]
        if len(existing) >= 2: # Se já tem 2 vídeos nessa categoria, pula
            continue
            
        print(f"[Assets] Baixando para categoria '{category}': {item['query']}")
        
        # Injeta categoria no info_dict para usar no template de saída
        # Hook customizado ou wrapper seria ideal, mas aqui vamos ajustar o outtmpl per loop
        current_opts = ydl_opts.copy()
        current_opts['outtmpl'] = os.path.join(base_dir, category, '%(title).20s-%(id)s.%(ext)s')
        
        try:
            with yt_dlp.YoutubeDL(current_opts) as ydl:
                ydl.download([item["query"]])
        except Exception as e:
            print(f"[Assets] Erro ao baixar {item['query']}: {e}")

    print("[Assets] Verificação completa.")

async def download_assets_background():
    """Wrapper assíncrono para rodar sem bloquear o main thread."""
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, download_initial_assets)
