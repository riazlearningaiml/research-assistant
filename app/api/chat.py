from fastapi import APIRouter, HTTPException

from app.models.question_request import QuestionRequest
from app.services.rag_service import answer_question

chat_router = APIRouter()


@chat_router.post("/ask")
async def ask(request: QuestionRequest):

    try:
        print(request.filename)
        result = answer_question(
            filename=request.filename,
            question=request.question
        )
        return result
    except FileNotFoundError as ex:
        raise HTTPException(status_code=404, detail=str(ex))
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))