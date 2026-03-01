# Estrutura do Projeto - Auto Content Factory (v13.0 Turbo)

## Raiz

- `docker-compose.yml`: orquestracao dos containers (freshrss, rss-bridge, n8n, python_service, postgres, flaresolverr, ollama, kokoro, dozzle, searxng). **[v13]** `shm_size: 2gb` no python_service.
- `credentials.json`: Credenciais da Google Cloud (YouTube API).
- `token.json`: Token OAuth2 autenticado para upload.
- `python_service/`: backend FastAPI e motor de processamento.
- `n8n_custom/`: **[NOVO v12]** Workflows modulares (Coletor, Processador, Render, Publisher).
- `Docs/`: documentacao operacional e handover.
- `data/`: volumes persistentes dos servicos.
- `legacy/`: **[LIMPEZA]** Pasta contendo +80 arquivos de scripts antigos, versões de workflows (v1 a v9) e testes temporários para manter o root limpo.

## n8n (Arquitetura Modular v12)

O sistema foi modularizado em 4 sub-fluxos principais localizados em `n8n_custom/`:

1. **[01] COLETOR**: Monitora FreshRSS e salva leads brutos no buffer (`/leads`).
2. **[02] PROCESSADOR**: Inteligência v11 (Roteiro, Triagem, Tradução) e busca de assets.
3. **[03] RENDER**: Orquestração assíncrona da renderização via polling.
4. **[04] PUBLISHER**: Agendamento inteligente (Randomizer) e publicação multi-plataforma.

## Python Service (Backend)

- Pasta: `python_service/`
  - `Dockerfile`: imagem de execucao (CUDA runtime + Playwright + TikTok uploader).
  - `requirements.txt`: dependencias Python.
  - `app/main.py`: bootstrap da API, routers e healthcheck.

### Rotas da API (`python_service/app/routes`)

- `extract.py`: `POST /extract/`, `POST /selector` (Cheerio Python), `POST /transcript` (YT Legendas Coletivas).
- `ai.py`: `POST /ai/analyze`, `POST /ai/detect`, `POST /ai/translate`, `POST /ai/script`, `POST /ai/metadata`, `POST /ai/viral-score` (v13).
- `comments.py`: **[NOVO v13]** `POST /social/analyze-feedback` (Análise de engajamento).
- `translate.py`: **[NOVO v12.6]** `POST /ai/translate` (Bypass idiomático internacional).

### Servicos (`python_service/app/services`)

- `video_engine.py`: **[TURBO v13]** Geração de vídeo com paralelo IO e cache de backgrounds.
- `vision.py`: **[NOVO v13]** Detecção de lances capitais via NLP sensorial.
- `visual_gate.py`: **[NOVO v11]** Validação semântica de imagens via CLIP.
- `google_news.py`: decodificador de URLs (RPC + Playwright).
- `quality_gate.py`: checklist pré-publicacao (Score 0-100).
- `trends.py`: integracao com Google Trends (pytrends).

### Utilitarios (`python_service/app/utils`)

- `database.py`: conexao e inicializacao do Postgres. **[v12]** Tabela `news_leads`.
- `assets.py`: bootstrap/download de assets.

- Implementado via `publish.py` usando o motor **haziq-exe/TikTokAutoUploader** (Phantomwright headless).
- Cookies centralizados em `/data_midia/tk_haziq_cookies_futebas_oficial.json`.
- Bridge script: `app/upload_tiktok_haziq.py` (chamado via subprocess).
- Configuração Docker: Exige `shm_size: 2gb` para evitar crash do Chromium no TikTok Studio.

## Dados e Volumes

- Midia compartilhada: `./data/midia` -> `/data_midia`
- Bancos/Logs: FreshRSS, n8n, Postgres, Ollama, Dozzle.

## Documentacao

- `Docs/README.md`: visao geral e operacao.
- `Docs/changelog.md`: historico de mudancas (v11/v12).
- `Docs/agent.md`: regras/guia operacional para agentes.
- `Docs/walkthrough.md`: passoa-a-passo detalhado da Fase 2.5 final.
