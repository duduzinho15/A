# =============================================================================
# app/routes/ai.py — Cérebro da Automação (Análise e Roteirização)
# =============================================================================
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
import httpx
import json
import re
import datetime
from app.config import settings
from app.utils.errors import ServicoExterno

router = APIRouter(prefix="/ai", tags=["IA"])

# --- Models ---

class AIRequest(BaseModel):
    content: str
    context: Optional[str] = None
    max_tokens: int = 1000

class AnalyzeResponse(BaseModel):
    relevant: bool
    category: str
    priority: str
    reasoning: str

class DecideResponse(BaseModel):
    decision: str  # "video", "discard"
    format: str    # "short", "long"
    aggregation: str # "solo", "giro"
    region: str    # "brasil", "europa", "mundo"
    reasoning: str

class ScriptResponse(BaseModel):
    title: str
    blocks: list[dict]
    thumbnail_text: str
    image_prompt: str
    hook: str
    cta: str
    metadata: dict

class MetadataResponse(BaseModel):
    title: str
    description: str
    tags: List[str]
    trending_sound: str

# --- Providers ---

async def call_ollama(prompt: str, system: str = "") -> Optional[str]:
    """Chama Ollama local."""
    try:
        url = f"{settings.OLLAMA_URL}/api/generate"
        payload = {
            "model": settings.OLLAMA_MODEL,
            "prompt": prompt,
            "system": system,
            "stream": False,
            "options": {"temperature": 0.7}
        }
        async with httpx.AsyncClient(timeout=60.0) as client:
            resp = await client.post(url, json=payload)
            if resp.status_code == 200:
                print(f"[AI] Ollama Success: {len(resp.json().get('response', ''))} chars")
                return resp.json().get("response", "")
            print(f"[AI] Ollama Error: {resp.status_code} - {resp.text}")
    except httpx.ConnectError:
        print(f"[AI] Ollama Connection Refused (Is Ollama running at {settings.OLLAMA_URL}?)")
    except Exception as e:
        import traceback
        print(f"[AI] Ollama Exception: {e}")
        traceback.print_exc()
    return None

