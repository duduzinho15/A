# =============================================================================
# app/routes/publish.py - Multi-platform publishing (YouTube + TikTok)
# =============================================================================
import json
import os
import pickle
import random
import string
import shutil
import subprocess
from enum import Enum
from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel
import requests

from app.services.youtube import YouTubeService

router = APIRouter(prefix="/publish", tags=["publicacao"])

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


class PublishRequest(BaseModel):
    video_path: Optional[str] = None
    title: str
    description: str
    platforms: List[Platform]
    privacy: str = DEFAULT_PUBLISH_PRIVACY
    hashtags: List[str] = []
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
        print(f"[Publish] Privacidade invalida '{privacy}'. Usando '{resolved_default}'.")
        return resolved_default
    return normalized


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
        print(f"[TikTok] Aviso na validacao de sessao (tentando upload mesmo assim): {session_error}")
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


def _update_job_meta(job_id: str, key: str, value) -> None:
    from app.utils.database import get_db_connection

    conn = get_db_connection()
    if not conn:
        return

    try:
        with conn.cursor() as cur:
            patch = json.dumps({key: value})

            # Persist publish info consistently for analytics/idempotency.
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
        print(f"[Publish] Erro ao salvar metadados job {job_id}: {exc}")
    finally:
        conn.close()


@router.post("/youtube")
async def publish_youtube(req: YouTubeUploadRequest):
    """Upload isolado para YouTube (bom para smoke tests via curl/Postman)."""
    if not req.video_path:
        return {"status": "error", "msg": "video_path vazio/nulo"}

    if not os.path.exists(req.video_path):
        return {"status": "error", "msg": f"Arquivo nao encontrado: {req.video_path}"}

    resolved_privacy = _resolve_youtube_privacy(req.privacy)
    normalized_tags = [_normalize_youtube_tag(t) for t in (req.tags or [])]
    normalized_tags = [t for t in normalized_tags if t]

    try:
        yt_service = YouTubeService()
        resp = yt_service.upload_video(
            file_path=req.video_path,
            title=req.title,
            description=req.description,
            privacy=resolved_privacy,
            tags=normalized_tags,
            category_id=req.category_id or "22",
        )
    except Exception as exc:
        return {"status": "error", "msg": str(exc)}

    video_id = (resp or {}).get("id")
    if req.job_id and video_id:
        _update_job_meta(req.job_id, "youtube_id", video_id)

    return {
        "status": "success",
        "video_id": video_id,
        "url": f"https://youtu.be/{video_id}" if video_id else None,
        "title": req.title,
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
        res = upload_to_tiktok_cli(
            req.video_path,
            req.title,
            req.hashtags,
            privacy=resolved_privacy,
        )
    except Exception as exc:
        return {"status": "error", "msg": str(exc)}

    if req.job_id and res.get("status") == "success":
        _update_job_meta(req.job_id, "tiktok_id", "published_via_cli")

    return res


@router.post("/multi", response_model=PublishResponse)
async def publish_multi(req: PublishRequest):
    from app.utils.database import get_db_connection

    if not req.video_path:
        print("[Publish] Encerrando com SKIP (video_path nulo/vazio).")
        return {
            "status": "skipped",
            "results": {"all": {"status": "skipped", "msg": "Job anterior falhou (sem video_path)."}},
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
                            print(f"[Publish] YouTube ja publicado para Job {req.job_id}. Pulando.")
                            skip_youtube = True

                        if meta.get("tiktok_id"):
                            print(f"[Publish] TikTok ja publicado para Job {req.job_id}. Pulando.")
                            skip_tiktok = True
            except Exception as exc:
                print(f"[Publish] Erro ao checar idempotencia: {exc}")
            finally:
                conn.close()

    if not os.path.exists(req.video_path):
        return {
            "status": "error",
            "results": {"all": {"status": "error", "msg": f"Arquivo nao encontrado: {req.video_path}"}},
        }

    resolved_privacy = _resolve_youtube_privacy(req.privacy)
    print(f"[Publish] Privacy efetiva para este job: {resolved_privacy}")

    results = {}

    if Platform.YOUTUBE in req.platforms:
        if skip_youtube:
            results["youtube"] = {"status": "skipped", "msg": "Ja publicado anteriormente."}
        else:
            try:
                print("[Publish] Iniciando upload para YouTube...")
                yt_desc = req.description + "\n\n" + " ".join(req.hashtags)
                yt_service = YouTubeService()
                resp = yt_service.upload_video(
                    file_path=req.video_path,
                    title=req.title,
                    description=yt_desc,
                    privacy=resolved_privacy,
                    tags=req.hashtags,
                )

                results["youtube"] = {"status": "success", "data": resp}
                if req.job_id and resp.get("id"):
                    _update_job_meta(req.job_id, "youtube_id", resp["id"])
            except Exception as exc:
                print(f"[Publish] Erro YouTube: {exc}")
                results["youtube"] = {"status": "error", "msg": str(exc)}

    if Platform.TIKTOK in req.platforms:
        if skip_tiktok:
            results["tiktok"] = {"status": "skipped", "msg": "Ja publicado anteriormente."}
        else:
            try:
                res = upload_to_tiktok_cli(
                    req.video_path,
                    req.title,
                    req.hashtags,
                    privacy=resolved_privacy,
                )
                results["tiktok"] = res
                if req.job_id and res.get("status") == "success":
                    _update_job_meta(req.job_id, "tiktok_id", "published_via_cli")
            except Exception as exc:
                results["tiktok"] = {"status": "error", "msg": str(exc)}

    return {"status": "completed", "results": results}
