import os
from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from app.services.pdf_service import upload_file

upload_router = APIRouter()


@upload_router.post('/upload', status_code=201)
async def upload_pdf(file: UploadFile=File(...)):
    result = await upload_file(file)
    return result
    

    

