import os
import httpx
from pydantic import BaseModel

AIRIA_API_URL = "https://api.airia.com/v1/execute" # Example endpoint
AIRIA_KEY = os.getenv("AIRIA_API_KEY")

class AuditReport(BaseModel):
    flags: list
    email_draft: str

async def call_airia_agent(prompt: str, context: str = ""):
    """Orchestrates the Statute Sentinel and Contract Auditor within Airia."""
    headers = {"Authorization": f"Bearer {AIRIA_KEY}", "Content-Type": "application/json"}
    
    payload = {
        "agent_id": os.getenv("AIRIA_AGENT_ID"),
        "input": {
            "user_prompt": prompt,
            "document_context": context,
            "jurisdiction": "Ontario, Canada",
            "date": "2026-02-22"
        }
    }

    async with httpx.AsyncClient() as client:
        # Airia's A2A protocol handles the routing between Sentinel and Auditor
        response = await client.post(AIRIA_API_URL, json=payload, headers=headers, timeout=30.0)
        return response.json()
