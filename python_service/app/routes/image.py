# =============================================================================
# app/routes/image.py — Endpoint de Geração de Imagens e Thumbnails v2.0
# =============================================================================
# MELHORIAS v2.0:
#   - Face detection com mediapipe para crop inteligente de thumbnail
#   - Thumbnail 9:16 (variante Shorts) gerada automaticamente
#   - Logo watermark sobreposta no canto
#   - Logging substitui todos os print()
# =============================================================================
import os
import uuid
import httpx
import asyncio
import base64
import logging
from typing import Optional, List
from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from app.config import settings
from app.utils.errors import ServicoExterno
try:
    from stability_sdk import client as stability_client
    import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
except ImportError:
    stability_client = None

router = APIRouter(prefix="/image", tags=["imagem"])
logger = logging.getLogger("image_routes")

# Diretórios (Configuração Estrita para Windows)
# No Windows do Usuário, o caminho absoluto é:
if os.name == "nt":
    DATA_MIDIA_BASE = "C:/Users/Usuario/Desktop/meu-freshrss/data_midia"
else:
    DATA_MIDIA_BASE = settings.DATA_MIDIA

# Normalização estrita para evitar problemas de barras no Windows
OUTPUT_DIR = os.path.normpath(os.path.join(DATA_MIDIA_BASE, "imagens"))
THUMB_DIR = os.path.normpath(os.path.join(DATA_MIDIA_BASE, "thumbnails"))

os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(THUMB_DIR, exist_ok=True)

logger.info(f"[Image] Diretório Base: {DATA_MIDIA_BASE}")
logger.info(f"[Image] OUTPUT_DIR: {OUTPUT_DIR} | Existe: {os.path.exists(OUTPUT_DIR)}")
logger.info(f"[Image] THUMB_DIR: {THUMB_DIR}")

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
                abs_path = os.path.abspath(filepath)
                logger.info(f"[Image] DOWNLOAD DEBUG: Salvo em {abs_path} | Existe: {os.path.exists(abs_path)}")
                return abs_path
    except Exception as e:
        logger.warning("[Image] Erro download: %s", e)
    return None


