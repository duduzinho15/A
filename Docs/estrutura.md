# Estrutura do Projeto - Auto Content Factory (v6)

## Raiz

- `docker-compose.yml`: orquestracao dos containers (freshrss, rss-bridge, n8n, python_service, postgres, flaresolverr, ollama, kokoro, dozzle, searxng).
- `openhands`: Agente CODE (OpenHands) rodando como container satélite (porta 3000).
- `workflow_producao_v9.json`: workflow principal de producao (IA + Automação).
- `python_service/`: backend FastAPI e motor de processamento.
- `n8n_custom/`: workflows auxiliares/customizados.
- `Docs/`: documentacao operacional e handover.
- `data/`: volumes persistentes dos servicos.
- `legacy/`: arquivos antigos preservados para referencia.

## n8n (Orquestracao)

- Workflow principal: `workflow_producao_v9.json`.
- Fluxo principal:
  - Monitora FreshRSS.
  - Faz triagem com IA.
  - Enriquecimento e agregacao de assets.
  - Cria job no `python_service`.
  - Publica em multiplas plataformas via `/publish/multi`.
  - Atualiza status e metadados no banco.
- Controle de resiliencia:
  - polling de job (`/jobs/{id}`), max 20 tentativas.
  - marca timeout quando excede o limite.

## Python Service (Backend)

- Pasta: `python_service/`
  - `Dockerfile`: imagem de execucao (CUDA runtime + Playwright + TikTok uploader).
  - `requirements.txt`: dependencias Python.
  - `test_tiktok_auth.py`: diagnostico de auth/CLI TikTok dentro do container.
  - `test_youtube_auth.py`: diagnostico de auth/API YouTube dentro do container.
  - `app/main.py`: bootstrap da API, routers e healthcheck.

### Rotas da API (`python_service/app/routes`)

- `extract.py`: `POST /extract/`
- `ai.py`: `POST /ai/analyze`, `POST /ai/decide`, `POST /ai/script`, `POST /ai/metadata`
- `audio.py`: `POST /audio/`
- `image.py`: `POST /image/generate`, `POST /image/thumbnail`, `GET /image/models`, `POST /image/options`
- `video.py`: `POST /video/render`
- `jobs.py`: `POST /jobs/`, `PATCH /jobs/{job_id}`, `GET /jobs/`, `GET /jobs/check`, `GET /jobs/{job_id}`
- `media.py`: `POST /media/scorebat`, `POST /media/reddit`
- `enrichment.py`: `POST /enrich/transfermarkt`, `POST /enrich/odds`, `POST /enrich/fixtures`
- `download.py`: `POST /download/`
- `publish.py`: `POST /publish/multi`
- `feedback.py`: `POST /feedback/loop`, `POST /feedback/optimize_prompt`

### Servicos (`python_service/app/services`)

- `audio.py`: pipeline TTS com fallback.
- `video_engine.py`: geracao de video em background.
- `subtitles.py`: geracao de legendas.
- `youtube.py`: upload no YouTube.
- `google_news.py`: decodificador de URLs do Google News (RPC + Playwright).
- `playwright_decoder.py`: serviço headless para resolução de redirects complexos.

### Utilitarios (`python_service/app/utils`)

- `database.py`: conexao e inicializacao do Postgres.
- `errors.py`: erros padronizados da API.
- `assets.py`: bootstrap/download de assets.
- `flaresolverr.py`: cliente para bypass de Cloudflare via FlareSolverr.

## TikTok Uploader (estado atual)

- Implementado via `publish.py` com CLI do repo `TiktokAutoUploader` clonado para `/app/tiktok_uploader` no container.
- Cookies aceitos em:
  - `/data_midia/cookies_tiktok.txt`
  - `/app/cookies_tiktok.txt`
- Conversao automatica para formato `.cookie` interno (`CookiesDir/tiktok_session-auto.cookie`).
- Diagnostico rapido:
  - `docker exec python_service python /app/test_tiktok_auth.py`

## Dados e Volumes

- Midia compartilhada: `./data/midia` -> `/data_midia`
- FreshRSS: `./data/freshrss`
- n8n: `./data/n8n`
- Postgres: `./data/postgres`
- Ollama: `./data/ollama`

## Documentacao

- `Docs/README.md`: visao geral e operacao.
- `Docs/changelog.md`: historico de mudancas.
- `Docs/agent.md`: regras/guia operacional para agentes.
- `Docs/handover_projeto_fabrica_videos.md`: contexto de transferencia.
