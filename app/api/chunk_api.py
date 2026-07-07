from app.storage.text_storage import EXTRACTED_DIR
from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.services.pdf_service import process_pdf
from app.services.chuk_service import chunk_service
chunk_router = APIRouter()

EXTRACTED_DIR = Path("data/extracted")

@chunk_router.post("/chunk_api")
async def chunk_api(filename: str):

    file_path = EXTRACTED_DIR / filename
    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} does not exist.")
    result = chunk_service(filename)
    return {"message":"Chunked Sucessfully", "embedding_file":result['embedding_file']}