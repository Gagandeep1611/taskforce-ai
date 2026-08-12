from fastapi import APIRouter
from starlette.responses import StreamingResponse

from models.chat import ChatRequest
from services.chat_service import generate_response

router = APIRouter()


@router.post("/chat")
def stream_chat(request: ChatRequest):
    return StreamingResponse(
        generate_response(request),
        media_type="text/plain"
    )
