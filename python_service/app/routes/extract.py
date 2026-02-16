# =============================================================================
# app/routes/extract.py — Endpoint de extração de texto/imagens
# =============================================================================
# Substitui diretamente o nó "Leitor Trafilatura" que rodava dentro do n8n.
# Chamado pelo n8n via HTTP Request node.
#
# POST /extract
#   Body: {
#     "url": "https://...",
#     "fallback_titulo": "...",
#     "fallback_snippet": "...",
#     "tamanho_minimo": 200
#   }
# =============================================================================

from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl
from trafilatura import fetch_url, extract

from app.utils.errors import ServicoExterno, ConteudoVazio

import re
import requests

# ---------------------------------------------------------------------------
# Configuração FlareSolverr
# ---------------------------------------------------------------------------

FLARESOLVERR_URL = "http://flaresolverr:8191/v1"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

def check_flaresolverr_health() -> bool:
    """Verifica se o container do FlareSolverr está acessível."""
    try:
        requests.get("http://flaresolverr:8191", timeout=3)
        return True
    except requests.RequestException:
        return False


def fetch_via_flaresolverr(url: str) -> str | None:
    """Baixa o HTML usando FlareSolverr (bypass Cloudflare)."""
    try:
        payload = {
            "cmd": "request.get",
            "url": url,
            "headers": HEADERS,
            "maxTimeout": 60000
        }

        resp = requests.post(
            FLARESOLVERR_URL,
            json=payload,
            timeout=65
        )

        if resp.status_code == 200:
            data = resp.json()
            if data.get("status") == "ok":
                return data.get("solution", {}).get("response")

    except Exception as e:
        print(f"[FlareSolverr] Erro: {e}")

    return None


# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------

router = APIRouter(prefix="/extract", tags=["extração"])


# ---------------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------------

class ExtractRequest(BaseModel):
    url: HttpUrl
    fallback_titulo: str = ""
    fallback_snippet: str = ""
    tamanho_minimo: int = 200


class ExtractResponse(BaseModel):
    status: str
    texto_materia: str
    imagens_encontradas: list[str]
    fonte_url: str
    total_caracteres: int


class ExtractFallbackResponse(BaseModel):
    status: str
    texto_materia: str
    imagens_encontradas: list[str]
    fonte_url: str
    erro: str


# ---------------------------------------------------------------------------
# Endpoint principal
# ---------------------------------------------------------------------------

import json
import base64
from lxml import html as lxml_html # Fail fast if missing

