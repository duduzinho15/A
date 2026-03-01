from fastapi import APIRouter, Query, HTTPException
from fastapi.responses import FileResponse
import os
import json
from typing import Optional
from app.utils.database import get_db_connection
from app.services.trainer_prep import format_to_jsonl

router = APIRouter(prefix="/datasets", tags=["datasets"])

@router.get("/export")
async def export_dataset(
    min_ctr: float = Query(5.0, description="CTR minimo para exportacao"),
    limit: int = Query(100, description="Limite de registros"),
    format: str = Query("jsonl", regex="^(jsonl|json)$")
):
    """
    Exporta dados de alta performance para treinamento de IA.
    """
    conn = get_db_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Erro DB")
    
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT title, raw_content, script, metrics
                FROM video_jobs
                WHERE (metrics->>'ctr')::float >= %s
                ORDER BY (metrics->>'ctr')::float DESC
                LIMIT %s
            """, (min_ctr, limit))
            
            rows = cur.fetchall()
            if not rows:
                return {"message": "Nenhum dado encontrado com os criterios informados."}
            
            output_dir = "app/datasets"
            os.makedirs(output_dir, exist_ok=True)
            filename = f"dataset_high_performance_{min_ctr}.jsonl"
            filepath = os.path.join(output_dir, filename)
            
            with open(filepath, "w", encoding="utf-8") as f:
                for row in rows:
                    jsonl_line = format_to_jsonl(row)
                    f.write(json.dumps(jsonl_line, ensure_ascii=False) + "\n")
            
            return {
                "status": "success",
                "file": filename,
                "count": len(rows),
                "path": filepath
            }
    finally:
        conn.close()
