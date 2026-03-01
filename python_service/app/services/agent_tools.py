# =============================================================================
# app/services/agent_tools.py — Tools do Agente Autônomo
# =============================================================================
# Cada tool é uma função decorada com @tool do LangChain.
# O agente LLM escolhe qual tool usar baseado no contexto.
# =============================================================================

import logging
import httpx
from langchain_core.tools import tool
from duckduckgo_search import DDGS

logger = logging.getLogger("agent_tools")

# Base URL interna do FastAPI (dentro do mesmo container)
BASE_URL = "http://localhost:8000"


@tool
def tool_health_check(query: str = "") -> str:
    """
    Verifica a saúde do sistema Auto Content Factory.
    Retorna o status dos componentes: database, disk, memory.
    Use esta ferramenta para diagnosticar se o sistema está funcionando.
    """
    try:
        r = httpx.get(f"{BASE_URL}/maintenance/health", timeout=10)
        data = r.json()
        status = data.get("status", "unknown")
        components = data.get("components", {})

        report = f"Status: {status}\n"
        for comp, info in components.items():
            if isinstance(info, dict):
                report += f"  - {comp}: {info}\n"
            else:
                report += f"  - {comp}: {info}\n"

        if status == "degraded":
            report += "\n⚠️ AÇÃO NECESSÁRIA: Sistema degradado. Considere rodar self_heal."

        logger.info(f"[AGENT-TOOL] health_check → {status}")
        return report
    except Exception as e:
        logger.error(f"[AGENT-TOOL] health_check falhou: {e}")
        return f"Erro ao verificar saúde: {e}"


@tool
def tool_self_heal(query: str = "") -> str:
    """
    Executa o auto-healing do sistema: limpa arquivos temporários,
    verifica conexões do banco de dados e corrige problemas comuns.
    Use quando o health_check reportar status 'degraded'.
    """
    try:
        r = httpx.post(f"{BASE_URL}/maintenance/heal", timeout=30)
        data = r.json()
        status = data.get("status", "unknown")
        actions = data.get("actions", [])

        if status == "healed":
            report = f"✅ Auto-healing executado com sucesso!\nAções: {', '.join(actions)}"
        else:
            report = "ℹ️ Nenhuma ação necessária — sistema operando normalmente."

        logger.info(f"[AGENT-TOOL] self_heal → {status} ({len(actions)} ações)")
        return report
    except Exception as e:
        logger.error(f"[AGENT-TOOL] self_heal falhou: {e}")
        return f"Erro no auto-healing: {e}"


@tool
def tool_dataset_export(query: str = "") -> str:
    """
    Exporta o dataset de vídeos processados para análise e fine-tuning.
    Use periodicamente para manter backup dos dados de treinamento.
    """
    try:
        r = httpx.post(f"{BASE_URL}/datasets/export", timeout=60)
        if r.status_code == 200:
            data = r.json()
            count = data.get("total_exported", 0)
            logger.info(f"[AGENT-TOOL] dataset_export → {count} registros")
            return f"✅ Dataset exportado: {count} registros."
        else:
            return f"⚠️ Export retornou status {r.status_code}: {r.text[:200]}"
    except Exception as e:
        logger.error(f"[AGENT-TOOL] dataset_export falhou: {e}")
        return f"Erro no export: {e}"


@tool
def tool_seo_suggest(query: str = "") -> str:
    """
    Analisa os últimos vídeos publicados e sugere otimizações de SEO.
    Verifica títulos, tags e descrições para maximizar alcance orgânico.
    """
    try:
        r = httpx.get(f"{BASE_URL}/datasets/summary", timeout=15)
        if r.status_code == 200:
            data = r.json()
            total = data.get("total_videos", 0)
            recent = data.get("recent_count", 0)

            suggestions = []
            if total == 0:
                suggestions.append("Nenhum vídeo no DB. Aguardando pipeline.")
            elif recent < 3:
                suggestions.append(f"Produção baixa: apenas {recent} vídeos recentes. Verificar pipeline.")
            else:
                suggestions.append(f"Pipeline ativo: {recent} vídeos recentes de {total} total.")

            logger.info(f"[AGENT-TOOL] seo_suggest → {len(suggestions)} sugestões")
            return "\n".join(suggestions)
        else:
            return f"⚠️ Endpoint /datasets/summary retornou {r.status_code}"
    except Exception as e:
        logger.error(f"[AGENT-TOOL] seo_suggest falhou: {e}")
        return f"Erro na análise SEO: {e}"


