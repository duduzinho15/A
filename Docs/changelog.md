# Changelog

## 2026-02-15

### 🔄 Fix Loop Infinito e Nós Não Executados (v6 Timeout)

- Causa: Nós paralelos de assets (Brave, Serper, etc.) não conectados ao fluxo principal → Agrupador vazio → Gera Vídeo Híbrido falha → polling sem job_id.
- Correção: Conexões de "Definir Prioridade" → todos os paralelos → Agrupador. Adicionado continueOnFail: true em APIs externas.
- Teste: Workflow manual executado, assets coletados, job criado, polling termina em <10min.

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

### 📦 Dependências

- Adicionados: `unrealspeech`, `kokoro-onnx`, `soundfile`, `huggingface-hub`, `faster-whisper`.

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

### 🛠️ Correções e Melhorias (2026-02-13)

- **Log Extractor Service**:
  - **Refatoração Zero-Touch**: Migrado para volume persistente `/data_midia/logs`.
  - **Networking**: Corrigido URL do webhook no workflow principal (`http://n8n:5678/...`) para comunicação interna do container.
  - **Docker**: Adicionado `N8N_DIAGNOSTICS_ENABLED=true` e ajustadas permissões (`chown node:node`).
  - **Cleanup**: Removidos workflows duplicados.
- **Resiliência / Timeout**:
  - **Python Service**: Implementado timeout de 300s (5min) na renderização de vídeo (`/video/render`) para evitar travamentos infinitos.
  - **n8n Workflow**: Criada versão `workflow_producao_v6_timeout.json` com lógica de Loop Breaker (Max 20 tentativas / 10min).
