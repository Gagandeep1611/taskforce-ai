import os
from dotenv import load_dotenv
from openai import OpenAI

openai_key = os.getenv('OPEN_AI_API_KEY')
load_dotenv()

def get_openai_client():
    api_key = os.getenv('OPEN_AI_API_KEY')
    client = OpenAI(api_key=api_key)
    return client

