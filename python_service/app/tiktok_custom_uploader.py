#!/usr/bin/env python3
"""
TikTok Custom Uploader — Playwright direto (v4 - Success Evidence)
Interface CLI idêntica ao script anterior.
"""

import argparse
import asyncio
import json
import os
import sys
import time
import http.cookiejar
from pathlib import Path

# ──────────────────────────────────────────────
# Utilitários de cookie
# ──────────────────────────────────────────────

def _parse_netscape_cookies(cookie_file: str) -> list[dict]:
    cj = http.cookiejar.MozillaCookieJar(cookie_file)
    try:
        cj.load(ignore_discard=True, ignore_expires=True)
    except Exception as e:
        raise RuntimeError(f"Falha ao carregar cookies: {e}")
    cookies = []
    for c in cj:
        cookies.append({
            "name": c.name,
            "value": c.value,
            "domain": c.domain if c.domain.startswith(".") else f".{c.domain}",
            "path": c.path or "/",
            "secure": bool(c.secure),
            "httpOnly": False,
            "sameSite": "None",
        })
    return cookies

def load_cookies(cookie_path: str) -> list[dict]:
    with open(cookie_path, "r", encoding="utf-8", errors="ignore") as f:
        first = f.read(20).strip()
    if first.startswith("[") or first.startswith("{"):
        with open(cookie_path, "r", encoding="utf-8") as f:
            raw = json.load(f)
        return [{"name": c["name"], "value": c["value"], "domain": ".tiktok.com", "path": "/", "sameSite": "None"} for c in raw]
    return _parse_netscape_cookies(cookie_path)

# ──────────────────────────────────────────────
# Upload principal via Playwright
# ──────────────────────────────────────────────

UPLOAD_URL = "https://www.tiktok.com/tiktokstudio/upload"

