# Auto Content Factory (IA + Automação)

![CI/CD: Active](https://img.shields.io/badge/CI%2FCD-Active-brightgreen)
![Build: Passing](https://img.shields.io/badge/Build-Passing-brightgreen)

- **Repositório:** [https://github.com/duduzinho15/A](https://github.com/duduzinho15/A)

Plataforma automatizada para coleta, análise, geração e publicação de vídeos usando IA, com orquestração no n8n e processamento central no `python_service`.

## Visão Geral

Fluxo principal:

`FreshRSS -> n8n -> Python Service -> mídia -> publicação`

### Troubleshooting Comum

- **Loop no Wait for Job**: Cheque logs Python para "render" ou "timeout". Mate job manual no banco se travado.
- **JSON Invalid**: Use modo Parameters em HTTP Request para expressões complexas.

### Erro "Resource not found" no Log Execution

- Causa comum: URL do webhook usando nome de container (`n8n:5678`) em vez de localhost.
- Correção: Sempre use `http://localhost:5679/webhook/<ID>` para chamadas internas do n8n.

### Troubleshooting Nós Não Executados

- Causa comum: Branches paralelas (assets) sem conexão do nó anterior.
- Fix: Arraste linha de "Definir Prioridade" ou "Extrai Midias" para todos os nós de API (Brave, Serper, etc.).
- Sempre adicione continueOnFail: true em HTTP Request para APIs externas.

O pipeline foi desenhado para operação contínua (24/7), com foco em:

- automação total (zero cliques no fluxo principal)
- IA local por padrão, com fallback para APIs externas
- controle de estado no Postgres (idempotência e retomada)
- observabilidade e resiliência (timeouts, retries e healthchecks)

## Arquitetura

Serviços principais do `docker-compose.yml`:

- `freshrss`: coleta de feeds
- `rss-bridge`: conversão de fontes para RSS
- `n8n`: orquestração do workflow
- `python_service`: API FastAPI para extração, IA, mídia e publicação
- `postgres`: estado de jobs e persistência
- `flaresolverr`: fallback para extração em sites protegidos
- `ollama`: LLM local
- `kokoro`: TTS local
- `dozzle`: monitoramento de logs
- `searxng`: busca federada auxiliar

## Workflow de Produção

Arquivo principal:

- `workflow_producao_v9.json`

Pontos importantes da versão v8:

- triagem com IA antes da geração
- criação e acompanhamento de job (`/jobs`)
- lógica de loop breaker (máx. 20 tentativas) corrigida com saída OR
- marcação explícita de timeout no job e reset de jobs stuck (>1h)
- publicação multicanal via `/publish/multi`

### Dica de Expressões no Publica Multi

- Sempre use `$if($node["Nome"].isExecuted, valor, fallback)` para nós em branches paralelas.
- Prefira modo **Parameters** ("Using Fields") em HTTP Request quando há muitas expressões complexas.

### Evitar Skips em Branches Paralelas (Ordem de Execução n8n)

- n8n processa left-to-right/top-to-bottom — use Merge Append + Always Output Data = true para esperar todos.
- Aplicado em: `Merge Contexto Roteiro`, `Merge Assets`, `Merge Suggest`.
- Para sub-cadeias seriais (ex: A → B → C em paralelo): Continue On Fail = true em todos + Set após Merge para forçar output.
- Teste: Execute Merge isolado → output tem dados de todos branches.

## API do Python Service

Swagger:

- `http://localhost:8000/docs`

Endpoints principais:

- `POST /extract/`
- `POST /ai/analyze`
- `POST /ai/decide`
- `POST /ai/script`
- `POST /ai/metadata`
- `POST /audio/`
- `POST /image/generate`
- `POST /image/thumbnail`
- `POST /video/render`
- `POST /jobs/`
- `PATCH /jobs/{job_id}`
- `GET /jobs/{job_id}`
- `POST /publish/multi`

## Publicação

### YouTube

- **Status**: ✅ Concluído
- **Endpoint**: `/publish/youtube` (isolado) + `/publish/multi`
- **Retries**: 5 tentativas com backoff exponencial (4–60s) para erros transitórios (quota 429, rede).
  - Exceção original propagada (`reraise=True`) para facilitar debug.
- **Privacidade Padrão**: `private` (configurável via env `YOUTUBE_DEFAULT_PRIVACY`).

A publicação no YouTube é feita pelo endpoint `POST /publish/multi` quando `platforms` inclui `youtube`.

Modo atual de testes:

- publicação em `private` para validar qualidade do vídeo e metadados antes de abrir para público;
- no workflow v8 isso está explícito no node `Publica Multi`.

Pré-requisitos:

- `client_secret.json` / `credentials.json` válidos
- `token.json` gerado para a conta de publicação

Diagnóstico rápido no container:

```bash
docker exec python_service python /app/test_youtube_auth.py
```

Se retornar `disabled_client`, o bloqueio é externo (Google Cloud):

1. Reative o OAuth Client ID atual no projeto GCP, ou gere novo `client_secret.json`.
2. Refaça o token com `docker exec -it python_service python auth_youtube.py`.

### TikTok

- **Publicação TikTok Integrada**: `app/routes/publish.py` utiliza script customizado `tiktok_custom_uploader.py` para invocar biblioteca `TiktokAutoUploader` (função nativa), contornando limitações do CLI.
- **Correção de Biblioteca**: `tiktok.py` patchado para usar User-Agent fixo e indentação correta.
- **Documentação Técnica**: Ver `Docs/tiktok_integration.md`.
- **Fallback**: Se o upload falhar, o workflow n8n captura o erro e envia notificação no Telegram com link para post manual.

Autenticação por cookies:

- `./data/midia/cookies_tiktok.txt` (montado em `/data_midia/cookies_tiktok.txt`)
- fallback: `./data/cookies_tiktok.txt` (montado em `/app/cookies_tiktok.txt`)

O backend converte automaticamente export de cookies (Netscape/JSON) para o formato interno do uploader.

Diagnóstico rápido no container:

```bash
docker exec python_service python /app/test_tiktok_auth.py
```

## Como Subir o Projeto

1. Configure variáveis no `.env`.
2. Garanta Docker + Docker Compose instalados.
3. Suba os serviços:

```bash
docker compose up -d --build
```

Acessos locais:

- FreshRSS: `http://localhost:8080`
- n8n: `http://localhost:5679`
- Python API (Swagger): `http://localhost:8000/docs`
- Dozzle: `http://localhost:8888`
- SearXNG: `http://localhost:8081`

## Como Importar o Workflow no n8n

1. Abra `http://localhost:5679`.
2. Crie ou limpe o workflow de produção antigo.
3. Importe `workflow_producao_v9.json`.
4. Configure credenciais dos nós externos (ex.: Brave/Serper/Tavily quando aplicável).
5. Ative o workflow.

## Qualidade e Testes

No `python_service`, execute:

```bash
docker exec python_service sh -lc "cd /app && PYTHONPATH=/app pytest -q"
```

Para validar somente publicação:

```bash
docker exec python_service sh -lc "cd /app && PYTHONPATH=/app pytest -q tests/test_publish.py"
```

### ✅ 4. Robustez na Extração de Notícias

- **Google News Decoder V4**: Sistema híbrido para resolver links "news.google.com":
  - **Nível 1**: Requests com Headers (para redirects simples).
  - **Nível 2**: RPC BatchExecute (protocolo interno do Google).
  - **Nível 3**: FlareSolverr (bypass de Cloudflare/Consent simples).
  - **Nível 4 (Final)**: **Playwright Headless** (navegador real para resolver redirects complexos de JavaScript).
- Endpoint unificado: `POST /extract/` lida automaticamente com a decodificação antes de extrair o texto.

## Operação e Debug

Logs do backend:

```bash
docker logs -f python_service
```

Status dos containers:

```bash
docker compose ps
```

## Estado Atual

- Infra principal operacional
- Workflow v8 com controle de timeout/retry e conexões corrigidas
- Publicação YouTube integrada
- Publicação TikTok via uploader CLI com fallback para Telegram
- CI/CD e suíte de testes em evolução contínua
