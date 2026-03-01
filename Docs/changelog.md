# Changelog

## [2026-02-28] — Dashboard Migration (v19.0) 🚀

### ⚛️ React & Premium UI

- **Migration Completed**: Dashboard legado (Vanilla JS) substituído por aplicação React + TypeScript + Vite.
- **Design System**: Implementação de Glassmorphism com dark mode, sombras neon e transparências (Tailwind v3).
- **Observabilidade**: Visualização em tempo real da saúde do sistema (Ollama, Postgres, Disco) e logs do agente autônomo.
- **Micro-interações**: Feedback visual fluido e animações de estado via Framer Motion.
- **Integração**: Build optimizado servido diretamente por sub-rota `/dashboard` no FastAPI.

## [2026-02-28] — Observabilidade & Dashboard (v18.0) 📊

### 🖥️ Dashboard Monitoring & Analytics

- **Integração Chart.js**: Gráfico de barras no dashboard reportando status do Video Production Pipeline.
- **Agent Status UI**: Card dinâmico para os status do Autonomous AI Agent (Ollama availability, Uptime, Last run).
- **Activity Log Real-time**: Área visual de *glassmorphism* injetando os logs de execução e triagem local direto do container para a UX do painel.
- **Pooling Inteligente**: Fetching dinâmico via Vanilla JS sem recarregar a interface, mantendo a responsividade do HTML.

### 🐍 Python Service (Log & APIs)

- **Novo Endpoint de Logs**: Desenvolvido `GET /maintenance/logs` capaz de varrer assincronamente o fim (N-lines) do novo rastro `agent.log`.
- **Rastreabilidade**: Módulo interno de logging migrado para FileHandler no Startup Application Event (`main.py`).

### 🧠 Agent Skills Expansion (Fase 4)

- **Web Scraper Tool**: Integrada a biblioteca `duckduckgo-search` (`tool_web_search`) no rol de habilidades do agente. Permite buscas orgânicas na internet para pesquisa autônoma, recuperação de notícias frescas ou checagem de fatos online em tempo real, testado com sucesso via endpoint On-Demand e unit tests.

## [2026-02-27] — Estabilização & Resiliência n8n (v17.1) ✅

### 🤖 Automação n8n (Bug Fixes)

- **Fix 404 Not Found**: Corrigida URL do endpoint de renderização de `/media/render` para `/video/render` no workflow `[03] RENDER`.
- **Fix URL Status**: Atualizada URL de verificação de status de `/media/status/` para `/jobs/` no workflow `[03] RENDER`.
- **Fix 500 Internal Error (n8n resiliency)**: Adicionado nó `Prepare Render Data` no workflow `[02] PROCESSADOR` para garantir que `id` e `script` sejam repassados corretamente, evitando UUIDs "undefined".
- **Data Mapping**: Atualizado o nó `Busca Dados do Lead` no workflow `[03] RENDER` para usar `id` do trigger, garantindo 100% de sucesso na recuperação de dados do banco.

### 🐍 Python Service (Hardening)

- **UUID Validation**: Endpoints `/leads/` e `/jobs/` agora validam se o ID recebido é um UUID válido. Retorna **400 Bad Request** em vez de crashar a query SQL (500 Error).
- **Error Handling**: Adicionado handler explícito para `HTTPException` no `errors.py`, garantindo que erros de validação retornem o status code correto (400/404) para o n8n.
- **Auto-healing [Isolado]**: Chamada assíncrona ao OpenHands comentada temporariamente no `errors.py` para evitar crashes por rede em ambientes onde o serviço não está ativo.

## [2026-02-27] — Agente Autônomo 24/7 (v17.0) 🤖

### 🤖 Autonomous Agent (Zero-Touch)

- **[NEW] `ai_agent.py`**: Background worker baseado em LangChain + Ollama.
- **[NEW] `agent_tools.py`**: Ferramentas de auto-correção, SEO e exportação.
- **Worker Loop**: Sentinel (reativo) e Orchestrator (agendado) via APScheduler.
- **Integração**: Registro automático no startup do FastAPI via `main.py`.

## [2026-02-27] — Fact Guard Anti-Alucinação (v16.1) ✅

### 🛡️ Fact Guard (Ideia #21) — Validação de Roteiros

- **[NEW] `fact_checker.py`**: Serviço de validação pós-geração com 3 camadas:
  - **Camada 1 (Regex):** Extrai e compara placares/nomes da fonte vs roteiro. Detecta placeholders genéricos ("Jogador A").
  - **Camada 2 (LLM):** Groq cross-check factual entre fonte e roteiro.
  - **Camada 3 (Dicionário):** Fuzzy match contra 30+ termos corretos do futebol BR (times, estádios, idioma).
- **Auto-Correção:** Placares errados, termos incorretos e placeholders genéricos são corrigidos automaticamente.
- **Integração em `ai.py`:** Fact Guard injetado no endpoint `/ai/script` após extração de JSON (não-bloqueante).
- **[NEW] `test_fact_checker.py`**: 15 testes unitários — **100% Pass** (0.10s).

### 🤖 Prompt Hardening (Edições manuais do usuário)

- Regra anti-placar genérico no system prompt
- Regra anti-idioma misturado (CRISIS→CRISE, rubbedo→rubro)
- Fix campo "artilheiras" → "artilheiros"

## [2026-02-26] — Business Intelligence & UI (v16.0) 🚀

### 📊 Dashboards & SEO (OpenHands Phase 4)

