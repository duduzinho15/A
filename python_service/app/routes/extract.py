# =============================================================================
# app/routes/extract.py — Endpoint de extração de texto/imagens
# =============================================================================
# Substitui diretamente o nó "Leitor Trafilatura" que rodava dentro do n8n.
# Chamado pelo n8n via HTTP Request node.
# =============================================================================

from fastapi import APIRouter
from pydantic import BaseModel, HttpUrl
from trafilatura import fetch_url, extract
import re
import requests
import subprocess
import os
import tempfile
from bs4 import BeautifulSoup

from app.utils.errors import ServicoExterno, ConteudoVazio
from app.utils.flaresolverr import check_flaresolverr_health, fetch_via_flaresolverr, HEADERS
from app.services.google_news import decode_google_news_url

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

class SelectorRequest(BaseModel):
    url: HttpUrl
    selectors: list[str]
    attr: str | None = None

class TranscriptRequest(BaseModel):
    url: HttpUrl
    lang: str = "pt"

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
# Endpoints
# ---------------------------------------------------------------------------

@router.post("/transcript")
async def extrair_transcript(dados: TranscriptRequest):
    """
    Extrai legendas do YouTube usando yt-dlp (já instalado).
    """
    url = str(dados.url)
    with tempfile.TemporaryDirectory() as tmpdir:
        output_template = os.path.join(tmpdir, "subs")
        try:
            subprocess.run([
                "yt-dlp", "--skip-download", "--write-auto-subs", "--write-subs",
                "--sub-langs", f"{dados.lang}.*", "--sub-format", "vtt",
                "--output", output_template, url
            ], check=True, capture_output=True, timeout=40)
            
            files = os.listdir(tmpdir)
            vtt_file = next((f for f in files if f.endswith(".vtt")), None)
            
            if not vtt_file:
                return {"status": "erro", "erro": "Legendas não encontradas."}
            
            path = os.path.join(tmpdir, vtt_file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            lines = content.split("\n")
            text_blocks = []
            for line in lines:
                line = line.strip()
                if not line or "-->" in line or "WEBVTT" in line or line.isdigit():
                    continue
                clean = re.sub(r'<.*?>', '', line)
                if clean and clean not in text_blocks:
                    text_blocks.append(clean)
            
            transcript = " ".join(text_blocks)
            return {"status": "sucesso", "transcript": transcript, "url": url}
        except Exception as e:
            return {"status": "erro", "erro": str(e), "url": url}

@router.post("/selector")
async def extrair_seletor(dados: SelectorRequest):
    """
    Equivalente ao Cheerio do n8n.
    """
    url = str(dados.url)
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, 'html.parser')
        
        resultados = {}
        for sel in dados.selectors:
            elements = soup.select(sel)
            if dados.attr:
                resultados[sel] = [el.get(dados.attr) for el in elements if el.get(dados.attr)]
            else:
                resultados[sel] = [el.get_text(strip=True) for el in elements]
        
        return {"status": "sucesso", "data": resultados, "url": url}
    except Exception as e:
        return {"status": "erro", "erro": str(e), "url": url}

@router.post("/", response_model=ExtractResponse | ExtractFallbackResponse)
async def extrair(dados: ExtractRequest):
    """
    Extrai texto e imagens de uma URL usando Trafilatura.
    """
    url_original = str(dados.url)
    url = await decode_google_news_url(url_original)
    
    try:
        html = None
        try:
            r = requests.get(url, headers=HEADERS, timeout=6, allow_redirects=True)
            if r.status_code == 200:
                html = r.text
        except:
            pass

        if not html:
            html = fetch_url(url)
            
        if not html and check_flaresolverr_health():
            html = fetch_via_flaresolverr(url)
            
        if not html:
            try:
                from app.services.playwright_scraper import fetch_html_playwright_sync
                html = fetch_html_playwright_sync(url)
                if html:
                    print(f"[Extract] Usando bypass via Playwright para {url}")
            except ImportError:
                pass

        if not html:
            raise ServicoExterno(mensagem="HTML not found via any method", url=url)

        texto_md = extract(html, include_comments=False, include_tables=True, include_formatting=True, include_images=True, output_format="markdown")
        texto = texto_md.strip() if texto_md else ""

        if len(texto) < dados.tamanho_minimo:
            alt_text = extract(html, include_tables=False)
            texto = alt_text.strip() if alt_text else ""
            if len(texto) < dados.tamanho_minimo:
                raise ConteudoVazio(mensagem="Content too short", url=url)

        imagens = re.findall(r'!\[.*?\]\((.*?)\)', texto)

        return {
            "status": "sucesso",
            "texto_materia": texto,
            "imagens_encontradas": imagens[:10],
            "fonte_url": url,
            "total_caracteres": len(texto)
        }

    except Exception as e:
        fallback = f"{dados.fallback_titulo}\n\n{dados.fallback_snippet}".strip()
        return {
            "status": "erro",
            "texto_materia": fallback,
            "imagens_encontradas": [],
            "fonte_url": url,
            "erro": str(e)
        }
