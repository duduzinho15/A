from fastapi import APIRouter, HTTPException
import os
import psutil
import json
from datetime import datetime
from app.utils.database import get_db_connection

router = APIRouter(prefix="/maintenance", tags=["maintenance"])

@router.get("/health")
async def health_check():
    """
    Verifica a saude dos componentes criticos do sistema.
    """
    report = {
        "timestamp": datetime.now().isoformat(),
        "status": "healthy",
        "components": {}
    }
    
    # 1. Database Check
    try:
        conn = get_db_connection()
        if conn:
            report["components"]["database"] = "connected"
            conn.close()
        else:
            report["components"]["database"] = "failed"
            report["status"] = "degraded"
    except Exception as e:
        report["components"]["database"] = f"error: {str(e)}"
        report["status"] = "degraded"

    # 2. Disk Space Check
    usage = psutil.disk_usage('/')
    report["components"]["disk"] = {
        "percent": usage.percent,
        "free_gb": usage.free // (2**30)
    }
    if usage.percent > 90:
        report["status"] = "degraded"
        report["components"]["disk"]["status"] = "warning"

    # 3. Memory Check
    mem = psutil.virtual_memory()
    report["components"]["memory"] = {
        "percent": mem.percent
    }
    if mem.percent > 95:
        report["status"] = "degraded"
    
    return report

@router.post("/heal")
async def trigger_auto_healing():
    """
    Trigger manual ou via webhook para o sistema de auto-healing.
    """
    from app.services.healer import autonomous_heal
    result = await autonomous_heal()
    return result

@router.get("/logs")
async def get_logs(lines: int = 100):
    """
    Retorna as ultimas N linhas do log (agent.log).
    """
    log_file = "agent.log"
    if not os.path.exists(log_file):
        return {"logs": ["Nenhum log encontrado ainda."]}
    
    try:
        with open(log_file, "r", encoding="utf-8") as f:
            all_lines = f.readlines()
            
        return {"logs": all_lines[-lines:]}
    except Exception as e:
        return {"logs": [f"Erro ao ler logs: {str(e)}"]}

@router.get("/docs/changelog")
async def get_changelog():
    """
    Retorna o conteudo do arquivo /Docs/changelog.md.
    """
    changelog_path = "/Docs/changelog.md"
    if not os.path.exists(changelog_path):
        # Tenta caminho relativo se o absoluto falhar (local dev)
        changelog_path = "../Docs/changelog.md"
        if not os.path.exists(changelog_path):
            return {"content": "# Changelog não encontrado\nO arquivo /Docs/changelog.md não foi localizado."}
    
    try:
        with open(changelog_path, "r", encoding="utf-8") as f:
            content = f.read()
        return {"content": content}
    except Exception as e:
        return {"content": f"# Erro ao ler changelog\n{str(e)}"}

# --- CONFIG MANAGEMENT ---
SAFE_CONFIG_KEYS = ["AGENT_INTERVAL", "LOG_LEVEL", "AUTO_HEAL_ENABLED", "MAX_VIDEO_QUEUE", "SENTINEL_MODE"]

@router.get("/config")
async def get_system_config():
    """
    Retorna as configuraçoes editáveis do sistema do arquivo .env.
    """
    config = {}
    env_path = ".env"
    if not os.path.exists(env_path):
        return {"error": ".env file not found"}
    
    with open(env_path, "r") as f:
        for line in f:
            if "=" in line and not line.startswith("#"):
                key, value = line.strip().split("=", 1)
                if key in SAFE_CONFIG_KEYS:
                    config[key] = value.strip("'").strip('"')
    
    # Preenche com defaults se nao existir no .env mas estiver na lista safe
    for key in SAFE_CONFIG_KEYS:
        if key not in config:
            config[key] = os.getenv(key, "")
            
    return config

@router.post("/config")
async def update_system_config(new_config: dict):
    """
    Atualiza o arquivo .env com os novos valores fornecidos.
    """
    env_path = ".env"
    if not os.path.exists(env_path):
        return {"error": ".env file not found"}
    
    # Valida chaves
    filtered_config = {k: v for k, v in new_config.items() if k in SAFE_CONFIG_KEYS}
    
    if not filtered_config:
        return {"status": "no_changes", "message": "Nenhuma chave válida para atualizar."}
    
    try:
        with open(env_path, "r") as f:
            lines = f.readlines()
        
        new_lines = []
        updated_keys = set()
        
        for line in lines:
            if "=" in line and not line.startswith("#"):
                key = line.split("=")[0].strip()
                if key in filtered_config:
                    new_lines.append(f"{key}={filtered_config[key]}\n")
                    updated_keys.add(key)
                else:
                    new_lines.append(line)
            else:
                new_lines.append(line)
        
        # Adiciona chaves que nao estavam no arquivo
        for key, value in filtered_config.items():
            if key not in updated_keys:
                new_lines.append(f"{key}={value}\n")
        
        with open(env_path, "w") as f:
            f.writelines(new_lines)
            
        return {"status": "success", "updated_keys": list(filtered_config.keys())}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
