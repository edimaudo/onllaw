import os
import httpx
from pydantic import BaseModel

AIRIA_API_URL = "https://api.airia.com/v1/execute"
AIRIA_KEY = os.getenv("AIRIA_API_KEY")

async def call_airia_agent(user_input: str, mode: str = "qa", context: str = ""):
    """
    Unified caller for Airia Agents.
    mode: 'qa' for general questions, 'audit' for contract review.
    """
    headers = {
        "X-API-Key": AIRIA_KEY,
        "Content-Type": "application/json"
    }
    
    # We define the behavior based on the mode
    if mode == "audit":
        system_instruction = "Audit this contract text against Ontario ESA. Identify illegal clauses."
    else:
        system_instruction = "Answer this employment law question based on current Ontario statutes."

    payload = {
        "agent_id": os.getenv("AIRIA_AGENT_ID"),
        "input": {
            "instruction": system_instruction,
            "text_content": context if context else user_input,
            "jurisdiction": "Ontario",
            "date_ref": "2026"
        }
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(AIRIA_API_URL, json=payload, headers=headers, timeout=60.0)
        
        if response.status_code != 200:
            return {"error": f"Agent Error: {response.status_code}"}
            
        return response.json().get("output", "No response.")
        return response.json()
