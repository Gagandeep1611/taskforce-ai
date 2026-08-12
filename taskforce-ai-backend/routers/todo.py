from fastapi import APIRouter
from services.todo_service import get_structured_response, get_todos
from schema.todo import Todo

router = APIRouter()

@router.post("/todo", response_model=Todo)
def get_structured_todo(input: str):
    response = get_structured_response(input)
    return response

@router.get("/todo/all")
def get_all_todos():
    return get_todos()