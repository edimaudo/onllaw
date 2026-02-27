import os
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

AIRIA_API_URL = os.getenv("AIRIA_API_URL") 
AIRIA_KEY = os.getenv("AIRIA_API_KEY")
AIRIA_AGENT_ID = os.getenv("AIRIA_AGENT_ID")

async def ask_esa_lawyer(question: str):
    """
    Logic to communicate with the Airia execution endpoint.
    This function is called by the /api/qa route in main.py.
    """
    
    # 1. Validation to prevent 500 errors before calling the API
    if not AIRIA_KEY or not AIRIA_AGENT_ID:
        raise HTTPException(status_code=500, detail="Airia configuration (API Key or Agent ID) is missing in .env")

    headers = {
        "X-API-Key": AIRIA_KEY,
        "Content-Type": "application/json"
    }
    
    # 2. Payload structure - ensure 'input' matches your Agent's expected schema
    payload = {
        "agent_id": AIRIA_AGENT_ID,
        "input": question 
    }

    async with httpx.AsyncClient() as client:
        try:
            # 3. Execution call
            response = await client.post(
                AIRIA_API_URL, 
                json=payload, 
                headers=headers, 
                timeout=60.0
            )
            
            # This will raise an error for 4xx or 5xx responses from Airia
            response.raise_for_status()
            
            data = response.json()
            
            # 4. RESILIENT KEY CHECKING
            # This prevents the 500 error if Airia labels the response differently
            answer = (
                data.get("output") or 
                data.get("response") or 
                data.get("result") or 
                data.get("text") or 
                "The agent processed the request but returned an empty or unknown format."
            )
            
            return answer
            
        except httpx.HTTPStatusError as e:
            # If Airia returns an error, we capture the actual message from their server
            error_detail = f"Airia API Error: {e.response.status_code} - {e.response.text}"
            print(error_detail) # Helpful for your terminal logs
            raise HTTPException(status_code=500, detail=error_detail)
            
        except Exception as e:
            # Captures timeouts or connection issues
            raise HTTPException(status_code=500, detail=f"Internal Logic Error: {str(e)}")
