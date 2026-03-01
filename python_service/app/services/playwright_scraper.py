import asyncio
from playwright.async_api import async_playwright
import logging

logger = logging.getLogger(__name__)

async def fetch_html_playwright(url: str, timeout_ms: int = 15000) -> str:
    """
    Inicia um navegador Chromium headless localmente via Playwright,
    acessa a URL aguardando o carregamento da rede e retorna o HTML.
    Serve como Fallback anti-Cloudflare e anti-LazyLoading.
    """
    logger.info(f"[Playwright Scraper] Iniciando extração local para: {url}")
    
    html_content = ""
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context(
                # Finge ser um navegador Windows comum
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
                viewport={"width": 1920, "height": 1080},
                device_scale_factor=1,
            )
            page = await context.new_page()
            
            # Bloqueia recursos desnecessários para economizar RAM/Banda
            await page.route("**/*", lambda route: route.abort() 
                if route.request.resource_type in ["image", "media", "font"] 
                else route.continue_()
            )
            
            # Acessa a página. networkidle garante que JS inicial rodou
            await page.goto(url, wait_until="networkidle", timeout=timeout_ms)
            
            # Pequeno scroll para estourar lazy loading se houver (opcional)
            await page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
            await asyncio.sleep(1) # Aguarda render de scroll
            
            html_content = await page.content()
            
            await browser.close()
            logger.info(f"[Playwright Scraper] Sucesso ao extrair: {url[:50]}...")
            
    except Exception as e:
        logger.error(f"[Playwright Scraper] Erro ao processar {url}: {str(e)}")
        # Retorna string vazia para o extract.py seguir pro próximo fallback
        return ""
        
    return html_content

# Wrapper síncrono útil se precisarmos em um contexto não async
def fetch_html_playwright_sync(url: str, timeout_ms: int = 15000) -> str:
    import asyncio
    return asyncio.run(fetch_html_playwright(url, timeout_ms))

if __name__ == "__main__":
    # Teste rápido direto pelo arquivo
    url_teste = "https://ge.globo.com/futebol/brasileirao-serie-a/"
    resultado = fetch_html_playwright_sync(url_teste)
    print(f"Extraídos {len(resultado)} bytes de HTMtL")
