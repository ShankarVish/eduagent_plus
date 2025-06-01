from crewai import Agent

def create_coordinator(llm):
    return Agent(
        role="Coordinator",
        goal="Manage the workflow and communicate with other agents",
        backstory="Responsible for orchestrating the sequence of tasks for personalized learning.",
        verbose=True,
        llm=llm
    )
