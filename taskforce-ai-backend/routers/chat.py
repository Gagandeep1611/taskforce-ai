from fastapi import APIRouter

from schema.chat import ChatResponse, ChatRequest
from services.chat_service import generate_response

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    return generate_response(request)
