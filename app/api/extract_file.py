from fastapi import APIRouter, HTTPException
from pathlib import Path
from app.services.pdf_service import process_pdf

extract_router = APIRouter()


@extract_router.post("/extract_pdf")
async def extract_pdf(filename: str):

    try:

        result = process_pdf(filename)

        return result

    except FileNotFoundError as ex:

        raise HTTPException(
            status_code=404,
            detail=str(ex)
        )

    except Exception as ex:

        raise HTTPException(
            status_code=500,
            detail=str(ex)
        )