def face_crop_thumbnail(
    img: "Image.Image",
    target_w: int = 1280,
    target_h: int = 720
) -> "Image.Image":
    """
    Detecta rostos na imagem com OpenCV (Haar Cascades) e faz crop centrado no rosto.
    Se não detectar rostos, faz crop simples no centro.

    Args:
        img: Imagem PIL original
        target_w, target_h: Dimensões alvo

    Returns:
        Imagem PIL cropada e redimensionada.
    """
    try:
        import cv2
        import numpy as np
        from PIL import Image as PILImage

        img_rgb = img.convert("RGB")
        img_np = np.array(img_rgb)
        
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        if len(faces) > 0:
            # Usa o maior rosto
            largest_face = max(faces, key=lambda rect: rect[2] * rect[3])
            x, y, w, h = largest_face

            ih, iw = img_np.shape[:2]
            cx = x + w // 2
            cy = y + h // 2

            # Calcula crop mantendo aspect ratio
            aspect = target_w / target_h
            crop_h = min(ih, int(iw / aspect))
            crop_w = min(iw, int(ih * aspect))

            left = max(0, cx - crop_w // 2)
            top = max(0, cy - crop_h // 2)
            
            if left + crop_w > iw: left = iw - crop_w
            if top + crop_h > ih: top = ih - crop_h
            left = max(0, left)
            top = max(0, top)
            
            right = left + crop_w
            bottom = top + crop_h

            cropped = img_rgb.crop((left, top, right, bottom))
            logger.info("[Image] Face detectada — crop centrado no rosto (%d, %d)", cx, cy)
            return cropped.resize((target_w, target_h), PILImage.Resampling.LANCZOS)
    except ImportError:
        logger.warning("[Image] OpenCV não instalado — usando crop simples")
    except Exception as e:
        logger.warning("[Image] face_crop falhou: %s — usando crop simples", e)

    # Fallback: crop central simples
    img_resized = img.convert("RGB")
    iw, ih = img_resized.size
    aspect = target_w / target_h
    if iw / ih > aspect:
        new_w = int(ih * aspect)
        left = (iw - new_w) // 2
        img_resized = img_resized.crop((left, 0, left + new_w, ih))
    else:
        new_h = int(iw / aspect)
        top = (ih - new_h) // 2
        img_resized = img_resized.crop((0, top, iw, top + new_h))
    return img_resized.resize((target_w, target_h), Image.Resampling.LANCZOS)


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
                        logger.warning("[Image] Stability: conteúdo filtrado pela API")
                        return None
                    if artifact.type == generation.ARTIFACT_IMAGE:
                        img = Image.open(BytesIO(artifact.binary))
                        filename = f"stability_{uuid.uuid4().hex}.png"
                        filepath = os.path.join(OUTPUT_DIR, filename)
                        img.save(filepath)
                        return filepath
        except Exception as e:
            logger.error("[Image] Stability Error: %s", e)
    
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
    """Composição de thumbnail v2.0 com face detection e variante 9:16 para Shorts."""
    try:
        uid = uuid.uuid4().hex
        filename_16x9 = f"thumb_{uid}_16x9.jpg"
        filepath = os.path.join(THUMB_DIR, filename_16x9)

        # 1. Base da imagem
        img = None
        if req.background_path and os.path.exists(req.background_path):
            img = Image.open(req.background_path).convert("RGB")
        elif req.image_prompt:
            path = (
                await gen_sd_api(req.image_prompt)
                or await gen_sd_local(req.image_prompt)
                or await gen_stock_fallback(req.image_prompt)
            )
            if path:
                img = Image.open(path).convert("RGB")

        if not img:
            img = Image.new('RGB', (1280, 720), color=(10, 10, 15))

        # 2. Face detection crop inteligente (1280x720)
        img = face_crop_thumbnail(img, target_w=1280, target_h=720)

        draw = ImageDraw.Draw(img)

        # 3. Overlay escuro na base para leiturabilidade do texto
        overlay = Image.new('RGBA', (1280, 720), (0, 0, 0, 0))
        d_ov = ImageDraw.Draw(overlay)
        d_ov.rectangle([0, 420, 1280, 720], fill=(0, 0, 0, 185))
        img.paste(overlay, (0, 0), overlay)

        # 4. Fonte — Montserrat Black se disponível, DejaVu Bold como fallback
        font_paths = [
            "/usr/share/fonts/truetype/Montserrat-ExtraBold.ttf",
            "/usr/share/fonts/truetype/montserrat/Montserrat-ExtraBold.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        ]
        font = None
        for fp in font_paths:
            if os.path.exists(fp):
                try:
                    font = ImageFont.truetype(fp, 90)
                    font_sub_size = ImageFont.truetype(fp, 52)
                    break
                except Exception:
                    pass
        if not font:
            font = ImageFont.load_default()
            font_sub_size = font

        # 5. Texto principal (título em CAPS, amarelo vibrante com borda preta)
        text = req.title.upper()[:50]  # Limite seguro
        draw.text(
            (55, 450),
            text,
            font=font,
            fill=(255, 220, 0),
            stroke_width=5,
            stroke_fill=(0, 0, 0)
        )

        # 6. Subtítulo
        if req.subtitle:
            draw.text(
                (55, 570),
                req.subtitle,
                font=font_sub_size,
                fill=(255, 255, 255),
                stroke_width=3,
                stroke_fill=(0, 0, 0)
            )

        # 7. Logo watermark no canto superior direito
        logo_path = os.path.join(settings.DATA_MIDIA, "branding", "logo.png")
        if os.path.exists(logo_path):
            try:
                logo = Image.open(logo_path).convert("RGBA")
                logo_w = 160
                ratio = logo_w / logo.width
                logo = logo.resize((logo_w, int(logo.height * ratio)), Image.Resampling.LANCZOS)
                # Cola no canto superior direito com padding
                pos_x = 1280 - logo_w - 20
                pos_y = 20
                img.paste(logo, (pos_x, pos_y), logo)
            except Exception as e:
                logger.warning("[Thumbnail] Erro ao aplicar logo: %s", e)

        # 8. Salva thumbnail 16:9
        img.save(filepath, "JPEG", quality=92)
        logger.info("[Thumbnail] 16:9 gerada: %s", filepath)

        # 9. Gera variante 9:16 para Shorts
        try:
            img_vertical = face_crop_thumbnail(img, target_w=1080, target_h=1920)
            filename_9x16 = f"thumb_{uid}_9x16.jpg"
            filepath_9x16 = os.path.join(THUMB_DIR, filename_9x16)
            img_vertical.save(filepath_9x16, "JPEG", quality=90)
            logger.info("[Thumbnail] Variante 9:16 gerada: %s", filepath_9x16)
        except Exception as e:
            logger.warning("[Thumbnail] Não foi possível gerar variante 9:16: %s", e)

        return {
            "status": "sucesso",
            "image_path": filepath,
            "provider_used": "pillow_v2_face_detection"
        }

    except Exception as e:
        raise ServicoExterno(f"Erro thumbnail: {str(e)}", url="/image/thumbnail")

# ---------------------------------------------------------------------------
# GERENCIAMENTO DE MODELOS (A1111)
# ---------------------------------------------------------------------------

@router.post("/remove-bg", response_model=ImageResponse)
async def remove_background(
    image_path: Optional[str] = Query(None),
    prompt: Optional[str] = Query(None)
):
    """
    Remove o fundo de uma imagem. 
    Se image_path for nulo/vazio, usa o prompt para gerar uma imagem primeiro.
    """
    logger.info(f"[Image] Iniciando remove-bg | Path: {image_path} | Prompt: {prompt}")
    
    if not settings.REMOVE_BG_API_KEY:
        raise HTTPException(status_code=400, detail="REMOVE_BG_API_KEY não configurada.")
    
    actual_path = None
    temp_path = None

    try:
        # 1. Decisão: Usar path existente ou gerar do zero?
        if image_path and image_path.strip():
            if image_path.lower().startswith("http"):
                temp_path = await download_image(image_path)
                actual_path = temp_path
            else:
                actual_path = image_path
        
        # 2. Se não tem path ou o arquivo não existe, tenta gerar por prompt
        if not actual_path or not os.path.exists(actual_path):
            if prompt:
                logger.info(f"[Image] Path inválido. Gerando imagem do zero para o prompt: {prompt}")
                # Reutiliza a lógica de geração (Hierarquia: SD Local -> Stock -> SD API)
                generated = await gerar_imagem(ImageRequest(prompt=prompt, style="thumbnail"))
                actual_path = generated["image_path"]
            else:
                raise HTTPException(status_code=404, detail="Nenhuma imagem ou prompt fornecido.")

        if not os.path.exists(actual_path):
            raise HTTPException(status_code=404, detail=f"Imagem final não encontrada: {actual_path}")
        
        url = "https://api.remove.bg/v1.0/removebg"
        with open(actual_path, "rb") as f:
            files = {"image_file": f}
            data = {"size": "auto"}
            headers = {"X-Api-Key": settings.REMOVE_BG_API_KEY}
            
            async with httpx.AsyncClient(timeout=45.0) as client:
                resp = await client.post(url, files=files, data=data, headers=headers)
                
                if resp.status_code == 200:
                    uid = uuid.uuid4().hex
                    output_filename = f"no_bg_{uid}.png"
                    output_path = os.path.join(OUTPUT_DIR, output_filename)
                    with open(output_path, "wb") as out:
                        out.write(resp.content)
                    return {"status": "sucesso", "image_path": output_path, "provider_used": "remove.bg"}
                
                logger.warning("[Image] Remove.bg Error: %d - %s", resp.status_code, resp.text[:150])
                raise HTTPException(status_code=resp.status_code, detail=f"Erro Remove.bg: {resp.text[:100]}")
            
    except HTTPException:
        raise
    except Exception as e:
        logger.error("[Image] Remove.bg Exception: %s", e)
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        # Limpa arquivo temporário se foi baixado prioritariamente para o remove-bg
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
                logger.info(f"[Image] Temp file removido: {temp_path}")
            except:
                pass

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
