from crewai import Agent
from crewai import LLM
from dotenv import load_dotenv
import os

from tools import search_ai_news

load_dotenv()

llm = LLM(
    model="anthropic/claude-haiku-5-5",
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

research_agent = Agent(
    role="AI News Research Specialist",

    goal="""
    Search the internet and find the latest AI news.
    """,

    backstory="""
    You are an experienced AI journalist.

    Your job is to search the internet for the latest
    AI news from reliable sources.

    Always provide accurate and up-to-date information.
    """,

    llm=llm,

    tools=[search_ai_news],

    verbose=True
)