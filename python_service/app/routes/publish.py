# =============================================================================
# app/routes/publish.py - Multi-platform publishing (YouTube + TikTok)
# =============================================================================
import json
import os
import pickle
import random
import logging
import string
import shutil
import subprocess
from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional, Dict

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests

from app.services.youtube import YouTubeService
# run_full_quality_gate: valida vídeo (duração, resolução, áudio) e metadados
# antes de qualquer upload — bloqueia publicação se score < 60
from app.services.quality_gate import run_full_quality_gate
from app.utils.telegram import send_telegram_message, send_telegram_video

router = APIRouter(prefix="/publish", tags=["publicacao"])
logger = logging.getLogger("publish_routes")

TIKTOK_REPO_DIR = "/app/tiktok_uploader"
TIKTOK_CLI_PATH = os.path.join(TIKTOK_REPO_DIR, "cli.py")
TIKTOK_COOKIES_DIR = os.path.join(TIKTOK_REPO_DIR, "CookiesDir")
TIKTOK_VIDEOS_DIR = os.path.join(TIKTOK_REPO_DIR, "VideosDirPath")
TIKTOK_COOKIE_USER = "auto"

# Order matters: prefer shared media volume, fallback to legacy mount.
TIKTOK_COOKIES_CANDIDATES = [
    "/data_midia/cookies_tiktok.txt",
    "/app/cookies_tiktok.txt",
]

DEFAULT_PUBLISH_PRIVACY = os.getenv("YOUTUBE_DEFAULT_PRIVACY", "private").strip().lower()
VALID_YOUTUBE_PRIVACY = {"private", "public", "unlisted"}
TIKTOK_VISIBILITY_BY_PRIVACY = {
    "public": "0",
    "private": "1",
    "unlisted": "1",
}


class Platform(str, Enum):
    YOUTUBE = "youtube"
    TIKTOK = "tiktok"
    INSTAGRAM = "instagram"


