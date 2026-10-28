from datetime import datetime
from crewai import Task
from agents import research_agent

current_date = datetime.now().strftime("%B %d, %Y")

research_task = Task(
    description=(
        f"Today's date is {current_date}.\n"
        f"Your goal is to gather the top 5 most important artificial intelligence news stories from the past week.\n"
        f"Conduct 2 to 3 targeted searches using keywords like 'Artificial Intelligence news', 'OpenAI Anthropic', or 'Google AI release'.\n"
        f"Any story published within the past 7 days of {current_date} is valid.\n"
        f"Compile exactly 5 high-impact stories. Include headline, date, source, a concise summary, and the link."
    ),
    expected_output=(
        "A structured Markdown report containing the top 5 AI news stories from this week.\n"
        "Each story must have:\n"
        "- Headline (### Title)\n"
        "- Date and Source\n"
        "- 2-3 sentence clear summary\n"
        "- Clickable markdown link [Read Full Story](URL)"
    ),
    agent=research_agent,
)