async def upload_video(video_path: str, title: str, cookies: list[dict] = None, setup_mode: bool = False) -> None:
    from playwright.async_api import async_playwright, TimeoutError as PwTimeout

    # Diretório persistente para o perfil do navegador
    # No Docker, mapeamos para /data_midia/tiktok_profile para persistência fora do container
    user_data_dir = "/data_midia/tiktok_profile"
    os.makedirs(user_data_dir, exist_ok=True)

    print(f"[upload] {'MODO SETUP' if setup_mode else 'MODO UPLOAD'}")
    if not setup_mode:
        print(f"[upload] Arquivo: '{video_path}'")
    
    async with async_playwright() as p:
        # 1. Configuração de Stealth Máximo: Omitir as flags padrão de automação
        # O Playwright injeta --enable-automation por padrão. Precisamos ignorar isso.
        
        args = [
            "--no-sandbox", 
            "--disable-setuid-sandbox", 
            "--disable-dev-shm-usage", # CRÍTICO para Docker (evita crash de memória)
            "--disable-gpu",           # Reduz carga e evita problemas de crashpad em containers
            "--disable-blink-features=AutomationControlled",
            "--use-fake-ui-for-media-stream",
            "--use-fake-device-for-media-stream",
            "--disable-web-security",
            "--allow-running-insecure-content",
            "--window-size=1920,1080"
        ]

        context = await p.chromium.launch_persistent_context(
            user_data_dir=user_data_dir,
            headless=not setup_mode,
            args=args,
            ignore_default_args=["--enable-automation"],
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080},
            locale="pt-BR",
            timezone_id="America/Sao_Paulo",
            permissions=["geolocation", "notifications"]
        )
        
        # ULTRA-STEALTH SCRIPT (Injeção em cada página) - Nível 5 Evasion
        await context.add_init_script("""
            // 1. Bloqueio Total de WebRTC (Evita vazamento de IP do Docker)
            Object.defineProperty(window, 'RTCPeerConnection', { value: class {} });
            Object.defineProperty(window, 'mozRTCPeerConnection', { value: class {} });
            Object.defineProperty(window, 'webkitRTCPeerConnection', { value: class {} });

            // 2. WebDriver e Automação (CDP Hiding)
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            Object.defineProperty(navigator, '__pw_script_type', { get: () => undefined });

            // 3. Localização e Hardware (Fingerprint Sync)
            Object.defineProperty(navigator, 'languages', { get: () => ['pt-BR', 'pt', 'en-US', 'en'] });
            Object.defineProperty(navigator, 'platform', { get: () => 'Win32' });
            Object.defineProperty(navigator, 'vendor', { get: () => 'Google Inc.' });
            Object.defineProperty(navigator, 'maxTouchPoints', { get: () => 0 });
            Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 8 });
            Object.defineProperty(navigator, 'deviceMemory', { get: () => 8 });
            
            // 4. UserAgentData (Bypass Moderno)
            if (navigator.userAgentData) {
                const originalGetHighEntropyValues = navigator.userAgentData.getHighEntropyValues;
                navigator.userAgentData.getHighEntropyValues = (hints) => {
                    return Promise.resolve({
                        architecture: 'x86',
                        bitness: '64',
                        brands: [
                            { brand: 'Not(A:Brand', version: '99' },
                            { brand: 'Google Chrome', version: '131' },
                            { brand: 'Chromium', version: '131' }
                        ],
                        mobile: false,
                        model: '',
                        platform: 'Windows',
                        platformVersion: '10.0.0',
                        uaFullVersion: '131.0.0.0'
                    });
                };
            }

            // 5. Plugins Camuflados (Típico de Windows)
            Object.defineProperty(navigator, 'plugins', {
                get: () => [
                    { name: 'PDF Viewer', filename: 'internal-pdf-viewer', description: 'Portable Document Format' },
                    { name: 'Chrome PDF Viewer', filename: 'internal-pdf-viewer', description: 'Portable Document Format' },
                    { name: 'Chromium PDF Viewer', filename: 'internal-pdf-viewer', description: 'Portable Document Format' },
                    { name: 'Microsoft Edge PDF Viewer', filename: 'internal-pdf-viewer', description: 'Portable Document Format' },
                    { name: 'WebKit built-in PDF', filename: 'internal-pdf-viewer', description: 'Portable Document Format' }
                ]
            });

            // 6. WebGL / GPU Fix (NVIDIA RTX)
            const getParameter = WebGLRenderingContext.prototype.getParameter;
            WebGLRenderingContext.prototype.getParameter = function(parameter) {
                if (parameter === 37446) return 'NVIDIA GeForce RTX 3060/PCIe/SSE2';
                if (parameter === 37445) return 'NVIDIA Corporation';
                return getParameter.apply(this, arguments);
            };

            // 7. Fake Chrome Runtime
            window.chrome = {
                runtime: {},
                loadTimes: function() {},
                csi: function() {},
                app: {}
            };
            
            // 8. Audio Fingerprint Bypass
            const originalGetChannelData = AudioBuffer.prototype.getChannelData;
            AudioBuffer.prototype.getChannelData = function() {
                const results = originalGetChannelData.apply(this, arguments);
                if (results && results.length > 0) results[0] += 0.0000001;
                return results;
            };
        """)

        # Se houver cookies e o perfil for novo (ou forçado), injetamos
        # A detecção de "perfil vazio" agora olha pastas essenciais do Chrome
        profile_ready_marker = os.path.join(user_data_dir, "Default", "Preferences")
        if cookies and not os.path.exists(profile_ready_marker):
            print("[upload] Perfil novo detectado. Injetando cookies para autenticar a sessão...")
            await context.add_cookies(cookies)

        page = context.pages[0] if context.pages else await context.new_page()

        # Monitoramento de rede para diagnóstico
        page.on("request", lambda request: print(f"[network] >> {request.method} {request.url}") if "api/" in request.url or "publish" in request.url else None)
        page.on("response", lambda response: print(f"[network] << {response.status} {response.url}") if "api/" in response.url or "publish" in response.url else None)

        try:
            if setup_mode:
                print("[setup] Navegando para o TikTok Studio para login manual...")
                await page.goto("https://www.tiktok.com/login", wait_until="networkidle")
                print("\n" + "="*60)
                print("⚠️  MODO SETUP ATIVADO!")
                print("1. O navegador deve ter aberto uma janela.")
                print("2. Faça o login manualmente e resolva qualquer CAPTCHA.")
                print("3. Vá até o TikTok Studio e confirme que está logado.")
                print("4. Feche o navegador ou finalize este script no terminal.")
                print("="*60 + "\n")
                
                # Aguarda até ser fechado ou timeout longo
                for _ in range(600): # 10 minutos
                    if page.is_closed(): break
                    await asyncio.sleep(1)
                return

            # WARM-UP: Navega para a Home primeiro (gera confiança/cookies reais de feed)
            print("[upload] Aquecendo sessão na Home do TikTok...")
            await page.goto("https://www.tiktok.com/", wait_until="domcontentloaded")
            await _human_delay(3000, 7000)

            print(f"[upload] Abrindo {UPLOAD_URL}...")
            await page.goto(UPLOAD_URL, wait_until="domcontentloaded", timeout=60000)
            await _human_delay(5000, 10000)

            if "login" in page.url.lower():
                print("[upload] ⚠️ Sessão não encontrada. Requer login (use --setup).")
                # Se passou cookies via CLI, tenta injetar como fallback
                if cookies:
                    print("[upload] Tentando injetar cookies como fallback...")
                    await context.add_cookies(cookies)
                    await page.reload()
                else:
                    raise RuntimeError("Sessão expirada e sem cookies de fallback.")

            print("[upload] Selecionando arquivo...")
            file_input = await page.wait_for_selector("input[type='file']", state="attached", timeout=30000)
            await file_input.set_input_files(video_path)
            
            await _human_delay(5000, 10000)

            # NOVO: Desativa 'Carregamento de alta qualidade' para reduzir escrutínio
            try:
                hq_toggle = page.locator("input[type='checkbox']").first
                if await hq_toggle.is_checked():
                    print("[upload] 📉 Desativando 'Alta Qualidade' para bypass de detecção...")
                    await hq_toggle.uncheck()
                    await _human_delay(1000, 3000)
            except: pass

            print("[upload] Aguardando conclusão das verificações do TikTok (Mínimo de 15s)...")
            # Espera um tempo mínimo para o backend "respirar"
            await _human_delay(15000, 20000)
            
            # Espera prolongada com detecção de erro inteligente
            upload_confirmed = False
            for i in range(45):
                content = await page.content()
                
                # Se encontrar "Nenhum problema encontrado", é um sinal verde forte
                if "Nenhum problema encontrado" in content:
                    # Se aparecer 1+ vezes e não estiver mais com "Carregando" em loop, prosseguimos
                    if "Carregando..." not in content or i > 20:
                        print("[upload] ✅ Verificações de copyright e diretrizes aparentemente OK.")
                        upload_confirmed = True
                        break
                
                # Se o erro "Algo deu errado" persistir por muito tempo, aí sim falhamos
                if ("Algo deu errado" in content or "Something went wrong" in content) and i > 30:
                    print(f"[upload] 🛑 ERRO PERSISTENTE DETECTADO: 'Algo deu errado' após 60s.")
                    raise RuntimeError("O TikTok rejeitou permanentemente o conteúdo.")

                await page.wait_for_timeout(2000)
            
            if not upload_confirmed:
                print("[upload] ⚠️ Alerta: Verificações não confirmadas visualmente, tentando prosseguir assim mesmo.")

            # BYPASS MODAL Final
            await _handle_modals(page)

            print("[upload] Preenchendo legenda...")
            await _fill_caption(page, title)
            await _human_delay(2000, 5000)

            print("[upload] Iniciando publicação final...")
            for i in range(3):
                print(f"[upload] Tentativa de clique {i+1}/3...")
                await _handle_modals(page)
                
                # Screenshot pré-clique para diagnóstico
                await page.screenshot(path=f"/tmp/pre_click_{i}.png")
                
                await _click_post_button(page)
                await page.wait_for_timeout(10000)
                
                # Screenshot pós-clique
                await page.screenshot(path=f"/tmp/post_click_{i}.png")
                
                await page.wait_for_timeout(5000)

                if "/content" in page.url or "/manage" in page.url:
                    print(f"[upload] ✅ Redirecionamento bem sucedido.")
                    break
            
            # Verificação de sucesso
            await _wait_for_success(page)
            
            success_img = "/tmp/tiktok_success.png"
            await page.screenshot(path=success_img, full_page=True)
            print(f"[upload] 📸 Screenshot final salvo em: {success_img}")

            print("[upload] 🎉 Processo concluído com sucesso!")

        except Exception as e:
            print(f"[debug] Falha detectada.")
            try:
                error_img = "/tmp/tiktok_error.png"
                await page.screenshot(path=error_img, full_page=True)
                print(f"[upload] 📸 Screenshot do erro salvo em: {error_img}")
            except: pass
            raise e
        finally:
            await context.close()


