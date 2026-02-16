# =============================================================================
# app/main.py — Aplicação FastAPI principal
# =============================================================================
# Registra todos os routers, health check e documentação.
# =============================================================================

import sys
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.utils.errors import registrar_handlers
from app.routes import extract, audio, video, download, image, ai, jobs, publish, enrichment, media, feedback
from app.utils.database import init_db


# ---------------------------------------------------------------------------
# Inicialização do app
# ---------------------------------------------------------------------------
app = FastAPI(
    title="Python Service — Pipeline de Vídeos",
    description=(
        "Microserviço Python que substitui os nós Python internos do n8n. "
        "Chamado pelo n8n via HTTP Request node. "
        "Endpoints: extração de texto, geração de áudio, montagem de vídeo, download e publicação."
    ),
    version="1.0.0",
    docs_url="/docs",           # Swagger UI (acessível em http://localhost:8000/docs)
    redoc_url="/redoc"          # ReDoc (alternativa mais bonita)
)

# ---------------------------------------------------------------------------
# Middleware
# ---------------------------------------------------------------------------
# CORS: permite chamadas da rede interna Docker sem problemas
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # na rede interna Docker isso é seguro
    allow_methods=["*"],
    allow_headers=["*"]
)

# ---------------------------------------------------------------------------
# Handlers de erro centralizados
# ---------------------------------------------------------------------------
registrar_handlers(app)

# ---------------------------------------------------------------------------
# Routers
# ---------------------------------------------------------------------------
app.include_router(extract.router)
app.include_router(audio.router)
app.include_router(video.router)
app.include_router(download.router)
app.include_router(image.router)
app.include_router(ai.router)
app.include_router(jobs.router)
app.include_router(publish.router)
app.include_router(enrichment.router)
app.include_router(media.router)
app.include_router(feedback.router) # Novo: Loop de SEO



@app.on_event("startup")
async def startup_event():
    init_db()
    try:
        from app.utils.assets import download_assets_background
        import asyncio
        asyncio.create_task(download_assets_background())
    except Exception as e:
        print(f"Erro ao iniciar download de assets: {e}")

# ---------------------------------------------------------------------------
# Health Check — usado pelo Docker e pelo n8n para verificar se está vivo
# ---------------------------------------------------------------------------

@app.get("/health", tags=["sistema"])
async def health():
    """
    Health check básico.
    Usado pelo Docker (HEALTHCHECK) e pelo n8n antes de chamar outros endpoints.
    Sempre retorna 200 se o serviço estiver rodando.
    """
    return {"status": "ok", "timestamp": datetime.now().isoformat()}


# ---------------------------------------------------------------------------
# Info — retorna versões das dependências (útil para debug)
# ---------------------------------------------------------------------------

@app.get("/info", tags=["sistema"])
async def info():
    """
    Retorna informações do ambiente e versões das bibliotecas.
    Útil para validar se tudo foi instalado corretamente no container.
    """
    info_pacotes = {}

    # Lista de pacotes para verificar
    pacotes = ["trafilatura", "fastapi", "moviepy", "edge_tts", "yt_dlp", "PIL", "numpy"]

    for nome in pacotes:
        try:
            modulo = __import__(nome)
            info_pacotes[nome] = getattr(modulo, "__version__", "versão desconhecida")
        except ImportError:
            info_pacotes[nome] = "NÃO INSTALADO"

    return {
        "python_versao": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        "pacotes": info_pacotes,
        "timestamp": datetime.now().isoformat()
    }
