# =============================================================================
# app/routes/ai.py — Cérebro da Automação v2.0 (Anti-Alucinação + AIDA)
# =============================================================================
# MELHORIAS v2.0:
#   - Persona de narrador configurável (raiz / fanático / analítico)
#   - Estrutura AIDA (Atenção, Interesse, Desejo, Ação) no roteiro
#   - Open Loop: pergunta no início respondida APENAS no final
#   - Chain-of-thought: LLM "pensa" antes de gerar o JSON
#   - Campos novos: keywords_visuais, quote, tipo_noticia
#   - Padrão de título forçado com número/pergunta/emoção
#   - Data Storytelling: stats → metáforas narrativas
#   - Integração com Google Trends (pytrends, gratuito)
#   - Logging estruturado (sem print())
# =============================================================================
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
import httpx
import json
import re
import datetime
import logging
from app.config import settings
from app.utils.errors import ServicoExterno
# get_db_connection: usada para salvar o log de IA no banco (coluna ai_log)
from app.utils.database import get_db_connection

router = APIRouter(prefix="/ai", tags=["IA"])
logger = logging.getLogger("ai_routes")

CURRENT_YEAR = 2026
CURRENT_DATE = f"20 de fevereiro de {CURRENT_YEAR}"

# =============================================================================
# MODELS
# =============================================================================

class AIRequest(BaseModel):
    content: str
    context: Optional[str] = None
    max_tokens: int = 1000
    persona: str = "fanático"       # "fanático" | "raiz" | "analítico"
    platform: str = "shorts"         # "shorts" | "long"
    tipo_noticia: Optional[str] = None  # transferência/crise/análise-tática/histórico/gol

class TranslateRequest(BaseModel):
    text: str
    target_lang: str = "português do Brasil"
    context: Optional[str] = "notícias de futebol"

@router.post("/translate")
async def translate_text(req: TranslateRequest):
    """
    Traduz texto preservando jargões de futebol. 
    Usa LLM para garantir tradução contextual (ex: 'clean sheet' -> 'não tomou gol').
    """
    system = (
        "Você é um tradutor especialista em futebol. "
        f"Traduza o texto para {req.target_lang} mantendo o tom esportivo e jargões adequados. "
        "Retorne APENAS o texto traduzido."
    )
    prompt = f"Contexto: {req.context}\n\nTexto para traduzir:\n{req.text}"
    
    resp = await call_ollama(prompt, system)
    if not resp:
        resp = await call_gemini(prompt, system)
    
    return {"status": "sucesso", "translated_text": resp or req.text}

@router.post("/detect")
async def detect_language(req: AIRequest):
    """Detecta o idioma do texto usando o LLM."""
    system = "Identifique o idioma do texto a seguir. Responda APENAS com o código ISO do idioma (ex: pt, en, es, fr)."
    prompt = req.content[:500]
    
    resp = await call_ollama(prompt, system)
    if not resp:
        resp = "pt" # Default
    
    clean_resp = re.sub(r'[^a-z]', '', resp.strip().lower())[:2]
    return {"status": "sucesso", "language": clean_resp or "pt"}

class AnalyzeResponse(BaseModel):
    relevant: bool
    category: str
    priority: str
    reasoning: str

class DecideResponse(BaseModel):
    decision: str
    format: str
    aggregation: str
    region: str
    reasoning: str

class ScriptResponse(BaseModel):
    title: str
    blocks: list[dict]
    thumbnail_text: str
    image_prompt: str
    hook: str
    cta: str
    metadata: dict
    keywords_visuais: Optional[List[str]] = []
    quote: Optional[str] = ""
    tipo_noticia: Optional[str] = "Noticia"
    mood: Optional[str] = "Epic"
    search_terms: Optional[List[str]] = []
    # --- Novos campos da Fase 2 (v11) ---
    placar: Optional[str] = ""
    gols: Optional[List[str]] = []
    artilheiros: Optional[List[str]] = []
    estadio: Optional[str] = ""

class ViralScoreResponse(BaseModel):
    score: int  # 0-100
    potential: str # "Viral", "Médio", "Nicho"
    recommendations: List[str]
    hook_strength: int # 1-10

class MetadataResponse(BaseModel):
    title: str
    description: str
    tags: List[str]
    trending_sound: str

# =============================================================================
# PERSONAS DE NARRADOR
# =============================================================================

