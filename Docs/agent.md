# Agent Guide - Auto Content Factory

> [!IMPORTANT]
> **REGRA MANDATÓRIA (P0):** Você DEVE ler este arquivo (`Docs/agent.md`) e o arquivo `Docs/README.md` no INÍCIO de cada nova tarefa ou sessão. Eles contêm a verdade absoluta sobre a arquitetura e as ferramentas do projeto.

## Missão

Voce e um agente tecnico para manter e evoluir a fabrica autonoma de videos.
Objetivo: operar pipeline 24/7 com alta resiliencia, baixo custo e minimo trabalho manual.

## Estado Atual (2026-02-23)

- **AntiGravity Kit 2.0**: Instalado e ativo (Pasta `.agent`).
- **Awesome Skills Kit**: Biblioteca de +800 habilidades especialistas em `.agent/skills/`.
- Workflow principal: `workflow_producao_v9.json`.
- Orquestracao: n8n.
- Backend: `python_service` (FastAPI).
- Inteligência: Loop de Feedback orgânico via `/social/feedback/` (Groq/Llama), injetando contexto no script.
- Extrator: Bypass local usando `Playwright` nativo no backend via `/extract/` para sites complexos.
- Publicacao Omni-Channel: YouTube, TikTok e Reels (Placeholder) via `POST /publish/multi` usando `platform_overrides`.
- Retenção: Injeções granulares de áudio via SSML (`[PAUSA]`) e mixagem auto de Sound Effects ("swoosh") por `video_engine.py`.
- **Modelo Principal**: `qwen2.5-coder:7b` (Ollama) via `/api/chat`.
- **Agentes Auxiliares**: OpenHands (Execução Autônoma de Tasks).
- **Fallbacks**: Groq (Llama 3.3), Gemini 1.5 Flash, Claude 3 Haiku.

## Servidores MCP Ativos (Ecossistema) 🛠️

O Antigravity está conectado a serviços externos via Model Context Protocol:

- **GitHub**: Gestão de repositórios, leitura de docs externas e automação de commits.
- **n8n**: Gestão e orquestração de workflows (via `n8n-mcp`).
- **Supabase**: Backend serverless para logs de sistema, estado de jobs e fallback de banco.
- **Notion**: Destino para roteiros gerados, checklists de produção e planejamento.
- **Sequential Thinking**: Protocolo de raciocínio profundo para resolução de bugs complexos.
- **Awesome Skills**: Mais de 800 habilidades otimizadas + **Skills Customizadas do Projeto** (`#n8n_expert`, `#video_expert`).

## Ferramentas AntiGravity Kit 2.0 🚀

O projeto agora conta com recursos avançados de IA para automação extrema:

### Comandos de Terminal (Slash Commands)

- `/agents`: Ativa o guia de orquestração específico do projeto Auto Content Factory.
- `/brainstorm`: Use para planejar abordagens técnicas complexas.
- `/plan`: Gera um `implementation_plan.md` estruturado.
- `/debug`: Modo de busca sistemática por bugs (Root Cause Analysis).
- `/ui-ux-pro-max`: Criação de UIs modernas e premium.
- `/test`: Criação e execução de suítes de teste (Pytest/Playwright).
- `/status`: Dashboard de progresso do projeto.

### Agentes Especialistas

- `@project-planner`: Arquitetura e planejamento.
- `@orchestrator`: Coordenação de tarefas multi-fase.
- `@debugger`: Especialista em "deep-fixing".
- `@security-auditor`: Auditoria de riscos e segurança.

### Protocolo de Trabalho

1. **PLANEJAMENTO**: Todo trabalho complexo começa com `/plan`.
2. **APROVAÇÃO**: Aguardar o aval do usuário no arquivo de plano.
3. **EXECUÇÃO**: Implementação com atualização constante do `task.md`.
4. **VERIFICAÇÃO**: Documentação final no `walkthrough.md`.

## Padrões de Uso Avançado (Elite Mode) 🧠

Para operar como os 1% melhores usuários do Antigravity:

- **Agentes Paralelos**: Ao realizar mudanças que afetam Backend (Python) e Orquestração (n8n), use janelas de chat separadas (Agentes) para cada contexto, garantindo que as lógicas não se misturem mas se complementem.
- **Auditoria Proativa**: Antes de finalizar qualquer alteração no workflow, use `#n8n_expert` para validar a resiliência do JSON exportado.
- **MCP Bridge**: Utilize o `n8n-mcp` para ler o status de execuções reais no seu servidor e pedir ao agente para corrigir erros sem sair da IDE.
- **Branding-First**: Ao gerar qualquer elemento técnico ou visual, cite a regra: "Referenciar `/inspirations` para garantir estética premium".

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
- **Ciclo de Documentação**: Após o sucesso de qualquer fix ou feature, é obrigatório atualizar:
  1. `Docs/changelog.md`: Breve nota técnica.
  2. `Docs/agent.md` ou `Docs/README.md`: Se o estado ou arquitetura mudou (ex: novo endpoint).
  3. `walkthrough.md` (via kit): Prova técnica visual/logs da mudança.

## Protocolo de Diagnóstico e Verificação (Obrigatório)

Antes de considerar uma tarefa concluída:

1. **Logs**: Verifique os logs reais (`docker logs python_service` ou `python_service_logs.txt`). Não assuma que o código funciona só porque não deu erro de lint.
2. **Ambiente**: Valide variáveis no `.env` se houver erro de conexão ou API.
3. **Database**: Se mexer em modelos, valide o schema no Postgres via ferramenta de banco.

## Padrões de Design e UX (Standards de Elite)

Ao criar interfaces ou templates visuais:

- **Purple Ban**: PROIBIDO o uso de tons de roxo/violeta como cor primária (regra estética do projeto).
- **Anti-Cliché**: Evitar layouts genéricos de "Admin Dashboard". Buscar estética premium, moderna e dinâmica.
- **Glassmorphism/Dark Mode**: Priorizar designs que pareçam produtos de alta tecnologia de 2025.

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
