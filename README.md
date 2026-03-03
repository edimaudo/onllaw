# onllaw

**onllaw** is a Legal Decision Support System focused on democratizing access to employment law in Ontario by providing contract review and employment rights Q&A.

## Key Features
- **Employment Standards Q&A**: Summarized answers regarding Ontario employment rights.
- **Dual-Mode Contract Review**:
    - **Full Review**: Upload `.pdf`, `.doc`, `.docx` files for compliance check.
    - **Clause Spotlight**: Paste specific sections (e.g., Termination, Non-solicit) for targeted review.

## Technological Implementation
- **AI Orchestration**: Airia
- **Backend**: FastAPI
- **Frontend**: Jinja2

## Project Structure
```
onllaw/
├── api/
│   ├── main.py         
│   ├── agents.py       
│   └── utils.py        
├── templates/
│   ├── base.html       
│   ├── index.html      
│   ├── qa.html         
│   ├── audit.html      
│   └── 404.html              
├── requirements.txt    
├── vercel.json         
└── README.md
```
