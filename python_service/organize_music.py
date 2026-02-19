import os
import shutil
import random

# --- CONFIGURAÇÃO ---
SOURCE_DIR = r"C:\Users\Usuario\Downloads\Musicas_free"
DEST_DIR = r"C:\Users\Usuario\Desktop\meu-freshrss\python_service\app\assets\music"

# Categorias e Palavras-Chave
MOODS = {
    "Epic": ["epic", "battle", "war", "dark", "tension", "action", "trailer", "heroic", "cinematic"],
    "Sad": ["sad", "piano", "emotional", "cry", "slow", "melancholic", "drama", "grief"],
    "Rock": ["rock", "sport", "energy", "fast", "upbeat", "punk", "stadium", "guitar"],
    "Happy": ["happy", "chill", "lo-fi", "summer", "fun", "positive", "uplifting", "pop"]
}

LIMIT_PER_CATEGORY = 12  # Copiar até 12 músicas de cada

def organize_music():
    print("🎧 Iniciando DJ Automático - Organização de Músicas...")
    
    if not os.path.exists(SOURCE_DIR):
        print(f"❌ Erro: Pasta de origem não encontrada: {SOURCE_DIR}")
        print("Certifique-se de que descompactou as músicas neste local.")
        return

    # Criar subpastas no destino
    for mood in MOODS.keys():
        path = os.path.join(DEST_DIR, mood)
        os.makedirs(path, exist_ok=True)
    
    # Varrer arquivos
    all_files = []
    for root, dirs, files in os.walk(SOURCE_DIR):
        for file in files:
            if file.lower().endswith(('.mp3', '.wav', '.m4a')):
                all_files.append(os.path.join(root, file))
    
    print(f"📂 Encontradas {len(all_files)} músicas na origem.")
    
    categorized_count = {k: 0 for k in MOODS.keys()}
    
    # Shuffle para pegar variadas se tiver muitas
    random.shuffle(all_files)
    
    for file_path in all_files:
        filename = os.path.basename(file_path).lower()
        target_mood = None
        
        # Tenta classificar
        for mood, keywords in MOODS.items():
            for kw in keywords:
                if kw in filename:
                    target_mood = mood
                    break
            if target_mood: break
            
        # Se não classificou, tenta "Chill" como fallback se for nome genérico? 
        # Não, melhor só copiar as categorizadas para garantir precisão.
        
        if target_mood and categorized_count[target_mood] < LIMIT_PER_CATEGORY:
            try:
                dest_path = os.path.join(DEST_DIR, target_mood, os.path.basename(file_path))
                if not os.path.exists(dest_path):
                    shutil.copy2(file_path, dest_path)
                    print(f"   ✅ [{target_mood}] Copiado: {os.path.basename(file_path)}")
                    categorized_count[target_mood] += 1
            except Exception as e:
                print(f"   ❌ Erro ao copiar {file_path}: {e}")

    print("\n📊 Resumo da Organização:")
    for mood, count in categorized_count.items():
        print(f"   - {mood}: {count} músicas")
        
    print("\n🚀 Biblioteca Musical Atualizada!")

if __name__ == "__main__":
    organize_music()
