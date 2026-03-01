import os
import logging
from typing import List, Optional
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from app.config import settings

logger = logging.getLogger("google_sheets")

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

class SheetsService:
    def __init__(self):
        self.spreadsheet_id = settings.GOOGLE_SHEETS_ID
        self.token_file = os.path.join("/app", "token_sheets.json")
        self.client_secret_file = os.path.join("/app", "client_secret.json")
        self.service = None

    def get_authenticated_service(self):
        """Autentica e retorna o serviço da API do Google Sheets."""
        creds = None
        if os.path.exists(self.token_file):
            creds = Credentials.from_authorized_user_file(self.token_file, SCOPES)
            
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                logger.error("[Sheets] Token inválido ou não encontrado. Execute o fluxo de autenticação.")
                return None
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())

        try:
            self.service = build('sheets', 'v4', credentials=creds)
            return self.service
        except Exception as e:
            logger.error("[Sheets] Erro ao construir serviço: %s", e)
            return None

    def append_row(self, values: List[any], range_name: str = "Página1!A1") -> bool:
        """
        Adiciona uma nova linha na planilha.
        
        Args:
            values: Lista de valores para a linha.
            range_name: Onde começar a busca pela próxima linha livre.
            
        Returns:
            True se sucesso, False se falha.
        """
        service = self.get_authenticated_service()
        if not service:
            return False
            
        try:
            body = {'values': [values]}
            result = service.spreadsheets().values().append(
                spreadsheetId=self.spreadsheet_id,
                range=range_name,
                valueInputOption="RAW",
                body=body
            ).execute()
            logger.info("[Sheets] Linha adicionada com sucesso: %s", result.get('updates').get('updatedRange'))
            return True
        except Exception as e:
            logger.error("[Sheets] Erro ao adicionar linha: %s", e)
            return False

    def update_row_by_id(self, row_id: str, new_values: List[any], col_range: str = "A:Z") -> bool:
        """
        Busca uma linha pelo ID (coluna A) e atualiza os valores.
        """
        service = self.get_authenticated_service()
        if not service:
            return False
            
        try:
            # 1. Busca todas as linhas da coluna A
            result = service.spreadsheets().values().get(
                spreadsheetId=self.spreadsheet_id,
                range=f"Página1!A:A"
            ).execute()
            rows = result.get('values', [])
            
            row_index = -1
            for i, row in enumerate(rows):
                if row and row[0] == row_id:
                    row_index = i + 1
                    break
            
            if row_index == -1:
                logger.warning("[Sheets] ID %s não encontrado para atualização.", row_id)
                return False
                
            # 2. Atualiza a linha encontrada
            body = {'values': [new_values]}
            service.spreadsheets().values().update(
                spreadsheetId=self.spreadsheet_id,
                range=f"Página1!A{row_index}",
                valueInputOption="RAW",
                body=body
            ).execute()
            logger.info("[Sheets] Linha %d (ID %s) atualizada.", row_index, row_id)
            return True
        except Exception as e:
            logger.error("[Sheets] Erro ao atualizar linha: %s", e)
            return False
