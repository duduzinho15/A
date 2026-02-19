
import requests

FLARESOLVERR_URL = "http://flaresolverr:8191/v1"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

def check_flaresolverr_health() -> bool:
    """Verifica se o container do FlareSolverr está acessível."""
    try:
        requests.get("http://flaresolverr:8191", timeout=3)
        return True
    except requests.RequestException:
        return False

def fetch_via_flaresolverr(url: str) -> str | None:
    """Baixa o HTML usando FlareSolverr (bypass Cloudflare)."""
    try:
        payload = {
            "cmd": "request.get",
            "url": url,
            "headers": HEADERS,
            "maxTimeout": 60000
        }

        resp = requests.post(
            FLARESOLVERR_URL,
            json=payload,
            timeout=65
        )

        if resp.status_code == 200:
            data = resp.json()
            if data.get("status") == "ok":
                return data.get("solution", {}).get("response")

    except Exception as e:
        print(f"[FlareSolverr] Erro: {e}")

    return None
