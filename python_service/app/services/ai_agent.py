# =============================================================================
# app/services/ai_agent.py — Agente Autônomo (LangChain + Ollama)
# =============================================================================
# Worker Loop que roda em background no FastAPI.
# Usa APScheduler para tarefas agendadas e reativas.
#
# 3 Motores:
#   1. Sentinel  (cada 5 min) — Health check + auto-heal
#   2. Orchestrator (diário 00:00) — Docs, Security, Datasets
#   3. On-Demand (API) — Executar tool específica
# =============================================================================

import logging
import asyncio
from datetime import datetime
from typing import Optional

from fastapi import APIRouter
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger

logger = logging.getLogger("ai_agent")

router = APIRouter(prefix="/agent", tags=["agent"])


# =============================================================================
# AGENT STATE — Singleton state for status tracking
# =============================================================================

class AgentState:
    """Estado global do agente (singleton)."""

    def __init__(self):
        self.running = False
        self.started_at: Optional[datetime] = None
        self.last_task: Optional[str] = None
        self.last_run: Optional[datetime] = None
        self.tasks_completed: int = 0
        self.errors: int = 0
        self.ollama_available: bool = False
        self.log: list[dict] = []  # Últimas 20 ações

    def record_action(self, task_name: str, result: str, success: bool = True):
        self.last_task = task_name
        self.last_run = datetime.now()
        self.tasks_completed += 1
        if not success:
            self.errors += 1
        self.log.append({
            "task": task_name,
            "result": result[:200],
            "success": success,
            "timestamp": self.last_run.isoformat()
        })
        # Manter apenas últimas 20 entradas
        if len(self.log) > 20:
            self.log = self.log[-20:]


# Singleton
_state = AgentState()


# =============================================================================
# AGENT CORE — AutoContentAgent
# =============================================================================

