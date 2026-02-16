
PROJETO: FÁBRICA AUTÔNOMA DE VÍDEOS (PIPELINE IA + AUTOMAÇÃO)
STATUS: FASES 2 A 5 CONCLUÍDAS COM TESTES AUTOMATIZADOS APROVADOS

============================================================

1. VISÃO GERAL DO PROJETO
============================================================

Objetivo:
Criar um sistema 100% autônomo e resiliente (24/7) para:

- Coletar notícias (via RSS / FreshRSS / fontes externas)
- Analisar conteúdo com IA
- Gerar roteiro
- Gerar áudio (TTS)
- Gerar mídia visual (imagem + B-roll)
- Renderizar vídeos automaticamente
- Controlar estado, retries e idempotência via banco
- Orquestrar tudo com n8n
- (Fase futura) Publicar em plataformas como YouTube/TikTok

Nenhuma decisão criativa ou lógica fica no n8n.
O n8n apenas ORQUESTRA.
Toda inteligência está no python_service.

============================================================
2. STACK TECNOLÓGICA
============================================================

- Python 3.12+ (atual testado: 3.14)
- FastAPI (python_service)
- MoviePy (renderização de vídeo)
- Pillow (imagens)
- FFmpeg (backend de mídia)
- Postgres (estado, fila e idempotência)
- n8n (orquestração)
- FreshRSS (origem de conteúdo)
- Docker / Docker Compose
- Pytest (testes automatizados)
- Dozzle (monitoramento de logs – planejado)

============================================================
3. FASES IMPLEMENTADAS
============================================================

FASE 2 – ÁUDIO

- Geração de áudio a partir de roteiro
- Output salvo em disco
- Controle por job_id

FASE 3 – IMAGEM + LEGENDAS

- Geração de imagem base
- Sistema de legendas sincronizadas

FASE 3.5 – SUBTÍTULOS

- Renderização automática de legendas no vídeo

FASE 4 – GESTÃO DE FILA E ESTADO (CRÍTICA)

- Tabela video_jobs no Postgres
- Endpoints /jobs:
  - POST /jobs (criação + idempotência)
  - PATCH /jobs/{id} (update de estágio)
  - GET /jobs/check (verificação de duplicidade)
- retry_count automático
- Recuperação após falha garantida

FASE 5 – MOTOR DE VÍDEO COM B-ROLL DINÂMICO

- Endpoint /video/render expandido
- Suporte a múltiplos assets:
  - image
  - video
  - broll (dinâmico)
- Biblioteca local de B-roll:
  /data_midia/broll/{categoria}
- Fallback automático se b-roll não existir
- Ken Burns automático para imagens
- Vídeos redimensionados, cortados e silenciados
- n8n NÃO decide composição

============================================================
4. TESTES AUTOMATIZADOS (PYTEST)
============================================================

Cobertura implementada com mocks (MoviePy, filesystem, DB):

- Fallback de B-roll inexistente
- Idempotência de jobs
- Incremento de retries em erro
- Validação de payload inválido

Resultado:
✔ 7 testes
✔ 100% PASS
✔ Execução rápida (sem render real)

============================================================
5. ESTRUTURA DE ARQUIVOS PRINCIPAIS
============================================================

python_service/
│
├── main.py
├── jobs.py
├── video.py
├── audio.py
├── image.py
├── database.py
├── models.py
│
├── tests/
│   ├── conftest.py
│   ├── test_jobs.py
│   └── test_video.py
│
├── requirements.txt
├── Dockerfile
└── docker-compose.yml

============================================================
6. COMO O N8N INTERAGE
============================================================

- n8n apenas:
  - cria job
  - chama endpoints
  - atualiza status
- Nenhuma lógica de mídia no n8n
- Idempotência garantida pelo backend

============================================================
7. MONITORAMENTO
============================================================

Decisão arquitetural:

- Adicionar Dozzle ao docker-compose
- Objetivo: logs centralizados, zero cliques, debug rápido

============================================================
8. PRÓXIMAS FASES (ROADMAP)
============================================================

Fase 6:

- Suíte de Testes Automatizados (Pytest) – CONCLUÍDO
- 100% Pass em 7 cenários críticos (B-roll, Idempotência, etc.)

Fase 7:

- CI/CD Automatizado (GitHub Actions) – CONCLUÍDO
- Linting (flake8), Formatting (black) e pytest em cada commit.

Fase 8 (CONCLUÍDO):

- Observabilidade: Instalação do Dozzle para monitoramento de logs "Zero Cliques" – CONCLUÍDO
- Integração n8n <-> Python Service: Simulação de chamadas Docker-a-Docker – CONCLUÍDO
- Script de Validação: `test_integration_flow.py` operacional.

FASE 9:

- Publicação automática (YouTube / TikTok)
- Upload via API

FASE 10:

- Métricas de performance (views, likes)
- Feedback loop para IA

- CI/CD (GitHub Actions)
- pytest automático em PR

============================================================
9. PROMPT PARA OUTRA IA CONTINUAR O PROJETO
============================================================

Você é uma IA arquiteta de software especialista em:
Python, FastAPI, MoviePy, automação, pipelines de mídia e sistemas resilientes.

Contexto:
Estou desenvolvendo uma fábrica autônoma de vídeos baseada em IA.
As fases 2 a 5 já estão totalmente implementadas e testadas.
O sistema é stateless no n8n e stateful no backend Python com Postgres.

Regras importantes:

- Não mover lógica para o n8n
- Manter MoviePy simples e modular
- Priorizar resiliência, idempotência e recuperação de falhas
- Nenhuma publicação automática sem aprovação explícita
- Pensar sempre em execução 24/7

Objetivo imediato:
Continuar a partir da FASE 10 (CONCLUÍDO):

- Publicação: Integração com YouTube API v3 operacional.
- Estabilidade: Bug de extração (Invalid JSON) corrigido via status 422 e Headers reais.
- Ferramentas: Script `setup_youtube.py` criado para autenticação local.
publicação automática

Arquivos anexados:

- Código completo do python_service
- docker-compose.yml
- walkthrough.md
- task.md
- implementation_plan.md

============================================================
FIM DO DOCUMENTO
============================================================
