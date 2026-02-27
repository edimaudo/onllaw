import os
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


AIRIA_API_URL = os.getenv("AIRIA_API_URL") 
AIRIA_KEY = os.getenv("AIRIA_API_KEY")
AIRIA_AGENT_ID = os.getenv("AIRIA_AGENT_ID")

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_esa_lawyer(request: QuestionRequest):
    headers = {
        "X-API-Key": AIRIA_KEY,
        "Content-Type": "application/json"
    }
    
    # Simplified payload: 'input' is now just the raw string from the user
    payload = {
        "agent_id": AIRIA_AGENT_ID,
        "input": request.question 
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(AIRIA_API_URL, json=payload, headers=headers, timeout=60.0)
            response.raise_for_status()
            
            # Airia 2026 typically returns the result in a field named 'output'
            data = response.json()
            return {"answer": data.get("output", "The agent could not process this request.")}
            
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
