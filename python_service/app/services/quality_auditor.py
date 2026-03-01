import json
import logging
import subprocess
from pathlib import Path
from typing import Optional, Dict

logger = logging.getLogger(__name__)

class QualityAuditor:
    """
    Quality Auditor responsável por baixar métricas de performance (via yt-dlp) 
    e preparar os dados do vídeo para auditoria visual/textual via IA.
    """
    
    def __init__(self, data_dir: str = "/data_midia"):
        self.data_dir = Path(data_dir)

    def fetch_metrics(self, video_url: str) -> Optional[Dict]:
        """
        Usa o yt-dlp de forma silenciosa e no-download para capturar 
        métricas de Views, Likes e informações básicas do player.
        """
        logger.info(f"Buscando métricas de performance para: {video_url}")
        try:
            cmd = [
                'yt-dlp',
                '--dump-json',
                '--no-download',
                video_url
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            data = json.loads(result.stdout)
            
            metrics = {
                "url": video_url,
                "title": data.get("title"),
                "view_count": data.get("view_count", 0),
                "like_count": data.get("like_count", 0),
                "duration": data.get("duration", 0),
                "platform": data.get("extractor")
            }
            logger.info(f"Métricas capturadas com sucesso: {metrics}")
            return metrics
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Erro no yt-dlp ao processar {video_url}: {e.stderr}")
            return None
        except Exception as e:
            logger.error(f"Falha inesperada ao buscar métricas: {str(e)}")
            return None

    async def audit_video_quality(self, local_video_path: str, transcript: str, title: str) -> Dict:
        """
        Integra LLM (Gemini 1.5 Flash via httpx) para analisar o vídeo final compilado.
        Atualmente envia a transcrição, título e contexto para julgar a coesão e as pausas.
        No futuro, arquivos de vídeo podem ser uploadeados via File API do Gemini se o tamanho permitir.
        """
        logger.info(f"Iniciando AI Quality Audit local na flag: {local_video_path}")
        
        if not Path(local_video_path).exists():
            logger.warning("Vídeo local não encontrado fisicamente, mas farei a auditoria por transcrição.")

        from app.config import settings
        import httpx

        if not settings.GEMINI_API_KEY:
            logger.error("Sem chave do Gemini. Auditoria falhou.")
            return {"error": "GEMINI_API_KEY ausente."}

        # Prompt de avaliação qualitativa
        system = (
            "Você é um Produtor de Conteúdo nível Sênior para YouTube Shorts e TikTok. "
            "Seu trabalho é revisar o roteiro de um vídeo de inteligência artificial ANTES que "
            "ele escale. Dê notas severas de 0 a 10 e dicas diretas."
        )
        prompt = (
            f"VÍDEO TÍTULO: {title}\n"
            f"ROTEIRO/TRANSCRIÇÃO:\n{transcript}\n\n"
            "Responda EXATAMENTE neste JSON:\n"
            "{\n"
            '  "pacing_score": 8.5,\n'
            '  "clickbait_alignment": "Good|Fair|Poor",\n'
            '  "orthography_warnings": ["lista", "de", "erros textuals", "ou vazio"],\n'
            '  "ai_suggestions": ["sugestao 1 curta", "sugestao 2 curta"]\n'
            "}"
        )

        try:
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={settings.GEMINI_API_KEY}"
            payload = {"contents": [{"parts": [{"text": f"{system}\n\n{prompt}"}]}]}
            
            async with httpx.AsyncClient(timeout=30.0) as client:
                resp = await client.post(url, json=payload)
                if resp.status_code == 200:
                    ai_reply = resp.json()["candidates"][0]["content"]["parts"][0]["text"]
                    
                    # Parse do JSON da Resposta
                    import re
                    match = re.search(r"\{.*\}", ai_reply, re.DOTALL)
                    if match:
                        return json.loads(match.group())
                    else:
                        logger.warning("Gemini não retornou JSON puro.")
                        return {"raw": ai_reply}
                else:
                    logger.error(f"Erro no Gemini: {resp.status_code} - {resp.text}")
                    return {"error": "Falha na API Vision/LLM"}
        except Exception as e:
            logger.error(f"Exceção durante Quality Audit: {str(e)}")
            return {"error": str(e)}

    async def log_to_notion(self, audit_data: Dict):
        """
        Envia os resultados da auditoria para a database do Notion.
        """
        from app.config import settings
        import httpx
        from datetime import datetime

        if not settings.NOTION_TOKEN or not settings.NOTION_DB_ID:
            logger.warning("Notion integration not configured. Skipping log.")
            return

        metrics = audit_data.get("performance_metrics") or {}
        quality = audit_data.get("quality_audit") or {}
        
        url = "https://api.notion.com/v1/pages"
        headers = {
            "Authorization": f"Bearer {settings.NOTION_TOKEN}",
            "Content-Type": "application/json",
            "Notion-Version": "2022-06-28"
        }

        # Preparar propriedades
        properties = {
            "Video Name": {"title": [{"text": {"content": metrics.get("title") or "Untitled Video"}}]},
            "Score": {"number": quality.get("pacing_score", 0)},
            "Pacing": {"number": quality.get("pacing_score", 0)},
            "Status": {"select": {"name": "Approved" if quality.get("pacing_score", 0) >= 7 else "Rejected"}},
            "Platform": {"select": {"name": metrics.get("platform") or "TikTok"}},
            "Views": {"number": metrics.get("view_count", 0)},
            "Likes": {"number": metrics.get("like_count", 0)},
            "Suggestions": {"rich_text": [{"text": {"content": ", ".join(quality.get("ai_suggestions", []))[:2000]}}]},
            "Video URL": {"url": metrics.get("url") or "https://placeholder.com"},
            "Date": {"date": {"start": datetime.now().isoformat()}}
        }

        payload = {
            "parent": {"database_id": settings.NOTION_DB_ID},
            "properties": properties
        }

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(url, headers=headers, json=payload)
                if resp.status_code == 200:
                    logger.info("Dados de auditoria salvos no Notion com sucesso.")
                else:
                    logger.error(f"Erro ao salvar no Notion: {resp.status_code} - {resp.text}")
        except Exception as e:
            logger.error(f"Falha na integração com Notion: {str(e)}")

    async def run_full_audit(self, video_url: str, local_video_path: str, transcript: str, title: str) -> Dict:
        """ Executa o pipeline de Performance + AI Audit e salva no Notion """
        metrics = self.fetch_metrics(video_url)
        quality = await self.audit_video_quality(local_video_path, transcript, title)
        
        audit_results = {
            "performance_metrics": metrics,
            "quality_audit": quality
        }
        
        await self.log_to_notion(audit_results)
        return audit_results

quality_auditor = QualityAuditor()