@tool
def tool_web_search(query: str = "") -> str:
    """
    Busca informações em tempo real na internet usando o buscador DuckDuckGo.
    Útil quando você precisar de informações recentes ou complementar dados.
    Mantenha a query focada, por exemplo: 'flamengo noticias de hoje'.
    """
    try:
        if not query:
            return "Erro: query não fornecida."
        
        logger.info(f"[AGENT-TOOL] web_search → Buscando por: '{query}'")
        
        # Inicia o client do DDGS
        ddgs = DDGS()
        
        # Extrai os primeiros 3 resultados de texto
        results = list(ddgs.text(query, max_results=3))
        
        if not results:
            return f"Nenhum resultado encontrado na web para: '{query}'"
        
        response = f"Resultados da busca para '{query}':\n\n"
        for i, res in enumerate(results, 1):
            title = res.get("title", "Sem título")
            body = res.get("body", "Sem descrição")
            href = res.get("href", "#")
            response += f"{i}. {title}\nURL: {href}\nResumo: {body}\n\n"
            
        return response
    except Exception as e:
        logger.error(f"[AGENT-TOOL] web_search falhou: {e}")
        return f"Erro na busca: {e}"


@tool
def tool_auto_docs(query: str = "") -> str:
    """
    Ferramenta Auto-Docs: Lê os arquivos '.py' modificados nas últimas 24h e escreve um changelog automático.
    Use quando desejar registrar as implementações e mudanças de código no sistema de forma autônoma.
    """
    import os
    import glob
    from datetime import datetime, timedelta

    try:
        logger.info("[AGENT-TOOL] auto_docs → Iniciando scan de arquivos...")
        
        # Scans app and tests
        app_files = glob.glob("/app/app/**/*.py", recursive=True)
        test_files = glob.glob("/app/tests/**/*.py", recursive=True)
        all_files = app_files + test_files
        
        now = datetime.now()
        yesterday = now - timedelta(days=1)
        
        modified_files = []
        for file_path in all_files:
            mtime = datetime.fromtimestamp(os.path.getmtime(file_path))
            if mtime >= yesterday:
                # Store relative to app standard
                modified_files.append(file_path.replace("/app/", ""))
        
        if not modified_files:
            return "Nenhum arquivo Python foi modificado nas últimas 24 horas. Nenhum log de changelog gerado."
            
        files_list = "\n".join([f"- `{f}`" for f in modified_files])
        
        changelog_entry = f"\n\n## [{now.strftime('%Y-%m-%d')}] — Auto-Audit Report (AI Agent) 🤖\n\n"
        changelog_entry += "### 🔄 Arquivos Modificados (Últimas 24h)\n\n"
        changelog_entry += files_list
        changelog_entry += "\n\n*Relatório gerado automaticamente pelo motor Orchestrator.*\n"
        
        changelog_path = "/Docs/changelog.md"
        if os.path.exists(changelog_path):
            with open(changelog_path, "a", encoding="utf-8") as f:
                f.write(changelog_entry)
            result_msg = f"Auto-Docs concluído com sucesso. {len(modified_files)} arquivos auditados e registrados em /Docs/changelog.md."
            logger.info(f"[AGENT-TOOL] auto_docs → {result_msg}")
            return result_msg
        else:
            return f"Arquivos modificados: {len(modified_files)}, mas o caminho /Docs/changelog.md não foi encontrado no container."
            
    except Exception as e:
        logger.error(f"[AGENT-TOOL] auto_docs falhou: {e}")
        return f"Erro ao executar Auto-Docs: {e}"

# =============================================================================
# REGISTRY — Lista de todas as tools disponíveis para o agente
# =============================================================================

ALL_TOOLS = [
    tool_health_check,
    tool_self_heal,
    tool_dataset_export,
    tool_seo_suggest,
    tool_web_search,
    tool_auto_docs,
]

TOOL_MAP = {t.name: t for t in ALL_TOOLS}
