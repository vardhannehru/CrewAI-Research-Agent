from crewai import Crew, Process

from agents import research_agent
from tasks import research_task

news_crew = Crew(
    agents=[research_agent],

    tasks=[research_task],

    process=Process.sequential,

    verbose=True
)