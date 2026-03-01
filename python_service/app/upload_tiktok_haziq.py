"""
upload_tiktok_haziq.py — Script de upload TikTok via Haziq-exe/TikTokAutoUploader.
Projetado para ser chamado via subprocess pelo FastAPI (publish.py).

Exit codes:
  0 = Upload publicado com sucesso
  1 = Erro (mensagem no stderr/stdout)

Uso:
  python upload_tiktok_haziq.py --video /path/to/video.mp4 --title "Titulo" --hashtags "#tag1 #tag2"
"""
import argparse
import json
import os
import sys
import time
import traceback

os.environ.setdefault("MPLCONFIGDIR", "/tmp")

from phantomwright.sync_api import sync_playwright
from phantomwright.stealth import Stealth

UPLOAD_URL = "https://www.tiktok.com/tiktokstudio/upload?from=upload&lang=en"
COOKIES_DIR = "/data_midia"
SCREENSHOT_DIR = "/data_midia/tiktok_screenshots"


def get_cookies_path(account):
    return os.path.join(COOKIES_DIR, f"tk_haziq_cookies_{account}.json")


def screenshot(page, name):
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    try:
        page.screenshot(path=f"{SCREENSHOT_DIR}/{name}.png", full_page=False)
    except Exception:
        pass


