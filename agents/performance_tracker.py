from crewai import Agent
from prompts.templates import PERFORMANCE_PROMPT

def create_performance_tracker(llm):
    return Agent(
        role="Performance Tracker",
        goal="Track performance and suggest next steps",
        backstory="Analyzes performance metrics and guides learning flow.",
        verbose=True,
        llm=llm,
        prompt_template=PERFORMANCE_PROMPT
    )