def decode_google_news_url(url: str) -> str:
    """
    Decodifica URLs do Google News usando o método RPC 'batchexecute'.
    1. Acessa a URL original para extrair assinaturas (data-n-a-sg, data-n-a-ts).
    2. Faz um POST para o endpoint interno do Google para recuperar a URL real.
    """
    if "news.google.com" not in url and "/articles/" not in url:
        return url
        
    print(f"[Decode] STARTING DECODE v4 for {url[:30]}...")
    
    try:
        # 1. Extração do ID Base64 da URL
        match = re.search(r'articles/([A-Za-z0-9_-]+)', url)
        if not match:
            return url
        base64_id = match.group(1)

        # 2. Request inicial para obter parâmetros de assinatura
        try:
            print(f"[Decode] Baixando: {url[:60]}...")
            r = requests.get(url, headers=HEADERS, timeout=8, allow_redirects=True)
            print(f"[Decode] Status Inicial: {r.status_code}, Length: {len(r.text)}")
            print(f"[Decode] Content-Type: {r.headers.get('Content-Type', 'unknown')}")
            
            if r.status_code != 200:
                print(f"[Decode] Falha no download inicial. Status: {r.status_code}")
                return url
        except requests.RequestException as e:
            print(f"[Decode] Exception no request inicial: {e}")
            return url
            
        html = r.text
        
        if not html:
            return url

        def extract_real_url_from_html(html_content):
            """Helper local para buscar URL em HTML via LXML e Regex."""
            try:
                # from lxml import html as lxml_html (Moved to top)
                tree = lxml_html.fromstring(html_content)
                
                # 1.1 Tentar pegar link do botão "Redirect" ou similar
                links = tree.xpath('//a/@href')
                print(f"[Decode] LXML encontrou {len(links)} links.")
                
                for link in links:
                    # Filtros para ignorar links irrelevantes
                    if (link.startswith("http") and 
                        "google.com" not in link and 
                        "googleusercontent" not in link and
                        "blogger.com" not in link):
                        return link
                        
                # 1.2 Tentar window.location.replace
                js_redirect = re.search(r'window\.location\.replace\("([^"]+)"\)', html_content)
                if js_redirect:
                    return js_redirect.group(1).replace("\\u003d", "=").replace("\\u0026", "&")
                    
                # 1.3 Tentar jsname="o" (comum em redirects google news)
                # <a href="..." jsname="o">
                special_links = tree.xpath('//a[@jsname]/@href')
                for link in special_links:
                     if link.startswith("http") and "google.com" not in link:
                        return link

            except Exception as e:
                print(f"[Decode] Erro helper lxml: {e}")
                
            return None

        # TENTATIVA 1: Requests Normal
        real_url = extract_real_url_from_html(html)
        if real_url:
            print(f"[Decode] Sucesso (Requests): -> {real_url}")
            return real_url
            
        # TENTATIVA 2: FlareSolverr (se requests falhou em trazer o link)
        print("[Decode] Requests falhou em achar links. Tentando FlareSolverr...")
        if check_flaresolverr_health():
            html_fs = fetch_via_flaresolverr(url)
            if html_fs:
                real_url = extract_real_url_from_html(html_fs)
                if real_url:
                    print(f"[Decode] Sucesso (FlareSolverr): -> {real_url}")
                    return real_url

        # Se falhar parsing, tenta extrair assinaturas para RPC
        print("[Decode] Fallback para RPC...")
        try:
            sn_match = re.search(r'data-n-a-sg="([^"]+)"', html)
            ts_match = re.search(r'data-n-a-ts="([^"]+)"', html)
            
            sn = sn_match.group(1) if sn_match else None
            ts = ts_match.group(1) if ts_match else None
            
            if not sn or not ts:
                print("[Decode] Assinaturas padrao nao encontradas. Tentando WIZ_global_data...")
                # Fallback para variaveis JS do Splash Screen
                sn_wiz = re.search(r'"FdrFJe":"([^"]+)"', html)
                ts_wiz = re.search(r'"eNnkwf":"([^"]+)"', html)
                
                if sn_wiz:
                    sn = sn_wiz.group(1)
                if ts_wiz:
                    ts = ts_wiz.group(1)
            
            # Default placeholder se ainda nao achou (evita NameError, mas vai falhar no RPC provavelmente)
            if not sn: sn = "null"
            if not ts: ts = "null"

            print(f"[Decode] Assinaturas para RPC: sg={sn}, ts={ts}")
        except Exception as e:
            print(f"[Decode] Erro ao extrair assinaturas: {e}")
            sn, ts = "null", "null"
        # RPC ID: Fbv4je
        # Formato: [["Fbv4je", "[\"garturlreq\",[[\"BASE64_ID\",\"TIMESTAMP\",\"SIGNATURE\"],\"US:en\"]]", null, "generic"]]
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
        
        # 4. Enviar Request RPC
        rpc_url = "https://news.google.com/_/DotsSplashUi/data/batchexecute"
        rpc_headers = HEADERS.copy()
        rpc_headers["Content-Type"] = "application/x-www-form-urlencoded;charset=UTF-8"
        
        resp = requests.post(rpc_url, data=rpc_data, headers=rpc_headers, timeout=10)
        
        if resp.status_code != 200:
            print(f"[Decode] Erro RPC: HTTP {resp.status_code}")
            return url
            
        # 5. Parsear Resposta
        # A resposta vem com "lixo" no começo. Ex: )]}' ...
        resp_text = resp.text
        if ")]}'" in resp_text:
            resp_text = resp_text.split("\n", 1)[1]
            
        try:
            data = json.loads(resp_text)
            # data é algo como: [[ "wrb.fr", "Fbv4je", "JSON_STRING", ... ]]
            # print(f"[Decode] DATA: {str(data)[:200]}") # Debug
            
            inner_json_str = None
            if isinstance(data, list) and len(data) > 0 and isinstance(data[0], list):
                if len(data[0]) > 2:
                    inner_json_str = data[0][2]
            
            if not inner_json_str:
                print("[Decode] JSON interno não encontrado na posição esperada data[0][2]")
                print(f"[Decode] Dump parcial: {str(data)[:500]}")
                # Tentativa de busca profunda por URL
                urls = re.findall(r'(https?://[^"\s\\\\]+)', resp.text)
                for u in urls:
                    # Filtros para evitar links do próprio google/assets
                    if "news.google.com" not in u and "gstatic" not in u and "google.com" not in u:
                        decoded = u.replace("\\u003d", "=").replace("\\u0026", "&")
                        print(f"[Decode] Fallback Regex encontrou: {decoded}")
                        return decoded
                return url

            inner_data = json.loads(inner_json_str)
            
            # A URL real geralmente está em inner_data[1]
            # Ex: ["garturlres","https://site-real.com.br/noticia...", ...]
            if len(inner_data) > 1 and isinstance(inner_data[1], str) and inner_data[1].startswith("http"):
                real_url = inner_data[1]
                print(f"[Decode] Sucesso: ...{base64_id[:10]} -> {real_url}")
                return real_url
                
        except (json.JSONDecodeError, IndexError, TypeError) as e:
            print(f"[Decode] Erro ao parsear JSON do RPC: {e}")
            print(f"[Decode] Raw response snippet: {resp.text[:200]}")
            
    except Exception as e:
        print(f"[Decode] Erro genérico na decodificação: {e}")
        
    return url