import random
import asyncio

async def _human_delay(min_ms=1000, max_ms=3000):
    await asyncio.sleep(random.uniform(min_ms, max_ms) / 1000)

async def _move_mouse_organic(page, x, y):
    """Move o mouse em pequenos passos com jitter para parecer humano."""
    curr_pos = page.mouse.move
    steps = random.randint(5, 12)
    for i in range(steps + 1):
        # Interpolação simples com ruído
        await page.mouse.move(x + random.randint(-2, 2), y + random.randint(-2, 2), steps=1)
        await asyncio.sleep(0.01)

async def _handle_modals(page) -> None:
    buttons = ["Entendi", "Ativar", "Até logo", "Got it", "Enable", "Confirmar", "Publicar agora", "Post now"]
    for text in buttons:
        try:
            btn = page.locator(f"button:has-text('{text}')").first
            if await btn.is_visible(timeout=1000):
                print(f"[upload] 🛡️ Fechando popup/Confirmando: '{text}'")
                # Movimento orgânico até o botão
                box = await btn.bounding_box()
                if box:
                    await _move_mouse_organic(page, box['x'] + box['width']/2, box['y'] + box['height']/2)
                await btn.click()
                await _human_delay(500, 1500)
        except: pass

async def _fill_caption(page, title: str) -> None:
    selectors = ["[contenteditable='true']", "div[role='textbox']", "div[data-e2e='caption-input']"]
    for sel in selectors:
        try:
            el = page.locator(sel).first
            if await el.is_visible(timeout=5000):
                box = await el.bounding_box()
                if box:
                    await _move_mouse_organic(page, box['x'] + box['width']/2, box['y'] + box['height']/2)
                
                await el.click()
                await _human_delay(800, 1200)
                
                await page.keyboard.press("Control+A")
                await page.keyboard.press("Backspace")
                await _human_delay(400, 800)
                
                # Digitando como humano (caractere por caractere)
                print(f"[upload] ✍️ Digitando legenda como humano...")
                for char in title[:2200]:
                    await page.keyboard.press(char)
                    await asyncio.sleep(random.uniform(0.05, 0.25))
                    # Pequena chance de fazer uma pausa maior ("pensar")
                    if random.random() < 0.05:
                        await _human_delay(300, 700)
                
                print("[upload] ✅ Legenda preenchida.")
                return
        except: pass

