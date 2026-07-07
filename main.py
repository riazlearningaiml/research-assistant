from fastapi import FastAPI
from app.api.upload_file import upload_router
from app.api.extract_file import extract_router
from app.api.chat import chat_router
from app.api.chunk_api import chunk_router

app = FastAPI(title="Research Assistant API")
app.include_router(upload_router)
app.include_router(extract_router)
app.include_router(chat_router)
app.include_router(chunk_router)