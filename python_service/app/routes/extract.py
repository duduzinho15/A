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


from app.utils.flaresolverr import check_flaresolverr_health, fetch_via_flaresolverr, HEADERS


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


from app.services.google_news import decode_google_news_url

@router.post(
    "/",
    response_model=ExtractResponse | ExtractFallbackResponse,
    summary="Extrai texto e imagens de uma URL"
)
async def extrair(dados: ExtractRequest):

    # 0. RESOLVER REDIRECTS (Google News specially)
    url_original = str(dados.url)
    
    from app.services.google_news import log_debug
    log_debug(f"[Extract] ENTRY: {url_original[:60]}...")
    
    url = await decode_google_news_url(url_original)
    
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
