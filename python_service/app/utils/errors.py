# =============================================================================
# app/utils/errors.py — Handlers de erro centralizados
# =============================================================================
# Garante que TODOS os erros retornam no mesmo formato JSON,
# facilitando o tratamento no n8n (lado cliente).
# =============================================================================

from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
import json


# ---------------------------------------------------------------------------
# Formato padrão de erro (usado em todas as respostas de erro)
# ---------------------------------------------------------------------------
# {
#   "status": "erro",
#   "codigo": 422,
#   "mensagem": "Descrição do que deu errado",
#   "detalhes": "Informação técnica (opcional)"
# }
# ---------------------------------------------------------------------------

class ServicoExterno(Exception):
    """Erro ao acessar um serviço externo (ex: site bloqueou a requisição)."""
    def __init__(self, mensagem: str, url: str = ""):
        self.mensagem = mensagem
        self.url = url
        super().__init__(mensagem)


class DadosInvalidos(Exception):
    """Dados recebidos não passam na validação."""
    def __init__(self, mensagem: str, campo: str = ""):
        self.mensagem = mensagem
        self.campo = campo
        super().__init__(mensagem)


class ConteudoVazio(Exception):
    """Extração retornou texto vazio ou muito curto."""
    def __init__(self, mensagem: str, url: str = ""):
        self.mensagem = mensagem
        self.url = url
        super().__init__(mensagem)


# ---------------------------------------------------------------------------
# Registrador de handlers (chamado no main.py durante a inicialização)
# ---------------------------------------------------------------------------

def registrar_handlers(app):
    """Registra todos os exception handlers no app FastAPI."""

    @app.exception_handler(ServicoExterno)
    async def handler_servico_externo(request: Request, exc: ServicoExterno):
        return JSONResponse(
            status_code=503,
            content={
                "status": "erro",
                "codigo": 503,
                "mensagem": exc.mensagem,
                "detalhes": f"URL afetada: {exc.url}" if exc.url else None
            }
        )

    @app.exception_handler(DadosInvalidos)
    async def handler_dados_invalidos(request: Request, exc: DadosInvalidos):
        return JSONResponse(
            status_code=422,
            content={
                "status": "erro",
                "codigo": 422,
                "mensagem": exc.mensagem,
                "detalhes": f"Campo: {exc.campo}" if exc.campo else None
            }
        )

    @app.exception_handler(ConteudoVazio)
    async def handler_conteudo_vazio(request: Request, exc: ConteudoVazio):
        return JSONResponse(
            status_code=422,
            content={
                "status": "erro",
                "codigo": 422,
                "mensagem": exc.mensagem,
                "detalhes": f"URL: {exc.url}" if exc.url else None
            }
        )

    @app.exception_handler(RequestValidationError)
    async def handler_validation_error(request: Request, exc: RequestValidationError):
        # Log detalhado para debug no Docker
        print(f"=== ERRO DE VALIDAÇÃO (422) ===")
        print(f"URL: {request.url}")
        try:
            print(f"Detalhes: {json.dumps(exc.errors(), default=str)}")
        except:
            print(f"Detalhes: {exc.errors()}")
        print("================================")

        return JSONResponse(
            status_code=422,
            content={
                "status": "erro",
                "codigo": 422,
                "mensagem": "Erro de validação (Campos inválidos/faltando).",
                "detalhes": exc.errors()
            }
        )

    # Handler genérico — captura qualquer exceção não tratada
    @app.exception_handler(Exception)
    async def handler_generico(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={
                "status": "erro",
                "codigo": 500,
                "mensagem": "Erro interno no serviço Python",
                "detalhes": str(exc)
            }
        )