class AutoContentAgent:
    """
    Agente Autônomo que roda como background worker no FastAPI.
    Usa LangChain + Ollama para raciocínio e APScheduler para agendamento.
    """

    def __init__(self, ollama_model: str = "llama3.2", ollama_base_url: str = "http://ollama:11434"):
        self.model_name = ollama_model
        self.ollama_base_url = ollama_base_url
        self.scheduler = AsyncIOScheduler()
        self.agent = None
        self._setup_llm()

    def _setup_llm(self):
        """Tenta inicializar o LLM (Ollama). Se falhar, opera em modo 'tools-only'."""
        try:
            from langchain_ollama import ChatOllama
            from langgraph.prebuilt import create_react_agent
            from langchain_core.messages import HumanMessage
            from app.services.agent_tools import ALL_TOOLS

            llm = ChatOllama(
                model=self.model_name,
                base_url=self.ollama_base_url,
                temperature=0.1,
                num_predict=512,
            )

            class AgentWrapper:
                def __init__(self, model, tools):
                    self.graph = create_react_agent(model, tools=tools)

                def invoke(self, inputs: dict) -> dict:
                    human_msg = inputs.get("input", "")
                    # Invoke langgraph using modern message list format
                    result = self.graph.invoke({"messages": [HumanMessage(content=human_msg)]})
                    messages = result.get("messages", [])
                    if messages:
                        return {"output": messages[-1].content}
                    return {"output": ""}

            self.agent = AgentWrapper(llm, ALL_TOOLS)



            _state.ollama_available = True
            logger.info("[AGENT] ✅ LLM (Ollama/%s) inicializado com sucesso", self.model_name)

        except Exception as e:
            import traceback
            logger.warning("[AGENT] ⚠️ Ollama não disponível (%s). Modo tools-only ativado.", e)
            logger.error("[AGENT] Traceback: %s", traceback.format_exc())
            _state.ollama_available = False
            self.agent = None

    async def start(self):
        """Inicia o scheduler com os 3 motores."""
        _state.running = True
        _state.started_at = datetime.now()

        # Motor #1: Sentinel (cada 5 minutos)
        self.scheduler.add_job(
            self._run_sentinel,
            trigger=IntervalTrigger(minutes=5),
            id="sentinel",
            name="Sentinel Health Monitor",
            replace_existing=True,
        )

        # Motor #2: Orchestrator (diário às 00:00)
        self.scheduler.add_job(
            self._run_orchestrator,
            trigger=CronTrigger(hour=0, minute=0),
            id="orchestrator",
            name="Daily Orchestrator",
            replace_existing=True,
        )

        self.scheduler.start()
        logger.info("=" * 60)
        logger.info("[AGENT] 🤖 Auto Content Agent STARTED")
        logger.info("[AGENT] 📡 Sentinel: cada 5 minutos")
        logger.info("[AGENT] 📅 Orchestrator: diário às 00:00")
        logger.info("[AGENT] 🧠 LLM: %s (%s)",
                     self.model_name,
                     "online" if _state.ollama_available else "offline — tools-only")
        logger.info("=" * 60)

        # Executar health check inicial
        await self._run_sentinel()

    async def stop(self):
        """Para o scheduler."""
        if self.scheduler.running:
            self.scheduler.shutdown(wait=False)
        _state.running = False
        logger.info("[AGENT] 🛑 Agent stopped")

    # -------------------------------------------------------------------------
    # Motor #1: Sentinel (Reativo)
    # -------------------------------------------------------------------------

    async def _run_sentinel(self):
        """Verifica saúde do sistema e executa auto-heal se necessário."""
        try:
            from app.services.agent_tools import tool_health_check, tool_self_heal

            # Passo 1: Health check
            health_result = await asyncio.to_thread(tool_health_check.invoke, "")
            logger.info("[SENTINEL] Health check: %s", health_result[:100])
            _state.record_action("sentinel_health_check", health_result)

            # Passo 2: Se degradado, auto-heal
            if "degraded" in health_result.lower() or "AÇÃO NECESSÁRIA" in health_result:
                logger.warning("[SENTINEL] ⚠️ Sistema degradado — iniciando auto-heal")
                heal_result = await asyncio.to_thread(tool_self_heal.invoke, "")
                logger.info("[SENTINEL] Auto-heal result: %s", heal_result[:100])
                _state.record_action("sentinel_auto_heal", heal_result)

                # Passo 3: Se temos LLM, pedir análise profunda
                if self.agent:
                    try:
                        analysis = await asyncio.to_thread(
                            self.agent.invoke,
                            {"input": f"O sistema está degradado. Health check: {health_result}. "
                                      f"Auto-heal executado: {heal_result}. "
                                      "Analise se alguma ação adicional é necessária."}
                        )
                        logger.info("[SENTINEL] LLM analysis: %s",
                                    analysis.get("output", "")[:200])
                        _state.record_action("sentinel_llm_analysis",
                                             analysis.get("output", ""), True)
                    except Exception as e:
                        logger.warning("[SENTINEL] LLM analysis falhou: %s", e)

        except Exception as e:
            logger.error("[SENTINEL] Erro: %s", e)
            _state.record_action("sentinel_error", str(e), False)

    # -------------------------------------------------------------------------
    # Motor #2: Orchestrator (Agendado)
    # -------------------------------------------------------------------------

    async def _run_orchestrator(self):
        """Executa tarefas diárias de manutenção."""
        try:
            logger.info("[ORCHESTRATOR] 🌙 Iniciando rotina diária...")

            # Task 1: Dataset check & Auto Docs
            from app.services.agent_tools import tool_seo_suggest, tool_auto_docs

            seo_result = await asyncio.to_thread(tool_seo_suggest.invoke, "")
            logger.info("[ORCHESTRATOR] SEO suggest: %s", seo_result[:100])
            _state.record_action("orchestrator_seo", seo_result)

            auto_docs_result = await asyncio.to_thread(tool_auto_docs.invoke, "")
            logger.info("[ORCHESTRATOR] Auto-Docs: %s", auto_docs_result[:100])
            _state.record_action("orchestrator_auto_docs", auto_docs_result)

            # Task 2: Se temos LLM, pedir relatório diário
            if self.agent:
                try:
                    report = await asyncio.to_thread(
                        self.agent.invoke,
                        {"input": "Faça um relatório resumido do status do sistema. "
                                  "Verifique a saúde do sistema e sugira melhorias de SEO."}
                    )
                    daily_report = report.get("output", "Sem relatório.")
                    logger.info("[ORCHESTRATOR] Relatório diário: %s", daily_report[:300])
                    _state.record_action("orchestrator_daily_report", daily_report)
                except Exception as e:
                    logger.warning("[ORCHESTRATOR] LLM report falhou: %s", e)

            logger.info("[ORCHESTRATOR] ✅ Rotina diária concluída")

        except Exception as e:
            logger.error("[ORCHESTRATOR] Erro: %s", e)
            _state.record_action("orchestrator_error", str(e), False)

    # -------------------------------------------------------------------------
    # Motor #3: On-Demand (API)
    # -------------------------------------------------------------------------

    async def run_tool(self, tool_name: str) -> dict:
        """Executa uma tool específica por nome."""
        from app.services.agent_tools import TOOL_MAP

        if tool_name not in TOOL_MAP:
            return {"error": f"Tool '{tool_name}' não encontrada. Disponíveis: {list(TOOL_MAP.keys())}"}

        try:
            tool_fn = TOOL_MAP[tool_name]
            result = await asyncio.to_thread(tool_fn.invoke, "")
            _state.record_action(f"on_demand_{tool_name}", result)
            return {"tool": tool_name, "result": result, "success": True}
        except Exception as e:
            _state.record_action(f"on_demand_{tool_name}", str(e), False)
            return {"tool": tool_name, "error": str(e), "success": False}


