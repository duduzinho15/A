# =============================================================================
# app/routes/image.py — Endpoint de Geração de Imagens e Thumbnails (Fase 2.5)
# =============================================================================
import os
import uuid
import httpx
import asyncio
import base64
from typing import Optional, List
from fastapi import APIRouter
from pydantic import BaseModel
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from app.config import settings
from app.utils.errors import ServicoExterno
# Import Stability SDK se necessário, mas HTTP requests costumam ser mais leves.
# Vamos usar requests simples para APIs REST para reduzir dependências pesadas runtime,
# exceto se stability-sdk for estritamente necessário. O user pediu SDK.
try:
    from stability_sdk import client as stability_client
    import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
except ImportError:
    stability_client = None

router = APIRouter(prefix="/image", tags=["imagem"])

# Diretórios
OUTPUT_DIR = os.path.join(settings.DATA_MIDIA, "imagens")
THUMB_DIR = os.path.join(settings.DATA_MIDIA, "thumbnails")
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(THUMB_DIR, exist_ok=True)

class ImageRequest(BaseModel):
    prompt: str
    style: str = "realista" # realista, ilustrado, thumbnail, vibrante
    aspect_ratio: str = "16:9"
    width: Optional[int] = None
    height: Optional[int] = None
    steps: int = 20
    sampler: str = "Euler a"

class ImageOptionsRequest(BaseModel):
    sd_model_checkpoint: str

class ImageModel(BaseModel):
    title: str
    model_name: str
    hash: Optional[str]

class ThumbnailRequest(BaseModel):
    title: str
    subtitle: Optional[str] = None
    image_prompt: Optional[str] = None
    background_path: Optional[str] = None

class ImageResponse(BaseModel):
    status: str
    image_path: str
    provider_used: str

# ---------------------------------------------------------------------------
# HELPERS
# ---------------------------------------------------------------------------

async def download_image(url: str) -> Optional[str]:
    """Baixa imagem de URL e salva localmente."""
    try:
        async with httpx.AsyncClient(timeout=20.0) as client:
            resp = await client.get(url)
            if resp.status_code == 200:
                filename = f"stock_{uuid.uuid4().hex}.jpg"
                filepath = os.path.join(OUTPUT_DIR, filename)
                with open(filepath, "wb") as f:
                    f.write(resp.content)
                return filepath
    except Exception as e:
        print(f"[Image] Erro download: {e}")
    return None

# ---------------------------------------------------------------------------
# PROVEDORES DE IMAGEM
# ---------------------------------------------------------------------------

async def gen_sd_api(prompt: str) -> Optional[str]:
    """2. Stable Diffusion External API (Stability / DeepAI)"""
    # Tenta Stability AI SDK
    if settings.STABILITY_API_KEY and stability_client:
        try:
            # Placeholder simplificado SDK
            # Na prática, requer setup GRPC. Vou usar requests REST endpoint da Stability
            # se o SDK falhar ou para simplificar.
            # Mas vamos seguir o pedido do user: Stability SDK.
            stability_api = stability_client.StabilityInference(
                key=settings.STABILITY_API_KEY,
                verbose=True,
                engine="stable-diffusion-xl-1024-v1-0",
            )
            answers = stability_api.generate(
                prompt=prompt,
                steps=30,
                width=1024 if "16:9" else 512, # Adaptação simples
                height=576 if "16:9" else 512,
            )
            for resp in answers:
                for artifact in resp.artifacts:
                    if artifact.finish_reason == generation.FILTER:
                        print("[Image] Stability Filtered")
                        return None
                    if artifact.type == generation.ARTIFACT_IMAGE:
                        img = Image.open(BytesIO(artifact.binary))
                        filename = f"stability_{uuid.uuid4().hex}.png"
                        filepath = os.path.join(OUTPUT_DIR, filename)
                        img.save(filepath)
                        return filepath
        except Exception as e:
            print(f"[Image] Stability Error: {e}")
    
    # Fallback DeepAI
    if settings.DEEPAI_API_KEY:
        try:
            async with httpx.AsyncClient() as client:
                r = await client.post(
                    "https://api.deepai.org/api/text2img",
                    data={'text': prompt},
                    headers={'api-key': settings.DEEPAI_API_KEY},
                    timeout=30.0
                )
                if r.status_code == 200:
                    url = r.json().get('output_url')
                    return await download_image(url)
        except Exception as e:
             print(f"[Image] DeepAI Error: {e}")
             
    return None

