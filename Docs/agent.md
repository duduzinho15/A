# Agent Guide - Auto Content Factory

## Missao

Voce e um agente tecnico para manter e evoluir a fabrica autonoma de videos.
Objetivo: operar pipeline 24/7 com alta resiliencia, baixo custo e minimo trabalho manual.

## Estado Atual (2026-02-14)

- Workflow principal: `workflow_producao_v6_timeout.json`.
- Orquestracao: n8n.
- Backend: `python_service` (FastAPI).
- Publicacao: YouTube e TikTok via `POST /publish/multi`.
- TikTok uploader: operacional via CLI (`TiktokAutoUploader`) com conversao automatica de cookies.
- Infra: Docker Compose com FreshRSS, RSS-Bridge, n8n, Python Service, Postgres, FlareSolverr, Ollama, Kokoro, Dozzle e SearXNG.

## Arquitetura (alto nivel)

FreshRSS/RSS -> n8n -> Python Service -> Geracao de midia -> Publicacao -> Atualizacao de status no Postgres.

## Regras de Arquitetura

- n8n apenas orquestra; evitar mover logica pesada para nodes do workflow.
- LLM, extracao, audio, video, publish e estado devem ficar no `python_service`.
- Priorizar idempotencia e recuperacao de falhas.
- Toda alteracao de fluxo deve preservar timeout/retry e observabilidade.

## Endpoints Principais

- `POST /extract/`
- `POST /ai/analyze`
- `POST /ai/decide`
- `POST /ai/script`
- `POST /ai/metadata`
- `POST /audio/`
- `POST /image/generate`
- `POST /image/thumbnail`
- `POST /video/render`
- `POST /jobs/`, `PATCH /jobs/{id}`, `GET /jobs/{id}`
- `POST /publish/multi`

## Publicacao TikTok (regras operacionais)

- Cookies aceitos em:
  - `/data_midia/cookies_tiktok.txt`
  - `/app/cookies_tiktok.txt`
- O backend converte export de cookies (Netscape/JSON) para o formato interno do uploader.
- Diagnostico rapido:
  - `docker exec python_service python /app/test_tiktok_auth.py`

## Qualidade e Entrega

- Sempre validar compilacao e testes quando alterar backend.
- Para `publish.py`, validar no minimo:
  - teste unitario de sucesso/falha
  - diagnostico TikTok no container
- Atualizar `Docs/changelog.md` em mudancas relevantes.
- Manter docs alinhadas com o estado real do workflow v6.

## Prioridades Atuais

1. Estabilidade do pipeline de producao (timeout, retries, idempotencia).
2. Qualidade de output (roteiro, audio, video, metadata).
3. Robustez de publicacao multi-plataforma.
4. Observabilidade e debug rapido.

## Checklist Antes de Finalizar Mudancas

1. Build do `python_service` concluido.
2. Container `python_service` saudavel (`healthy`).
3. Testes afetados executados.
4. Docs atualizadas (`README`, `estrutura`, `changelog` quando aplicavel).
