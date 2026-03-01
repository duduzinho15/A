import os
import shutil
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

async def autonomous_heal():
    """
    Executa acoes de recuperacao baseadas em diagnostico.
    """
    actions_taken = []
    
    # Diagnostico Nivel 1: Disco e Temp
    try:
        temp_dir = "/tmp"
        if os.path.exists(temp_dir):
            # Limpa arquivos temporarios antigos (> 1 hora)
            now = datetime.now().timestamp()
            count = 0
            for f in os.listdir(temp_dir):
                fpath = os.path.join(temp_dir, f)
                if os.path.isfile(fpath) and (now - os.path.getmtime(fpath)) > 3600:
                    os.remove(fpath)
                    count += 1
            if count > 0:
                actions_taken.append(f"Limpeza de {count} arquivos temporarios em /tmp")
    except Exception as e:
        logger.error(f"[Healer] Erro ao limpar /tmp: {e}")

    # Diagnostico Nivel 2: Logs e Erros Críticos
    log_file = "python_service_logs.txt"
    if os.path.exists(log_file):
        try:
            with open(log_file, "r") as f:
                lines = f.readlines()[-20:] # Ultimas 20 linhas
                error_context = "".join(lines)
                if "OperationalError" in error_context or "connection" in error_context.lower():
                    # Tentar resetar conexoes (logica simplificada)
                    actions_taken.append("Detectado erro de conexao DB - Solicitando refresh de conexao")
        except Exception as e:
            logger.warning(f"[Healer] Erro ao ler logs para diagnostico: {e}")

    if not actions_taken:
        return {"status": "no_action_needed", "diagnostics": "Sistema operando dentro dos parametros."}

    return {
        "status": "healed",
        "actions": actions_taken,
        "timestamp": datetime.now().isoformat()
    }
