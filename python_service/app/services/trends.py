"""
trends.py — Google Trends Integration (100% Gratuito via pytrends)
===================================================================
Módulo para enriquecer roteiros e prompts de IA com palavras-chave
em alta no Google Trends Brasil — sem chave de API, completamente free.

Uso principal:
  - Detectar ângulos virais antes de gerar o roteiro
  - Enriquecer o prompt do LLM com contexto de tendências
  - Priorizar notícias que coincidam com termos em alta

Fallback: se pytrends falhar (rate limit do Google), retorna lista vazia
sem bloquear o pipeline de geração de vídeo.
"""

import logging
from typing import List, Dict, Optional

logger = logging.getLogger("trends")

# =============================================================================
# TENDÊNCIAS EM TEMPO REAL
# =============================================================================

def get_trending_now(geo: str = "BR", count: int = 10) -> List[str]:
    """
    Retorna os trending topics em tempo real no Google (Brasil por padrão).

    Args:
        geo: Código do país (BR, US, PT...)
        count: Número máximo de trends para retornar

    Returns:
        Lista de strings com os tópicos em alta.
        Ex: ["Palmeiras", "Copa do Brasil", "Vini Jr", ...]
    """
    try:
        from pytrends.request import TrendReq

        logger.info("[Trends] Buscando trends em tempo real (geo=%s)...", geo)
        pt = TrendReq(hl="pt-BR", tz=-180)
        trending_df = pt.trending_searches(pn=geo.lower())
        trends = trending_df[0].tolist()[:count]

        logger.info("[Trends] %d trends encontrados: %s", len(trends), trends[:5])
        return trends

    except ImportError:
        logger.warning("[Trends] pytrends não instalado — instale com: pip install pytrends")
        return []
    except Exception as e:
        logger.warning("[Trends] Erro ao buscar trends em tempo real: %s", e)
        return []


def get_interest_over_time(keywords: List[str], geo: str = "BR") -> Dict[str, int]:
    """
    Retorna o nível de interesse (0-100) para cada keyword no Google Trends.
    Útil para ranquear qual ângulo de notícia tem mais potencial viral.

    Args:
        keywords: Lista de termos para checar (máx 5 por limitação da API)
        geo: Código do país

    Returns:
        Dicionário {keyword: score} onde score é 0-100.
        Ex: {"Vini Jr gol": 85, "Palmeiras treino": 12}
    """
    if not keywords:
        return {}

    # pytrends limita a 5 keywords por requisição
    keywords = keywords[:5]

    try:
        from pytrends.request import TrendReq

        logger.info("[Trends] Checando interesse para: %s", keywords)
        pt = TrendReq(hl="pt-BR", tz=-180)
        pt.build_payload(keywords, cat=20, timeframe="now 7-d", geo=geo)
        df = pt.interest_over_time()

        if df.empty:
            logger.info("[Trends] Sem dados para as keywords fornecidas.")
            return {}

        # Retorna a média da última semana por keyword
        scores = {}
        for kw in keywords:
            if kw in df.columns:
                scores[kw] = int(df[kw].mean())
        logger.info("[Trends] Scores: %s", scores)
        return scores

    except ImportError:
        logger.warning("[Trends] pytrends não instalado.")
        return {}
    except Exception as e:
        logger.warning("[Trends] Erro ao buscar interest_over_time: %s", e)
        return {}


def get_related_queries(topic: str, geo: str = "BR") -> List[str]:
    """
    Retorna consultas relacionadas ao tópico no Google Trends.
    Excelente para descobrir o que as pessoas REALMENTE perguntam sobre um tema.

    Args:
        topic: Tópico principal (ex: "São Paulo FC", "Palmeiras")
        geo: Código do país

    Returns:
        Lista de queries relacionadas em alta.
    """
    try:
        from pytrends.request import TrendReq

        logger.info("[Trends] Buscando queries relacionadas a '%s'...", topic)
        pt = TrendReq(hl="pt-BR", tz=-180)
        pt.build_payload([topic], cat=20, timeframe="now 7-d", geo=geo)

        related = pt.related_queries()
        result = []

        if topic in related and related[topic]["rising"] is not None:
            rising = related[topic]["rising"]
            result = rising["query"].tolist()[:8]

        logger.info("[Trends] Queries relacionadas: %s", result)
        return result

    except ImportError:
        logger.warning("[Trends] pytrends não instalado.")
        return []
    except Exception as e:
        logger.warning("[Trends] Erro ao buscar queries relacionadas: %s", e)
        return []


# =============================================================================
# HELPER INTEGRADO PARA O PIPELINE DE ROTEIRO
# =============================================================================

def enrich_script_context(news_title: str, news_content: str) -> dict:
    """
    Função principal de integração com o pipeline de geração de roteiro.
    Retorna um dicionário de contexto de tendências para injetar no prompt da IA.

    Args:
        news_title: Título da notícia
        news_content: Conteúdo/resumo da notícia

    Returns:
        {
            "trending_now": [...],          # Trends gerais Brasil
            "interest_score": {...},        # Score de interesse por keyword
            "related_queries": [...],       # Queries relacionadas
            "trend_context": "string"       # Texto formatado para injetar no prompt
        }
    """
    context = {
        "trending_now": [],
        "interest_score": {},
        "related_queries": [],
        "trend_context": ""
    }

    # 1. Trending agora no Brasil
    trending = get_trending_now(geo="BR", count=10)
    context["trending_now"] = trending

    # 2. Extrai keywords do título para checar interesse
    # Usa as primeiras 3 palavras do título como keywords
    title_words = [w for w in news_title.split() if len(w) > 3][:3]
    if title_words:
        context["interest_score"] = get_interest_over_time(title_words)

    # 3. Queries relacionadas ao tema principal
    if title_words:
        context["related_queries"] = get_related_queries(title_words[0])

    # 4. Formata contexto para o prompt
    parts = []
    if trending:
        parts.append(f"🔥 TRENDING AGORA (Brasil): {', '.join(trending[:5])}")
    if context["interest_score"]:
        high_interest = {k: v for k, v in context["interest_score"].items() if v > 50}
        if high_interest:
            parts.append(f"📈 ALTO INTERESSE: {', '.join(f'{k}({v})' for k, v in high_interest.items())}")
    if context["related_queries"]:
        parts.append(f"🔍 BUSCAS RELACIONADAS: {', '.join(context['related_queries'][:4])}")

    context["trend_context"] = "\n".join(parts) if parts else "Sem dados de trends disponíveis."

    logger.info("[Trends] Contexto gerado para '%s': %d trends | %d scores | %d queries",
                news_title[:30], len(trending), len(context["interest_score"]),
                len(context["related_queries"]))

    return context
