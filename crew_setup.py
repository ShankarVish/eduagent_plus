from crewai import Crew, Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini", 
    temperature=1.2
)

def build_crew() -> Crew:
    curriculum_planner = Agent(
        name="Curriculum Planner Agent",
        role="Plan study curriculum based on goals and time",
        goal="Create a detailed study plan with topics and timeline",
        backstory="Expert in curriculum design and scheduling",
        llm=llm
    )

    content_generator = Agent(
        name="Content Generator Agent",
        role="Generate summaries, notes, and flashcards for topics",
        goal="Provide easy-to-understand content for learning",
        backstory="Skilled content creator and educator",
        llm=llm
    )

    quiz_generator = Agent(
        name="Quiz Generator Agent",
        role="Create quizzes and MCQs to evaluate learning",
        goal="Test user knowledge on the given topics",
        backstory="Experienced quiz maker and evaluator",
        llm=llm
    )

    performance_tracker = Agent(
        name="Performance Tracker Agent",
        role="Track user progress and quiz results",
        goal="Adjust study plans based on performance",
        backstory="Analyst tracking learning improvements",
        llm=llm
    )

    motivational_agent = Agent(
        name="Motivational Agent",
        role="Send motivational messages and learning tips",
        goal="Keep user motivated and engaged in learning",
        backstory="Motivational coach and supporter",
        llm=llm
    )

    crew = Crew(
        name="EduAgent+ Crew",
        agents=[
            curriculum_planner,
            content_generator,
            quiz_generator,
            performance_tracker,
            motivational_agent,
        ],
    )

    return crew
