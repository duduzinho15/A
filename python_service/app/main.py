import sys
from datetime import datetime
import logging
import os

LOG_FILE = "agent.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.utils.errors import registrar_handlers
from app.utils.database import init_db
from app.routes import (
    jobs, publish, maintenance, datasets, enrichment, media, feedback, leads, dashboard, translate, comments,
    extract, audio, video, download, image, ai, analytics, openhands
)
from app.services.ai_agent import router as agent_router

app = FastAPI(
    title="Python Service — Pipeline de Vídeos",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

registrar_handlers(app)

app.include_router(extract.router)
app.include_router(audio.router)
app.include_router(video.router)
app.include_router(download.router)
app.include_router(image.router)
app.include_router(ai.router)
app.include_router(jobs.router)
app.include_router(maintenance.router)
app.include_router(datasets.router)
app.include_router(enrichment.router)
app.include_router(media.router)
app.include_router(feedback.router)
app.include_router(leads.router)
app.include_router(dashboard.router)
app.include_router(translate.router)
app.include_router(comments.router)
app.include_router(analytics.router)
app.include_router(openhands.router)
app.include_router(agent_router)

# Serve Dashboard static files
dashboard_path = "/dashboard-dist"
if os.path.exists(dashboard_path):
    app.mount("/dashboard", StaticFiles(directory=dashboard_path, html=True), name="dashboard")
else:
    # Fallback to local path for development outside docker
    local_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static", "dashboard"))
    if os.path.exists(local_path):
        app.mount("/dashboard", StaticFiles(directory=local_path, html=True), name="dashboard")
    else:
        print(f"Warning: Dashboard static path not found at {dashboard_path} or {local_path}")

@app.on_event("startup")
async def startup_event():
    init_db()
    try:
        from app.utils.assets import download_assets_background
        import asyncio
        asyncio.create_task(download_assets_background())
    except Exception as e:
        print(f"Startup error (assets): {e}")

    # --- Autonomous Agent (Fase 2) ---
    try:
        from app.services.ai_agent import start_agent
        import asyncio
        asyncio.create_task(start_agent())
    except Exception as e:
        print(f"Startup error (agent): {e} — server continues without agent")

@app.get("/health", tags=["sistema"])
async def health():
    return {"status": "ok", "timestamp": datetime.now().isoformat()}

@app.get("/info", tags=["sistema"])
async def info():
    return {
        "python_versao": f"{sys.version_info.major}.{sys.version_info.minor}",
        "timestamp": datetime.now().isoformat()
    }
