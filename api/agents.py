import os
import httpx
import json
from fastapi import HTTPException

AIRIA_API_URL = os.getenv("AIRIA_API_URL")
AIRIA_KEY = os.getenv("AIRIA_API_KEY")
AIRIA_AGENT_ID = os.getenv("AIRIA_AGENT_ID")


async def ask_esa_lawyer(question: str):
    """
    Logic to communicate with the Airia execution endpoint.
    """

    if not AIRIA_KEY or not AIRIA_AGENT_ID:
        raise HTTPException(
            status_code=500,
            detail="Airia configuration (API Key or Agent ID) is missing",
        )

    headers = {"X-API-Key": AIRIA_KEY, "Content-Type": "application/json"}

    # Payload structure - ensure 'input' matches your Agent's expected schema
    payload = {
        "agent_id": AIRIA_AGENT_ID,
        "UserInput": question,
        "UserId": os.getenv("AIRIA_USER_ID"), 
    }

    async with httpx.AsyncClient() as client:
        try:
            # 3. Execution call
            response = await client.post(
                AIRIA_API_URL, json=payload, headers=headers, timeout=10 #60.0
            )

            response.raise_for_status()

            data = response.json()

            answer = (
                data.get("output")
                or data.get("response")
                or data.get("result")
                or data.get("text")
                or "The agent processed the request but returned an empty or unknown format."
            )

            if isinstance(answer, str):
                try:
                    
                    answer = json.loads(answer)
                except json.JSONDecodeError:
                    
                    pass

            if isinstance(answer, dict):
                summary = answer.get("legal_summary", "")
                enforce = answer.get("enforceability_status", "")
                sections = answer.get("applicable_sections", "")
                steps = answer.get("recommended_next_steps", "")
                email_hr = answer.get("email_draft_hr", "")
                email_lawyer = answer.get("email_draft_lawyer", "")
                disclaimer = answer.get("disclaimer", "")

                answer = (
                    f"### LEGAL ANALYSIS\n{summary}\n\n"
                    f"### STATUS\n{enforce}\n\n"
                    f"### APPLICABLE SECTIONS\n{sections}\n\n"
                    f"### RECOMMENDED NEXT STEPS\n{steps}\n\n"
                )
                
                # Only add the email section if it actually exists
                if email_hr:
                    answer += f"### DRAFT HR EMAIL \n{email_hr}\n\n"
                if email_lawyer:
                    answer += f"### DRAFT lawyer EMAIL \n{email_lawyer}\n\n"
                
                answer += f"NOTICE: {disclaimer}"

            return str(answer)

        except httpx.HTTPStatusError as e:

            error_detail = (
                f"Airia API Error: {e.response.status_code} - {e.response.text}"
            )
            print(error_detail) 
            raise HTTPException(status_code=500, detail=error_detail)

        except Exception as e:
            raise HTTPException(
                status_code=500, detail=f"Internal Logic Error: {str(e)}"
            )
