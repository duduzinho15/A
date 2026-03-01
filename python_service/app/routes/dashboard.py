from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.services.sheets import SheetsService

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

class DashboardSyncRequest(BaseModel):
    job_id: str
    title: str
    status: str
    video_url: Optional[str] = ""
    notes: Optional[str] = ""

class DashboardSyncResponse(BaseModel):
    status: str
    action: str
    message: Optional[str] = None

@router.post("/sync", response_model=DashboardSyncResponse)
async def sync_dashboard(req: DashboardSyncRequest):
    """
    Sincroniza dados do job com o Google Sheets Dashboard.
    Se o ID já existir (coluna A), atualiza a linha; senão, adiciona uma nova.
    """
    service = SheetsService()
    
    # Prepara os valores
    # Esquema sugerido: ID | Data | Título | Status | Link | Notas
    now = datetime.now().strftime("%d/%m/%Y %H:%M")
    values = [req.job_id, now, req.title, req.status, req.video_url, req.notes]
    
    try:
        # Tenta atualizar primeiro (busca pelo job_id na coluna A)
        updated = service.update_row_by_id(req.job_id, values)
        
        if not updated:
            # Se não encontrou para atualizar, adiciona nova linha ao final
            success = service.append_row(values)
            if not success:
                 raise HTTPException(status_code=500, detail="Erro ao adicionar linha no Google Sheets.")
            return DashboardSyncResponse(status="success", action="append", message="Nova entrada adicionada ao dashboard.")
            
        return DashboardSyncResponse(status="success", action="update", message="Entrada existente atualizada no dashboard.")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na sincronização: {str(e)}")