async def gen_sd_local(prompt: str, width: int = 1024, height: int = 576, steps: int = 20, sampler: str = "Euler a") -> Optional[str]:
    """3. Stable Diffusion Local (A1111) — Tenta múltiplos endpoints"""
    
    # Lista de possíveis URLs (Docker service name ou Host local)
    possible_urls = [
        "http://a1111:7861/sdapi/v1/txt2img",
        "http://host.docker.internal:7861/sdapi/v1/txt2img",
        "http://host.docker.internal:7860/sdapi/v1/txt2img"
    ]
    
    payload = {
        "prompt": prompt,
        "steps": steps,
        "width": width,
        "height": height, 
        "sampler_name": sampler
    }
    
    async with httpx.AsyncClient(timeout=90.0) as client:
        for url in possible_urls:
            try:
                print(f"[Image] Tentando SD Local em: {url}")
                resp = await client.post(url, json=payload)
                if resp.status_code == 200:
                    data = resp.json()
                    if "images" in data and data["images"]:
                        img_b64 = data["images"][0]
                        img = Image.open(BytesIO(base64.b64decode(img_b64)))
                        filename = f"local_sd_{uuid.uuid4().hex}.png"
                        filepath = os.path.join(OUTPUT_DIR, filename)
                        img.save(filepath)
                        return filepath
                    else:
                        print(f"[Image] A1111 retornou sem imagens: {data}")
                else:
                    print(f"[Image] A1111 Error ({url}): {resp.status_code}")
            except Exception as e:
                print(f"[Image] Falha ao conectar em {url}: {e}")
                
    return None

async def gen_stock_fallback(prompt: str) -> Optional[str]:
    """4. Stock (Pexels / Pixabay)"""
    # Pexels
    if settings.PEXELS_API_KEY:
        try:
            headers = {"Authorization": settings.PEXELS_API_KEY}
            async with httpx.AsyncClient() as client:
                r = await client.get(
                    f"https://api.pexels.com/v1/search?query={prompt}&per_page=1",
                    headers=headers
                )
                if r.status_code == 200:
                    data = r.json()
                    if data.get("photos"):
                        url = data["photos"][0]["src"]["landscape"]
                        return await download_image(url)
        except Exception as e:
            print(f"[Image] Pexels Error: {e}")

    # Pixabay
    if settings.PIXABAY_API_KEY:
         try:
            async with httpx.AsyncClient() as client:
                r = await client.get(
                    f"https://pixabay.com/api/?key={settings.PIXABAY_API_KEY}&q={prompt}&image_type=photo"
                )
                if r.status_code == 200:
                    data = r.json()
                    if data.get("hits"):
                        url = data["hits"][0]["largeImageURL"]
                        return await download_image(url)
         except Exception as e:
            print(f"[Image] Pixabay Error: {e}")
            
    # Unsplash
    if settings.UNSPLASH_ACCESS_KEY:
        try:
            async with httpx.AsyncClient() as client:
                r = await client.get(
                    f"https://api.unsplash.com/search/photos?query={prompt}&per_page=1&client_id={settings.UNSPLASH_ACCESS_KEY}"
                )
                if r.status_code == 200:
                    data = r.json()
                    if data.get("results"):
                        url = data["results"][0]["urls"]["regular"]
                        return await download_image(url)
        except Exception as e:
            print(f"[Image] Unsplash Error: {e}")

    return None

# ---------------------------------------------------------------------------
# ENDPOINTS
# ---------------------------------------------------------------------------

@router.post("/generate", response_model=ImageResponse)
async def gerar_imagem(req: ImageRequest):
    """
    Gera imagem seguindo hierarquia e ensemble.
    Suporta SDXL via A1111 (Local) ou APIs externas.
    """
    
    # Determina resolução
    width = req.width
    height = req.height
    
    if not width or not height:
        if req.aspect_ratio == "16:9":
            width, height = 1024, 576 # SDXL Default
        elif req.aspect_ratio == "9:16":
             width, height = 576, 1024
        else:
             width, height = 1024, 1024 # 1:1

    pipeline = [
        # ("sd_api", lambda: gen_sd_api(req.prompt)), 
        ("sd_local", lambda: gen_sd_local(req.prompt, width=width, height=height, steps=req.steps, sampler=req.sampler)),
        ("stock", lambda: gen_stock_fallback(req.prompt)),
        ("sd_api", lambda: gen_sd_api(req.prompt)) 
    ]
    
    ordered_pipeline = [
        ("sd_api", lambda: gen_sd_api(req.prompt)), # Tenta API primeiro se configurada (User pref) ou mude ordem
        ("sd_local", lambda: gen_sd_local(req.prompt, width=width, height=height, steps=req.steps, sampler=req.sampler)),
        ("stock", lambda: gen_stock_fallback(req.prompt))
    ]

    for name, func in ordered_pipeline:
        try:
            path = await func()
            if path and os.path.exists(path):
                return {"status": "sucesso", "image_path": path, "provider_used": name}
        except Exception as e:
            print(f"Erro no provedor {name}: {e}")
            continue

    raise ServicoExterno("Todos os provedores de imagem falharam.", url="/image/generate")

