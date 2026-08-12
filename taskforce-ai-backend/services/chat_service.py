from config import get_openai_client
from models.chat import ChatRequest

client = get_openai_client()

def generate_response(request : ChatRequest):
    stream = client.responses.create(
        model = "gpt-5.4-nano",
        input=request.question,
        stream=True
    )

    for event in stream:
        if event.type == "response.output_text.delta":
            yield event.delta

