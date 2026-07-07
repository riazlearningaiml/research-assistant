from asyncio import coroutines
import fitz
from pathlib import Path

EXTRACT_DIR = Path("data/extracted")
UPLOAD_DIR = Path("data/uploads")

def extract_text(pdf_file: str) ->tuple[str, int]:
    """
    Read a PDF from disk and return:
        - extracted text
        - total number of pages
    """
    
    pdf_path = UPLOAD_DIR / pdf_file
    if not pdf_path.exists():
        raise FileNotFoundError(f'{pdf_path} not found.')

    extracted_pages = []
    with fitz.open(pdf_path) as doc:

        total_pages = len(doc)

        for page_number, page in enumerate(doc, start=1):

            text = page.get_text("text").strip()

            if text:
                extracted_pages.append(
                    f"--- Page {page_number} ---\n{text}\n"
                )

    final_text = "\n".join(extracted_pages)

    return final_text, total_pages