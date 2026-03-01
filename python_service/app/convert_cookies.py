"""
Converte cookies do formato de extensão de navegador (cookies.txt)
para o formato Playwright que o TikTokAutoUploader espera.

Uso: python convert_cookies.py <input_cookies.txt> <output_cookies.json>
"""
import json
import sys
import os


def convert_cookie(cookie):
    """Converte um cookie do formato de extensão para formato Playwright."""
    pw_cookie = {
        "name": cookie["name"],
        "value": cookie["value"],
        "domain": cookie["domain"],
        "path": cookie.get("path", "/"),
    }

    # sameSite: Playwright espera "Strict", "Lax", ou "None"
    same_site = cookie.get("sameSite")
    if same_site == "no_restriction":
        pw_cookie["sameSite"] = "None"
    elif same_site == "lax":
        pw_cookie["sameSite"] = "Lax"
    elif same_site == "strict":
        pw_cookie["sameSite"] = "Strict"
    elif same_site is None or same_site == "null":
        pw_cookie["sameSite"] = "Lax"
    else:
        pw_cookie["sameSite"] = "Lax"

    # expires: Playwright usa "expires" (Unix timestamp float)
    expiration = cookie.get("expirationDate")
    if expiration:
        pw_cookie["expires"] = expiration
    else:
        # Session cookie - usar -1 ou omitir
        pw_cookie["expires"] = -1

    # httpOnly e secure
    pw_cookie["httpOnly"] = cookie.get("httpOnly", False)
    pw_cookie["secure"] = cookie.get("secure", False)

    return pw_cookie


def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else "/app/cookies.txt"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "/data_midia/tk_haziq_cookies_futebas_oficial.json"

    print(f"[convert] Lendo cookies de: {input_path}")

    with open(input_path, "r") as f:
        content = f.read()

    # Tentar parsear apenas a parte JSON (ignorar o cookie string no final)
    # O arquivo tem JSON na primeira parte e uma cookie string na última linha
    try:
        # Encontrar o fim do array JSON
        bracket_count = 0
        json_end = 0
        for i, char in enumerate(content):
            if char == "[":
                bracket_count += 1
            elif char == "]":
                bracket_count -= 1
                if bracket_count == 0:
                    json_end = i + 1
                    break

        json_str = content[:json_end]
        raw_cookies = json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"[convert] Erro ao parsear JSON: {e}")
        sys.exit(1)

    print(f"[convert] Encontrados {len(raw_cookies)} cookies brutos")

    # Converter para formato Playwright
    pw_cookies = [convert_cookie(c) for c in raw_cookies]

    # Garantir diretório existe
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, "w") as f:
        json.dump(pw_cookies, f, indent=4)

    print(f"[convert] ✅ {len(pw_cookies)} cookies convertidos e salvos em: {output_path}")

    # Verificar cookies críticos
    critical = ["sessionid", "sid_tt", "sessionid_ss"]
    found = [c["name"] for c in pw_cookies if c["name"] in critical]
    missing = [n for n in critical if n not in found]

    if missing:
        print(f"[convert] ⚠️ Cookies críticos ausentes: {missing}")
    else:
        print(f"[convert] ✅ Todos os cookies críticos presentes: {found}")


if __name__ == "__main__":
    main()