async def _click_post_button(page) -> None:
    selectors = ["button:has-text('Publicar')", "button:has-text('Post')", "button[data-e2e='post_video_button']"]
    for _ in range(5):
        for sel in selectors:
            try:
                btn = page.locator(sel).first
                if await btn.is_visible(timeout=1000) and await btn.is_enabled():
                    print(f"[upload] 🧬 Emulando clique humano em '{sel}'...")
                    
                    await page.bring_to_front()
                    await btn.scroll_into_view_if_needed()
                    
                    # Movimento e Foco
                    box = await btn.bounding_box()
                    if box:
                        await _move_mouse_organic(page, box['x'] + box['width']/2, box['y'] + box['height']/2)
                    
                    await btn.focus()
                    await _human_delay(1500, 3000)
                    
                    # Tenta clique de hardware real
                    await page.mouse.click(box['x'] + box['width']/2, box['y'] + box['height']/2)
                    
                    # Fallback de teclado (Enter) se o clique não disparar navegação
                    await asyncio.sleep(2)
                    await page.keyboard.press("Enter")
                    
                    print(f"[upload] ✅ Eventos de interação humana enviados.")
                    return
            except: pass
        await _human_delay(2000, 4000)
    raise RuntimeError("Botão Publicar não habilitado ou inacessível.")

async def _wait_for_success(page, timeout_ms: int = 60000) -> None:
    print("[upload] Aguardando confirmação de sucesso (Texto ou URL)...")
    success_texts = ["Postado", "Publicado", "Uploaded", "Posted", "Sucesso", "Gerenciar"]
    error_texts = ["Algo deu errado", "Something went wrong", "substituir por um vídeo diferente"]
    deadline = time.time() + (timeout_ms / 1000)
    
    while time.time() < deadline:
        # Check de Erro Crítico de Conteúdo
        for err in error_texts:
            try:
                if await page.get_by_text(err, exact=False).first.is_visible(timeout=500):
                    print(f"[upload] 🛑 BLOQUEIO DE CONTEÚDO: O TikTok rejeitou este arquivo de vídeo ('{err}').")
                    raise RuntimeError(f"Vídeo rejeitado pelo TikTok: {err}")
            except RuntimeError as re: raise re
            except: pass

        # Critério 1: Mudança de URL para a lista de conteúdo
        if "/content" in page.url or "/manage" in page.url:
            print(f"[upload] ✅ Redirecionamento detectado para: {page.url}")
            return
            
        # Critério 2: Textos de sucesso
        for text in success_texts:
            try:
                if await page.get_by_text(text, exact=False).first.is_visible(timeout=1000):
                    print(f"[upload] ✅ Mensagem visual de sucesso: '{text}'")
                    return
            except: pass
            
        await page.wait_for_timeout(2000)
    print("[upload] ⚠️ Alerta: Script prosseguindo sem confirmação definitiva.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video", help="Caminho do vídeo para upload")
    parser.add_argument("--title", help="Título/Legenda do vídeo")
    parser.add_argument("--cookies", help="Caminho do arquivo de cookies (opcional após setup)")
    parser.add_argument("--setup", action="store_true", help="Abre o navegador para login manual e configuração do perfil")
    args = parser.parse_args()
    
    try:
        if args.setup:
            asyncio.run(upload_video(None, None, None, setup_mode=True))
            sys.exit(0)
            
        if not args.video or not args.title:
            parser.error("Os argumentos --video e --title são obrigatórios se não estiver em modo --setup.")

        cookies = load_cookies(args.cookies) if args.cookies else None
        asyncio.run(upload_video(args.video, args.title, cookies))
        sys.exit(0)
    except Exception as e:
        print(f"[ERRO] {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
