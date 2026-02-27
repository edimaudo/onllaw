import os
import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

AIRIA_API_URL = os.getenv("AIRIA_API_URL") 
AIRIA_KEY = os.getenv("AIRIA_API_KEY")
AIRIA_AGENT_ID = os.getenv("AIRIA_AGENT_ID")

async def ask_esa_lawyer(question: str):
    """
    This is a PURE function. No FastAPI decorators here.
    It is called by main.py.
    """
    headers = {
        "X-API-Key": AIRIA_KEY,
        "Content-Type": "application/json"
    }
    
    payload = {
        "agent_id": AIRIA_AGENT_ID,
        "input": question 
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(AIRIA_API_URL, json=payload, headers=headers, timeout=60.0)
        response.raise_for_status()
        data = response.json()
        return data.get("output", "The agent could not process this request.")
