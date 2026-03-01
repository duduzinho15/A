# Auto Content Factory (IA + Automação)

> [!IMPORTANT]
> **REGRA MANDATÓRIA (P0):** Você DEVE ler este arquivo (`Docs/README.md`) e o arquivo `Docs/agent.md` no INÍCIO de cada nova tarefa ou sessão para entender o estado atual do projeto e as ferramentas disponíveis.

![CI/CD: Active](https://img.shields.io/badge/CI%2FCD-Active-brightgreen)
![Build: Passing](https://img.shields.io/badge/Build-Passing-brightgreen)

- **Repositório:** [https://github.com/duduzinho15/A](https://github.com/duduzinho15/A)
- **OLLAMA_MODEL**: `qwen2.5-coder:7b` (Alta qualidade narrativa + estabilidade JSON).

Plataforma automatizada para coleta, análise, geração e publicação de vídeos usando IA, com orquestração no n8n e processamento central no `python_service`.

## Visão Geral

Fluxo principal omni-channel integrado com feedback orgânico em loop:

`Audiência (Comentários) -> [LLM Analysis] -> Prompt IA -> FreshRSS -> n8n -> Python Service -> Mídia (com retração SFX e micro-pausas) -> Multi-plataforma (Shorts, TikTok, Reels)`

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
- `openhands`: agente de IA autônomo para engenharia (Porta 3000)
- **MCP Servers**: GitHub, Supabase, Notion, Sequential Thinking (Protocolo de IA)
- **Awesome Skills**: Kit de +800 habilidades especialistas (Pasta `.agent/skills`)

## Workflow de Produção

Arquivo principal:

- `workflow_producao_v9.json`

Pontos importantes da versão v9 (e atualizações de resiliência):

- triagem com IA antes da geração
- criação e acompanhamento de job (`/jobs`)
- **Resiliência Avançada (2º Ciclo Audit)**:
  - **Loop Breaker Ativo**: Máximo de 40 tentativas (aprox. 20min) no Render antes de marcar timeout.
  - **Sincronização de Erros**: Falhas no Render ou Publisher são reportadas via `POST /dashboard/sync` com status `ERROR`.
  - **Network Retry**: `Proxy RSS` configurado com 3 retentativas automáticas para evitar quedas por instabilidade.
  - **Alertas Interativos**: Telegram conta agora com botões de "Re-tentar Job" direto na notificação de erro.
- marcação explícita de timeout no job e reset de jobs stuck (>1h)
- publicação multicanal via `/publish/multi`
- conexões dos nós paralelos corrigidas para evitar skips (alwaysOutputData + continueOnFail)

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
- no workflow v9 isso está explícito no node `Publica Multi`.

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

- **Publicação TikTok Integrada**: Utiliza o motor de upload **[haziq-exe/TikTokAutoUploader](https://github.com/haziq-exe/TikTokAutoUploader)** via script bridge `app/upload_tiktok_haziq.py`.
- **Phantomwright Stealth Engine**: Bypass avançado de bot detection e captchas via IA e fingerprinting dinâmico.
- **Fix Crítico Docker**: Necessário `shm_size: 2gb` no `docker-compose.yml` para evitar crash do Chromium no TikTok Studio (página pesada).
- **Fallback**: Se o upload automatizado falhar, o workflow n8n envia os arquivos via Telegram para postagem manual.

Autenticação por cookies:

- `/data_midia/tk_haziq_cookies_futebas_oficial.json` (Playwright JSON format).
- Use `convert_cookies.py` para converter de Netscape/JSON de extensão para o formato do Playwright.

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
- OpenHands: `http://localhost:3000`

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

### 🐛 Dica de Debug (Novo)

Agora você pode usar o painel **Run and Debug** do editor para rodar o FastAPI localmente ou executar testes individuais sem depender do Docker para cada pequena mudança. Veja o [guia de debug](file:///C:/Users/Usuario/.gemini/antigravity/brain/841d890f-ad00-47cd-a2ce-0e58412b930d/walkthrough_debug.md).

## Operação e Debug

Logs do backend:

```bash
docker logs -f python_service
```

Status dos containers:

```bash
docker compose ps
```

## Estado Atual (2026-02-20) — v10

- Infra principal operacional (docker-compose com 10+ serviços)
- Workflow **v9** como produção oficial
- Publicação YouTube integrada com agendamento nos horários de pico (12h/18h/21h BRT) e comentário fixado automático
- Publicação TikTok via uploader CLI com fallback para Telegram
- **v11 — Inteligência Visual e Semântica (Fase 2):**
  - **Triple Filtragem**: Whitelist de domínios + Filtro de Relevância + **CLIP Visual Gate** (validação semântica local).
  - **IA Roteirista v11**: Vídeos de 60s, roteiros narrativos com dados factuais de placar e estádio.
  - **Edição Avançada**: Scoreboard dinâmico, Smart Crop 9:16 e estabilização de legendas word-by-word.
- **v12.6 — Expansão Global & Tradução:**
  - **Rede de 36 Canais**: Monitoramento automático de Fabrizio Romano, Sky Sports, TyC, Bundesliga, etc.
  - **AI Translation Bridge**: Endpoint nativo que traduz transcrições internacionais para PT-BR preservando terminologia esportiva.

- **v10 — ~40 features gratuitas implementadas:**

### ✅ ai.py v2.0 (Roteiro)

- Persona de narrador configurável: fanático / raiz / analítico
- Estrutura AIDA (Atenção → Interesse → Desejo → Ação)
- Open Loop (pergunta no início respondida no final)
- Chain-of-thought antes do JSON de saída
- Campos: `keywords_visuais`, `quote`, `tipo_noticia`, `mood`
- Padrão de título forçado (número / pergunta / CAPS)
- Data Storytelling: números → metáforas narrativas
- Modelo upgrade: llama3.2 → **qwen2.5-coder:7b** (Ollama local, otimizado para narrativa e JSON)
- Chamada via **Chat API** (api/chat) para suporte completo a System Prompts e Persona
- Google Trends integrado via pytrends (gratuito) como contexto do prompt
- Migração completa de `print()` → `logging`

### ✅ audio.py v2.0 (Áudio)

- SSML gerado automaticamente: `<emphasis>` em palavras CAPS, `<break>` após pontuação
- Prosody por estilo: `fast` para Shorts, `+8%` pitch para urgente
- Auto-trim de silêncios via pydub (remove dead air do TTS)
- Vozes múltiplas por estilo: AntonioNeural (news) / FranciscaNeural (urgent)
- Migração completa de `print()` → `logging`

### ✅ video_engine.py (Novas Funções)

- `reject_placeholder_urls()` — filtra dummyimage.com e afins; integrado no pipeline
- `score_clip_relevance()` — pontua B-rolls por keywords visuais do roteiro
- `fetch_youtube_cc()` — busca vídeo Creative Commons via yt-dlp (gratuito)
- `add_lower_third()` — banner dinâmico na base do frame (primeiros 5s)
- `add_end_screen()` — overlay "Siga o Futebas" nos últimos 3.5s
- `add_teaser_intro()` — preview de 2s do clipe mais dinâmico no início
- `apply_color_grading()` — tonalidade por mood (Epic/Happy/Rock/Sad) via PIL
- Pipeline integra `quality_gate.py` após o render (score 0-100 logado)
- Payload passa `keywords_visuais` e `mood` do roteiro para o motor de vídeo

### ✅ image.py v2.0 (Thumbnail)

- `face_crop_thumbnail()` com mediapipe: crop centrado no rosto detectado
- Fallback: crop central inteligente por aspect ratio
- Fonte Montserrat ExtraBold (com fallback DejaVu Bold)
- Logo watermark no canto superior direito
- Variante 9:16 gerada automaticamente para Shorts
- Migração completa de `print()` → `logging`

### ✅ publish.py (Publicação)

- `get_peak_hours_schedule()` — agendamento automático: 12h/18h/21h BRT
- Comentário fixado (CTA) após upload via `pin_comment()`
- Migração completa de `print()` → `logging`

### ✅ youtube.py (Upload)

- Parâmetro `scheduled_at` (ISO 8601 UTC) para publicação agendada
- Campos SEO: `defaultLanguage: pt`, `defaultAudioLanguage: pt`
- Novo método `pin_comment()` — cria comentário top-level com CTA
- Migração completa de `print()` → `logging`

### ✅ Novos Módulos

- `services/quality_gate.py` — checklist pré-publicação (vídeo + metadata), score 0-100
- `services/trends.py` — Google Trends via pytrends, sem API key

### ✅ requirements.txt

- Adicionados: `pytrends>=4.9.0`, `mediapipe>=0.10.9`