@router.post(
    "/",
    response_model=ExtractResponse | ExtractFallbackResponse,
    summary="Extrai texto e imagens de uma URL"
)
async def extrair(dados: ExtractRequest):
    # 0. RESOLVER REDIRECTS (Google News specially)
    url_original = str(dados.url)
    url = decode_google_news_url(url_original)
    
    if url != url_original:
        print(f"[Extract] URL Decodificada: {url_original} -> {url}")
        
    texto = ""

    try:
        # 1. Tentativa com requests + headers (Muitas vezes mais confiável que Trafilatura direto)
        html = None
        try:
            r = requests.get(url, headers=HEADERS, timeout=12, allow_redirects=True)
            if r.status_code == 200:
                html = r.text
        except Exception as e:
            print(f"[Extract] Erro request inicial: {e}")

        # 2. Fallback: Trafilatura direto (se html vazio)
        if not html:
            try:
                html = fetch_url(url)
            except:
                pass
                
        # 3. Fallback: FlareSolverr
        if not html and check_flaresolverr_health():
            print(f"[Extract] Tentando FlareSolverr para: {url}")
            html = fetch_via_flaresolverr(url)

        if not html:
            raise ServicoExterno(mensagem="Não foi possível baixar o HTML da página.", url=url)

        # -----------------------------------------------------------------
        # 3. Extração do conteúdo principal
        # -----------------------------------------------------------------
        try:
            texto_md = extract(
                html,
                include_comments=False,
                include_tables=True,
                include_formatting=True,
                include_images=True,
                output_format="markdown"
            )
        except Exception as e:
            print(f"[Extract] Erro no extract trafilatura: {e}")
            texto_md = None

        texto = texto_md.strip() if texto_md else ""

        if not texto or len(texto) < dados.tamanho_minimo:
            # Tentar extrair apenas o texto bruto se o markdown falhou
            alt_text = extract(html, include_tables=False)
            texto = alt_text.strip() if alt_text else ""
            
            if len(texto) < dados.tamanho_minimo:
                raise ConteudoVazio(
                    mensagem=f"Extração falhou ou conteudo insuficiente ({len(texto)} chars)",
                    url=url
                )

        # -----------------------------------------------------------------
        # 4. Extração de imagens
        # -----------------------------------------------------------------
        imagens = re.findall(r'!\[.*?\]\((.*?)\)', texto)

        return {
            "status": "sucesso" if not imagens else "sucesso_com_imagens",
            "texto_materia": texto,
            "imagem_principal": imagens[0] if imagens else None,
            "imagens_encontradas": imagens[:10],
            "fonte_url": url,
            "total_caracteres": len(texto)
        }

    except (ServicoExterno, ConteudoVazio) as e:
        # Tentar usar o fallback passado pelo n8n se existir
        fallback = f"{dados.fallback_titulo}\n\n{dados.fallback_snippet}".strip()
        
        return {
            "status": "erro",
            "texto_materia": fallback if len(fallback) > 20 else "",
            "imagens_encontradas": [],
            "fonte_url": url,
            "erro": str(e)
        }

    except Exception as e:
        print(f"[Extract] Erro inesperado: {e}")
        fallback = f"{dados.fallback_titulo}\n\n{dados.fallback_snippet}".strip()
        
        return {
            "status": "erro_inesperado",
            "texto_materia": fallback if len(fallback) > 50 else "",
            "imagens_encontradas": [],
            "fonte_url": url,
            "erro": str(e)
        }
