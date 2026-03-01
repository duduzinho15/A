import os
import httpx
import logging
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class OpenHandsClient:
    """
    Bridge client to interact with the OpenHands API.
    Used for Auto-healing, Documentation, and Autonomous Tasks.
    """
    def __init__(self, base_url: str = "http://openhands:3000"):
        self.base_url = base_url.rstrip('/')
        self.timeout = 60.0 # OpenHands can take time to respond

    async def send_task(self, task: str, workspace_dir: Optional[str] = None) -> Dict[str, Any]:
        """
        Sends a new task to OpenHands.
        """
        url = f"{self.base_url}/api/tasks"
        payload = {
            "task": task,
            "workspace_dir": workspace_dir or "/opt/workspace_base"
        }
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.post(url, json=payload)
                response.raise_for_status()
                return response.json()
        except Exception as e:
            logger.error(f"Failed to send task to OpenHands: {str(e)}")
            return {"error": str(e), "success": False}

    async def get_task_status(self, task_id: str) -> Dict[str, Any]:
        """
        Checks the status of a specific task.
        """
        url = f"{self.base_url}/api/tasks/{task_id}"
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url)
                response.raise_for_status()
                return response.json()
        except Exception as e:
            logger.error(f"Failed to get OpenHands task status: {str(e)}")
            return {"error": str(e), "success": False}

# Singleton instance
openhands_client = OpenHandsClient(base_url=os.getenv("OPENHANDS_URL", "http://openhands:3000"))