async def call_gemini(prompt: str, system: str = "") -> Optional[str]:
    """Fallback: Chama Google Gemini API."""
    if not settings.GEMINI_API_KEY:
        print("[AI] Gemini key not configured.")
        return None
        
    try:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={settings.GEMINI_API_KEY}"
        full_prompt = f"{system}\n\nTask: {prompt}" if system else prompt
        
        payload = {
            "contents": [{
                "parts": [{"text": full_prompt}]
            }]
        }
        
        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(url, json=payload)
            if resp.status_code == 200:
                data = resp.json()
                try:
                    return data["candidates"][0]["content"]["parts"][0]["text"]
                except (KeyError, IndexError):
                    return None
            print(f"[AI] Gemini Error: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"[AI] Gemini Exception: {e}")
    return None

async def call_claude(prompt: str, system: str = "") -> Optional[str]:
    """Fallback Secundário: Chama Anthropic Claude API."""
    if not settings.CLAUDE_API_KEY:
        print("[AI] Claude key not configured.")
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
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }
        if system:
            payload["system"] = system

        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(url, json=payload, headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                return data["content"][0]["text"]
            print(f"[AI] Claude Error: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"[AI] Claude Exception: {e}")
    return None

# --- External Tools (Search) ---

async def get_trending_topics(query: str = "futebol") -> List[str]:
    """Busca trending topics/hashtags via Tavily ou Serper."""
    trends = []
    
    # 1. Tavily
    if settings.TAVILY_API_KEY:
        try:
            url = "https://api.tavily.com/search"
            payload = {
                "api_key": settings.TAVILY_API_KEY,
                "query": f"{query} trending topics news",
                "search_depth": "basic",
                "max_results": 3
            }
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.post(url, json=payload)
                if resp.status_code == 200:
                    results = resp.json().get("results", [])
                    for r in results:
                        trends.append(r["title"])
        except Exception:
            pass

    # 2. Serper (se Tavily falhar ou para complementar)
    if not trends and settings.SERPER_API_KEY:
        try:
            url = "https://google.serper.dev/search"
            headers = {
                "X-API-KEY": settings.SERPER_API_KEY,
                "Content-Type": "application/json"
            }
            payload = {"q": f"{query} trending now", "num": 3}
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.post(url, json=payload, headers=headers)
                if resp.status_code == 200:
                    organic = resp.json().get("organic", [])
                    for r in organic:
                        trends.append(r["title"])
        except Exception:
            pass
            
    return trends[:5]

# --- Helper de JSON ---

def extract_json(text: str) -> Dict[str, Any]:
    """Tenta extrair e parsear JSON de uma string."""
    try:
        match = re.search(r"\{.*\}", text, re.DOTALL)
        json_str = match.group() if match else text
        return json.loads(json_str)
    except:
        return {}

# --- Endpoints ---

@router.post("/analyze", response_model=AnalyzeResponse)
async def analyze_content(req: AIRequest):
    """Analisa relevância e categoriza o conteúdo."""
    system = (
        "Você é um editor chefe de um canal de esporte/futebol. "
        "Analise o conteúdo. Responda APENAS um JSON: "
        '{"relevant": bool, "category": "futebol"|"geral"|"outro", "priority": "high"|"medium"|"low", "reasoning": "explicação curta"}. '
        "Critérios: 'high' para polêmicas, transferências bomba, finais. 'medium' para jogos normais. 'low' para rumores fracos."
    )
    prompt = f"Analise notícia de futebol:\n{req.content}\n\nData Hoje: {datetime.date.today()}"
    
    resp = await call_ollama(prompt, system)
    if not resp: resp = await call_gemini(prompt, system)
    if not resp: resp = await call_claude(prompt, system)

    if not resp:
        return {"relevant": False, "category": "unknown", "priority": "low", "reasoning": "AI unavailable"}

    data = extract_json(resp)
    return {
        "relevant": data.get("relevant", False),
        "category": data.get("category", "geral"),
        "priority": data.get("priority", "low"),
        "reasoning": data.get("reasoning", "Parsed from AI")
    }

@router.post("/decide", response_model=DecideResponse)
async def decide_format(req: AIRequest):
    """Decide o formato do vídeo (Short/Long) e estratégias."""
    system = (
        "Você é um estrategista de conteúdo digital (YouTube/TikTok). "
        "Decida o melhor formato. JSON: "
        '{"decision": "video"|"discard", "format": "short"|"long", "aggregation": "solo"|"giro", "region": "brasil"|"europa"|"mundo", "reasoning": "..."}. '
        "Regras: Vídeos virais/rápidos/curiosidades -> 'short'. Análises táticas/histórias profundas -> 'long'."
    )
    prompt = f"Conteúdo: {req.content}\nDecida a estratégia."

    resp = await call_ollama(prompt, system)
    if not resp: resp = await call_gemini(prompt, system)
    if not resp: resp = await call_claude(prompt, system)

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
    """Gera roteiro estruturado + hook + CTA."""
    system = (
        "Você é um roteirista de vídeos virais (TikTok/Shorts). "
        "Estruture o roteiro. JSON Obrigatório: "
        '{"title": "Texto com Hook", "blocks": [{"text": "fala", "type": "speech"}], '
        '"thumbnail_text": "Texto Capa", "image_prompt": "Prompt Imagem", '
        '"hook": "Frase inicial <3s", "cta": "Chamada para ação"}. '
        "IMPORTANTE: O roteiro DEVE ter no mínimo 80-100 palavras para garantir 30-45s de vídeo. "
        "Divida em 3 blocos: "
        "1. Hook (Reação/Curiosidade) - 5s. "
        "2. Desenvolvimento (Contexto + Resposta da Manchete) - 20-30s. "
        "3. Conclusão (CTA + Gancho final) - 5-10s. "
        "NÃO termine o vídeo sem entregar a informação prometida no Hook."
    )
    prompt = f"Gere roteiro sobre: {req.content}"

    resp = await call_ollama(prompt, system)
    if not resp: resp = await call_gemini(prompt, system)
    if not resp: resp = await call_claude(prompt, system)

    if not resp:
        raise ServicoExterno("Falha ao gerar roteiro.", url="/ai/script")

    data = extract_json(resp)
    if not data:
         # Fallback simples
         return {
             "title": "Notícia do Futebol",
             "blocks": [{"text": resp, "type": "speech"}],
             "thumbnail_text": "VEJA ISSO",
             "image_prompt": "Estádio de futebol lotado",
             "hook": "Você não vai acreditar nisso!",
             "cta": "Siga para mais.",
             "metadata": {"raw": resp[:50]}
         }

    return {
        "title": data.get("title", "Título Viral"),
        "blocks": data.get("blocks", []),
        "thumbnail_text": data.get("thumbnail_text", "Urgente"),
        "image_prompt": data.get("image_prompt", "Imagem de futebol"),
        "hook": data.get("hook", "Olha isso!"),
        "cta": data.get("cta", "Comenta aí!"),
        "search_terms": data.get("search_terms", ["soccer match", "football stadium"]),
        "mood": data.get("mood", "Rock"),
        "metadata": {"provider": "ai-service"}
    }

@router.post("/metadata", response_model=MetadataResponse)
async def generate_metadata(req: AIRequest):
    """Gera Título, Descrição, Tags e Trending Sound para YouTube/TikTok."""
    
    # 1. Buscar Trends (externo)
    trends = await get_trending_topics(req.content[:50])
    trends_str = ", ".join(trends)

    system = (
        "Você é um estrategista de conteúdo viral para TikTok e YouTube Shorts. "
        "JSON Obrigatório: "
        '{"title": "Título com GANCHO DE 3s (use CAPS, Emojis, Números, Perguntas)", '
        '"description": "Comece com Hook de curiosidade. Inclua CTA \'Siga para mais\'. Use 8-10 hashtags fortes.", '
        '"tags": ["#PremierLeague", "#Futebol", "#Viral", "#Transferencias", "#Shorts"], "trending_sound": "Nome de som em alta"}. '
        "REGRAS DE OURO PARA O TÍTULO: "
        "1. Use Palavras de Poder mas mantenha LINGUAGEM NATURAL (como um fã falaria). "
        "2. Evite traduções literais (ex: 'Leva para casa' -> 'Venceu/Conquistou'). "
        "3. Se for notícia de jogo, coloque o placar ou o fato principal. "
        "4. Crie curiosidade sem mentir (entregue o valor). "
        f"CONTEXTO: {trends_str}"
    )
    prompt = f"Gere metadata IMPOSSÍVEL DE IGNORAR para: {req.content}"

    resp = await call_ollama(prompt, system)
    if not resp: resp = await call_gemini(prompt, system)
    if not resp: resp = await call_claude(prompt, system)

    if not resp:
        return {
            "title": "Vídeo de Futebol",
            "description": "Confira as notícias.",
            "tags": ["futebol", "shorts", "viral"],
            "trending_sound": "Original Sound"
        }

    data = extract_json(resp)
    return {
        "title": data.get("title", "Título Incrível"),
        "description": data.get("description", "Descrição do vídeo."),
        "tags": data.get("tags", ["futebol", "brasil"]),
        "trending_sound": data.get("trending_sound", "Som Viral")
    }
