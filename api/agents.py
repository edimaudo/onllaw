import os
import httpx
from pydantic import BaseModel

AIRIA_API_URL = "https://api.airia.com/v1/execute" 
AIRIA_KEY = os.getenv("AIRIA_API_KEY")

class AuditReport(BaseModel):
    flags: list
    email_draft: str

async def call_airia_agent(prompt: str, context: str = ""):
    """Sends raw text to Airia and triggers the Sentinel + Auditor workflow."""
    
    # Airia expects X-API-Key for its execution interfaces
    headers = {
        "X-API-Key": f"{AIRIA_KEY}", 
        "Content-Type": "application/json"
    }
    
    # We enhance the prompt to tell the agent to 'clean' the raw input text
    enhanced_prompt = (
        f"INSTRUCTION: {prompt}\n\n"
        "NOTE: The following context is raw text extraction. Please reconstruct "
        "the document structure mentally before auditing against 2026 ESA rules."
    )
    
    payload = {
        "agent_id": os.getenv("AIRIA_AGENT_ID"),
        "input": {
            "user_prompt": enhanced_prompt,
            "document_context": context,
            "jurisdiction": "Ontario, Canada",
            "date": "2026-02-24"
        }
    }

    async with httpx.AsyncClient() as client:
        # Increased timeout to 60s as multi-agent hops can take time
        response = await client.post(AIRIA_API_URL, json=payload, headers=headers, timeout=60.0)
        
        if response.status_code != 200:
            return {"error": f"Airia API Error: {response.text}"}
            
        return response.json()
