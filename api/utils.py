from pathlib import Path
import os
import fitz
from docx import Document
import io

def extract_text_from_file(file_bytes: bytes, filename: str) -> str:
    """Detects file type and extracts text using lightweight libraries."""
    ext = filename.split('.')[-1].lower()
    
    if ext == 'pdf':
        doc = fitz.open(stream=file_bytes, filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text("text") + "\n"
        
        if not text.strip() and len(doc) > 0:
            return "ERROR_IMAGE_ONLY_PDF"
            
        return text

    elif ext in ['docx', 'doc']:
        f = io.BytesIO(file_bytes)
        try:
            doc = Document(f)
            return "\n".join([para.text for para in doc.paragraphs])
        except:
            return "ERROR_CORRUPT_WORD"

    return "Unsupported file format."



def chunk_text(text: str, max_chars: int = 5000):
    """Utility to break large contracts into digestible parts for the AI."""
    return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]
