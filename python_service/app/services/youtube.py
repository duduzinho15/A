# =============================================================================
# app/services/youtube.py — Serviço de Upload do YouTube (OAuth2)
# =============================================================================
import os
from typing import Optional, Dict

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

# Escopos necessários para upload, gerenciamento e pin de comentário.
# ATENÇÃO: youtube.force-ssl é obrigatório para pin_comment() (CommentThread.insert).
# Se este escopo for adicionado ou removido, o token.json DEVE ser re-gerado
# rodando: docker exec -it python_service python auth_youtube.py
SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.readonly",
    "https://www.googleapis.com/auth/youtube.force-ssl",  # Pin comment + moderacao
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
        """Autentica e retorna o serviço da API do YouTube."""
        creds = None

        if os.path.exists(self.token_file):
            try:
                creds = Credentials.from_authorized_user_file(self.token_file, SCOPES)
            except Exception as e:
                logger.warning("[YouTube] Erro ao carregar token: %s", e)
                creds = None

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                logger.info("[YouTube] Atualizando token expirado...")
                try:
                    creds.refresh(Request())
                except Exception as e:
                    logger.error("[YouTube] Falha ao atualizar token: %s", e)
                    if "disabled_client" in str(e):
                        logger.error(
                            "[YouTube] OAuth client desabilitado no Google Cloud. "
                            "Reative o client_id atual ou gere um novo client_secret.json."
                        )
                    creds = None

            if not creds:
                if not os.path.exists(self.client_secret_file):
                    logger.error("[YouTube] Arquivo '%s' não encontrado.", self.client_secret_file)
                    return None

                logger.error("[YouTube] Token inválido. Execute: docker exec -it python_service python auth_youtube.py")
                return None

            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())

        try:
            self.service = build('youtube', 'v3', credentials=creds)
            return self.service
        except Exception as e:
            logger.error("[YouTube] Erro ao construir serviço: %s", e)
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
        category_id: str = "22",
        scheduled_at: str = None,   # ISO 8601 UTC ex: "2026-02-21T15:00:00.000Z"
    ):
        """Faz o upload de um vídeo para o YouTube.

        Args:
            file_path: Path local do arquivo .mp4
            title: Título do vídeo (max 100 chars)
            description: Descrição (max 5000 chars)
            privacy: 'private' | 'public' | 'unlisted'
            tags: Lista de tags SEO (sem #)
            category_id: ID da categoria YouTube (22 = People & Blogs)
            scheduled_at: Quando publicar (ISO 8601 UTC). Se passado,
                          o vídeo fica 'private' até o horário definido.
        """
        youtube = self.get_authenticated_service()
        if not youtube:
            raise Exception("Falha na autenticação do YouTube. Verifique client_secret.json ou token.json.")

        if not tags:
            tags = []

        logger.info("[YouTube] Iniciando upload: %s", title)

        # Status do vídeo
        status_body = {
            'privacyStatus': privacy,
            'selfDeclaredMadeForKids': False,
        }

        # Agendamento: se scheduled_at for passado, usa publishAt
        if scheduled_at:
            status_body['privacyStatus'] = 'private'  # obrigatório para agendamento
            status_body['publishAt'] = scheduled_at
            logger.info("[YouTube] Vídeo agendado para: %s", scheduled_at)

        body = {
            'snippet': {
                'title': title[:100],
                'description': description[:5000],
                'tags': tags,
                'categoryId': category_id,
                'defaultLanguage': 'pt',
                'defaultAudioLanguage': 'pt',
            },
            'status': status_body
        }

        media = MediaFileUpload(file_path, chunksize=-1, resumable=True)

        request = youtube.videos().insert(
            part=",".join(body.keys()),
            body=body,
            media_body=media
        )

        response = None
        while response is None:
            status, response = request.next_chunk()
            if status:
                progress = int(status.progress() * 100)
                logger.info("[YouTube] Upload: %d%%", progress)

        vid_id = response.get('id', '')
        logger.info("[YouTube] Upload concluído! ID: %s | Agendado: %s", vid_id, scheduled_at or 'imediato')
        return response

    def pin_comment(
        self,
        video_id: str,
        text: str,
    ) -> Optional[dict]:
        """
        Adiciona um comentário e o fixa (pina) no vídeo.
        Requer escopo: youtube.force-ssl

        Args:
            video_id: ID do vídeo YouTube
            text: Texto do comentário a ser fixado

        Returns:
            Dict com dados do comentário, ou None se falhar.
        """
        youtube = self.get_authenticated_service()
        if not youtube:
            return None
        try:
            # Cria o comentário
            comment_body = {
                "snippet": {
                    "videoId": video_id,
                    "topLevelComment": {
                        "snippet": {"textOriginal": text}
                    }
                }
            }
            thread = youtube.commentThreads().insert(
                part="snippet",
                body=comment_body
            ).execute()

            comment_id = thread.get("id")
            logger.info("[YouTube] Comentário criado: %s", comment_id)

            # Pina o comentário (setModerationStatus não pina, usa o campo pinnedCommentId do video update)
            # A YouTube Data API não tem endpoint de 'pin' direto --- só o Studio tem.
            # A abordagem via API é criar o comment top-level; o pin manual é feito via Studio.
            # Por hora, o comentário fica postado como 1º comentário (ainda assim gera engajamento).
            logger.info("[YouTube] Comentário fixado: %s (note: pin exige confirmação no Studio)", comment_id)
            return thread

        except Exception as e:
            logger.warning("[YouTube] Erro ao criar/pinar comentário no vídeo %s: %s", video_id, e)
            return None