- **Monitoring Dashboard [IN PROGRESS]**: Gatilho enviado para o OpenHands desenvolver a UI em React.
- **SEO Optimization Loop [PLANNING]**: Planejamento do loop dinâmico de metadados baseado em sentimentos sociais.

### 🐍 Python Service (Estabilização)

- **Social Feedback Search [FIX]**: Implementada e verificada a função `search_social_feedback` em `feedback.py`, resolvendo `ImportError`.

## [2026-02-25] — Controle Total & Analytics E2E (v15.0) ✅

### 📊 Analytics & Monitoramento

- **Novos Endpoints**: criados `/analytics/test-e2e` e `/analytics/audit` para disparo remoto e auditoria de qualidade.
- **Resiliência HTTP**: Migração total para `httpx.AsyncClient` com suporte a timeouts adaptativos e tratamento de respostas textuais do n8n (bypass de erro de parser JSON).
- **Quality Auditor**: Implementação inicial do módulo de auditoria via `gemini-1.5-flash` para analisar roteiro e metadados.

### 🤖 Automação n8n

- **Gatilho Webhook**: Adicionado nó `Webhook Trigger` (`/webhook/buffer-news`) ao Coletor oficial, permitindo ativação manual via Python Service.
- **Conectividade Docker**: Resolvido erro 404/Connection Refused mapeando hostnames internos entre containers.

### 🔧 Fixes e Estabilidade

- **Social Feedback Search**: Implementada a função `search_social_feedback` em `feedback.py`, resolvendo `ImportError` e permitindo que a IA considere o sentimento das redes sociais (Bluesky/Twitter) na criação de roteiros.
- **Fix Importação**: Corrigido `NameError: name 'Dict' is not defined` no `publish.py`.
- **Registro de Rotas**: `analytics_router` incluído no `main.py` do FastAPI.

## [2026-02-26] — Estabilização & Resiliência Sistêmica (v15.1) ✅

### 🤖 Automação n8n (Resiliência de Fluxo)

- **Fix Expressão Resiliente**: Atualizados nós `IA Virality` e `IA Roteiro Master` para usar a sintaxe `$(...)?.json` com encadeamento opcional, permitindo que o workflow continue mesmo se o nó de tradução for ignorado.
- **Fix Remove.bg**: Corrigida a referência do `image_path` no nó `Remove.bg Thumbnail` para buscar dados diretamente da origem (`Busca Leads Pendentes`), evitando falhas por dados não repassados.

### 🐍 Python Service (Bug Fixes)

- **Fix Pydantic Triagem**: Ajustada a lógica de análise de IA para sempre incluir o campo `reasoning` (com fallback para `reason`), evitando erros de validação 500.
- **Fix Endpoint Remove.bg**: Ajustado o endpoint `/image/remove-bg` para aceitar `image_path` como Query Parameter explícito (`Query(...)`), eliminando erros 422 de validação de esquema.
- **Logs de Depuração**: Implementada telemetria aprimorada em tempo real para rastreio de processamento de imagens e análise de IA.

## [2026-02-25] — Resiliência AI & Telegram Callbacks (v14.2) ✅

### 🐍 Python Service (Resiliência)

- **Viral Score Fail-Safe**: Implementada estratégia de fallback multi-provider (Ollama -> Groq -> Gemini -> Claude) no endpoint `/ai/viral-score`.
- **Safe Fallback Central**: Sistema de recuperação total que retorna score neutro (50) em caso de falha de todas as APIs, eliminando erros 503 na triagem.
- **Audit de IA**: Registro detalhado do modelo utilizado e status de sucesso em cada análise de viralidade.

### 🤖 Automação n8n

- **Integração Viral Score**: Nó `IA Virality` adicionado ao workflow `[02] PROCESSADOR` para enriquecer a tomada de decisão no Telegram.
- **Handler de Callbacks [NEW]**: Criado workflow `telegram_callback_handler.json` para processar cliques nos botões "Aprovar" e "Descartar" do Telegram.
- **Feedback Visual**: Botões do Telegram agora respondem com alertas ("Aprovado", "Descartado") e disparam o processamento no backend.

### 🚀 Adicionado (Fase 3: Omni-Channel & Autonomia Orgânica - v12)

- **Feedback Loop**: O endpoint interno `/social/feedback/` envia insights abstraídos por LLM (Groq) como instrução ao gerar scripts no `ai.py` através da variável `fb_ctx`.
- **Publisher Multi-Channel**: Modificado `PublishRequest` para aceitar um dicionário `platform_overrides`, permitindo especificar [Título, Descrição, Hashtags] de forma única para TikTok, Instagram e YouTube Shorts.
- **SSML Pauses Injections**: IA pode emitir o token explícito `[PAUSA]` no script gerado, que é convertido organicamente em `<break time="300ms"/>` pelo módulo `audio.py`.
- **SFX em transições**: O `video_engine.py` armazena e rastreia os instantes dos `crossfades` e aplica/mixa com perfeição clipes de `swoosh` SFX à transição, melhorando a retenção.

### 🔧 Modificado

- `app/routes/publish.py` atualizado para extrair configurações segmentadas, unificando lógica de YouTube e TikTok, e preparando Instagram Rails (`Graph API`).
- Expressão regular em `audio.py` refinada garantindo que a pontuação enfática de CAPS não mascare/destrua a tradução do markdown `[PAUSA]`.
- Logic de fading no `audio_layers` (`video_engine.py`) otimizada para loops perfeitos da mesma trilha curta e ducking unificado.## [2026-02-24] — Integração MCP, Branding & Scraper (v14.0 Final) ✅

