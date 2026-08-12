from config import get_openai_client
from schema.todo import Todo

client = get_openai_client()

Todos = [Todo(
        title="Learn FastAPI",
        description="Complete the FastAPI backend section"
        ),
        Todo(
            title="Learn OpenAI APIs",
            description="Implement Structured Outputs and Tool Calling"
        ),
        Todo(
            title="Build TaskForce-AI",
            description="Complete the Phase 9 features"
        )
]

def get_structured_response(user_input: str):
    response = client.responses.parse(
        model = "gpt-5.4-nano",
        input = user_input,
        instructions = "Extract the todo information",
        text_format = Todo
    )
    create_todo(response.output_parsed.title,response.output_parsed.description)
    return response.output_parsed

def create_todo(title: str, description: str):
    new_todo = Todo(
        title=title,
        description=description
    )
    Todos.append(new_todo)
    return new_todo

def get_todos():
    return Todos


def update_todo(title: str, description: str):
    for todo in Todos:
        if todo.title == title:
            todo.description = description
            return todo

    return None


def delete_todo(title: str):
    for todo in Todos:
        if todo.title == title:
            Todos.remove(todo)
            return todo

    return None



