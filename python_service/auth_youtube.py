from google_auth_oauthlib.flow import Flow
import os
import argparse
import sys

SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.readonly"
]

def authenticate(code=None):
    print("=== Autenticação Manual YouTube (CLI Mode) ===")
    
    if not os.path.exists("client_secret.json"):
        print("ERRO: client_secret.json não encontrado.")
        return

    flow = Flow.from_client_secrets_file(
        "client_secret.json",
        scopes=SCOPES,
        redirect_uri='http://localhost'
    )
    
    if not code:
        print("1. Visite a URL abaixo para autorizar:")
        auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')
        print(auth_url)
        print("=========================================")
        print("2. Após o login, o navegador dará erro em 'http://localhost'.")
        print("3. Copie o parâmetro 'code=...' da URL.")
        print("4. Execute este script novamente passando o código:")
        print('   docker exec python_service python auth_youtube.py --code "SEU_CODIGO_AQUI"')
        print("=========================================")
    else:
        print(f"Tentando autenticar com o código fornecido...")
        try:
            flow.fetch_token(code=code)
            creds = flow.credentials
            
            with open("token.json", "w") as f:
                f.write(creds.to_json())
            print("SUCESSO! token.json gerado.")
        except Exception as e:
            print(f"Falha ao gerar token: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--code", help="O código de autorização obtido no navegador", type=str)
    args = parser.parse_args()
    
    authenticate(code=args.code)
