# =============================================================================
# app/services/youtube.py — Serviço de Upload do YouTube (OAuth2)
# =============================================================================
import os

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
from fastapi import HTTPException
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
    before_sleep_log,
)
import logging

logger = logging.getLogger(__name__)

# Escopos necessários para upload e gerenciamento
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.readonly"
]

class YouTubeService:
    def __init__(self):
        client_secret = os.getenv("YOUTUBE_CLIENT_SECRET_FILE", "client_secret.json")
        token_file = os.getenv("YOUTUBE_TOKEN_FILE", "token.json")

        self.client_secret_file = self._resolve_container_path(
            client_secret, "client_secret.json"
        )
        self.token_file = self._resolve_container_path(token_file, "token.json")
        self.service = None

    @staticmethod
    def _resolve_container_path(configured_path: str, fallback_name: str) -> str:
        if configured_path and os.path.exists(configured_path):
            return configured_path

        fallback_in_app = os.path.join("/app", fallback_name)
        if os.path.exists(fallback_in_app):
            return fallback_in_app

        return configured_path or fallback_name

    def get_authenticated_service(self):
        """Autentica o usuário e retorna o serviço da API do YouTube."""
        creds = None
        
        # 1. Carrega token existente se houver
        if os.path.exists(self.token_file):
            try:
                creds = Credentials.from_authorized_user_file(self.token_file, SCOPES)
            except Exception as e:
                print(f"[YouTube] Erro ao carregar token: {e}")
                creds = None

        # 2. Se não houver creds válidas, inicia login
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                print("[YouTube] Atualizando token expirado...")
                try:
                    creds.refresh(Request())
                except Exception as e:
                    print(f"[YouTube] Falha ao atualizar token: {e}")
                    if "disabled_client" in str(e):
                        print(
                            "[YouTube] OAuth client desabilitado no Google Cloud. "
                            "Reative o client_id atual ou gere um novo "
                            "client_secret.json."
                        )
                    creds = None
            
            if not creds:
                if not os.path.exists(self.client_secret_file):
                    print(f"[YouTube] Arquivo '{self.client_secret_file}' não encontrado na pasta {os.getcwd()}.")
                    return None

                print("[YouTube] Token inválido ou inexistente. Auth browser não suportado em Docker.")
                print("[YouTube] Por favor, execute: docker exec -it python_service python auth_youtube.py")
                return None

            # Salva o token para próximas execuções
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())

        try:
            self.service = build('youtube', 'v3', credentials=creds)
            return self.service
        except Exception as e:
            print(f"[YouTube] Erro ao construir serviço: {e}")
            return None

    @retry(
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=4, max=60),
        retry=retry_if_exception_type((HttpError, ConnectionError, TimeoutError)),
        before_sleep=before_sleep_log(logger, logging.WARNING),
        reraise=True
    )
    def upload_video(
        self,
        file_path: str,
        title: str,
        description: str,
        privacy: str = "private",
        tags: list = None,
        category_id: str = "22"
    ):
        """Faz o upload de um vídeo para o YouTube."""
        youtube = self.get_authenticated_service()
        if not youtube:
            # Não lançar erro 500 se for apenas falta de auth, mas sim retornar um erro amigável ou None
            # Mas como isso é chamado via endpoint, exception é capturada pelo publish.py
            raise Exception("Falha na autenticação do YouTube. Verifique client_secret.json ou token.json.")

        if not tags:
            tags = []

        print(f"[YouTube] Iniciando upload: {title}")
        
        body = {
            'snippet': {
                'title': title[:100],  # Limite 100 chars
                'description': description[:5000],  # Limite 5000 chars
                'tags': tags,
                'categoryId': category_id
            },
            'status': {
                'privacyStatus': privacy,  # private, public, unlisted
                'selfDeclaredMadeForKids': False,
            }
        }

        # MediaFileUpload suporta resumable uploads
        media = MediaFileUpload(file_path, chunksize=-1, resumable=True)

        request = youtube.videos().insert(
            part=','.join(body.keys()),
            body=body,
            media_body=media
        )

        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                progress = int(status.progress() * 100)
                print(f"[YouTube] Upload progresso: {progress}%")

        print(f"[YouTube] Upload concluído! ID: {response.get('id')}")
        return response
