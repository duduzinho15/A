
import re
import json
import base64
import requests
from lxml import html as lxml_html
from app.utils.flaresolverr import check_flaresolverr_health, fetch_via_flaresolverr, HEADERS

def log_debug(msg):
    try:
        with open("/app/google_news_debug.log", "a", encoding="utf-8") as f:
            f.write(msg + "\n")
            f.flush()
    except Exception as e:
        print(f"LOG ERROR: {e}")
    # Print to stdout/stderr so docker logs captures it
    print(msg, flush=True)

async def decode_google_news_url(url: str) -> str:
    """
    Decodifica URLs do Google News usando múltiplas estratégias (Requests, RPC 'batchexecute', FlareSolverr).
    """
    if "news.google.com" not in url and "/articles/" not in url:
        return url
        
    log_debug(f"[Decode] START: {url[:60]}...")
    
    try:
        # 1. Extração do ID Base64 da URL (para uso posterior no RPC)
        match = re.search(r'articles/([A-Za-z0-9_-]+)', url)
        base64_id = match.group(1) if match else None

        # 2. Request inicial para obter HTML (e tentar resolver via redirect simples/js)
        try:
            r = requests.get(url, headers=HEADERS, timeout=10, allow_redirects=True)
            if r.status_code != 200:
                log_debug(f"[Decode] STATUS {r.status_code} no requests inicial")
                html = ""
            else:
                html = r.text
                log_debug(f"[Decode] HTML obtido ({len(html)} chars). Tentando extrair...")
                
                # Helper local para extrair URL real do HTML
                def extract_real_url_from_html(html_content):
                    try:
                        tree = lxml_html.fromstring(html_content)
                        # 2.1 Links 'normais' que não são do Google
                        links = tree.xpath('//a/@href')
                        for link in links:
                            if (link.startswith("http") and 
                                "google.com" not in link and 
                                "googleusercontent" not in link and
                                "blogger.com" not in link):
                                return link
                                
                        # 2.2 JS Redirect
                        js_redirect = re.search(r'window\.location\.replace\("([^"]+)"\)', html_content)
                        if js_redirect:
                            return js_redirect.group(1).replace("\\u003d", "=").replace("\\u0026", "&")
                            
                        # 2.3 Links 'especiais' (jsname="o")
                        special_links = tree.xpath('//a[@jsname]/@href')
                        for link in special_links:
                             if link.startswith("http") and "google.com" not in link:
                                return link
                    except Exception as e:
                        log_debug(f"[Decode] Erro helper lxml: {e}")
                    return None

                # TENTA EXTRAIR DO HTML (REQUESTS)
                real_url = extract_real_url_from_html(html)
                if real_url:
                    log_debug(f"[Decode] SUCESSO via HTML/SJ: {real_url}")
                    return real_url

        except requests.RequestException as e:
            log_debug(f"[Decode] Erro requests: {e}")
            html = ""

        # 3. TENTATIVA COM FLARESOLVERR
        if not html or (html and "google.com" in url):
             log_debug("[Decode] Tentando FlareSolverr...")
             if check_flaresolverr_health():
                html_fs = fetch_via_flaresolverr(url)
                if html_fs:
                    real_url = extract_real_url_from_html(html_fs)
                    if real_url:
                        log_debug(f"[Decode] SUCESSO via FlareSolverr: {real_url}")
                        return real_url
             else:
                 log_debug("[Decode] FlareSolverr offline/unreachable")
             
             # 4. TENTATIVA FINAL COM PLAYWRIGHT (Se FlareSolverr falhar)
             log_debug("[Decode] Tentando Playwright...")
             try:
                 from app.services.playwright_decoder import decode_url_with_playwright
                 real_url = await decode_url_with_playwright(url)
                 if real_url and "google.com" not in real_url:
                     log_debug(f"[Decode] SUCESSO via Playwright: {real_url}")
                     return real_url
                 else:
                     log_debug(f"[Decode] Playwright retornou: {real_url} (ainda google?)")
             except Exception as e:
                 log_debug(f"[Decode] Erro Playwright: {e}")
            
        # 4. TENTATIVA VIA RPC (BATCHEXECUTE) - Método mais robusto para URLs novas
        if base64_id:
            log_debug("[Decode] Tentando RPC...")
            try:
                # Tenta extrair assinaturas do HTML que já baixamos (se tiver)
                sn, ts = "null", "null"
                if html:
                    sn_match = re.search(r'data-n-a-sg="([^"]+)"', html)
                    ts_match = re.search(r'data-n-a-ts="([^"]+)"', html)
                    if sn_match: sn = sn_match.group(1)
                    if ts_match: ts = ts_match.group(1)
                    
                    if sn == "null":
                         sn_wiz = re.search(r'"FdrFJe":"([^"]+)"', html)
                         if sn_wiz: sn = sn_wiz.group(1)
                    if ts == "null":
                         ts_wiz = re.search(r'"eNnkwf":"([^"]+)"', html)
                         if ts_wiz: ts = ts_wiz.group(1)

                
                # Payload RPC
                rpc_payload = [
                    [
                        "Fbv4je",
                        json.dumps(
                            ["garturlreq", [[base64_id, ts, sn], "US:en"]],
                            separators=(',', ':')
                        ),
                        None,
                        "generic"
                    ]
                ]
                
                rpc_data = {
                    "f.req": json.dumps([rpc_payload], separators=(',', ':'))
                }
                
                rpc_url = "https://news.google.com/_/DotsSplashUi/data/batchexecute"
                rpc_headers = HEADERS.copy()
                rpc_headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"
                
                resp = requests.post(rpc_url, data=rpc_data, headers=rpc_headers, timeout=15)
                
                if resp.status_code == 200:
                    resp_text = resp.text
                    if ")]}'" in resp_text:
                        resp_text = resp_text.split("\n", 1)[1]
                        
                    data = json.loads(resp_text)
                    inner_json_str = None
                    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], list):
                        if len(data[0]) > 2:
                            inner_json_str = data[0][2]
                    
                    if inner_json_str:
                        inner_data = json.loads(inner_json_str)
                        if len(inner_data) > 1 and isinstance(inner_data[1], str) and inner_data[1].startswith("http"):
                            real_url = inner_data[1]
                            log_debug(f"[Decode] SUCESSO via RPC: {real_url}")
                            return real_url
                    else:
                        # Fallback Regex na resposta RPC
                        urls = re.findall(r'(https?://[^"\s\\\\]+)', resp.text)
                        for u in urls:
                            if "news.google.com" not in u and "gstatic" not in u and "google.com" not in u:
                                decoded = u.replace("\\u003d", "=").replace("\\u0026", "&")
                                log_debug(f"[Decode] SUCESSO via RPC (Regex): {decoded}")
                                return decoded
                                
            except Exception as e:
                log_debug(f"[Decode] Erro RPC: {e}")
                
    except Exception as e:
        log_debug(f"[Decode] CRITICAL ERROR: {e}")
    
    log_debug("[Decode] FALHA TOTAL. Retornando URL original.")
    return url # Retorna original se falhar tudo