@router.post("/thumbnail", response_model=ImageResponse)
async def gerar_thumbnail(req: ThumbnailRequest):
    """Composição de thumbnail estilo 'Shorts' (Texto Impactante)."""
    try:
        filename = f"thumb_{uuid.uuid4().hex}.jpg"
        filepath = os.path.join(THUMB_DIR, filename)

        # 1. Base
        img = None
        if req.background_path and os.path.exists(req.background_path):
            img = Image.open(req.background_path).convert("RGB")
        elif req.image_prompt:
            # Tenta gerar na hora
            path = await gen_sd_api(req.image_prompt) or await gen_sd_local(req.image_prompt) or await gen_stock_fallback(req.image_prompt)
            if path:
                img = Image.open(path).convert("RGB")
        
        if not img:
             img = Image.new('RGB', (1080, 1920), color=(20, 20, 20)) # Vertical 9:16 default para Shorts? 
             # Mas o endpoint anterior era 1280x720 (16:9). Se for shorts, devia ser 9:16.
             # Vou assumir 16:9 padrão do user, mas user pediu "SEO Shorts".
             # Vamos manter 16:9 seguro, ou checar aspect ratio.
             # Assumindo 16:9 (youtube standard thumb).
             img = Image.new('RGB', (1280, 720), color=(10, 10, 15))

        img = img.resize((1280, 720), Image.Resampling.LANCZOS)
        draw = ImageDraw.Draw(img)
        
        # 2. Overlay "Vignette" ou contraste
        overlay = Image.new('RGBA', (1280, 720), (0,0,0,0))
        d_ov = ImageDraw.Draw(overlay)
        # Sombra em baixo para texto
        d_ov.rectangle([0, 450, 1280, 720], fill=(0, 0, 0, 180))
        img.paste(overlay, (0,0), overlay)

        # 3. Fonte
        try:
            # Tenta achar fonte bold
            font_size = 90
            font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
        except:
            font = ImageFont.load_default()

        # 4. Texto (Centralizado ou Base)
        # Cor amarela/branca vibrante
        text = req.title.upper()
        # Calculo posição (mock simples)
        text_x = 60
        text_y = 500
        
        # Stroke (Borda preta no texto)
        stroke_width = 4
        draw.text((text_x, text_y), text, font=font, fill=(255, 255, 0), stroke_width=stroke_width, stroke_fill=(0,0,0))
        
        if req.subtitle:
            try:
                font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 50)
            except:
                font_sub = ImageFont.load_default()
            draw.text((text_x, text_y + 100), req.subtitle, font=font_sub, fill=(255, 255, 255), stroke_width=3, stroke_fill=(0,0,0))

        img.save(filepath, "JPEG", quality=90)
        return {
            "status": "sucesso",
            "image_path": filepath,
            "provider_used": "pillow_seo_composite"
        }

    except Exception as e:
        raise ServicoExterno(f"Erro thumbnail: {str(e)}", url="/image/thumbnail")

# ---------------------------------------------------------------------------
# GERENCIAMENTO DE MODELOS (A1111)
# ---------------------------------------------------------------------------

@router.get("/models", response_model=List[ImageModel])
async def list_models():
    """Lista modelos disponíveis no A1111 Local."""
    urls = [
        "http://a1111:7861/sdapi/v1/sd-models",
        "http://host.docker.internal:7861/sdapi/v1/sd-models",
         "http://host.docker.internal:7860/sdapi/v1/sd-models"
    ]
    async with httpx.AsyncClient(timeout=10.0) as client:
        for url in urls:
            try:
                resp = await client.get(url)
                if resp.status_code == 200:
                    return resp.json()
            except:
                continue
    return []

@router.post("/options")
async def set_options(opts: ImageOptionsRequest):
    """Muda opções do A1111 (ex: Trocar Model Checkpoint)."""
    urls = [
        "http://a1111:7861/sdapi/v1/options",
        "http://host.docker.internal:7861/sdapi/v1/options",
        "http://host.docker.internal:7860/sdapi/v1/options"
    ]
    payload = {"sd_model_checkpoint": opts.sd_model_checkpoint}
    
    async with httpx.AsyncClient(timeout=30.0) as client:
        for url in urls:
            try:
                resp = await client.post(url, json=payload)
                if resp.status_code == 200:
                    return {"status": "ok", "message": f"Model switched to {opts.sd_model_checkpoint}"}
            except:
                continue
    
    return {"status": "error", "message": "Failed to connect to A1111"}