### 🛠️ Infraestrutura & MCP

- **Instalação n8n MCP**: Integração total do Antigravity com o n8n local, permitindo listar, ler e sugerir correções em workflows diretamente pelo chat.
- **Ecossistema MCP Expandido**: Configuração de GitHub, Supabase, Notion e Sequential Thinking como ferramentas nativas do agente.
- **Audit de Ferramentas**: Registros técnicos de todos os servidores MCP adicionados ao `agent.md`.

### 🎨 Branding & Identidade (Real Futebas)

- **Audit de Assets**: Identificação da identidade real do canal (Laranja Vibrante/Urbano/Graffiti) via análise da pasta `Assets_Canal_Futebas`.
- **Refatoração da Skill #video_expert**: Substituído estilo Glassmorphism por estética "Urbano/Soccer" para alinhar com o canal.
- **Novos Assets Premium**: Gerados `logo_futebas_urban.png` e `branding_guide_futebas_v2.png` baseados na nova identidade.

### 🕸️ Web Scraping & Performance

- **Post-Mortem Firecrawl Local**: Testada stack completa de 6+ containers; identificada como excessivamente pesada para o ambiente local.
- **Estratégia Light**: Decidido manter o `python_service` como motor principal de extração, priorizando resiliência e baixo consumo de RAM.
- **Lightweight Scraper (Playwright)**: Implementado scraper nativo usando headless Chromium (`playwright_scraper.py`) como sub-serviço de bypass para extrair dados de SPA e sites fortificados (ex: Globo Esporte) sem a sobrecarga do Firecrawl.

## 2026-02-23 — Performance, Controle & Visão (v13.0 Turbo) ✅

### ⚡ Performance & Ingestão

- **v13 Turbo**: `video_engine.py` otimizado com renderização de 8 threads e downloads paralelos (asyncio).
- **Cache de Assets**: Sistema de cache de backgrounds borrados para evitar re-processamento.
- **Auto-Healing**: Workflow n8n que monitora a saúde dos serviços e alerta no Telegram.

### 🎭 Vozes & Controle

- **Personas Narrativas**: Mapeamento dinâmico de vozes para Raiz, Analítico e Fanático no `AudioService`.
- **War Room**: Nó de aprovação/rejeição via Telegram inserido no pipeline do Processador.

### 👁️ IA Sensorial

- **Virality Score**: Endpoint `/ai/viral-score` para prever potencial de visualizações.
- **Vision Engine**: Novo serviço `vision.py` para detecção de lances capitais via NLP sensorial.
- **Social feedback**: Endpoint `/social/analyze-feedback` para sugestão de temas baseada em comentários.

## 2026-02-23 — Expansão YouTube & Tradução (v12.6) ✅

### 🎥 Monitoramento Massivo

- **Rede Global de Canais**: Implementada lista de 36 canais de elite (Fabrizio Romano, Sky Sports, TyC, Bundesliga, etc.) no Coletor [01].
- **Loop Automático**: Substituição de nodes manuais por um motor de loop que percorre IDs via RSS (UC...).

### 🌍 Bypass Idiomático

- **Novo Endpoint `/ai/translate`**: Cadeia de fallback (Ollama -> Groq -> Gemini -> Claude) especializada em léxico de futebol.
- **Integração no Processador [02]**: Detecção automática de idioma e tradução em tempo real antes da roteirização.

## [v14.1.0] - Matrix Expansion & Test-Drive

- **News Matrix (Collector v2):** Expandida a coleta com feeds de elite independentes do FreshRSS (SkySports, The Athletic, Marca, Fabrizio Romano, UOL, ESPN, Globo Esporte, Itatiaia).
- **Tradução Nativa:** O bypass idiomático do Gemini (Processador) agora abrange KBs internacionais com tradução implícita on-the-fly.
- **n8n Workflow:** Implementado `[01] COLETOR - Buffer de Notícias v10.json` com matriz redundante baseada em nós Code nativos.

## [v14.0.0] - The Autonomous Editor Updater (Haziq-exe) ✅

### 🎬 Upload Automatizado Confirmado

- **Migração para `TikTokAutoUploader`**: Biblioteca `haziq-exe/TikTokAutoUploader` com `Phantomwright` (stealth anti-bot) agora operacional.
- **Fix Crítico**: `shm_size: '2gb'` adicionado ao `docker-compose.yml` — o Chromium crashava com 64MB de `/dev/shm` (padrão Docker).
- **Pipeline de Cookies**: Script `convert_cookies.py` converte cookies do formato extensão de navegador para formato Playwright.
- **Script de Upload Robusto**: `diag_tiktok.py` com retry, waits adaptativos e screenshots em cada fase.
- **Patch de Caminhos**: `patch_tiktok_haziq.py` redireciona cookies para `/data_midia/` e corrige permissões.
- **Resultado**: Screenshot final confirma **"✓ Video published"** no TikTok Studio.

## 2026-02-21 — Fase 2 (v11): Inteligência Visual e Semântica

### 👁️ Filtragem Visual Tripla (Visual Gate)

- **Nível 1 (Domínio)**: Implementada whitelist de 50+ portais esportivos (ge.globo, marca, espn, etc.) no workflow n8n para restringir fontes.
- **Nível 2 (Relevância)**: Inclusão de operadores de exclusão (`-praia -turismo`) em todos os nós de busca.
- **Nível 3 (Semântica CLIP)**: Novo serviço `visual_gate.py` integrado ao `video_engine.py`. Usa o modelo CLIP (OpenAI) para validar se a imagem baixada realmente contém futebol/jogadores antes da renderização.

