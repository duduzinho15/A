---
description: Guia de Orquestração da Fábrica de Conteúdo (Auto Content Factory)
---

# /agents - Guia de Orquestração Auto Content Factory 🐙

Este comando ativa o modo de orquestrador sênior para o projeto. Ao ser acionado, o agente deve assumir a responsabilidade total pela saúde da pipeline.

## Contexto do Projeto

Você está operando uma fábrica automatizada de vídeos (Zero-Touch).

- **Backend:** Python (FastAPI) em Docker.
- **Orquestração:** n8n (Workflows JSON).
- **IA:** Local (Ollama) + Fallbacks (Groq/Gemini).

## Skills Disponíveis

- #n8n_expert: Para auditoria de workflows.
- #video_expert: Para ajustes no motor de renderização.
- #Project_Planner: Para expansão de funcionalidades.

## Protocolo de Operação

1. **Auditoria:** Sempre verifique se as rotas do Python e os nós do n8n estão sincronizados.
2. **Resiliência:** Implementar retries e fallbacks em cada nova funcionalidade.
3. **Estética:** Consultar a pasta `/inspirations` para garantir que o output visual seja premium.
4. **Docs:** Manter o `Docs/changelog.md` atualizado em tempo real.

## Comandos Adicionais

- Use #status para ver o progresso atual das tarefas.
- Use #n8n_expert para auditar o arquivo mais recente em `n8n_custom/`.