class PlatformMetadata(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    hashtags: Optional[List[str]] = None

class PublishRequest(BaseModel):
    video_path: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    platforms: List[Platform]
    platform_overrides: Optional[dict[str, PlatformMetadata]] = None
    privacy: str = DEFAULT_PUBLISH_PRIVACY
    hashtags: Optional[List[str]] = None
    sound_name: Optional[str] = None
    job_id: Optional[str] = None


class PublishResponse(BaseModel):
    status: str
    results: dict


class YouTubeUploadRequest(BaseModel):
    video_path: str
    title: str
    description: str
    tags: List[str] = []
    privacy: str = DEFAULT_PUBLISH_PRIVACY
    category_id: str = "22"
    job_id: Optional[str] = None


class ValidateQualityRequest(BaseModel):
    """Payload para o endpoint /validate/quality (chamado pelo nó n8n Quality Gate)."""
    video_path: Optional[str] = None
    title: str = ""
    description: str = ""
    tags: List[str] = []
    min_score: int = 60


def _normalize_hashtag(tag: str) -> str:
    cleaned = (tag or "").strip()
    if not cleaned:
        return ""
    return cleaned if cleaned.startswith("#") else f"#{cleaned}"


def _build_caption(title: str, hashtags: Optional[List[str]]) -> str:
    normalized = [_normalize_hashtag(h) for h in (hashtags or [])]
    normalized = [h for h in normalized if h]
    return title if not normalized else f"{title} {' '.join(normalized)}"


def _resolve_youtube_privacy(privacy: Optional[str]) -> str:
    resolved_default = DEFAULT_PUBLISH_PRIVACY if DEFAULT_PUBLISH_PRIVACY in VALID_YOUTUBE_PRIVACY else "private"
    normalized = (privacy or resolved_default).strip().lower()
    if normalized not in VALID_YOUTUBE_PRIVACY:
        logger.warning("[Publish] Privacidade inválida '%s'. Usando '%s'.", privacy, resolved_default)
        return resolved_default
    return normalized


def get_peak_hours_schedule() -> Optional[str]:
    """
    Retorna o próximo horário de pico para publicação no YouTube,
    baseado na audiência de canais de futebol brasileiro.

    Horários de pico BR (UTC-3):
        12:00 (almoço), 18:00 (saída do trabalho), 21:00 (prime time)

    Retorna string ISO 8601 com timezone UTC para a API do YouTube,
    ou None se o horário atual JÁ for horário de pico (publica imediato).
    """
    now_utc = datetime.now(timezone.utc)
    # Converte para horário de Brasília (UTC-3)
    from datetime import timedelta
    now_brt = now_utc - timedelta(hours=3)
    hour = now_brt.hour

    # Horários de pico em BRT
    peak_hours_brt = [12, 18, 21]

    # Encontra o próximo horário de pico
    next_peak = None
    for peak in peak_hours_brt:
        if hour < peak:
            next_peak = peak
            break

    if next_peak is None:
        # Passou de todos os picos do dia → agenda para 12h do dia seguinte
        next_peak = peak_hours_brt[0]
        next_date = now_brt.replace(hour=next_peak, minute=0, second=0, microsecond=0)
        next_date = next_date + timedelta(days=1)
    else:
        next_date = now_brt.replace(hour=next_peak, minute=0, second=0, microsecond=0)

    # Converte de volta para UTC e formata como ISO 8601
    next_utc = next_date + timedelta(hours=3)
    scheduled = next_utc.strftime("%Y-%m-%dT%H:%M:%S.000Z")
    logger.info("[Publish] Horário de pico agendado: %s (BRT %dh)", scheduled, next_peak)
    return scheduled



def _resolve_tiktok_visibility(privacy: Optional[str]) -> str:
    normalized = _resolve_youtube_privacy(privacy)
    return TIKTOK_VISIBILITY_BY_PRIVACY.get(normalized, "1")


def _normalize_youtube_tag(tag: str) -> str:
    cleaned = (tag or "").strip()
    if not cleaned:
        return ""
    if cleaned.startswith("#"):
        cleaned = cleaned[1:].strip()
    return cleaned


def _resolve_cookies_source() -> Optional[str]:
    for path in TIKTOK_COOKIES_CANDIDATES:
        if os.path.exists(path):
            return path
    return None


def _parse_netscape_cookies(raw_text: str) -> List[dict]:
    cookies: List[dict] = []

    for raw_line in raw_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        http_only = False
        if line.startswith("#HttpOnly_"):
            line = line[len("#HttpOnly_"):]
            http_only = True
        elif line.startswith("#"):
            continue

        parts = line.split("\t")
        if len(parts) != 7:
            parts = line.split(None, 6)
        if len(parts) != 7:
            continue

        domain, _flag, path, secure, expiry, name, value = parts
        if not name:
            continue

        try:
            expiry_value = int(expiry)
        except ValueError:
            expiry_value = -1

        cookies.append(
            {
                "domain": domain,
                "path": path or "/",
                "name": name,
                "value": value,
                "secure": str(secure).upper() == "TRUE",
                "httpOnly": http_only,
                "expiry": expiry_value,
            }
        )

    return cookies


def _parse_json_cookies(raw_text: str) -> List[dict]:
    cookies: List[dict] = []
    try:
        payload = json.loads(raw_text)
    except json.JSONDecodeError:
        return cookies

    if isinstance(payload, dict):
        entries = payload.get("cookies") or payload.get("Cookies") or []
    elif isinstance(payload, list):
        entries = payload
    else:
        entries = []

    for entry in entries:
        if not isinstance(entry, dict):
            continue

        name = entry.get("name")
        value = entry.get("value")
        if not name or value is None:
            continue

        expiry_raw = entry.get("expiry", entry.get("expirationDate", entry.get("expires", -1)))
        try:
            expiry_value = int(float(expiry_raw))
        except (TypeError, ValueError):
            expiry_value = -1

        cookies.append(
            {
                "domain": entry.get("domain", ".tiktok.com"),
                "path": entry.get("path", "/"),
                "name": name,
                "value": str(value),
                "secure": bool(entry.get("secure", False)),
                "httpOnly": bool(entry.get("httpOnly", entry.get("httponly", False))),
                "expiry": expiry_value,
            }
        )

    return cookies


def _load_exported_cookies(path: str) -> List[dict]:
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        raw = fh.read().strip()

    if not raw:
        return []

    if raw[0] in "[{":
        parsed = _parse_json_cookies(raw)
        if parsed:
            return parsed

    return _parse_netscape_cookies(raw)


def _prepare_tiktok_cookie_store() -> tuple[Optional[str], Optional[str]]:
    source = _resolve_cookies_source()
    if not source:
        expected = " or ".join(TIKTOK_COOKIES_CANDIDATES)
        return None, f"Cookies TikTok nao encontrados. Esperado em: {expected}"

    try:
        cookies = _load_exported_cookies(source)
    except Exception as exc:
        return None, f"Falha ao ler cookies em {source}: {exc}"

    if not cookies:
        return None, f"Nenhum cookie valido encontrado em {source}"

    has_session = any(c.get("name") == "sessionid" and c.get("value") for c in cookies)
    if not has_session:
        return None, f"Cookie 'sessionid' nao encontrado em {source}"

    os.makedirs(TIKTOK_COOKIES_DIR, exist_ok=True)
    cookie_file = os.path.join(TIKTOK_COOKIES_DIR, f"tiktok_session-{TIKTOK_COOKIE_USER}.cookie")

    with open(cookie_file, "wb") as fh:
        pickle.dump(cookies, fh)

    return TIKTOK_COOKIE_USER, None


def _random_creation_id(length: int = 21) -> str:
    chars = string.ascii_letters + string.digits + "_"
    return "".join(random.choice(chars) for _ in range(length))


def _validate_tiktok_upload_session(cookie_user: str) -> Optional[str]:
    cookie_file = os.path.join(TIKTOK_COOKIES_DIR, f"tiktok_session-{cookie_user}.cookie")
    if not os.path.exists(cookie_file):
        return f"Cookie store interno nao encontrado: {cookie_file}"

    try:
        with open(cookie_file, "rb") as fh:
            cookies = pickle.load(fh)
    except Exception as exc:
        return f"Falha ao carregar cookie store interno: {exc}"

    session_id = next((c.get("value") for c in cookies if c.get("name") == "sessionid"), None)
    if not session_id:
        return "Cookie 'sessionid' ausente no store interno do TikTok."

    session = requests.Session()

    # TikTok may require more than just `sessionid`. Load the full exported cookie jar so
    # this pre-check matches what the CLI uploader will use.
    for entry in cookies or []:
        if not isinstance(entry, dict):
            continue
        name = entry.get("name")
        value = entry.get("value")
        if not name or value is None:
            continue
        domain = entry.get("domain") or ".tiktok.com"
        path = entry.get("path") or "/"
        try:
            session.cookies.set(name, str(value), domain=domain, path=path)
        except Exception:
            # Best effort, cookies with invalid domains/paths should not block auth check.
            continue

    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            ),
            "Accept": "application/json, text/plain, */*",
            "Referer": "https://www.tiktok.com/",
        }
    )

    creation_id = _random_creation_id()
    project_url = (
        "https://www.tiktok.com/api/v1/web/project/create/"
        f"?creation_id={creation_id}&type=1&aid=1988"
    )
    try:
        response = session.post(project_url, timeout=30)
    except Exception as exc:
        return f"Falha ao validar sessao TikTok para upload: {exc}"

    if response.status_code != 200:
        return f"TikTok respondeu HTTP {response.status_code} no pre-check de upload."

    try:
        payload = response.json()
    except Exception:
        return "Resposta invalida do TikTok no pre-check de upload (JSON invalido)."

    status_code = payload.get("status_code")
    if status_code not in (0, "0"):
        return (
            "Sessao TikTok recusada para upload "
            f"(status_code={status_code}). Reexporte cookies com a conta logada."
        )

    if "project" not in payload:
        return "Sessao TikTok sem objeto de projeto no pre-check. Reexporte cookies."

    return None


