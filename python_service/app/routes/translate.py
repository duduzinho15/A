import logging
from typing import Optional
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.config import settings
from app.routes.ai import call_ollama, call_groq, call_gemini, call_claude

router = APIRouter(prefix="/ai", tags=["ai"])
logger = logging.getLogger("translate_route")

class TranslateRequest(BaseModel):
    text: str
    target_lang: str = "Portuguese (Brazil)"
    context: str = "Futebol / Esportes"

class TranslateResponse(BaseModel):
    status: str
    translated_text: str
    provider_used: str

async def call_translation_ai(text: str, target_lang: str, context: str) -> Optional[tuple[str, str]]:
    """Cadeia de fallback para tradução especializada."""
    system = (
        f"Você é um tradutor especializado em {context}. "
        f"Traduza o texto para {target_lang}. "
        "Mantenha gírias de futebol, nomes de jogadores, estádios e termos técnicos intactos. "
        "O tom deve ser natural para um narrador brasileiro. "
        "Retorne APENAS a tradução, sem comentários."
    )
    prompt = f"Traduza o seguinte conteúdo:\n\n{text}"

    # 1. Ollama (Local)
    resp = await call_ollama(prompt, system)
    if resp: return resp, "ollama"

    # 2. Groq (Fast Fallback)
    resp = await call_groq(prompt, system)
    if resp: return resp, "groq"

    # 3. Gemini
    resp = await call_gemini(prompt, system)
    if resp: return resp, "gemini"

    # 4. Claude
    resp = await call_claude(prompt, system)
    if resp: return resp, "claude"

    return None

@router.post("/translate", response_model=TranslateResponse)
async def translate_content(req: TranslateRequest):
    """Endpoint para tradução de transcrições e notícias estrangeiras."""
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Texto vazio")

    result = await call_translation_ai(req.text, req.target_lang, req.context)
    if result:
        translated, provider = result
        return TranslateResponse(
            status="sucesso",
            translated_text=translated,
            provider_used=provider
        )

    raise HTTPException(status_code=500, detail="Falha em todos os provedores de tradução")