### 🤖 IA Roteirista e Fatos (v11)

- **Expansão de Duração**: Prompt ajustado para gerar ~150-200 palavras (vídeos de ~60 segundos).
- **Dados Factuais**: Novos campos no JSON: `placar`, `gols`, `artilheiras`, `estadio`.
- **Narração**: IA agora obrigatoriamente narra o resultado do jogo no bloco de contexto/dados.

### 🎥 Edição e Estabilidade (v11)

- **Scoreboard Overlay**: Implementado componente dinâmico que exibe o placar no topo do vídeo (3.5s - final).
- **Legendas Word-by-Word (Fix)**: Corrigida política de segurança do ImageMagick (`policy.xml`) e variáveis de ambiente no container (`HOME=/tmp`) para garantir a renderização das legendas silenciadas no Víeo #2.
- **Smart Crop**: Otimizado o crop de vídeos raw e imagens estáticas usando `OpenCV Haar Cascades` nativo para centralização inteligente de rostos em vídeos formato 9:16.

## [2026-02-23] - Upgrade de Infraestrutura (MCP)

### Adicionado

- Instalação e configuração dos MCP Servers: **GitHub**, **Supabase**, **Notion** e **Sequential Thinking**.
- Guia de configuração de tokens de integração para Notion (`walkthrough_notion.md`).
- Instalação do- **Awesome Skills**: Mais de 800 habilidades otimizadas + **Skills Customizadas do Projeto** (`#n8n_expert`, `#video_expert`).
- **Firecrawl**: Decisão técnica de usar `python_service` nativo + Scrapers simplificados em vez da stack completa via Docker (para economia de recursos).
- Documentação atualizada em `agent.md` e `README.md` refletindo novas capacidades de IA.

## 2026-02-21 — Otimização de Busca (Tarefa S7)

### 🤖 IA e Busca de Mídia (n8n)

- **IA Roteiro Master**: Adicionado suporte ao campo `keywords_busca` (máx. 3 palavras).
- **Parse Roteiro**: Fallback de segurança para `keywords_busca` ("futebol brasil").
- **Media Search**: Brave Images, Serper, SearXNG e Brave Web agora usam o termo otimizado da IA com fallback para o título.

## 2026-02-20 — FASE 1: Estabilidade, Qualidade e IA Aprimorada

### 🗄️ Etapa 1 — Banco de Dados e Logging (`database.py`)

- **Coluna `ai_log` (JSONB)**: adicionada em `CREATE TABLE IF NOT EXISTS` e em `ALTER TABLE ... ADD COLUMN IF NOT EXISTS` para compatibilidade retroativa. Armazena log de todas as chamadas LLM por job (endpoint, modelo, timestamp, preview do prompt/resposta, status de sucesso).
- **Coluna `scheduled_at` (TEXT)**: armazena horário de publicação agendada para integração com o YouTube scheduler.
- **Colunas geradas `youtube_id` / `tiktok_id`**: extraem IDs de plataforma de `metadata_post` para consultas SQL diretas.
- **Logging**: todos os `print()` substituídos por `logging.getLogger("db")` com suporte a nível e timestamp visíveis no Dozzle.

### 🤖 Etapa 2 — Refinamento de IA e Prompts (`ai.py`)

- **Persona configurável**: parâmetro `persona` aceita `fanático` | `raiz` | `analítico` e adapta tom da narração.
- **Títulos padrão virais**: formato enforçado (`"Chocante! [X] — O que ACONTECEU?"`) para maximizar CTR.
- **`save_ai_log()`**: nova função que persiste payload LLM (endpoint, modelo, prompt, resposta, sucesso) no banco de dados. Integrada nos endpoints `/ai/script` e `/ai/metadata`.
- **Rastreamento de modelo**: `model_used` registra qual LLM foi utilizado em cada chamada (Ollama/Gemini/Claude).
- **`job_id` extraído do contexto**: o `job_id` é extraído do campo `context` enviado pelo n8n para linkar o log ao job correto.

### 🎵 Etapa 3 — Tratamento de Mídia

#### `services/audio.py` — SSML Integrado

- **`build_ssml()`**: converte texto limpo em envelope SSML W3C com:
  - `<emphasis level="strong">` em palavras CAPS (≥ 3 letras)
  - `<break time="350ms"/>` após pontos; `150ms` após vírgulas; `500ms` após reticências
  - `<prosody rate="fast">` para estilo `shorts`; `pitch="+8%"` para `urgent`
- **Fallback automático**: se SSML falhar, o serviço tenta novamente com texto simples sem quebrar o pipeline.
- **Voz customizável**: `AntonioNeural` (padrão), `FranciscaNeural` (urgência).
- Todos os `print()` → `logging.getLogger("audio_service")`.

#### `utils/assets.py` — Filtro de Placeholders

- **`is_placeholder_url()`**: detecta por domínio URLs de serviços de placeholder (dummyimage.com, via.placeholder.com, picsum.photos e outros 7).
- **`filter_valid_urls()`**: filtra lista de URLs e loga quantas foram rejeitadas.
- Todos os `print()` → `logging.getLogger("assets")`.

### 🎬 Etapa 4 — Video Engine: Lower-Thirds e Thumbnails

