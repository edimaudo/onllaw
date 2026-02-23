from docling.document_converter import DocumentConverter
from pathlib import Path
import os

converter = DocumentConverter()

def extract_text_from_file(file_path: str) -> str:
    """Extracts clean markdown text from PDF or DOCX using Docling."""
    try:
        result = converter.convert(file_path)
        # Exporting to markdown preserves legal structure (headings, lists)
        return result.document.export_to_markdown()
    except Exception as e:
        return f"Error processing document: {str(e)}"

def chunk_text(text: str, max_chars: int = 5000):
    """Utility to break large contracts into digestible parts for the AI."""
    return [text[i:i+max_chars] for i in range(0, len(text), max_chars)]