# =============================================================================
# SINGLETON INSTANCE
# =============================================================================

_agent_instance: Optional[AutoContentAgent] = None


def get_agent() -> Optional[AutoContentAgent]:
    return _agent_instance


async def start_agent():
    """Chamado pelo startup do FastAPI."""
    global _agent_instance
    try:
        _agent_instance = AutoContentAgent()
        await _agent_instance.start()
    except Exception as e:
        logger.error("[AGENT] ❌ Falha ao iniciar agente: %s", e)
        _state.running = False


# =============================================================================
# ENDPOINTS
# =============================================================================

@router.get("/status")
async def agent_status():
    """Retorna o status atual do agente autônomo."""
    import httpx
    # Re-check Ollama if currently marked as offline (Dynamic check)
    if not _state.ollama_available:
        try:
            # Tenta o host configurado (ollama:11434) e fallback para localhost
            for base_url in ["http://ollama:11434", "http://localhost:11434"]:
                try:
                    async with httpx.AsyncClient() as client:
                        resp = await client.get(f"{base_url}/api/tags", timeout=1.0)
                        print(f"[AGENT] OLLAMA RE-CHECK for {base_url} returned {resp.status_code}", flush=True)
                        if resp.status_code == 200:
                            _state.ollama_available = True
                            logger.info(f"[AGENT] ✅ Ollama re-conectado via {base_url}")
                            # Se recuperou a conexão, tenta re-inicializar o setup do LLM se necessário
                            agent = get_agent()
                            if agent and not agent.agent:
                                agent.ollama_base_url = base_url
                                agent._setup_llm()
                            break
                except Exception as loop_e:
                    print(f"[AGENT] OLLAMA RE-CHECK FAILED for {base_url}: {repr(loop_e)}", flush=True)
                    continue
        except Exception as e:
            print(f"[AGENT] Erro no re-check dinâmico de Ollama: {e}", flush=True)

    uptime = None
    if _state.started_at:
        uptime = (datetime.now() - _state.started_at).total_seconds()

    return {
        "running": _state.running,
        "ollama_available": _state.ollama_available,
        "ollama_host_fallback": "http://localhost:11434" if "localhost" in getattr(get_agent(), 'ollama_base_url', '') else "standard",
        "uptime_seconds": round(uptime, 1) if uptime else None,
        "last_task": _state.last_task,
        "last_run": _state.last_run.isoformat() if _state.last_run else None,
        "tasks_completed": _state.tasks_completed,
        "errors": _state.errors,
        "next_scheduled": {
            "sentinel": "every 5 minutes",
            "orchestrator": "daily at 00:00"
        }
    }


@router.get("/log")
async def agent_log():
    """Retorna as últimas 20 ações do agente."""
    return {
        "total_actions": _state.tasks_completed,
        "recent": _state.log
    }


@router.post("/run/{tool_name}")
async def agent_run_tool(tool_name: str):
    """Executa uma tool específica do agente sob demanda."""
    agent = get_agent()
    if not agent:
        return {"error": "Agent não inicializado"}
    return await agent.run_tool(tool_name)