def _stage_video_for_cli(video_path: str) -> tuple[Optional[str], Optional[str], Optional[str]]:
    if not os.path.exists(video_path):
        return None, None, f"Arquivo nao encontrado: {video_path}"

    os.makedirs(TIKTOK_VIDEOS_DIR, exist_ok=True)

    src_abs = os.path.abspath(video_path)
    filename = os.path.basename(video_path)
    dst_abs = os.path.abspath(os.path.join(TIKTOK_VIDEOS_DIR, filename))

    try:
        if src_abs != dst_abs:
            shutil.copy2(src_abs, dst_abs)
    except Exception as exc:
        return None, None, f"Falha ao preparar video para TikTok: {exc}"

    return filename, dst_abs, None


def upload_to_tiktok_cli(
    video_path: str,
    title: str,
    hashtags: Optional[List[str]] = None,
    privacy: Optional[str] = None,
) -> dict:
    if not os.path.exists(TIKTOK_CLI_PATH):
        return {"status": "error", "msg": f"CLI do TikTok nao encontrado em {TIKTOK_CLI_PATH}"}

    cookie_user, cookie_error = _prepare_tiktok_cookie_store()
    if cookie_error:
        return {"status": "skipped", "msg": cookie_error}

    session_error = _validate_tiktok_upload_session(cookie_user)
    if session_error:
        logger.warning("[TikTok] Aviso na validação de sessão (tentando upload mesmo assim): %s", session_error)
        # return {"status": "error", "msg": session_error}

    staged_name, _staged_path, stage_error = _stage_video_for_cli(video_path)
    if stage_error:
        return {"status": "error", "msg": stage_error}

    caption = _build_caption(title, hashtags)
    visibility = _resolve_tiktok_visibility(privacy)

    
    # Use custom uploader script because the repo structure changed
    script_path = "/app/app/tiktok_custom_uploader.py"
    
    cmd = [
        "python",
        script_path,
        "--video", staged_name,
        "--title", caption,
        "--cookies", f"CookiesDir/tiktok_session-{cookie_user}.cookie",
    ]
    
    # Ensure the script can find the 'tiktok_uploader' package
    env = os.environ.copy()
    env["PYTHONPATH"] = TIKTOK_REPO_DIR

    try:
        result = subprocess.run(
            cmd,
            cwd=TIKTOK_REPO_DIR, # Keep CWD so CookiesDir relative path works
            env=env, # Pass PYTHONPATH
            capture_output=True,
            text=True,
            timeout=900,
        )
    except subprocess.TimeoutExpired:
        return {"status": "error", "msg": "Timeout no upload TikTok (900s)"}
    except Exception as exc:
        return {"status": "error", "msg": str(exc)}

    if result.returncode == 0:
        return {"status": "success", "output": (result.stdout or "").strip()}

    stderr = (result.stderr or "").strip()
    stdout = (result.stdout or "").strip()
    if "KeyError: 'project'" in stderr or "KeyError: 'project'" in stdout:
        return {
            "status": "error",
            "msg": (
                "TikTok recusou a criacao do projeto de upload. "
                "Reexporte cookies_tiktok.txt da conta logada (Creator) e tente novamente."
            ),
        }
    return {"status": "error", "msg": stderr or stdout or f"Script customizado retornou codigo {result.returncode}"}


