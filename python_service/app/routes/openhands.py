from fastapi import APIRouter, HTTPException, BackgroundTasks
from app.services.openhands_client import openhands_client
from pydantic import BaseModel
from typing import Optional, Dict, Any

router = APIRouter(prefix="/openhands", tags=["OpenHands"])

class TaskRequest(BaseModel):
    task: str
    workspace_dir: Optional[str] = "/opt/workspace_base"

class ScraperRequest(BaseModel):
    url: str
    target_fields: Optional[list[str]] = ["title", "content", "date", "image"]

class InfraRequest(BaseModel):
    action_description: str
    target_files: Optional[list[str]] = ["docker-compose.yml", "Dockerfile"]

class DatasetRequest(BaseModel):
    topic: str
    max_samples: int = 100

class UIRequest(BaseModel):
    description: str
    framework: Optional[str] = "Vanilla JS/CSS"

class SEORequest(BaseModel):
    keywords: list[str]
    target_pages: Optional[list[str]] = ["index.html"]

@router.post("/task")
async def create_openhands_task(request: TaskRequest):
    """
    Envia uma tarefa para o agente OpenHands de forma assíncrona.
    """
    result = await openhands_client.send_task(request.task, request.workspace_dir)
    if "error" in result:
        raise HTTPException(status_code=500, detail=result["error"])
    return result

@router.get("/task/{task_id}")
async def get_task_status(task_id: str):
    """
    Consulta o status de uma tarefa enviada ao OpenHands.
    """
    result = await openhands_client.get_task_status(task_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result

@router.post("/auto-docs")
async def trigger_auto_docs(background_tasks: BackgroundTasks):
    """
    Ideia #4: Gatilho para o OpenHands atualizar a documentação do projeto.
    """
    task_description = (
        "Analyze the current state of the project files, including routes, "
        "services, and n8n workflows. Update Docs/estrutura.md and Docs/README.md "
        "to reflect any recent changes. Ensure the documentation is accurate and technical."
    )
    background_tasks.add_task(openhands_client.send_task, task_description)
    return {"status": "Doc update task scheduled with OpenHands", "idea": "Auto-Documentation (#4)"}

@router.post("/security-scan")
async def trigger_security_scan(background_tasks: BackgroundTasks):
    """
    Ideia #5: Gatilho para o OpenHands realizar uma auditoria de segurança no código.
    """
    task_description = (
        "Perform a comprehensive security audit of the current project. "
        "Check for: 1. Exposed API keys or secrets in code/.env. "
        "2. Vulnerable dependencies in requirements.txt. "
        "3. Common web vulnerabilities (SQL Injection, XSS) in FastAPI routes. "
        "4. Unauthorized access points. "
        "Generate a report in Docs/security_audit.md with findings and recommendations."
    )
    background_tasks.add_task(openhands_client.send_task, task_description)
    return {"status": "Security scan task scheduled with OpenHands", "idea": "Security Scanner (#5)"}

@router.post("/generate-scraper")
async def trigger_scraper_generation(request: ScraperRequest, background_tasks: BackgroundTasks):
    """
    Ideia #2: Gerador de Scrapers Autónomo.
    """
    task_description = (
        f"AUTONOMOUS SCRAPER GENERATOR: Create a new Python scraper for the URL: {request.url}. "
        f"Target fields to extract: {', '.join(request.target_fields)}. "
        "The script should use Playwright (for JS heavy sites) or Trafilatura/Requests as fallback. "
        "Save the resulting script in python_service/app/scrapers/ (create folder if missing). "
        "The scraper should follow the existing modular pattern of the project."
    )
    background_tasks.add_task(openhands_client.send_task, task_description)
    return {"status": "Scraper generation task scheduled with OpenHands", "idea": "Scraper Generator (#2)"}

@router.get("/debug-500")
async def trigger_debug_500():
    """
    Rota de teste para verificar se o Auto-healing está funcionando.
    """
    raise RuntimeError("Teste de Auto-healing acionado propositalmente!")

@router.post("/infra-task")
async def trigger_infra_task(request: InfraRequest, background_tasks: BackgroundTasks):
    """
    Ideia #8: Automação de Infraestrutura e Migrações.
    """
    task_description = (
        f"INFRASTRUCTURE AUTOMATION: {request.action_description}. "
        f"Target files to modify: {', '.join(request.target_files)}. "
        "Ensure all changes are validated and don't break existing services. "
        "Follow the project's Docker and networking patterns."
    )
    background_tasks.add_task(openhands_client.send_task, task_description)
    return {"status": "Infra task scheduled with OpenHands", "idea": "Infra & Migrations (#8)"}

@router.post("/prepare-dataset")
async def trigger_dataset_preparation(request: DatasetRequest, background_tasks: BackgroundTasks):
    """
    Ideia #9: Gestor de datasets para Fine-tuning.
    """
    task_description = (
        f"DATASET PREPARATION: Collect and format data for fine-tuning on the topic: {request.topic}. "
        f"Target sample size: {request.max_samples}. "
        "1. Extract relevant examples from the local database or logs. "
        "2. Format the output as a valid JSONL file for AI training. "
        "3. Save the result in the /datasets folder."
    )
    background_tasks.add_task(openhands_client.send_task, task_description)
    return {"status": "Dataset preparation scheduled with OpenHands", "idea": "Dataset Manager (#9)"}

@router.post("/develop-ui")
async def trigger_ui_development(request: UIRequest, background_tasks: BackgroundTasks):
    """
    Ideia #6: Desenvolvimento Autónomo de UI.
    """
    task_description = (
        f"UI DEVELOPMENT TASK: {request.description}. "
        f"Preferred stack: {request.framework}. "
        "Create modern, high-quality UI components. Follow the existing Design System (Purple-ban, Glassmorphism). "
        "Save resulting HTML/CSS/JS in the relevant frontend or templates directory."
    )
    background_tasks.add_task(openhands_client.send_task, task_description)
    return {"status": "UI development task scheduled with OpenHands", "idea": "UI/Dashboards (#6)"}

@router.post("/optimize-seo")
async def trigger_seo_optimization(request: SEORequest, background_tasks: BackgroundTasks):
    """
    Ideia #7: Otimização Proativa de SEO.
    """
    task_description = (
        f"SEO OPTIMIZATION: Research and implement SEO best practices for keywords: {', '.join(request.keywords)}. "
        f"Target pages: {', '.join(request.target_pages)}. "
        "1. Update meta tags, titles, and alt descriptions. "
        "2. Suggest content improvements for better ranking. "
        "3. Generate a report in Docs/seo_strategy.md."
    )
    background_tasks.add_task(openhands_client.send_task, task_description)
    return {"status": "SEO optimization scheduled with OpenHands", "idea": "SEO Optimization (#7)"}
