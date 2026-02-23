# onllaw

**onllaw** is a Legal Decision Support System focused on democratizing access to employment law in Ontario by providing instant contract audits and rights-based Q&A.

## Key Features
- **Employment Standards Q&A**: Summarized answers regarding Ontario employment rights.
- **Dual-Mode Contract Audit**:
    - **Full Audit**: Upload `.pdf` or `.docx` files for a comprehensive compliance check.
    - **Clause Spotlight**: Paste specific sections (e.g., Termination, Non-solicit) for instant, targeted analysis.

## Technological Implementation
- **AI Orchestration**: [Airia](https://airia.com)
- **Backend**: FastAPI (Python 3.11+)
- **Frontend**: Jinja2 + Tailwind CSS .

## Project Structure
```
onllaw/
├── api/
│   ├── main.py         # Entry point & FastAPI routing
│   ├── agents.py       # Airia SDK orchestration logic
│   └── utils.py        # Docling document extraction & text cleaning
├── templates/
│   ├── base.html       
│   ├── index.html      
│   ├── qa.html         
│   ├── audit.html      
│   └── 404.html        
├── static/             
├── requirements.txt    
├── vercel.json         
└── README.md

## Setup
pip install -r requirements.txt

Configure .env with AIRIA_API_KEY and AIRIA_AGENT_ID.

Start locally: uvicorn api.main:app --reload
