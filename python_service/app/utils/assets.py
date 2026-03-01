# =============================================================================
# app/utils/assets.py — Download de Assets Iniciais (B-Roll sem copyright)
# =============================================================================
#
# RESPONSABILIDADE:
#   Baixa vídeos de B-roll (futebol, torcida) sem direitos autorais via yt-dlp
#   ao iniciar o container, garantindo que o motor de vídeo sempre tenha
#   material básico disponível caso as buscas externas falhem.
#
# VALIDAÇÃO DUMMYIMAGE:
#   Adicionamos _PLACEHOLDER_DOMAINS — conjunto de domínios conhecidos que
#   retornam imagens de placeholder/erro (ex: dummyimage.com, via.placeholder.com).
#   Qualquer URL desses domínios é rejeitada ANTES de ser baixada, evitando
#   que imagens genéricas de "404 not found" entrem no vídeo.
#
#   POR QUE ISSO IMPORTA:
#   Algumas APIs de imagem retornam URLs de placeholder quando o item não existe.
#   Se não filtrarmos, o vídeo ficaria com uma imagem cinza genérica com texto
#   "400x300" — algo completamente inadequado para um vídeo de futebol.
# =============================================================================

import os
import asyncio
import logging
import yt_dlp
from typing import List
from urllib.parse import urlparse
from app.config import settings

logger = logging.getLogger("assets")

# =============================================================================
# LISTA NEGRA DE DOMÍNIOS PLACEHOLDER (Etapa 3 — FASE 1)
# =============================================================================
#
# Esses são serviços que geram imagens genéricas de tamanho/cor aleatória.
# Quando uma API retorna uma URL desses domínios, significa que o conteúdo
# real não estava disponível — o servidor devolveu um placeholder de erro.
#
# A verificação é feita pelo DOMÍNIO (não pela URL completa) para pegar
# qualquer variação: dummyimage.com/100x100, dummyimage.com/400x300/red, etc.
#
_PLACEHOLDER_DOMAINS = {
    "dummyimage.com",
    "via.placeholder.com",
    "placeholder.com",
    "placekitten.com",
    "lorempixel.com",
    "fillmurray.com",
    "picsum.photos",       # Útil em dev, mas não em produção de vídeo
    "fakeimg.pl",
    "loremflickr.com",
    "placeimg.com",
}


def is_placeholder_url(url: str) -> bool:
    """
    Verifica se uma URL aponta para um domínio de placeholder/dummy.

    Retorna True se deve ser REJEITADA, False se é uma URL válida.

    Como funciona:
      1. Parseamos a URL para extrair apenas o hostname (netloc)
      2. Comparamos com a lista negra _PLACEHOLDER_DOMAINS
      3. Usamos .removeprefix("www.") para pegar "www.dummyimage.com" também

    Exemplos:
      is_placeholder_url("https://dummyimage.com/400x300") → True (REJEITAR)
      is_placeholder_url("https://i.imgur.com/abc.jpg")    → False (ACEITAR)
    """
    try:
        parsed = urlparse(url)
        # netloc retorna o hostname completo, ex: "www.dummyimage.com"
        # removemos o "www." para simplificar a comparação
        domain = parsed.netloc.lower().removeprefix("www.")
        return domain in _PLACEHOLDER_DOMAINS
    except Exception:
        # URL malformada: melhor rejeitar do que arriscar
        return True


def filter_valid_urls(urls: List[str]) -> List[str]:
    """
    Filtra uma lista de URLs, removendo placeholders e URLs vazias.

    Deve ser chamado ANTES de qualquer download de imagem.
    Registra no log quantas URLs foram rejeitadas para diagnóstico.

    Args:
        urls: Lista de URLs brutas vindas de APIs de imagem

    Returns:
        Lista filtrada com apenas URLs válidas
    """
    valid = []
    rejected_count = 0

    for url in urls:
        if not url or not url.startswith("http"):
            rejected_count += 1
            continue
        if is_placeholder_url(url):
            logger.warning(
                "[Assets] URL de placeholder rejeitada: %s", url[:80]
            )
            rejected_count += 1
            continue
        valid.append(url)

    if rejected_count > 0:
        logger.info(
            "[Assets] Filtradas %d URL(s) inválida(s)/%s placeholder(s). Restam %d URLs válidas.",
            rejected_count, rejected_count, len(valid)
        )

    return valid


# URLs ou Queries para B-roll inicial
# Usando busca do yt-dlp para garantir que sempre ache algo
INITIAL_ASSETS = [
    {"category": "torcida", "query": "ytsearch1:football crowd atmosphere no copyright"},
    {"category": "torcida", "query": "ytsearch1:soccer fans chanting stock footage"},
    {"category": "futebol", "query": "ytsearch1:soccer cinematic skills 4k no copyright"},
    {"category": "futebol", "query": "ytsearch1:football training b-roll no copyright"},
    {"category": "futebol", "query": "ytsearch1:soccer slow motion goal celebration no copyright"},
]


def download_initial_assets():
    """
    Baixa assets iniciais de B-roll se a pasta estiver vazia.

    Estratégia:
      - Roda no startup do container (ou em background)
      - Para cada categoria, verifica se já existem ≥ 2 vídeos
      - Só baixa o que falta — idempotente e seguro para re-deploy
      - Formato preferencial: mp4 ≤ 1080p (compatível com moviepy)
    """
    base_dir = os.path.join(settings.DATA_MIDIA, "broll")
    logger.info("[Assets] Verificando assets iniciais em %s ...", base_dir)

    ydl_opts = {
        "format": "bestvideo[ext=mp4][height<=1080]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "quiet": True,
        "no_warnings": True,
        "ignoreerrors": True,   # Não para em erro de um vídeo — continua os outros
        "noplaylist": True,
    }

    for item in INITIAL_ASSETS:
        category = item["category"]
        cat_dir = os.path.join(base_dir, category)
        os.makedirs(cat_dir, exist_ok=True)

        # Idempotência: pula se já tem ≥ 2 vídeos MP4 nessa categoria
        existing = [f for f in os.listdir(cat_dir) if f.endswith(".mp4")]
        if len(existing) >= 2:
            logger.info("[Assets] Categoria '%s' já tem %d vídeos — skip", category, len(existing))
            continue

        logger.info("[Assets] Baixando B-roll para '%s': %s", category, item["query"])

        current_opts = ydl_opts.copy()
        current_opts["outtmpl"] = os.path.join(
            base_dir, category, "%(title).20s-%(id)s.%(ext)s"
        )

        try:
            with yt_dlp.YoutubeDL(current_opts) as ydl:
                ydl.download([item["query"]])
            logger.info("[Assets] B-roll baixado para categoria '%s'", category)
        except Exception as e:
            # Não deixamos um erro de download parar o servidor
            logger.warning("[Assets] Erro ao baixar '%s': %s", item["query"], e)

    logger.info("[Assets] Verificação completa de assets iniciais.")


async def download_assets_background():
    """Wrapper assíncrono para rodar download_initial_assets() sem bloquear o main thread."""
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, download_initial_assets)
