"""
Script de upload TikTok ROBUSTO — com retry e waits longos.
Projetado para rede Docker lenta.
"""
import json
import time
import sys
import os
import traceback

os.environ.setdefault("MPLCONFIGDIR", "/tmp")

from phantomwright.sync_api import sync_playwright
from phantomwright.stealth import Stealth

UPLOAD_URL = "https://www.tiktok.com/tiktokstudio/upload?from=upload&lang=en"
SCREENSHOT_DIR = "/data_midia/diag_screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)
COOKIES_PATH = "/data_midia/tk_haziq_cookies_futebas_oficial.json"


def ss(page, name):
    try:
        page.screenshot(path=f"{SCREENSHOT_DIR}/{name}.png", full_page=False)
        print(f"  📸 {name}")
    except Exception:
        pass


def main():
    print("=" * 60)
    print("[UPLOAD] TikTok Robust Upload v5")
    print("=" * 60)

    with open(COOKIES_PATH, "r") as f:
        cookies = json.load(f)
    print(f"[1] ✅ {len(cookies)} cookies carregados")

    with sync_playwright() as p:
        stealth = Stealth(navigator_languages_override=("en-US", "en"))
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
            ],
        )
        context = browser.new_context(
            viewport={"width": 1280, "height": 900},
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            locale="en-US",
            timezone_id="America/New_York",
        )
        stealth.apply_stealth_sync(context)
        context.add_cookies(cookies)
        page = context.new_page()

        # FASE 1: Navegar (com retry)
        print("[2] Navegando para TikTok Studio...")
        for attempt in range(3):
            try:
                page.goto(UPLOAD_URL, timeout=90000)
                print(f"  ✅ Página carregou (tentativa {attempt+1})")
                break
            except Exception as e:
                print(f"  ⚠️ Tentativa {attempt+1} falhou: {str(e)[:80]}")
                if attempt == 2:
                    ss(page, "nav_final_fail")
                    print("  ❌ Não foi possível carregar a página")
                    browser.close()
                    sys.exit(1)
                time.sleep(5)

        ss(page, "01_domloaded")
        print(f"  URL: {page.url}")

        # Check login
        if "login" in page.url.lower():
            print("  ❌ COOKIES INVÁLIDOS - Redirecionado para login!")
            ss(page, "login_redirect")
            browser.close()
            sys.exit(1)

        # FASE 2: Esperar upload container
        print("[3] Aguardando área de upload (até 90s)...")
        upload_ready = False
        for i in range(18):  # 18 * 5s = 90s
            time.sleep(5)
            if page.locator(".upload-text-container").is_visible():
                upload_ready = True
                break
            if page.locator('input[type="file"][accept="video/*"]').count() > 0:
                upload_ready = True
                break
            if i % 3 == 0:
                ss(page, f"02_wait_{i*5}s")
                print(f"  ... {i*5}s")

        if not upload_ready:
            ss(page, "02_upload_fail")
            body = page.locator("body").inner_text()[:300]
            print(f"  ❌ Upload não carregou. Texto: {body[:200]}")
            browser.close()
            sys.exit(1)

        ss(page, "02_upload_ready")
        print("  ✅ Área de upload pronta!")

        # FASE 3: Inserir vídeo
        print("[4] Inserindo vídeo...")
        video_path = "/tmp/test_upload.mp4"
        if not os.path.exists(video_path):
            import subprocess
            subprocess.run([
                "ffmpeg", "-y", "-f", "lavfi", "-i",
                "color=c=blue:size=720x1280:d=3",
                "-f", "lavfi", "-i", "anullsrc",
                "-shortest", "-c:v", "libx264", "-c:a", "aac",
                video_path
            ], capture_output=True)

        page.set_input_files('input[type="file"][accept="video/*"]', video_path)
        print("  ✅ Vídeo inserido")
        time.sleep(8)
        ss(page, "03_video")

        # FASE 4: Descrição
        print("[5] Adicionando descrição...")
        page.wait_for_selector('div[data-contents="true"]', timeout=30000)

        for text in ["Cancel", "Got it", "Dismiss"]:
            try:
                btn = page.locator(f"button:has-text('{text}')")
                if btn.is_visible():
                    btn.click()
                    time.sleep(0.5)
            except Exception:
                pass

        desc_box = page.locator('div[data-contents="true"]')
        desc_box.click()
        time.sleep(0.5)

        for _ in range(50):
            page.keyboard.press("Backspace")
            page.keyboard.press("Delete")
        time.sleep(0.3)

        page.keyboard.type("Teste Upload Futebas")
        time.sleep(1)
        ss(page, "04_desc")
        print("  ✅ Descrição adicionada")

        # FASE 5: Esperar Post
        print("[6] Aguardando processamento do TikTok (até 5 min)...")
        post_ready = False
        for i in range(60):  # 60 * 5s = 5 min
            time.sleep(5)
            try:
                post_btn = page.locator('button:has-text("Post")[aria-disabled="false"]')
                if post_btn.is_visible():
                    post_ready = True
                    break
            except Exception:
                pass
            if i % 6 == 0:
                ss(page, f"05_wait_{i*5}s")
                print(f"  ... {i*5}s")

        if not post_ready:
            ss(page, "05_post_fail")
            print("  ❌ Botão Post não ficou ativo em 5min")
            try:
                disabled = page.locator('button:has-text("Post")').first.get_attribute("aria-disabled")
                print(f"  disabled={disabled}")
            except Exception:
                pass
            browser.close()
            sys.exit(1)

        ss(page, "05_post_ready")
        print("  ✅ Botão Post ativo!")

        # FASE 6: Clicar Post
        print("[7] Clicando Post...")
        time.sleep(2)
        page.click('button:has-text("Post")[aria-disabled="false"]', timeout=5000)
        print("  ✅ Post clicado!")
        time.sleep(10)
        ss(page, "06_posted")
        print(f"  URL: {page.url}")

        time.sleep(5)
        ss(page, "07_final")

        body = page.locator("body").inner_text()[:300]
        if "leaving" in body.lower() or "content" in page.url.lower():
            print("\n🎉 UPLOAD CONFIRMADO COM SUCESSO!")
        else:
            print(f"\n⚠️ Status incerto. URL: {page.url}")
            print(f"  Texto: {body[:200]}")

        browser.close()

    print(f"\nScreenshots: {SCREENSHOT_DIR}/")


if __name__ == "__main__":
    main()
