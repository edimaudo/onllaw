from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from .utils import extract_text_from_file
from .agents import ask_esa_lawyer
import shutil
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")
#app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def landing(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.exception_handler(404)
async def custom_404_handler(request: Request, __):
    return templates.TemplateResponse("404.html", {"request": request}, status_code=404)

@app.post("/api/audit")
 async def handle_audit(
     file: UploadFile = File(None), 
     clause_text: str = Form(None)
 ):
     context = ""
    # Check if user uploaded a file OR pasted a clause
    if file:
        temp_path = f"temp_{file.filename}"
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        context = extract_text_from_file(temp_path)
        os.remove(temp_path)
    elif clause_text:
        context = clause_text

    #
    analysis = ''#await call_airia_agent("Audit this for 2026 ESA compliance", context)
    return analysis


@app.get("/api/qa", response_class=HTMLResponse)
async def get_qa_page(request: Request):
    """Reasoning: This renders the UI when the user clicks the link."""
    return templates.TemplateResponse("qa.html", {"request": request})

@app.post("/api/qa")
async def handle_qa_logic(question: str = Form(...)):
    """Reasoning: This processes the actual AI question after the user hits submit."""
    answer = await ask_esa_lawyer(question)
    return {"answer": answer}
    return response

@app.get("/api/lawyers", response_class=HTMLResponse)
async def get_lawyers_page(request: Request):
    """
    Serves the list of LSO Certified Specialists. 
    """
    specialists = [
        {"name": "S. Margot Blight", "firm": "S. Margot Blight, Lawyer", "city": "Mississauga"},
        {"name": "David Bannon", "firm": "Hicks Morley Hamilton Stewart Storie LLP", "city": "Toronto"},
        {"name": "Matthew Louis Certosimo", "firm": "Borden Ladner Gervais LLP", "city": "Toronto"},
        {"name": "Patrick Michael Rory Groom", "firm": "McMillan LLP", "city": "Toronto"},
        {"name": "John Hyde", "firm": "Hyde HR Law", "city": "Toronto"},
        {"name": "Donald B. Jarvis", "firm": "Filion Wakely Thorup Angeletti LLP", "city": "Toronto"},
        {"name": "Jeffrey David Arthur Murray", "firm": "Stringer LLP", "city": "Toronto"},
        {"name": "Garth O'Neill", "firm": "GOLaw Professional Corporation", "city": "Thunder Bay"},
        {"name": "Donald Shanks", "firm": "Cheadles LLP", "city": "Thunder Bay"},
        {"name": "Ronald Snyder", "firm": "Xphoria Spirits Inc.", "city": "Ottawa"}
    ]
    
    return templates.TemplateResponse("lawyers.html", {
        "request": request, 
        "specialists": specialists
    })
