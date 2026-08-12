from fastapi import APIRouter

from services.productivity_service import process_request

router = APIRouter()

@router.post("/productivity")
def productivity(request:str):
    return {
        "response": process_request(request)
    }