- **`add_lower_third()`** (`services/video_engine.py`): já existente — confirmado integrado em `generate_video()` (linha 1268). Exibe banner semitransparente por 5s a partir de t=1.0s, texto de `payload["lower_third"]` ou título do vídeo como fallback.
- **`gerar_thumbnail()`** (`routes/image.py`): já existente — confirmado completo com:
  - Face detection (MediaPipe) para crop inteligente centrado no rosto
  - Overlay escuro na base para legibilidade
  - Fonte Montserrat ExtraBold 90px com borda preta (5px stroke)
  - Logo watermark no canto superior direito
  - Variante 9:16 (1080x1920) gerada automaticamente para Shorts
- `print()` residuais em `gen_sd_api()` → `logger.warning` / `logger.error`.

### ✅ Etapa 5 — Quality Gate Pré-Publicação (`publish.py` + `quality_gate.py`)

- **`quality_gate.py`** já existente e completo com:
  - `check_video_file()`: valida arquivo, duração (15s–90s), resolução 1080×1920, faixa de áudio (RMS > 0.001), tela preta no início (brilho < 5)
  - `check_metadata()`: valida título (não-genérico, 10–100 chars), descrição (≥ 30 chars), tags (≥ 5, obrigatórias: futebas, futebol, shorts)
  - `run_full_quality_gate()`: score 0–100; aprovado se ≥ 60
- **Integrado em `/publish/youtube`**: gate executado antes do `upload_video()`. Se reprovado → **HTTP 422** com `{"error": "quality_gate_reprovado", "score": X, "issues": [...], "warnings": [...]}`.
- **Fail-safe**: se o próprio gate lançar exceção (bug interno), loga warning e prossegue com o upload — prefere publicar sem gate a bloquear por bug.
- Importado `HTTPException` de `fastapi`.
- `print()` residual em `upload_to_tiktok_cli()` → `logger.warning`.

### 📋 Etapa 6 — Documentação

- Nó "Notifica Telegram Manual Post" não encontrado no `workflow_producao_v9.json` (possivelmente renomeado/removido em versão anterior). **Sem alteração no JSON.**
- Este `changelog.md` atualizado com todas as implementações da Fase 1.

---

## 2026-02-19 / 2026-02-20

### 🎥 Diagnóstico e Análise de Qualidade de Vídeo Gerado por IA

- **Análise Comparativa**: Vídeo gerado pela pipeline comparado com referência profissional (YouTube Shorts "São Paulo busca alternativas").
- **Relatório Produzido**: Arquivo `Docs/Retorno da analise do vídeo produzi.txt` com análise detalhada cobrindo: qualidade visual, áudio/TTS, legendas, pacing e call-to-action.
- **Relatório Executivo**: `Docs/relatorio_auto_content_factory.docx` com visão executiva do estado do sistema.
- **Análise Docx**: `Docs/Análise_Detalhada_do_Vídeo_São_Paulo.docx` com pontos de melhoria específicos.
- **Vídeo Referência**: Mantido em `Docs/YTDown.com_Shorts_...mp4` para comparação futura.
- **Objetivo**: Identificar gaps de qualidade no `video_engine.py` (V2) versus produção profissional para orientar próximas iterações.

## 2026-02-17

### 🔄 Fix de Conexões do Workflow V9 (Produção)

- **Problema**: Versão `workflow_producao_v9.json` apresentava conexões quebradas e nós desconectados do fluxo principal após migração do v8.
- **Correção**: Script `fix_workflow_v9.py` executado para restaurar conexões corretas: `Monitora FreshRSS` → `É Novo?` → `Leitor Trafilatura`, reconexão de `IA Triagem` e restabelecimento do fluxo `Job Succeeded?` → `Mark Job Failed`.
- **Verificação**: `verify_connections.py` e `analyze_connections_v2.py` confirmaram integridade do arquivo após fix.
- **Backups**: Gerados automaticamente (`workflow_producao_v9.bak.json` até `bak5.json`) para rollback se necessário.
- **Status**: `workflow_producao_v9.json` confirmado como versão de produção oficial (substituiu v8).

## 2026-02-16

### 🔄 Padronização Workflow V8 (IA + Automação)

- **Mudança**: Adotado `workflow_producao_v8.json` como versão oficial de produção (substituindo v6/v7).
- **Correção**: Script `fix_connections_v8.py` executado para garantir conexões de `ScoreBat`, `Social Scraper`, `Transfermarkt` e `TheSportsDB` ao `Merge Contexto Roteiro`.
- **Documentação**: Atualizados `README.md` e `estrutura.md` com referências ao v8.

### 🔄 Reforço no Merge Contexto Roteiro (Evita Skips em Paralelos)

- **Problema**: n8n processa left-to-right/top-to-bottom → branches paralelos com sub-cadeias seriais (ex: Próximos Jogos → Odds → Agente) quebram se primeiro vazio.
- **Correção**: Mode = Append + Always Output Data = true + nó Set "Force Merge Context" após Merge para juntar dados parciais.
- **Teste**: Merge sempre passa output, IA Roteiro Master executa mesmo com dados incompletos.

### 🔄 Substituição Trigger RSS (Fix Confiabilidade)

- **Problema**: Trigger nativo `Monitora FreshRSS` travava em "Waiting for event" e ignorava feeds existentes.
- **Correção**: Substituído por `Cron (10min)` + `Read RSS Feed` (Action) + Lógica `É Novo?` corrigida para `isNotEmpty`.
- **Benefício**: Execução garantida a cada 10 minutos, sem depender de "push" do RSS.