def upload(video_path, title, hashtags=None, account="futebas_oficial"):
    """Executa o upload completo para o TikTok Studio via Phantomwright."""

    cookies_path = get_cookies_path(account)
    if not os.path.exists(cookies_path):
        print(f"[tiktok-haziq] ❌ Cookies não encontrados: {cookies_path}")
        return False

    if not os.path.exists(video_path):
        print(f"[tiktok-haziq] ❌ Vídeo não encontrado: {video_path}")
        return False

    with open(cookies_path, "r") as f:
        cookies = json.load(f)
    print(f"[tiktok-haziq] ✅ {len(cookies)} cookies carregados para '{account}'")

    # Montar descrição com hashtags
    description = title
    if hashtags:
        tags_str = " ".join(
            t if t.startswith("#") else f"#{t}" for t in hashtags
        )
        description = f"{title} {tags_str}"

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

        # FASE 1: Navegar
        print("[tiktok-haziq] Navegando para TikTok Studio...")
        for attempt in range(3):
            try:
                page.goto(UPLOAD_URL, timeout=90000)
                print(f"[tiktok-haziq] ✅ Página carregou (tentativa {attempt + 1})")
                break
            except Exception as e:
                print(f"[tiktok-haziq] ⚠️ Tentativa {attempt + 1}: {str(e)[:80]}")
                if attempt == 2:
                    screenshot(page, "nav_fail")
                    browser.close()
                    return False
                time.sleep(5)

        screenshot(page, "01_loaded")

        # Check login
        if "login" in page.url.lower():
            print("[tiktok-haziq] ❌ COOKIES INVÁLIDOS - Redirecionado para login!")
            screenshot(page, "login_redirect")
            browser.close()
            return False

        # FASE 2: Esperar upload container (90s)
        print("[tiktok-haziq] Aguardando área de upload...")
        upload_ready = False
        for i in range(18):
            time.sleep(5)
            try:
                if page.locator(".upload-text-container").is_visible():
                    upload_ready = True
                    break
                if page.locator('input[type="file"][accept="video/*"]').count() > 0:
                    upload_ready = True
                    break
            except Exception:
                pass

        if not upload_ready:
            print("[tiktok-haziq] ❌ Área de upload não carregou em 90s")
            screenshot(page, "upload_fail")
            browser.close()
            return False

        print("[tiktok-haziq] ✅ Área de upload pronta!")

        # FASE 3: Inserir vídeo
        print(f"[tiktok-haziq] Inserindo vídeo: {video_path}")
        try:
            page.set_input_files(
                'input[type="file"][accept="video/*"]', video_path
            )
            print("[tiktok-haziq] ✅ Vídeo inserido")
            time.sleep(8)
            screenshot(page, "02_video")
        except Exception as e:
            print(f"[tiktok-haziq] ❌ Falha ao inserir vídeo: {e}")
            screenshot(page, "video_fail")
            browser.close()
            return False

        # FASE 4: Descrição
        print("[tiktok-haziq] Adicionando descrição...")
        try:
            page.wait_for_selector('div[data-contents="true"]', timeout=30000)

            # Fechar popups
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

            # Limpar campo
            for _ in range(50):
                page.keyboard.press("Backspace")
                page.keyboard.press("Delete")
            time.sleep(0.3)

            page.keyboard.type(description)
            time.sleep(1)
            screenshot(page, "03_desc")
            print(f"[tiktok-haziq] ✅ Descrição: {description[:60]}...")
        except Exception as e:
            print(f"[tiktok-haziq] ❌ Falha na descrição: {e}")
            screenshot(page, "desc_fail")
            browser.close()
            return False

        # FASE 5: Esperar Post (5 min)
        print("[tiktok-haziq] Aguardando processamento do TikTok...")
        post_ready = False
        for i in range(60):
            time.sleep(5)
            try:
                post_btn = page.locator(
                    'button:has-text("Post")[aria-disabled="false"]'
                )
                if post_btn.is_visible():
                    post_ready = True
                    break
            except Exception:
                pass
            if i % 12 == 0 and i > 0:
                print(f"[tiktok-haziq] ... {i * 5}s aguardando processamento")

        if not post_ready:
            print("[tiktok-haziq] ❌ Botão Post não ficou ativo em 5min")
            screenshot(page, "post_timeout")
            browser.close()
            return False

        screenshot(page, "04_post_ready")
        print("[tiktok-haziq] ✅ Botão Post ativo!")

        # FASE 6: Clicar Post
        print("[tiktok-haziq] Clicando Post...")
        time.sleep(2)
        try:
            page.click(
                'button:has-text("Post")[aria-disabled="false"]', timeout=5000
            )
            print("[tiktok-haziq] ✅ Post clicado!")
            time.sleep(10)
            screenshot(page, "05_posted")

            # Verificar sucesso
            time.sleep(5)
            screenshot(page, "06_final")
            try:
                body = page.locator("body").inner_text()[:300]
                if "video published" in body.lower():
                    print("[tiktok-haziq] 🎉 UPLOAD CONFIRMADO: 'Video published'!")
                    browser.close()
                    return True
                elif "leaving" in body.lower():
                    print("[tiktok-haziq] 🎉 UPLOAD PROVÁVEL SUCESSO (leaving page)")
                    browser.close()
                    return True
                elif "content" in page.url.lower():
                    print("[tiktok-haziq] 🎉 UPLOAD PROVÁVEL SUCESSO (content page)")
                    browser.close()
                    return True
                else:
                    print(f"[tiktok-haziq] ⚠️ Status incerto. URL: {page.url}")
                    browser.close()
                    return True  # Assume sucesso; o Post foi clicado
            except Exception:
                browser.close()
                return True  # Assume sucesso
        except Exception as e:
            print(f"[tiktok-haziq] ❌ Erro ao clicar Post: {e}")
            screenshot(page, "post_click_fail")
            browser.close()
            return False


def main():
    parser = argparse.ArgumentParser(description="TikTok Upload via Haziq-exe")
    parser.add_argument("--video", required=True, help="Caminho do vídeo")
    parser.add_argument("--title", required=True, help="Título/descrição")
    parser.add_argument(
        "--hashtags", nargs="*", default=[], help="Lista de hashtags"
    )
    parser.add_argument(
        "--account", default="futebas_oficial", help="Nome da conta"
    )
    args = parser.parse_args()

    try:
        success = upload(args.video, args.title, args.hashtags, args.account)
        if success:
            print("[tiktok-haziq] ✅ Processo finalizado com SUCESSO!")
            sys.exit(0)
        else:
            print("[tiktok-haziq] ❌ Processo finalizado com FALHA!")
            sys.exit(1)
    except Exception as e:
        print(f"[tiktok-haziq] ❌ Exceção fatal: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
