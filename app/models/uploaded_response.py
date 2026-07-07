from pydantic import BaseModel

class UploadResponse(BaseModel):
    status: str
    filename: str
    saved_to: str