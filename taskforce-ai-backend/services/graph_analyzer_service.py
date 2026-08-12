import base64

from config import get_openai_client

client = get_openai_client()

async def analyze_graph(image):

    image_bytes = await image.read()
    base64_image = base64.b64encode(image_bytes).decode("utf-8")

    response = client.responses.create(
        model="gpt-5.4-nano",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": """If this image is a graph, chart, or statistical representation,
                    analyze its patterns, trends, and observations.
                    If it is not, respond with:
                    'This is not the required input image.'"""
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:{image.content_type};base64,{base64_image}"
                    }
                ]
            }
        ]

    )

    return {
        "analysis": response.output_text
    }