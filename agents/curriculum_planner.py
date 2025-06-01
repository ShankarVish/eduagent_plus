from crewai import Agent
from prompts.templates import CURRICULUM_PROMPT

def create_curriculum_planner(llm):
    return Agent(
        role="Curriculum Planner",
        goal="Create a personalized learning schedule",
        backstory="Specialized in breaking down large subjects into daily learning goals.",
        verbose=True,
        llm=llm,
        prompt_template=CURRICULUM_PROMPT
    )
