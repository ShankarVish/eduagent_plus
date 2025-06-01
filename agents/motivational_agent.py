from crewai import Agent
from prompts.templates import MOTIVATION_PROMPT

def create_motivational_agent(llm):
    return Agent(
        role="Motivational Agent",
        goal="Keep the user motivated and engaged",
        backstory="Encourages learners with timely feedback, quotes, and tips.",
        verbose=True,
        llm=llm,
        prompt_template=MOTIVATION_PROMPT
    )
