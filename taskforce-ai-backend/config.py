from dotenv import load_dotenv
from openai import OpenAI
import os
load_dotenv()


def get_openai_client():
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return client