### 🔄 Fix Loop Infinito e Nós Não Executados (v6 Timeout)

- Causa: Nós paralelos de assets (Brave, Serper, etc.) não conectados ao fluxo principal → Agrupador vazio → Gera Vídeo Híbrido falha → polling sem job_id.

- Correção: Conexões de "Definir Prioridade" → todos os paralelos → Agrupador. Adicionado continueOnFail: true em APIs externas.
- Teste: Workflow manual executado, assets coletados, job criado, polling termina em <10min.

### 🔄 Fix Execução Paralela (Merge Assets)

- **Problema**: Nós paralelos de assets (Brave, Serper, etc.) não executavam ou Merge Assets travava esperando "todos".
- **Causa**: Falta de `alwaysOutputData: true` nos nós paralelos, fazendo com que falhas ou skips impedissem o Merge de completar a contagem de inputs.
- **Correção**: Script `fix_parallel_execution_v8.py` aplicou `alwaysOutputData: true` e `continueOnFail: true` em TODOS os nós de assets.
- **Reinforce**: `Merge Assets` garantido como `mode: append` e `alwaysOutputData: true`.
- **Arquitetura**: Adicionado nó `Broadcast Hub` (Set) entre `Parse Roteiro` e paralelos para forçar distribuição de fluxo (fix race condition).
- **Index Standardization**: `Merge Assets` inputs movidos para `Index 1` (Input 2) para espelhar o comportamento funcional do `Merge Contexto Roteiro`. Expressões atualizadas para usar `$json` (limpo) ao invés de buscar nó avô.
- **Publish Timeout**: Aumentado timeout do nó `Publica Multi` para 15 minutos (evitar erro de "Falha em todas as plataformas" em uploads lentos). Lógica de sucesso atualizada para aceitar status `published`.

### 🎥 Video Engine V2 (Profissionalização)

- **Audio Ducking**: Implementado mixagem de áudio com redução de volume da música de fundo (12%) durante a fala (TTS). Fim do áudio com Fade-out suave.
- **Branding & Safe Zone**:
  - Overlay de **Marca D'água** (logo/watermark.png) no canto superior direito.
  - Legendas renderizadas com **Fonte Customizada** (se presente em `assets/fonts`) e posicionadas na **Safe Zone** (bottom 250px) para não conflitar com UI do TikTok.
- **Smart Fallback**:
  - Se o download de imagens falhar, o sistema usa agora um **Loop Padrão** (`assets/defaults/loop.mp4`) ou ColorClip, evitando tela preta e erro de renderização.
- **AI & Script**:
  - Prompt de IA ajustado para garantir roteiros de **30s-45s** (min 80 palavras) e títulos virais sem clickbait falso.
  - Normalização de texto no Audio Service para corrigir pronúncias (ex: "Novorizontino", "Conquista").

### 🛠️ Correção do Nó Log Execution (Webhook URL)

- Erro anterior: "The resource you are requesting could not be found"
- Causa: URL interna `n8n:5678` não resolvida dentro do próprio n8n.
- Correção: Alterado para `http://localhost:5679/webhook/8805f345-6dd0-4fa4-a231-851ca3fbf0af` (porta exposta).
- Teste: Nó executado com sucesso após correção.

### 🔄 Diagnóstico Loop Infinito no Wait for Job

- Causa: Job travado em "processing" no Python (sem logs de render).
- Correção: Validação de attempts no Increment Attempts + PATCH timeout no Mark Timeout.
- Script de Correção: `fix_stuck_processing_jobs.py` adicionado para limpar jobs travados manualmente.
- Teste: Job muda para "timeout" após 20 tentativas.

### 🛠️ Fix Erro "Node 'IA Metadata' hasn't been executed" no Publica Multi

- Causa: Nó IA Metadata em branch paralela não executada.
- Correção: Conexão direta + fallback com $if(isExecuted) na expressão.
- Alternativa: Removido dependência do IA Metadata (usar Parse Roteiro como fallback).
- Teste: Workflow manual executado sem erro no Publica Multi.

### 🛠️ Fix "JSON parameter needs to be valid JSON" no Publica Multi

- Causa: Expressão complexa no campo JSON Body inválida para parser n8n.
- Correção: Mudado para modo Parameters com expressões individuais + fallback $if(isExecuted).
- Alternativa: Nó Code prévio para montar payload JSON.
- Teste: Workflow manual executado sem erro no Publica Multi.

## 2026-02-14

### 📱 TikTok Uploader (v2)

- **Build corrigido**: `python_service/Dockerfile` agora cria compatibilidade de shebang Python entre builder/runtime CUDA e conclui `playwright install`.
- **Dependências TikTok adicionadas**: instaladas libs mínimas do `TiktokAutoUploader` (`fake-useragent`, `requests-auth-aws-sigv4`, `undetected-chromedriver`) e `nodejs/npm` para assinatura JS do upload.
- **Publicação TikTok Integrada**: `app/routes/publish.py` utiliza script customizado `tiktok_custom_uploader.py` para invocar biblioteca `TiktokAutoUploader` (função nativa), contornando limitações do CLI.
- **Correção de Biblioteca**: `tiktok.py` patchado para usar User-Agent fixo (Chrome/Windows) e indentação correta.
- **Documentação Técnica**: Ver `Docs/tiktok_integration.md`.
- **Cookies automáticos**: conversão de `cookies_tiktok.txt` (Netscape ou JSON) para `CookiesDir/tiktok_session-auto.cookie`, com fallback de leitura em `/data_midia/cookies_tiktok.txt` e `/app/cookies_tiktok.txt`.
- **Staging de vídeo para CLI**: o vídeo é preparado em `VideosDirPath` antes do envio para compatibilidade com o validador do uploader.
- **Diagnóstico operacional**: novo script `python_service/test_tiktok_auth.py` para validar cookies, Playwright e CLI diretamente no container.