PERSONAS = {
    "fanático": (
        "Você é um torcedor fanático de futebol brasileiro — apaixonado, "
        "emotivo, usa gírias como 'rapaziada', 'é nóis', 'que absurdo', 'meu'. "
        "Linguagem direta, coloquial, como um fã falaria no grupo do WhatsApp."
    ),
    "raiz": (
        "Você é um jornalista esportivo veterano — sério, factual, respeitoso. "
        "Tom neutro, informativo. Usa termos técnicos de futebol brasileiro "
        "('pressão alta', 'giro de bola', 'saída de bola'). "
        "Linguagem de rádio esportiva brasileira dos anos 90."
    ),
    "analítico": (
        "Você é um analista tático de futebol — preciso, usa dados e estatísticas. "
        "Compara com histórico, cita xG, pressão, posse. "
        "Tom de podcast de análise, inteligente mas acessível ao torcedor comum."
    )
}

# =============================================================================
# PROVIDERS LLM (Ollama → Gemini → Claude)
# =============================================================================

async def call_ollama(prompt: str, system: str = "") -> Optional[str]:
    """Chama Ollama local — modelo principal via Chat API."""
    try:
        url = f"{settings.OLLAMA_URL}/api/chat"
        payload = {
            "model": settings.OLLAMA_MODEL, 
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            "stream": False,
            "format": "json",
            "options": {"temperature": 0.7, "num_ctx": 4096}
        }
        async with httpx.AsyncClient(timeout=90.0) as client:
            resp = await client.post(url, json=payload)
            if resp.status_code == 200:
                result = resp.json().get("message", {}).get("content", "")
                logger.info("[AI] Ollama OK (Model: %s): %d chars", settings.OLLAMA_MODEL, len(result))
                return result
            logger.warning("[AI] Ollama Error: %d - %s", resp.status_code, resp.text[:150])
    except httpx.ConnectError:
        logger.warning("[AI] Ollama recusou conexão (rodando em %s?)", settings.OLLAMA_URL)
    except Exception as e:
        logger.error("[AI] Ollama Exception: %s", e)
    return None


async def call_gemini(prompt: str, system: str = "") -> Optional[str]:
    """Fallback: Google Gemini API (v1)."""
    if not settings.GEMINI_API_KEY:
        return None
    try:
        # v1 é mais estável para modelos flash recentes
        url = (
            f"https://generativelanguage.googleapis.com/v1/models/"
            f"gemini-1.5-flash:generateContent?key={settings.GEMINI_API_KEY}"
        )
        full_prompt = f"{system}\n\nTask: {prompt}" if system else prompt
        payload = {"contents": [{"parts": [{"text": full_prompt}]}]}
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(url, json=payload)
            if resp.status_code == 200:
                logger.info("[AI] Gemini OK")
                return resp.json()["candidates"][0]["content"]["parts"][0]["text"]
            logger.warning("[AI] Gemini Error: %d - %s", resp.status_code, resp.text[:150])
    except Exception as e:
        logger.error("[AI] Gemini Exception: %s", e)
    return None