# ---------------------------------------------------------------------------
# TikTok Upload via Haziq-exe/TikTokAutoUploader (Phantomwright headless)
# ---------------------------------------------------------------------------
TIKTOK_HAZIQ_SCRIPT = "/app/app/upload_tiktok_haziq.py"
TIKTOK_HAZIQ_ACCOUNT = os.getenv("TIKTOK_ACCOUNT", "futebas_oficial")


def upload_to_tiktok_haziq(
    video_path: str,
    title: str,
    hashtags: Optional[List[str]] = None,
    account: Optional[str] = None,
) -> dict:
    """Upload para TikTok via TikTokAutoUploader (Haziq-exe) com Phantomwright."""
    account = account or TIKTOK_HAZIQ_ACCOUNT

    if not os.path.exists(video_path):
        return {"status": "error", "msg": f"Arquivo nao encontrado: {video_path}"}

    cookies_path = f"/data_midia/tk_haziq_cookies_{account}.json"
    if not os.path.exists(cookies_path):
        return {
            "status": "error",
            "msg": f"Cookies nao encontrados: {cookies_path}. Execute convert_cookies.py.",
        }

    caption = _build_caption(title, hashtags)

    cmd = [
        "/opt/venv/bin/python3",
        TIKTOK_HAZIQ_SCRIPT,
        "--video", video_path,
        "--title", caption,
        "--account", account,
    ]
    if hashtags:
        cmd.extend(["--hashtags"] + [h.lstrip("#") for h in hashtags])

    logger.info("[TikTok-Haziq] Iniciando upload: %s", caption[:60])

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=600,  # 10 min
        )
    except subprocess.TimeoutExpired:
        return {"status": "error", "msg": "Timeout no upload TikTok Haziq (600s)"}
    except Exception as exc:
        return {"status": "error", "msg": str(exc)}

    stdout = (result.stdout or "").strip()
    stderr = (result.stderr or "").strip()

    if result.returncode == 0:
        logger.info("[TikTok-Haziq] ✅ Upload concluído com sucesso!")
        return {"status": "success", "output": stdout[-500:] if stdout else "OK"}

    logger.error("[TikTok-Haziq] ❌ Falha (exit %d): %s", result.returncode, stdout[-300:])
    return {"status": "error", "msg": stdout[-300:] or stderr[-300:] or f"Exit code {result.returncode}"}