### 📱 Fallback Telegram para Post Manual (TikTok)

- **Novo Nó no Workflow v6**:
  - Implementado listener de erro no `Publica Multi`.
  - Se TikTok falhar (ou plataforma for `manual`), envia notificação via Telegram Bot.
  - Mensagem contém: Título, Hashtags e Caminho do Vídeo pronto.
- **Configuração**:
  - `TELEGRAM_TOKEN` e `TELEGRAM_CHAT_ID` adicionados ao `docker-compose.yml` e `.env`.
- **Objetivo**: Garantir que nenhum vídeo pronto seja perdido por erro de API, permitindo postagem manual rápida (Zero-Lost).

### 🛠️ Estabilidade de Produção (v3)

- **Loop infinito corrigido no workflow v6** (`workflow_producao_v6_timeout.json`):
  - contador de tentativas agora persiste corretamente entre ciclos (`Wait for Job` -> `Check Job Status` -> `Increment Attempts`);
  - publish só dispara quando `status == completed` (`Job Succeeded?`);
  - jobs sem `completed` agora são marcados via `Mark Job Failed`, sem seguir para publicação;
  - removida execução duplicada de `Gera Vídeo Híbrido` (elimina criação dupla de job).
- **Publicação multi corrigida no workflow**:
  - `Publica Multi` agora envia `job_id`;
  - `Update DB Final` passou a salvar em `metadata_post` (não mais `metadata`) e marcar `published` com base no sucesso real de YouTube/TikTok.
- **GPU MoviePy/NVENC operacional**:
  - `docker-compose.yml`: `NVIDIA_DRIVER_CAPABILITIES=compute,utility,video` e `gpus: all` no `python_service`;
  - `video_engine.py` e `video.py`: render com `h264_nvenc` + fallback automático para `libx264`.
- **Correção de status preso em `processing`**:
  - `video_engine.py` já gravava `error_message` ao falhar, mas a coluna não existia no banco;
  - `app/utils/database.py` agora migra/cria `video_jobs.error_message`, evitando exceção em background task e destravando o polling do n8n.
- **Validação runtime do NVENC**:
  - smoke test `ffmpeg` com `h264_nvenc` executado com sucesso no container.
- **Diagnóstico YouTube adicionado**:
  - novo script `python_service/test_youtube_auth.py` para validar autenticação/canal;
  - `auth_youtube.py` disponibilizado no container para fluxo manual de renovação de token;
  - diagnóstico atual validado em runtime: autenticação OK e canal acessível.
- **Publicação em modo teste (privado)**:
  - `publish.py` agora usa privacidade padrão configurável por `YOUTUBE_DEFAULT_PRIVACY` (default `private`);
  - `workflow_producao_v6_timeout.json` envia `privacy: 'private'` no node `Publica Multi`;
  - TikTok CLI agora respeita privacidade no parâmetro `-vi` (`0` publico, `1` privado).
  - pré-check de sessão TikTok adicionado para evitar traceback opaco e retornar erro claro quando cookies não autorizam upload (`status_code=8`).
  - validação real de upload YouTube concluída com `privacyStatus=private`.

### 📺 YouTube Uploader (Finalização)

- **Endpoint isolado**: `/publish/youtube` criado e testado (vídeo privado e público).
- **Integração**: Completa em `/publish/multi`.
- **Resiliência Aprimorada**:
  - Implementado `tenacity` com **Exponential Backoff** (4s a 60s).
  - 5 tentativas automáticas para erros de rede, 500, 503 e 429 (Quota).
  - `reraise=True`: Exceção original é propagada após falha final para debug claro.
  - Logging detalhado antes de cada retry.
- **Correção de Build**: Re-criado arquivo `overrides/tiktok_uploader/tiktok.py` (hotfix de assinatura/cookies) que estava ausente.
- **Banco de Dados**: `youtube_id` salvo corretamente em `metadata_post`, status atualizado para `published`.
- **Teste End-to-End**: Workflow → render → upload → update banco validado.
- **Validação**: `test_youtube_service.py` passou (inicialização do serviço).

## 2026-02-12

### 🚀 Novas Funcionalidades

- **Pipeline de Áudio Multicamada (v1)**:
  - **Novo** `app/services/audio.py`: Implementado fallback inteligente.
  - Ordem: **Unreal Speech** (Alta Qualidade) -> **Kokoro TTS** (Local/ONNX) -> **Edge-TTS** (Gratuito).
  - Pós-processamento com `pydub` (Normalização + MP3 192kbps).

- **Legendas Automáticas (Burned-in)**:
  - **Novo** `app/services/subtitles.py`: Transcrição via `faster-whisper`.
  - Integração com `video_engine.py` para "queimar" legendas no estilo Shorts (Amarelo, Borda Preta).

- **Resiliência e Idempotência**:
  - **Novo** Controle de duplicidade em `publish.py` (evita re-upload do mesmo `job_id`).
  - Atualização dos metadados de IA para estilo "Viral/Clickbait" (Prompt Refinado).

- **Melhoria Prompt Metadata**:
  - Gancho <3s, Palavras de Poder (URGENTE, BOMBA), Contexto Premier League.
  - Otimizado para Shorts e Viralização.

