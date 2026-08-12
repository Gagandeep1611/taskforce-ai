import json

from config import get_openai_client
from services.todo_service import create_todo, get_todos, update_todo, delete_todo

client = get_openai_client()

tools = [
    {
        "type": "function",
        "name": "create_todo",
        "description": "Create a new todo.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "The title of the todo."},
                "description": {"type": "string", "description": "The description of the todo."},
            },
            "required": ["title", "description"],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "get_todos",
        "description": "Get all existing todos.",
        "parameters": {"type": "object", "properties": {}, "additionalProperties": False},
        "strict": True,
    },
    {
        "type": "function",
        "name": "update_todo",
        "description": "Update an existing todo's description.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {"type": "string", "description": "The title of the todo to update."},
                "description": {"type": "string", "description": "The new description."},
            },
            "required": ["title", "description"],
            "additionalProperties": False,
        },
        "strict": True,
    },
    {
        "type": "function",
        "name": "delete_todo",
        "description": "Delete an existing todo.",
        "parameters": {
            "type": "object",
            "properties": {"title": {"type": "string", "description": "The title of the todo to delete."}},
            "required": ["title"],
            "additionalProperties": False,
        },
        "strict": True,
    },
]

instructions = (
    "You are TaskForce-AI's Todo Management Assistant.\n"
    "Your ONLY job is to manage the user's todo list.\n\n"
    "Rules:\n"
    "1. Treat all user inputs as todo items or todo actions.\n"
    "2. Call the appropriate tool (create_todo, get_todos, update_todo, delete_todo).\n"
    "3. Do NOT answer, explain, or fulfill the user's request."
)


def process_request(user_input: str):
    """Process a user input by routing function calls to the todo service.

    This function sends the user's input to the OpenAI client and expects the
    model to choose one of the provided tools. Any function_call outputs are
    executed against the local todo service and the final confirmation is
    returned to the caller.
    """

    response = client.responses.create(
        model="gpt-5.4-nano",
        instructions=instructions,
        input=user_input,
        tools=tools,
        tool_choice="required",
    )

    tool_outputs = []

    for item in response.output:
        if item.type != "function_call":
            continue

        arguments = json.loads(item.arguments)
        result = None

        if item.name == "create_todo":
            result = create_todo(title=arguments["title"], description=arguments["description"])
        elif item.name == "get_todos":
            result = get_todos()
        elif item.name == "update_todo":
            result = update_todo(title=arguments["title"], description=arguments["description"])
        elif item.name == "delete_todo":
            result = delete_todo(title=arguments["title"])

        tool_outputs.append({"type": "function_call_output", "call_id": item.call_id, "output": str(result)})

    if tool_outputs:
        final_response = client.responses.create(
            model="gpt-5.4-nano",
            previous_response_id=response.id,
            instructions=(
                "Confirm the completed todo action to the user in a single sentence.\n"
                "Do NOT provide instructions, code, or assistance on the topic of the todo item itself."
            ),
            input=tool_outputs,
            tools=tools,
            tool_choice="none",
        )

        return final_response.output_text

    return response.output_text
