from crewai import Agent
from prompts.templates import QUIZ_PROMPT

def create_quiz_generator(llm):
    return Agent(
        role="Quiz Generator",
        goal="Create quizzes to test the user's understanding",
        backstory="Experienced in educational assessments and MCQ generation.",
        verbose=True,
        llm=llm,
        prompt_template=QUIZ_PROMPT
    )