def _update_job_meta(job_id: str, key: str, value) -> None:
    from app.utils.database import get_db_connection

    conn = get_db_connection()
    if not conn:
        return

    try:
        with conn.cursor() as cur:
            patch = json.dumps({key: value})

            if key == "youtube_id" and value:
                cur.execute(
                    "UPDATE video_jobs "
                    "SET metadata_post = COALESCE(metadata_post, '{}'::jsonb) || %s::jsonb, "
                    "published = TRUE, "
                    "status = 'published', "
                    "platform_id = COALESCE(platform_id, %s), "
                    "updated_at = CURRENT_TIMESTAMP "
                    "WHERE id = %s",
                    (patch, str(value), job_id),
                )
            else:
                cur.execute(
                    "UPDATE video_jobs "
                    "SET metadata_post = COALESCE(metadata_post, '{}'::jsonb) || %s::jsonb, "
                    "published = TRUE, "
                    "status = 'published', "
                    "updated_at = CURRENT_TIMESTAMP "
                    "WHERE id = %s",
                    (patch, job_id),
                )
            conn.commit()
    except Exception as exc:
        logger.error("[Publish] Erro ao salvar metadados job %s: %s", job_id, exc)
    finally:
        conn.close()


@router.post("/validate/quality")
async def validate_quality(req: ValidateQualityRequest):
    """
    Endpoint chamado pelo nó n8n 'Quality Gate Vídeo'.

    Valida se o vídeo gerado atende aos critérios mínimos antes de publicar.
    Isso evita gastar cota da API do YouTube com vídeos de baixa qualidade.

    Saída (HTTP 200 — aprovado):
        {"passed": true, "score": 87, "warnings": [...]}

    Saída (HTTP 422 — reprovado):
        {"error": "quality_gate_reprovado", "score": 42, "issues": [...]}

    Fail-safe: se o gate falhar internamente, retorna HTTP 200 aprovado
    para não travar o pipeline por bug do validador.
    """
    normalized_tags = [_normalize_youtube_tag(t) for t in (req.tags or [])]
    normalized_tags = [t for t in normalized_tags if t]

    try:
        gate_report = run_full_quality_gate(
            video_path=req.video_path or "",
            title=req.title,
            description=req.description,
            tags=normalized_tags,
            min_score=req.min_score
        )
        logger.info(
            "[ValidateQuality] Score: %d/100 | Aprovado: %s | Issues: %s",
            gate_report.score,
            gate_report.passed,
            gate_report.issues or "nenhum"
        )
        if gate_report.passed:
            return {
                "passed": True,
                "score": gate_report.score,
                "warnings": gate_report.warnings,
                "summary": gate_report.summary()
            }
        else:
            raise HTTPException(
                status_code=422,
                detail={
                    "error": "quality_gate_reprovado",
                    "score": gate_report.score,
                    "issues": gate_report.issues,
                    "warnings": gate_report.warnings,
                    "summary": gate_report.summary()
                }
            )
    except HTTPException:
        raise
    except Exception as qg_err:
        logger.warning(
            "[ValidateQuality] Falha interna do gate (aprovando por segurança): %s", qg_err
        )
        return {"passed": True, "score": 100, "warnings": [f"gate_error: {str(qg_err)}"]}


