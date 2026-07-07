from pathlib import Path

from app.parser.pdf_parser import extract_text
from app.storage.text_storage import save_text
from fastapi import HTTPException, UploadFile
from app.models.uploaded_response import UploadResponse

UPLOAD_DIR = Path("data/uploads")
EXTRACT_DIR = Path("data/extracted")

async def upload_file(file: UploadFile) -> UploadResponse:

    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    if (
        not file.filename.lower().endswith(".pdf")
        or file.content_type != "application/pdf"
    ):
        raise HTTPException(
            status_code=400, 
            detail="Invalid file type. Only PDF files are accepted."
        )
    save_path = UPLOAD_DIR / file.filename
    try:
        # 3. Read the uploaded streams and write to the destination path
        with open(save_path, "wb") as buffer:
            while chunk := await file.read(1024 * 1024):
                buffer.write(chunk)
            
        return UploadResponse(
            status="success",
            filename=file.filename,
            saved_to=str(save_path)
        )
        
    except HTTPException:
        raise

    except Exception as e:
        # Handle unexpected I/O errors gracefully
        raise HTTPException(
            status_code=500, 
            detail=f"An error occurred while saving the file: {str(e)}"
        )


def process_pdf(filename: str) -> dict:
    """
    Complete PDF processing pipeline.

    PDF
      ↓
    Extract Text
      ↓
    Save TXT
      ↓
    Return Result
    """

    text, pages = extract_text(filename)
    saved_path = save_text(filename, text)
    filename = Path(saved_path).name
    return {
        "pages": pages,
        "text_file": filename
    }