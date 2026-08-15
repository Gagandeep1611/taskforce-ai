from dotenv import load_dotenv
import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient

from models.job_search import AgentResponse

load_dotenv()
tavily = TavilyClient()

@tool
def search(query: str)-> str:
    """Search for information relevant to the user's query."""
    print(f"Searching for {query}")
    return tavily.search(query=query)


llm = ChatOpenAI(model = "gpt-5.4-nano")
tools = [search]

agent = create_agent(model = llm, tools=tools, response_format=AgentResponse)


def run():
    print("Running application")
    result = agent.invoke({"messages": HumanMessage(content="Search for 5 job postings with java and 2 years experience required in India and list their details")})
    print(result)

if __name__ == "__main__":
    run()