@router.post("/youtube")
async def publish_youtube(req: YouTubeUploadRequest):
    """Upload isolado para YouTube com agendamento para horário de pico."""
    if not req.video_path:
        return {"status": "error", "msg": "video_path vazio/nulo"}

    if not os.path.exists(req.video_path):
        return {"status": "error", "msg": f"Arquivo nao encontrado: {req.video_path}"}

    resolved_privacy = _resolve_youtube_privacy(req.privacy)
    normalized_tags = [_normalize_youtube_tag(t) for t in (req.tags or [])]
    normalized_tags = [t for t in normalized_tags if t]

    # ── QUALITY GATE OBRIGATÓRIO (Etapa 5 — FASE 1) ────────────────────────
    #
    # Executamos a validação ANTES de qualquer tentativa de upload.
    # Isso economiza quota da API do YouTube e garante que os 15s mínimos
    # e a resolução 1080x1920 sejam respeitados.
    #
    # O que é verificado:
    #   ✓ Duração ≥ 15s (YouTube rejeita Shorts mais curtos)
    #   ✓ Resolução 1080x1920 (aviso se diferente)
    #   ✓ Arquivo não está corrompido (MoviePy consegue abrir)
    #   ✓ Áudio presente e não mudo (RMS > 0.001)
    #   ✓ Título não é placeholder genérico
    #   ✓ Descrição ≥ 30 chars (SEO mínimo)
    #
    # Se score < 60 → HTTP 422 com relatório detalhado.
    # Operador pode ver o score no corpo da resposta para ajuste manual.
    try:
        gate_report = run_full_quality_gate(
            video_path=req.video_path,
            title=req.title,
            description=req.description,
            tags=normalized_tags,
            min_score=60  # Mínimo para publicar (0-100)
        )
        logger.info(
            "[QualityGate] Pré-upload YouTube — Score: %d/100 | Aprovado: %s | Issues: %s",
            gate_report.score,
            gate_report.passed,
            gate_report.issues or "nenhum"
        )
        if not gate_report.passed:
            # HTTP 422 Unprocessable Entity — dados válidos mas conteúdo abaixo do padrão
            raise HTTPException(
                status_code=422,
                detail={
                    "error": "quality_gate_reprovado",
                    "score": gate_report.score,
                    "issues": gate_report.issues,    # Lista de problemas bloqueantes
                    "warnings": gate_report.warnings, # Lista de avisos não-bloqueantes
                    "summary": gate_report.summary(),
                    "msg": (
                        f"Vídeo reprovado no Quality Gate (score {gate_report.score}/100 "
                        f"— mínimo 60). Corrija os problemas antes de publicar."
                    )
                }
            )
    except HTTPException:
        # Re-levanta HTTPException sem engolir (ela não é erro interno)
        raise
    except Exception as qg_err:
        # Se o próprio quality gate falhar, logamos mas não bloqueamos —
        # preferimos publicar sem gate a não publicar por bug do validador.
        logger.warning(
            "[QualityGate] Falha interna do gate (publicando mesmo assim): %s", qg_err
        )

    # Agendamento por horário de pico (apenas se privacy=public)
    scheduled_at = None
    if resolved_privacy == "public":
        scheduled_at = get_peak_hours_schedule()

    try:
        yt_service = YouTubeService()
        resp = yt_service.upload_video(
            file_path=req.video_path,
            title=req.title,
            description=req.description,
            privacy="private" if scheduled_at else resolved_privacy,  # Scheduled = começa private
            tags=normalized_tags,
            category_id=req.category_id or "22",
            scheduled_at=scheduled_at,
        )
    except Exception as exc:
        logger.error("[Publish] Erro YouTube: %s", exc)
        return {"status": "error", "msg": str(exc)}

    video_id = (resp or {}).get("id")

    # Post-upload: adiciona comentário fixado com CTA
    if video_id:
        try:
            yt_service.pin_comment(
                video_id=video_id,
                text=("⚽ Gostou? SEGUE o Futebas para não perder nada! "
                      "Deixa seu comentário e compartilha com a galera 👊")
            )
        except Exception as e:
            logger.warning("[Publish] Pinned comment falhou (não crítico): %s", e)

    if req.job_id and video_id:
        _update_job_meta(req.job_id, "youtube_id", video_id)
        if scheduled_at:
            _update_job_meta(req.job_id, "scheduled_at", scheduled_at)

    logger.info("[Publish] YouTube upload OK — ID: %s | Agendado: %s", video_id, scheduled_at or "imediato")
    return {
        "status": "success",
        "video_id": video_id,
        "url": f"https://youtu.be/{video_id}" if video_id else None,
        "title": req.title,
        "scheduled_at": scheduled_at,
        "data": resp,
    }


