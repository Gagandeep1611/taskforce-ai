from config import get_openai_client
from schema.chat import ChatResponse, ChatRequest

client = get_openai_client()

def generate_response(request : ChatRequest):
    response = client.responses.create(
        model = "gpt-5.4-nano",
        input=request.question
    )
    response_request = ChatResponse(
        response = response.output_text,
    )
    return response_request