async def call_groq(prompt: str, system: str = "") -> Optional[str]:
    """Fallback Ultrarrápido: Groq API (Llama 3.3)."""
    if not settings.GROQ_API_KEY:
        return None
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {settings.GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.3-70b-versatile",  # Atualizado (antigo 8192 decommissioned)
            "messages": [
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 1024
        }
        async with httpx.AsyncClient(timeout=20.0) as client:
            resp = await client.post(url, json=payload, headers=headers)
            if resp.status_code == 200:
                logger.info("[AI] Groq (Llama3-70B) OK")
                return resp.json()["choices"][0]["message"]["content"]
            logger.warning("[AI] Groq Error: %d - %s", resp.status_code, resp.text[:150])
    except Exception as e:
        logger.error("[AI] Groq Exception: %s", e)
    return None


async def call_claude(prompt: str, system: str = "") -> Optional[str]:
    """Fallback Secundário: Anthropic Claude API."""
    if not settings.CLAUDE_API_KEY:
        return None
    try:
        url = "https://api.anthropic.com/v1/messages"
        headers = {
            "x-api-key": settings.CLAUDE_API_KEY,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
        payload = {
            "model": "claude-3-haiku-20240307",
            "max_tokens": 1024,
            "messages": [{"role": "user", "content": prompt}]
        }
        if system:
            payload["system"] = system
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(url, json=payload, headers=headers)
            if resp.status_code == 200:
                logger.info("[AI] Claude OK")
                return resp.json()["content"][0]["text"]
            logger.warning("[AI] Claude Error: %d - %s", resp.status_code, resp.text[:150])
    except Exception as e:
        logger.error("[AI] Claude Exception: %s", e)
    return None


# =============================================================================
# TRENDS (pytrends) + SEARCH FALLBACK
# =============================================================================

async def get_trending_topics_enhanced(query: str = "futebol") -> dict:
    """
    Combina Google Trends (gratuito, pytrends) + Serper/Tavily como fallback.
    Retorna dict com trending_now, trend_context e lista de tendências.
    """
    trend_context = {}

    # 1. Google Trends (pytrends — 100% gratuito)
    try:
        from app.services.trends import enrich_script_context
        trend_context = enrich_script_context(query, "")
        if trend_context.get("trending_now"):
            logger.info("[AI] Trends via pytrends: %d itens", len(trend_context["trending_now"]))
            return trend_context
    except Exception as e:
        logger.warning("[AI] pytrends falhou: %s — usando Serper/Tavily", e)

    # 2. Fallback: Tavily / Serper
    trends_list = []
    if settings.TAVILY_API_KEY:
        try:
            url = "https://api.tavily.com/search"
            payload = {
                "api_key": settings.TAVILY_API_KEY,
                "query": f"{query} trending futebol brazil 2026",
                "search_depth": "basic", "max_results": 3
            }
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.post(url, json=payload)
                if resp.status_code == 200:
                    for r in resp.json().get("results", []):
                        trends_list.append(r["title"])
        except Exception:
            pass

    if not trends_list and settings.SERPER_API_KEY:
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.post(
                    "https://google.serper.dev/search",
                    headers={"X-API-KEY": settings.SERPER_API_KEY, "Content-Type": "application/json"},
                    json={"q": f"{query} trending now", "num": 3}
                )
                if resp.status_code == 200:
                    for r in resp.json().get("organic", []):
                        trends_list.append(r["title"])
        except Exception:
            pass

    return {
        "trending_now": trends_list[:5],
        "trend_context": f"🔥 EM ALTA: {', '.join(trends_list[:5])}" if trends_list else ""
    }


# =============================================================================
# HELPERS
# =============================================================================

def extract_json(text: str) -> Dict[str, Any]:
    """Extrai e parseia JSON de uma string (mesmo com texto antes/depois)."""
    try:
        # Tenta encontrar o bloco de JSON mais externo
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            json_str = match.group()
            # Se o JSON estiver truncado (falta fechar }), tenta consertar
            if json_str.count('{') > json_str.count('}'):
                logger.warning("[AI] JSON truncado detectado. Tentando fechar chaves...")
                json_str += "}" * (json_str.count('{') - json_str.count('}'))
            return json.loads(json_str)
        return json.loads(text)
    except Exception as e:
        logger.error("[AI] Falha ao extrair JSON: %s | Texto original: %s", e, text[:100])
        return {}


def save_ai_log(
    job_id: Optional[str],
    endpoint: str,
    model_used: str,
    prompt_summary: str,
    response_text: str,
    success: bool
) -> None:
    """
    Persiste o log da chamada LLM na coluna ai_log do Postgres.

    Por que salvar isso?
      - Auditoria: conseguimos rever exatamente o que foi enviado ao LLM.
      - Debug: se o roteiro sair ruim, comparamos prompt vs resposta.
      - Reprocessamento: podemos re-executar o prompt sem reprocessar a notícia.
      - Analytics: podemos ver qual modelo foi usado com mais frequência.

    Args:
        job_id:        ID do job no banco. None = chamada sem job (ex: chamada direta via Swagger).
        endpoint:      Nome do endpoint: '/ai/script', '/ai/metadata', '/ai/analyze'.
        model_used:    'llama3.3', 'gemini-1.5-flash' ou 'claude-3-haiku'.
        prompt_summary: Primeiros 200 chars do prompt (evita payload gigante no banco).
        response_text:  Primeiros 500 chars da resposta do LLM.
        success:       True se o JSON foi parseado com sucesso.
    """
    # Se não temos job_id, não há linha no banco para atualizar — sair silenciosamente.
    if not job_id:
        return

    try:
        conn = get_db_connection()
        if not conn:
            logger.warning("[AI Log] Banco indisponível — log não salvo para job %s", job_id)
            return

        # Montamos o payload JSON que será gravado na coluna ai_log.
        # Usamos json.dumps para garantir encoding correto de caracteres especiais.
        log_payload = json.dumps({
            "endpoint": endpoint,
            "model": model_used,
            "timestamp_utc": datetime.datetime.utcnow().isoformat(),
            "prompt_preview": prompt_summary[:200],    # Truncamos para não estourar o banco
            "response_preview": response_text[:500],   # Idem
            "success": success
        }, ensure_ascii=False)

        with conn.cursor() as cur:
            # jsonb_build_object + || (merge JSONB) anexa o novo log sem apagar os anteriores.
            # Isso permite múltiplas chamadas de IA no mesmo job (script + metadata = 2 entradas).
            cur.execute(
                """
                UPDATE video_jobs
                SET ai_log = COALESCE(ai_log, '{}')::jsonb
                            || jsonb_build_object(%s, %s::jsonb),
                    updated_at = CURRENT_TIMESTAMP
                WHERE id = %s
                """,
                (endpoint, log_payload, job_id)
            )
            conn.commit()
            logger.info("[AI Log] Log salvo para job %s | endpoint=%s | model=%s | ok=%s",
                        job_id, endpoint, model_used, success)
    except Exception as e:
        # Não deixamos o log quebrar o fluxo de produção.
        # A resiliência do pipeline é mais importante que o log.
        logger.warning("[AI Log] Falha ao salvar log (não crítico): %s", e)
    finally:
        try:
            conn.close()
        except Exception:
            pass


# =============================================================================
# ENDPOINTS
# =============================================================================

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_content(req: AIRequest):
    """Analisa relevância e categoriza o conteúdo."""
    system = (
        "Você é um editor chefe de canal de futebol brasileiro. "
        f"Data atual: {CURRENT_DATE}. "
        "Analise e responda estritamente em formato JSON: "
        '{"relevant": bool, "category": "futebol"|"geral"|"outro", '
        '"priority": "high"|"medium"|"low", "reasoning": "explicação curta"}. '
        "'high' para polêmicas, transferências, finais. 'medium' para jogos. 'low' para rumores."
    )
    prompt = f"Analise a notícia:\n{req.content}"

    resp = await call_ollama(prompt, system)
    if not resp:
        resp = await call_groq(prompt, system)
    if not resp:
        resp = await call_gemini(prompt, system)
    if not resp:
        resp = await call_claude(prompt, system)
    if not resp:
        return {"relevant": False, "category": "unknown", "priority": "low", "reasoning": "AI unavailable"}

    data = extract_json(resp)
    # Garante que o campo 'reasoning' exista (fallback para 'reason' se a IA ignorar o prompt)
    reasoning = data.get("reasoning", data.get("reason", "Parsed from AI"))
    
    return {
        "relevant": data.get("relevant", False),
        "category": data.get("category", "geral"),
        "priority": data.get("priority", "low"),
        "reasoning": reasoning
    }


@router.post("/decide", response_model=DecideResponse)
async def decide_format(req: AIRequest):
    """Decide o formato do vídeo (Short/Long) e estratégias."""
    system = (
        "Você é um estrategista de conteúdo digital (YouTube/TikTok). "
        f"Data: {CURRENT_DATE}. "
        "Decida o melhor formato. JSON: "
        '{"decision": "video"|"discard", "format": "short"|"long", '
        '"aggregation": "solo"|"giro", "region": "brasil"|"europa"|"mundo", "reasoning": "..."}. '
        "Shorts para notícias rápidas/virais. Long para análises táticas."
    )
    prompt = f"Conteúdo: {req.content}\nPlataforma: {req.platform}"

    resp = await call_ollama(prompt, system)
    if not resp:
        resp = await call_groq(prompt, system)
    if not resp:
        resp = await call_gemini(prompt, system)
    if not resp:
        resp = await call_claude(prompt, system)
    if not resp:
        return {"decision": "discard", "format": "short", "aggregation": "solo", "region": "mundo", "reasoning": "AI unavailable"}

    data = extract_json(resp)
    return {
        "decision": data.get("decision", "discard"),
        "format": data.get("format", "short"),
        "aggregation": data.get("aggregation", "solo"),
        "region": data.get("region", "mundo"),
        "reasoning": data.get("reasoning", "Parsed from AI")
    }


@router.post("/script", response_model=ScriptResponse)
async def generate_script(req: AIRequest):
    """
    Gera roteiro estruturado com:
    - Estrutura AIDA (Atenção → Interesse → Desejo → Ação)
    - Open Loop (pergunta no início respondida no final)
    - Chain-of-thought (reflexão antes do JSON)
    - Persona configurável (fanático / raiz / analítico)
    - Keywords visuais para B-roll
    - Quote de jogador/técnico se disponível
    - Tipo de notícia para seleção de template
    - Integração com Google Trends
    """
    # Busca contexto de tendências
    trends = await get_trending_topics_enhanced(req.content[:60])
    trend_ctx = trends.get("trend_context", "")

    # NOVIDADE: Busca feedback orgânico (Bluesky / YouTube / Twitter)
    try:
        from app.routes.feedback import search_social_feedback
        social_fb = await search_social_feedback(req.content[:60])
        fb_ctx = social_fb.get("social_context", "")
    except Exception as e:
        logger.warning(f"[AI] Erro ao buscar social feedback: {e}")
        fb_ctx = ""

    # Persona do narrador
    persona_desc = PERSONAS.get(req.persona, PERSONAS["fanático"])

    # Template por tipo de notícia
    tipo = req.tipo_noticia or "Noticia"
    tipo_instructions = {
        "transferência": "Foque na negociação, valores, impacto no elenco. Use verbos de ação: 'assinou', 'fechou', 'acertou'.",
        "crise": "Tom mais sério/reflexivo. Mostre impacto no torcedor. Termine com esperança.",
        "análise-tática": "Use termos técnicos. Dados e métricas. Tom analítico.",
        "histórico": "Contexto emocional. Compare com feitos históricos. Tom épico.",
        "gol": "Máxima energia! Descreva o momento. Tom explosivo e comemorativo.",
        "Noticia": "Factual, objetivo, informativo. Entregue o fato principal no segundo 5."
    }.get(tipo, "Factual e direto.")

    system = (
        f"{persona_desc}\n\n"
        f"🗓️ ANO ATUAL: {CURRENT_YEAR}. Data: {CURRENT_DATE}.\n"
        "🚫 PROIBIÇÕES ABSOLUTAS:\n"
        "  - NUNCA mencione COVID-19, pandemia ou eventos antes de 2024\n"
        "  - NUNCA invente fatos, estatísticas ou falas de jogadores\n"
        "  - NUNCA invente placares ou nomes de gols genéricos (ex: 'Jogador A', 'Jogador B'). Se não souber, deixe os campos vazios.\n"
        "  - NUNCA use 'inclusive', 'destaque-se', 'vale ressaltar'\n"
        "  - NUNCA use linguagem corporativa ou jornalística formal em excesso\n"
        "  - NUNCA misture idiomas. Use APENAS Português Brasileiro correto:\n"
        "    ✗ 'CRISIS' → ✓ 'CRISE'\n"
        "    ✗ 'rubbedo-negro' → ✓ 'rubro-negro'\n"
        "    ✗ 'team' → ✓ 'time'\n\n"
        f"🎬 TIPO DE VÍDEO: {tipo}\n"
        f"📋 INSTRUÇÃO DE ESTILO: {tipo_instructions}\n\n"
        "📐 ESTRUTURA OBRIGATÓRIA (AIDA — DURAÇÃO 60s):\n"
        "  Parte 1 — GANCHO EXPLOSIVO (0-5s): Pergunta retórica OU fato chocante.\n"
        "    ↳ Abra um Open Loop: 'Você sabe o que aconteceu com X?' (responda SÓ no final)\n"
        "  Parte 2 — CONTEXTO E DADOS (5-45s): Fatos reais, placar e estatísticas.\n"
        "    ↳ SE HOUVER RESULTADO: Narre o placar com entusiasmo! 'O jogo terminou em X a Y!'.\n"
        "    ↳ Data storytelling: converta números em metáforas.\n"
        "    ↳ Se houver quote de jogador/técnico no texto, USE-O literalmente.\n"
        "  Parte 3 — IMPACTO E CALLBACK (45-55s): O que isso muda? Feche o Open Loop.\n"
        "  Parte 4 — CTA (55-65s): Pergunta para comentários + 'siga o Futebas'\n\n"
        "⏳ RITMO E ENTONAÇÃO:\n"
        "  - Use a marcação '[PAUSA]' no meio do texto para criar suspense dramático de 300ms. Ex: 'E o resultado foi... [PAUSA] inacreditável!'\n\n"
        "📦 SAÍDA: APENAS JSON válido:\n"
        "{\n"
        '  "think": "raciocínio interno em 1-2 frases antes do roteiro",\n'
        '  "title": "Título IMPACTANTE — use CAPS em 1 palavra-chave + número ou pergunta",\n'
        '  "blocks": [{"text": "fala do narrador", "type": "speech"}],\n'
        '  "thumbnail_text": "Texto da capa (max 4 palavras, CAPS)",\n'
        '  "image_prompt": "Descrição visual em inglês para busca de imagem",\n'
        '  "hook": "Frase do gancho <5s",\n'
        '  "cta": "Pergunta para comentários",\n'
        '  "keywords_visuais": ["Palmeiras Arena", "gols partida", "torcida comemorando"],\n'
        '  "quote": "Fala literal se houver, ou string vazia",\n'
        '  "tipo_noticia": "transferência"|"crise"|"análise-tática"|"histórico"|"gol"|"Noticia",\n'
        '  "mood": "Epic"|"Happy"|"Rock"|"Sad",\n'
        '  "search_terms": ["termo em inglês", "para busca"],\n'
        '  "placar": "2x1",\n'
        '  "gols": ["Nome Jogador 10\'", "Nome Jogador 45\'"],\n'
        '  "artilheiros": ["Nome 1", "Nome 2"],\n'
        '  "estadio": "Nome do Estádio"\n'
        "}\n"
        "IMPORTANTE: roteiro deve ter entre 300 e 400 palavras para garantir ~60s de áudio."
    )

    prompt = (
        f"📰 NOTÍCIA:\n{req.content}\n\n"
        f"{trend_ctx}\n\n"
        f"{fb_ctx}\n\n"
        "Gere o roteiro seguindo RIGOROSAMENTE a estrutura AIDA acima."
    )

    resp = await call_ollama(prompt, system)
    # Controla qual modelo foi realmente usado (para o ai_log)
    model_used = settings.OLLAMA_MODEL
    if not resp:
        resp = await call_groq(prompt, system)
        model_used = "groq-llama3-70b"
    if not resp:
        resp = await call_gemini(prompt, system)
        model_used = "gemini-1.5-flash"
    if not resp:
        resp = await call_claude(prompt, system)
        model_used = "claude-3-haiku"

    if not resp:
        logger.error("[AI] Falha TOTAL em todos os provedores de IA (Ollama, Groq, Gemini, Claude)")
        # Fallback de emergência (Hardcoded) para não quebrar a produção
        return {
            "title": "URGENTE: Notícia de Futebol",
            "blocks": [{"text": f"Atenção torcedor! Temos novidades sobre: {req.content[:100]}... Fique ligado para mais detalhes em breve.", "type": "speech"}],
            "thumbnail_text": "URGENTE",
            "image_prompt": "soccer stadium epic",
            "hook": "Olha o que aconteceu!",
            "cta": "Siga para mais!",
            "keywords_visuais": ["soccer stadium"],
            "quote": "",
            "tipo_noticia": tipo,
            "mood": "Epic",
            "search_terms": ["football news"],
            "placar": "",
            "gols": [],
            "artilheiras": [],
            "estadio": "",
            "metadata": {"provider": "emergency-fallback"}
        }

    data = extract_json(resp)
    script_ok = bool(data)  # True se o JSON foi parseado com sucesso

    # --- SALVA LOG NO BANCO (Etapa 2 — FASE 1) ---
    # job_id pode vir no campo context (n8n envia como string "job_id=...") ou ser None.
    # Tentamos extrair: "job_id=uuid" do campo req.context.
    job_id_match = re.search(r"job_id=([\w-]+)", req.context or "")
    job_id = job_id_match.group(1) if job_id_match else None
    save_ai_log(
        job_id=job_id,
        endpoint="/ai/script",
        model_used=model_used,
        prompt_summary=prompt[:200],
        response_text=resp[:500],
        success=script_ok
    )

    if not data:
        logger.warning("[AI] JSON inválido do roteiro, usando fallback simples")
        return {
            "title": "Notícia do Futebol",
            "blocks": [{"text": resp, "type": "speech"}],
            "thumbnail_text": "VEJA ISSO",
            "image_prompt": "Estádio de futebol Brasil",
            "hook": "Você não vai acreditar!",
            "cta": "Deixa seu comentário!",
            "metadata": {"raw": resp[:50]},
            "keywords_visuais": ["soccer stadium Brazil", "football players training"],
            "quote": "",
            "tipo_noticia": tipo,
            "mood": "Epic"
        }

    logger.info("[AI] Roteiro gerado: tipo=%s | mood=%s | %d blocks | model=%s",
                data.get("tipo_noticia", tipo),
                data.get("mood", "Epic"),
                len(data.get("blocks", [])),
                model_used)

    # --- FACT GUARD (Ideia #21) — Validação Anti-Alucinação ---
    try:
        from app.services.fact_checker import validate_script, apply_corrections
        fact_report = await validate_script(req.content, data, use_llm=True)
        if not fact_report["valid"]:
            logger.warning(
                "[FACT-CHECK] %d issue(s) detectada(s) — aplicando correções automáticas",
                fact_report["total_issues"]
            )
            data = fact_report["corrected_data"]
    except Exception as e:
        logger.error(f"[FACT-CHECK] Erro no Fact Guard (não bloqueante): {e}")

    return {
        "title": data.get("title", "Título Viral"),
        "blocks": data.get("blocks", []),
        "thumbnail_text": data.get("thumbnail_text", "URGENTE"),
        "image_prompt": data.get("image_prompt", "football match Brazil"),
        "hook": data.get("hook", "Olha isso!"),
        "cta": data.get("cta", "Comenta aí!"),
        "keywords_visuais": data.get("keywords_visuais", ["soccer stadium", "football"]),
        "quote": data.get("quote", ""),
        "tipo_noticia": data.get("tipo_noticia", tipo),
        "mood": data.get("mood", "Epic"),
        "search_terms": data.get("search_terms", ["soccer match", "football stadium"]),
        "placar": data.get("placar", ""),
        "gols": data.get("gols", []),
        "artilheiros": data.get("artilheiros", data.get("artilheiras", [])),
        "estadio": data.get("estadio", ""),
        "metadata": {"provider": "ai-service", "persona": req.persona, "model": model_used}
    }


@router.post("/metadata", response_model=MetadataResponse)
async def generate_metadata(req: AIRequest):
    """
    Gera Título, Descrição (≤280 chars), Tags (exatamente 15 hashtags SEO).
    Integra Google Trends para hashtags em alta.
    """
    # Busca context de tendências e feedback social (Ideia #7)
    trends = await get_trending_topics_enhanced(req.content[:50])
    trends_str = ", ".join(trends.get("trending_now", [])[:5])
    
    social_fb_ctx = ""
    try:
        from app.routes.feedback import search_social_feedback
        social_fb = await search_social_feedback(req.content[:60])
        social_fb_ctx = social_fb.get("social_context", "")
        if social_fb_ctx:
            logger.info("[AI] SEO Loop: Contexto social integrado na metadata")
    except Exception as e:
        logger.warning(f"[AI] Erro ao buscar social feedback para metadata: {e}")

    system = (
        "Você é um Especialista em SEO para YouTube Shorts e TikTok de futebol brasileiro. "
        f"Data atual: {CURRENT_DATE}. "
        "REGRAS ABSOLUTAS:\n"
        "  1. Título: use padrão 'CHOCANTE! [Fato Principal] — O que ACONTECEU?' ou similar\n"
        "     — inclua número OU pergunta OU palavra em CAPS\n"
        "  2. Description: máx 280 chars. Comece com emoji. Termine com CTA. SEM hashtags aqui.\n"
        "  3. Tags: EXATAMENTE 15 hashtags. SEMPRE incluir: #Futebas #Futebol #Shorts\n"
        "     + 12 hashtags SEO do tema (times, competição, jogadores, termos virais)\n\n"
        "JSON ESTRITO — APENAS ISSO:\n"
        '{"title": "...", "description": "...", "tags": ["#tag1", ..., "#tag15"], '
        '"trending_sound": "nome de som em alta"}\n\n'
        f"TRENDS BRASIL AGORA: {trends_str}\n"
        f"{social_fb_ctx}\n"
        "Se houver debate social (FEEDBACK SOCIAL), use termos polêmicos ou de curiosidade das redes para o título."
    )
    prompt = f"Gere metadata IRRESISTÍVEL para o vídeo sobre:\n{req.content}"

    resp = await call_ollama(prompt, system)
    # Controla qual modelo foi realmente usado (para o ai_log)
    model_used = settings.OLLAMA_MODEL
    if not resp:
        resp = await call_groq(prompt, system)
        model_used = "groq-llama3-70b"
    if not resp:
        resp = await call_gemini(prompt, system)
        model_used = "gemini-1.5-flash"
    if not resp:
        resp = await call_claude(prompt, system)
        model_used = "claude-3-haiku"

    if not resp:
        return {
            "title": "Notícia de Futebol",
            "description": "⚽ Confira as últimas do futebol brasileiro! Siga o Futebas para mais.",
            "tags": ["#Futebas", "#Futebol", "#Shorts", "#FutebolBrasileiro",
                     "#Paulistao2026", "#Noticias", "#Viral", "#Brazil",
                     "#Futebol2026", "#CampeonatoBrasileiro", "#Gols",
                     "#Esportes", "#TikTok", "#YouTube", "#Copa"],
            "trending_sound": "Original Sound"
        }

    data = extract_json(resp)
    metadata_ok = bool(data)

    # --- SALVA LOG NO BANCO (Etapa 2 — FASE 1) ---
    job_id_match = re.search(r"job_id=([\w-]+)", req.context or "")
    job_id = job_id_match.group(1) if job_id_match else None
    save_ai_log(
        job_id=job_id,
        endpoint="/ai/metadata",
        model_used=model_used,
        prompt_summary=prompt[:200],
        response_text=resp[:500],
        success=metadata_ok
    )

    # Garante que as tags obrigatórias estão presentes
    tags = data.get("tags", [])
    mandatory = ["#Futebas", "#Futebol", "#Shorts"]
    for m in mandatory:
        if not any(t.lower() == m.lower() for t in tags):
            tags.insert(0, m)
    tags = tags[:15]

    logger.info("[AI] Metadata gerada: %d chars descrição | %d tags | model=%s",
                len(data.get("description", "")), len(tags), model_used)

    return {
        "title": data.get("title", "Título Incrível"),
        "description": data.get("description", "Confira as notícias do futebol!"),
        "tags": tags,
        "trending_sound": data.get("trending_sound", "Original Sound")
    }


@router.post("/viral-score", response_model=ViralScoreResponse)
async def analyze_virality(req: AIRequest):
    """Prediz o potencial de viralização da pauta."""
    system = (
        "Você é um especialista em algoritmos de Reels/Shorts/TikTok. "
        "Analise a pauta e dê um score de virality (0-100). "
        "Considere: polêmica, busca, impacto emocional e novidade. "
        "JSON: "
        '{"score": int, "potential": "Viral"|"Médio"|"Nicho", '
        '"recommendations": ["dica de edição", "dica de hook"], "hook_strength": int}'
    )
    prompt = f"Analise a virilidade desta notícia de futebol:\n{req.content}"

    resp = await call_ollama(prompt, system)
    model_used = settings.OLLAMA_MODEL
    if not resp:
        resp = await call_groq(prompt, system)
        model_used = "groq-llama3-70b"
    if not resp:
        resp = await call_gemini(prompt, system)
        model_used = "gemini-1.5-flash"
    if not resp:
        resp = await call_claude(prompt, system)
        model_used = "claude-3-haiku"

    success = True
    if not resp:
        logger.error("[AI] Falha total no viral-score. Usando fallback seguro.")
        data = {"score": 50, "potential": "Médio", "recommendations": ["Foque em um vídeo dinâmico"], "hook_strength": 5}
        model_used = "fallback"
        success = False
    else:
        data = extract_json(resp)
        if not data:
            data = {"score": 50, "potential": "Médio", "recommendations": ["Foque em um vídeo dinâmico"], "hook_strength": 5}
            success = False

    # Log para auditoria
    save_ai_log(
        job_id=None,
        endpoint="/ai/viral-score",
        model_used=model_used,
        prompt_summary=req.content[:100],
        response_text=str(resp),
        success=success
    )

    return {
        "score": data.get("score", 50),
        "potential": data.get("potential", "Médio"),
        "recommendations": data.get("recommendations", ["Foque em um bom gancho"]),
        "hook_strength": data.get("hook_strength", 5)
    }
