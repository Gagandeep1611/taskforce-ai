from config import get_openai_client
from schema.todo import Todo

client = get_openai_client()

def get_structured_response(user_input: str):
    response = client.responses.parse(
        model = "gpt-5.4-nano",
        input = user_input,
        instructions = "Extract the todo information",
        text_format = Todo
    )
    return response.output_parsed