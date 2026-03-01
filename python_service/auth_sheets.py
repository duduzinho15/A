from google_auth_oauthlib.flow import Flow
import os
import argparse
import sys

# Scopes para Google Sheets.
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
]

def authenticate(code=None):
    print("=== Autenticação Manual Google Sheets (CLI Mode) ===")
    
    # Define caminhos absolutos baseados no diretório do script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    secret_path = os.path.join(base_dir, "client_secret.json")
    token_path = os.path.join(base_dir, "token_sheets.json")

    if not os.path.exists(secret_path):
        print(f"ERRO: client_secret.json não encontrado em {secret_path}")
        return

    flow = Flow.from_client_secrets_file(
        secret_path,
        scopes=SCOPES,
        redirect_uri='http://localhost'
    )
    
    if not code:
        print("1. Visite a URL abaixo para autorizar o acesso às Planilhas:")
        auth_url, _ = flow.authorization_url(prompt='consent', access_type='offline')
        try:
            with open("/data_midia/auth_url_found.txt", "w") as f:
                f.write(auth_url)
        except:
             with open("auth_url_found.txt", "w") as f:
                f.write(auth_url)
        print(auth_url)
        print("=========================================")
        print("2. Após o login, o navegador dará erro em 'http://localhost'.")
        print("3. Copie o parâmetro 'code=...' da URL.")
        print("4. Execute este script novamente passando o código:")
        print('   docker exec python_service python auth_sheets.py --code "SEU_CODIGO_AQUI"')
        print("=========================================")
    else:
        print(f"Tentando autenticar com o código fornecido...")
        try:
            flow.fetch_token(code=code)
            creds = flow.credentials
            
            with open(token_path, "w") as f:
                f.write(creds.to_json())
            print(f"SUCESSO! {token_path} gerado.")
            print("AVISO: Certifique-se de que este arquivo está montado no docker-compose.yml.")
        except Exception as e:
            print(f"Falha ao gerar token: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--code", help="O código de autorização obtido no navegador", type=str)
    args = parser.parse_args()
    
    authenticate(code=args.code)
