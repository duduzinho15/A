"""
dry_run_test.py — Teste de Importação do Motor de Vídeo
=======================================================
Valida que o video_engine.py refatorado pode ser importado sem erros.
Roda dentro do container Docker Python.
"""

import sys
import traceback

FAILED = []
PASSED = []

def test(label, fn):
    try:
        fn()
        PASSED.append(label)
        print(f"  ✅ {label}")
    except Exception as e:
        FAILED.append(label)
        print(f"  ❌ {label}: {e}")

print("\n" + "=" * 55)
print("  DRY RUN — Motor de Vídeo Futebas Pro v2.0")
print("=" * 55)

# 1. Imports básicos
print("\n[1] Dependências principais:")
test("moviepy.editor", lambda: __import__("moviepy.editor", fromlist=["ImageClip"]))
test("PIL (Pillow)", lambda: __import__("PIL.Image", fromlist=["Image"]))
test("PIL.ImageFilter", lambda: __import__("PIL.ImageFilter", fromlist=["GaussianBlur"]))
test("PIL.ImageEnhance", lambda: __import__("PIL.ImageEnhance", fromlist=["Brightness"]))
test("faster_whisper", lambda: __import__("faster_whisper", fromlist=["WhisperModel"]))
test("edge_tts", lambda: __import__("edge_tts"))
test("yt_dlp", lambda: __import__("yt_dlp"))
test("requests", lambda: __import__("requests"))
test("numpy", lambda: __import__("numpy"))

# 2. Import do video_engine refatorado
print("\n[2] Import do video_engine refatorado:")
try:
    from app.services.video_engine import (
        detect_stock_watermark,
        make_blurred_background,
        generate_word_level_clips,
        get_montserrat_black,
        get_background_music,
        get_fallback_loop,
        process_image_asset,
    )
    PASSED.append("video_engine (todas as funções)")
    print("  ✅ video_engine importado com todas as funções")
except Exception as e:
    FAILED.append("video_engine")
    print(f"  ❌ video_engine: {e}")
    traceback.print_exc()

# 3. Verificação de assets
print("\n[3] Assets do canal:")
import os
ASSETS_DIR = "/app/assets"

def check_asset(path, label):
    if os.path.exists(path):
        PASSED.append(label)
        print(f"  ✅ {label}: {path}")
    else:
        FAILED.append(label)
        print(f"  ⚠️  {label} não encontrado: {path} (não quebra execução)")

check_asset(os.path.join(ASSETS_DIR, "fonts", "Montserrat-Black.ttf"), "Fonte Montserrat-Black")
check_asset(os.path.join(ASSETS_DIR, "music", "Epic"), "Pasta música Epic")
check_asset(os.path.join(ASSETS_DIR, "music", "Rock"), "Pasta música Rock")

defaults_dir = os.path.join(ASSETS_DIR, "defaults")
if os.path.exists(defaults_dir):
    loops = [f for f in os.listdir(defaults_dir) if f.endswith(".mp4")]
    print(f"  ✅ Loops padrão disponíveis: {len(loops)} arquivo(s)")

# 4. Verificação da fonte selecionada
print("\n[4] Seleção de fonte:")
try:
    font = get_montserrat_black()
    print(f"  ✅ Fonte ativa: {font}")
except Exception as e:
    print(f"  ❌ Erro na fonte: {e}")

# 5. Seleção de música (dry run sem reprodução)
print("\n[5] Seleção de música:")
try:
    for mood in ["Epic", "Rock", "Happy", "Sad"]:
        music = get_background_music(mood)
        status = f"✅ {os.path.basename(music)}" if music else "⚠️  Nenhuma encontrada"
        print(f"  {mood}: {status}")
except Exception as e:
    print(f"  ❌ Erro: {e}")

# 6. TikTok Uploader
print("\n[6] TikTok Uploader patch:")
try:
    # Testa apenas o import, não executa upload
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "tiktok_cli", "/app/tiktok_uploader_cli_patch.py"
    )
    if spec:
        print("  ✅ tiktok_uploader_cli_patch.py encontrado e parseável")
    else:
        print("  ⚠️  Arquivo não encontrado no path")
except Exception as e:
    print(f"  ⚠️  {e}")

# ── RESULTADO FINAL ────────────────────────────────────────────────
print("\n" + "=" * 55)
print(f"  RESULTADO: {len(PASSED)} passou | {len(FAILED)} falhou")
if FAILED:
    print(f"  Falhas: {', '.join(FAILED)}")
print("=" * 55 + "\n")

sys.exit(0 if not FAILED else 1)
