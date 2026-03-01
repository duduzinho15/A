import asyncio
from playwright.async_api import async_playwright

async def run_diagnostic():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox", 
                "--disable-setuid-sandbox", 
                "--disable-blink-features=AutomationControlled"
            ]
        )
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )
        
        # O mesmo stealth que estamos usando
        await context.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
            Object.defineProperty(navigator, 'hardwareConcurrency', { get: () => 8 });
            Object.defineProperty(navigator, 'devicePixelRatio', { get: () => 1 });
            Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
            window.chrome = { runtime: {} };
        """)
        
        page = await context.new_page()
        
        print("Acessando bot.sannysoft.com...")
        await page.goto("https://bot.sannysoft.com/", wait_until="networkidle")
        await page.wait_for_timeout(5000)
        await page.screenshot(path="/tmp/stealth_check.png", full_page=True)
        
        print("Teste concluído. Screenshot salvo em /tmp/stealth_check.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_diagnostic())
