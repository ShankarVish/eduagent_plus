from crewai import Agent
from prompts.templates import CONTENT_PROMPT

def create_content_generator(llm):
    return Agent(
        role="Content Generator",
        goal="Summarize and explain concepts clearly",
        backstory="Expert at turning topics into digestible summaries and notes.",
        verbose=True,
        llm=llm,
        prompt_template=CONTENT_PROMPT
    )
