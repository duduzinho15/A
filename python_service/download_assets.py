import os
import requests
import sys

# Adiciona o diretório atual ao path para importar app.config corretamente
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(current_dir)

try:
    from app.config import settings
except ImportError:
    # Fallback para execução direta
    sys.path.append(os.path.join(current_dir, ".."))
    from app.config import settings

# --- CONFIGURAÇÃO ---
BASE_DIR = os.path.join(current_dir, "app", "assets")
DIRS = {
    "fonts": os.path.join(BASE_DIR, "fonts"),
    "music": os.path.join(BASE_DIR, "music"),
    "defaults": os.path.join(BASE_DIR, "defaults"),
}

# 1. Fontes (Identidade Visual)
FONT_URLS = [
    # Principal (Manchetes/Títulos) - Impactante
    ("Anton", "https://github.com/google/fonts/raw/main/ofl/anton/Anton-Regular.ttf"),
    ("Oswald-Bold", "https://github.com/google/fonts/raw/main/ofl/oswald/static/Oswald-Bold.ttf"),
    
    # Secundária (Legendas Longas) - Leitura Fácil
    ("Roboto-Bold", "https://github.com/google/fonts/raw/main/apache/roboto/static/Roboto-Bold.ttf"),
    ("Montserrat-Black", "https://github.com/google/fonts/raw/main/ofl/montserrat/static/Montserrat-Black.ttf"),
    
    # Especial (Citações)
    ("PermanentMarker", "https://github.com/google/fonts/raw/main/apache/permanentmarker/PermanentMarker-Regular.ttf")
]

# 2. Músicas (Pixabay) - 20 a 30 faixas
# Categorias: Tensão, Rock, Chill
MUSIC_CATEGORIES = {
    "Tension": ["epic dramatic", "news breaking", "suspense build up", "crime thriller"],
    "Rock": ["rock sport", "stadium stomp", "punk rock energy", "action drums"],
    "Chill": ["lofi hip hop", "sad piano", "emotional storytelling"]
}

# 3. Vídeos de Fundo (Pexels) - 15 a 20 loops
VIDEO_QUERIES = [
    "soccer stadium", "football fans", "soccer ball grass", 
    "stadium lights", "football goal", "soccer crowd cheering",
    "waving flag soccer", "football pitch night", "soccer shoes",
    "referee whistler"
]

def setup_dirs():
    print(f"📂 Criando diretórios em: {BASE_DIR}")
    for d in DIRS.values():
        os.makedirs(d, exist_ok=True)

def download_fonts_bulk():
    print(f"\n📚 Baixando Fontes...")
    for name, url in FONT_URLS:
        dest = os.path.join(DIRS["fonts"], f"{name}.ttf")
        if not os.path.exists(dest):
            try:
                print(f"   ⬇️ Baixando {name}...", end=" ")
                r = requests.get(url, timeout=10)
                if r.status_code == 200:
                    with open(dest, 'wb') as f:
                        f.write(r.content)
                    print("✅")
                else:
                    print(f"❌ Erro {r.status_code}")
            except Exception as e:
                print(f"❌ Erro: {e}")
        else:
            print(f"   ℹ️ {name} já existe.")

def download_music_bulk():
    if not settings.PIXABAY_API_KEY:
        print("\n⚠️ Pixabay API Key ausente. Pulando músicas.")
        return

    print(f"\n🎵 Baixando Pacote de Músicas (Pixabay)...")
    total_downloaded = 0
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    for category, queries in MUSIC_CATEGORIES.items():
        print(f"   🎸 Categoria: {category}")
        limit_per_query = 3 if category == "Chill" else 4 # Mais tensão e rock
        
        for query in queries:
            url = f"https://pixabay.com/api/audio/?key={settings.PIXABAY_API_KEY}&q={query}&per_page={limit_per_query * 2}"
            try:
                r = requests.get(url, headers=headers, timeout=15)
                try:
                    data = r.json()
                except ValueError:
                    print(f"      ❌ Erro JSON. Status: {r.status_code}. Content: {r.text[:200]}")
                    continue
                
                if "hits" in data:
                    count = 0
                    for track in data["hits"]:
                        if count >= limit_per_query: break
                        
                        # Limpa nome
                        safe_name = "".join([c for c in track['tags'] if c.isalnum() or c in (' ', '_')]).rstrip()
                        safe_name = safe_name.replace(" ", "_")[:30]
                        filename = f"{category}_{safe_name}_{track['id']}.mp3"
                        dest = os.path.join(DIRS["music"], filename)
                        
                        if not os.path.exists(dest):
                            print(f"      ⬇️ Baixando: {filename}...", end=" ")
                            r_audio = requests.get(track["url"], headers=headers, timeout=30)
                            with open(dest, 'wb') as f:
                                f.write(r_audio.content)
                            print("✅")
                            total_downloaded += 1
                            count += 1
                        else:
                            # print(f"      ℹ️ Já existe: {filename}")
                            count += 1 # Conta como 'processado' para o limite
            except Exception as e:
                print(f"      ❌ Erro na busca '{query}': {e}")
    
    print(f"   ✅ Total de músicas baixadas: {total_downloaded}")

def download_videos_bulk():
    if not settings.PEXELS_API_KEY:
        print("\n⚠️ Pexels API Key ausente. Pulando vídeos.")
        return

    print(f"\n🎬 Baixando Pacote de Vídeos (Pexels)...")
    headers = {"Authorization": settings.PEXELS_API_KEY}
    total_downloaded = 0
    
    for query in VIDEO_QUERIES:
        # Busca vertical (portrait) para Shorts
        url = f"https://api.pexels.com/videos/search?query={query}&orientation=portrait&per_page=2"
        try:
            r = requests.get(url, headers=headers, timeout=15)
            try:
                data = r.json()
            except ValueError:
                print(f"   ❌ Erro JSON (Pexels). Status: {r.status_code}. Content: {r.text[:200]}")
                continue

            if "videos" in data:
                for video_data in data["videos"]:
                    # Escolhe melhor qualidade HD
                    video_files = video_data["video_files"]
                    best = sorted([v for v in video_files if v['width'] >= 720 and v['width'] <= 1440], key=lambda x: x['width'], reverse=True)
                    
                    if best:
                        link = best[0]["link"]
                        # Extensão
                        ext = "mp4" # Pexels links often clean, but fallback
                        
                        safe_query = query.replace(" ", "_")
                        filename = f"loop_{safe_query}_{video_data['id']}.{ext}"
                        dest = os.path.join(DIRS["defaults"], filename)
                        
                        if not os.path.exists(dest):
                            print(f"   ⬇️ Baixando: {filename}...", end=" ")
                            r_vid = requests.get(link, timeout=60, stream=True)
                            with open(dest, 'wb') as f:
                                for chunk in r_vid.iter_content(chunk_size=1024*1024):
                                    if chunk: f.write(chunk)
                            print("✅")
                            total_downloaded += 1
                        else:
                            pass
                            # print(f"   ℹ️ Já existe: {filename}")
        except Exception as e:
            print(f"   ❌ Erro na busca '{query}': {e}")
            
    print(f"   ✅ Total de vídeos baixados: {total_downloaded}")

if __name__ == "__main__":
    setup_dirs()
    download_fonts_bulk()
    download_music_bulk()
    download_videos_bulk()
    print("\n🎉 Pacote de Assets concluído! Seu canal FUTEBAS está abastecido.")
