from fastapi import APIRouter, UploadFile, File, Form
from services.graph_analyzer_service import analyze_graph

router = APIRouter()

@router.post("/analyze")
async def analyze_image(image: UploadFile = File(...)):
    return await analyze_graph(image)