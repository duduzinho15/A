
import asyncio
from playwright.async_api import async_playwright
import logging

# Configuração de Logs
logger = logging.getLogger("playwright_decoder")

async def decode_url_with_playwright(url: str) -> str:
    """
    Usa um browser headless (Playwright) para resolver redirects complexos (JS, Meta Refresh).
    Ideal para Google News e links obfuscados.
    """
    logger.info(f"Iniciando Playwright para: {url[:60]}...")
    print(f"[Playwright] Iniciando navegação: {url[:60]}...")

    try:
        async with async_playwright() as p:
            # Lança o browser (Headless)
            # Args para rodar em container (sandbox disabled se necessario, mas idealmente default)
            browser = await p.chromium.launch(
                headless=True,
                args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"]
            )
            
            # Contexto com User Agent real
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            
            page = await context.new_page()
            
            # Navegar e esperar network idle ou timeout
            try:
                # Goto com timeout de 20s
                # wait_until='domcontentloaded' é mais rápido que 'networkidle'
                response = await page.goto(url, timeout=20000, wait_until="domcontentloaded")
                
                # Esperar um pouco para redirects JS acontecerem
                await page.wait_for_timeout(3000)
                
                final_url = page.url
                title = await page.title()
                
                print(f"[Playwright] URL Final: {final_url}")
                print(f"[Playwright] Título: {title}")
                
                # Verifica se ainda estamos no google (consent page?)
                if "google.com" in final_url and "consent" in final_url:
                    print("[Playwright] Preso na Consent Page. Tentando aceitar...")
                    try:
                        # Tenta clicar em "Aceitar" ou "Concordo"
                        # Seletores comuns do Google
                        await page.click('button:has-text("Aceitar")', timeout=2000)
                        await page.wait_for_timeout(3000)
                        final_url = page.url
                    except:
                        pass
                
                return final_url
                
            except Exception as e:
                print(f"[Playwright] Erro durante navegação: {e}")
                # Se falhou, retorna a URL onde parou (pode ser a final mesmo com erro de timeout)
                return page.url
            finally:
                await browser.close()

    except Exception as e:
        print(f"[Playwright] Erro crítico: {e}")
        return url