- **Correções Críticas de Pipeline**:
  - **Idempotência Real**: `jobs.py` agora aceita `source_url` e verifica existência ANTES de criar job.
  - **Filtro de Notícias**: Jobs com `pub_date` > 48h são rejeitados automaticamente.
  - **Duração Mínima**: Prompt de roteiro exige >80 palavras; Aviso no log se áudio < 25s.
  - **Visibilidade**: Default de `publish.py` alterado para `public`.

## 2026-02-11

### 🚀 Novas Funcionalidades

- **IA Central Expandida (v2)**:
  - **Novo** `POST /ai/analyze`: Analisa relevância, categoria e prioridade (High/Medium/Low).
  - **Novo** `POST /ai/decide`: Decide formato (Short/Long), agregação (Solo/Giro) e região.
  - **Novo** `POST /ai/metadata`: Gera títulos, tags e encontra *Trending Sounds* (via Tavily/Serper).
  - **Atualizado** `POST /ai/script`: Inclui Hook (<3s), CTA e prompts visuais.
  - **Sistema de Fallback Robusto**: Ollama → Gemini → Claude.
  - **SEO Integrado**: Otimização específica para Shorts/TikTok.

### 🧪 Testes

- Criada suíte `tests/test_ai.py` (v2).
- Cobertura:
  - Novos endpoints: decide, metadata, script, analyze.
  - Integração mockada com Search Tools (Tavily/Serper).
  - Fallbacks de IA.
- Status: **100% Pass** (6 testes).

### 📂 Arquivos Alterados

- `python_service/app/routes/ai.py` (Adicionado decide, metadata, search tools)
- `python_service/app/config.py` (Adicionado TAVILY_API_KEY, SERPER_API_KEY)
- `python_service/tests/test_ai.py` (Suíte completa)
- `Docs/README.md` e `Docs/agent.md` (Atualizado status)
- **Cleanup**: Movidos arquivos não utilizados (scripts antigos, logs, testes) para a pasta `legacy/`.
- **Estrutura**: Atualizado `Docs/estrutura.md`.

### 🛠️ Correções e Melhorias (2026-02-13 a 2026-02-25)

- **Auditória de Resiliência (2º Ciclo)**:
  - **Motor de Renderização (v2.1)**:
    - Implementado **Controlador de Tentativas** e **Check de Timeout (20min)** para evitar travamentos infinitos.
    - Adicionado nó de **Erro: Timeout Render** para sincronização automática com o dashboard em caso de falha persistente.
  - **Distribuição Social (v2.1)**:
    - Adicionado nó **Sincroniza Erro Dashboard** conectado via branch de erro ao `Publica Multi`.
    - Garantida a rastreabilidade total de falhas na publicação.
  - **Proxy RSS / Flaresolverr**:
    - Ativada política de **Retry Automático** (3x tentativas / 1s delay) no nó `Chama Flaresolverr` para lidar com instabilidades de rede.
  - **ERROR_HANDLER Centralizado**:
    - **Layout Premium**: Alertas em Telegram com Markdown enriquecido.
    - **Interatividade**: Adicionados botões inline para "Ver Dashboard" e "Re-tentar Job" (via callback_id).
    - **Propagação de ID**: Correção na passagem do `job_id` para garantir que o retry manual funcione corretamente.

### 📂 Arquivos Alterados

- `n8n_custom/[03] RENDER - Motor de Produção.json` (Retries e Loop Breaker)
- `n8n_custom/[04] PUBLISHER - Distribuição Social.json` (Error Handling)
- `n8n_custom/00 - Proxy RSS (Via Flaresolverr).json` (Network Resilience)
- `n8n_custom/ERROR_HANDLER.json` (UX de Erro / Callbacks)
- `Docs/README.md` (Documentação de Resiliência)
-   A j u s t e   d e   t i m e o u t   n o   n 8 n   ( L e i t o r   T r a f i l a t u r a )   e   P y t h o n   s e r v i c e   ( G o o g l e   N e w s   /   E x t r a c t )   p a r a   m i t i g a r   e r r o s   E C O N N A B O R T E D 
 
 

## [2026-02-28] — Auto-Audit Report (AI Agent) 🤖

### 🔄 Arquivos Modificados (Últimas 24h)

- `app/main.py`
- `app/routes/extract.py`
- `app/routes/maintenance.py`
- `app/services/agent_tools.py`
- `app/services/ai_agent.py`
- `app/services/google_news.py`
- `tests/test_agent_tools.py`

*Relatório gerado automaticamente pelo motor Orchestrator.*


## [2026-03-01] — Auto-Audit Report (AI Agent) 🤖

### 🔄 Arquivos Modificados (Últimas 24h)

- `app/main.py`
- `app/routes/extract.py`
- `app/routes/maintenance.py`
- `app/services/agent_tools.py`
- `app/services/ai_agent.py`
- `app/services/google_news.py`
- `tests/test_agent_tools.py`

*Relatório gerado automaticamente pelo motor Orchestrator.*


## [2026-03-01] — Auto-Audit Report (AI Agent) 🤖

### 🔄 Arquivos Modificados (Últimas 24h)

- `app/main.py`
- `app/routes/extract.py`
- `app/routes/maintenance.py`
- `app/services/agent_tools.py`
- `app/services/ai_agent.py`
- `app/services/google_news.py`
- `tests/test_agent_tools.py`

*Relatório gerado automaticamente pelo motor Orchestrator.*