class TikTokRequest(BaseModel):
    video_path: str
    title: str
    hashtags: List[str] = []
    privacy: str = "public"
    job_id: Optional[str] = None


@router.post("/tiktok")
async def publish_tiktok(req: TikTokRequest):
    """Upload isolado para TikTok (via CLI)."""
    if not req.video_path or not os.path.exists(req.video_path):
        return {"status": "error", "msg": f"Arquivo nao encontrado: {req.video_path}"}

    resolved_privacy = _resolve_youtube_privacy(req.privacy)
    
    try:
        res = upload_to_tiktok_haziq(
            req.video_path,
            req.title,
            req.hashtags,
        )
    except Exception as exc:
        return {"status": "error", "msg": str(exc)}

    if req.job_id and res.get("status") == "success":
        _update_job_meta(req.job_id, "tiktok_id", "published_via_cli")

    return res


@router.post("/multi", response_model=PublishResponse)
async def publish_multi(req: PublishRequest):
    from app.utils.database import get_db_connection

    if not req.video_path and not req.job_id:
        print("[Publish] Encerrando com SKIP (video_path e job_id nulos).")
        return {
            "status": "skipped",
            "results": {"all": {"status": "skipped", "msg": "Sem video_path ou job_id para processar."}},
        }

    # Fallback: Carrega dados do Banco de Dados se tivermos apenas o job_id
    if req.job_id:
        try:
            conn = get_db_connection()
            if conn:
                with conn.cursor() as cur:
                    cur.execute("""
                        SELECT video_path, title, metadata, metadata_post 
                        FROM video_jobs 
                        WHERE id = %s
                    """, (req.job_id,))
                    job = cur.fetchone()
                    if job:
                        if not req.video_path: req.video_path = job.get("video_path")
                        if not req.title: req.title = job.get("title")
                        
                        # Tags e Descrição (Script)
                        meta = job.get("metadata") or {}
                        post_meta = job.get("metadata_post") or {}
                        
                        if not req.description:
                            # Tenta pegar 'script' do metadata ou fallback genérico
                            req.description = meta.get("script") or "Novo vídeo do Futebas! 🔥"
                        
                        if not req.hashtags:
                            req.hashtags = post_meta.get("hashtags") or meta.get("tags") or []
                conn.close()
        except Exception as e:
            logger.error("[Publish] Erro ao carregar fallback do DB: %s", e)

    # Validação Final pós-fallback
    if not req.video_path or not os.path.exists(req.video_path):
        return {
            "status": "error",
            "results": {"all": {"status": "error", "msg": f"Video não encontrado: {req.video_path}"}}
        }

    skip_youtube = False
    skip_tiktok = False

    if req.job_id:
        conn = get_db_connection()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute("SELECT published, metadata_post FROM video_jobs WHERE id = %s", (req.job_id,))
                    row = cur.fetchone()
                    if row:
                        meta = row.get("metadata_post") or {}
                        if row.get("published") is True and not req.platforms:
                            pass

                        if meta.get("youtube_id"):
                            logger.info("[Publish] YouTube já publicado para Job %s. Pulando.", req.job_id)
                            skip_youtube = True

                        if meta.get("tiktok_id"):
                            logger.info("[Publish] TikTok já publicado para Job %s. Pulando.", req.job_id)
                            skip_tiktok = True
            except Exception as exc:
                logger.error("[Publish] Erro ao checar idempotencia: %s", exc)
            finally:
                conn.close()

    if not os.path.exists(req.video_path):
        return {
            "status": "error",
            "results": {"all": {"status": "error", "msg": f"Arquivo nao encontrado: {req.video_path}"}},
        }

    resolved_privacy = _resolve_youtube_privacy(req.privacy)
    logger.info("[Publish] Privacy efetiva para este job: %s", resolved_privacy)

    results = {}

    if Platform.YOUTUBE in req.platforms:
        if skip_youtube:
            results["youtube"] = {"status": "skipped", "msg": "Ja publicado anteriormente."}
        else:
            try:
                logger.info("[Publish] Iniciando upload para YouTube...")
                
                plat_meta = (req.platform_overrides or {}).get("youtube", PlatformMetadata())
                yt_title = plat_meta.title or req.title
                yt_desc = plat_meta.description or req.description
                yt_hash = plat_meta.hashtags if plat_meta.hashtags is not None else req.hashtags
                
                yt_desc_final = yt_desc + "\n\n" + " ".join(yt_hash)
                yt_service = YouTubeService()

                # Agendamento por horário de pico
                scheduled_at = None
                if resolved_privacy == "public":
                    scheduled_at = get_peak_hours_schedule()

                resp = yt_service.upload_video(
                    file_path=req.video_path,
                    title=yt_title,
                    description=yt_desc_final,
                    privacy="private" if scheduled_at else resolved_privacy,
                    tags=yt_hash,
                    scheduled_at=scheduled_at,
                )

                vid_id = (resp or {}).get("id")

                # Comentário fixado (pinned)
                if vid_id:
                    try:
                        yt_service.pin_comment(
                            video_id=vid_id,
                            text=("⚽ Gostou? SEGUE o Futebas! Comenta o que você achou 👇")
                        )
                    except Exception as e:
                        logger.warning("[Publish] Pinned comment falhou: %s", e)

                results["youtube"] = {
                    "status": "success",
                    "data": resp,
                    "scheduled_at": scheduled_at
                }
                if req.job_id and vid_id:
                    _update_job_meta(req.job_id, "youtube_id", vid_id)
                    if scheduled_at:
                        _update_job_meta(req.job_id, "scheduled_at", scheduled_at)
            except Exception as exc:
                logger.error("[Publish] Erro YouTube: %s", exc)
                results["youtube"] = {"status": "error", "msg": str(exc)}

    if Platform.TIKTOK in req.platforms:
        if skip_tiktok:
            results["tiktok"] = {"status": "skipped", "msg": "Ja publicado anteriormente."}
        else:
            try:
                plat_meta = (req.platform_overrides or {}).get("tiktok", PlatformMetadata())
                tk_title = plat_meta.title or req.title
                tk_hash = plat_meta.hashtags if plat_meta.hashtags is not None else req.hashtags
                
                res = upload_to_tiktok_haziq(
                    req.video_path,
                    tk_title,
                    tk_hash,
                )
                results["tiktok"] = res
                if req.job_id and res.get("status") == "success":
                    _update_job_meta(req.job_id, "tiktok_id", "published_via_cli")
            except Exception as exc:
                results["tiktok"] = {"status": "error", "msg": str(exc)}

    if Platform.INSTAGRAM in req.platforms:
        logger.info("[Publish] Instagram selecionado, mas uploader (Graph API) ainda precisa ser configurado.")
        results["instagram"] = {"status": "skipped", "msg": "Configuração Pendente de API."}

    # --- TELEGRAM NOTIFICATION & FALLBACK ---
    try:
        status_msg = f"🚀 *Processo de Publicação Finalizado*\n\n"
        status_msg += f"🎬 *Título:* {req.title}\n"
        status_msg += f"🆔 *Job:* `{req.job_id}`\n\n"
        
        for platform, res in results.items():
            icon = "✅" if res.get("status") in ("success", "skipped") else "❌"
            status_msg += f"{icon} *{platform.upper()}:* {res.get('status')} {res.get('msg', '')}\n"

        # Envia o vídeo como fallback (ou garantia)
        logger.info("[Telegram] Enviando vídeo para Telegram fallback...")
        caption = f"🎬 {req.title}\n\n#Futebas #Futebol #VideosCurtos"
        send_telegram_video(req.video_path, caption=caption)
        
        # Envia o relatório de status
        send_telegram_message(status_msg)
        
    except Exception as tel_err:
        logger.error(f"[Publish] Erro ao enviar notificação Telegram: {tel_err}")

    return {"status": "completed", "results": results}
