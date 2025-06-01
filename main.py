from crew_setup import build_crew
from crewai import Task

if __name__ == "__main__":
    print("What do you want to learn?", end=" ")
    topic = input().strip()

    print("In how many days?", end=" ")
    days = input().strip()

    task_description = f"I want to learn {topic} in {days} days"

    crew = build_crew()

    # Define a Task object for the crew
    crew.tasks = [
        Task(
            description=task_description,
            agent=crew.agents[0],  # Start with the Curriculum Planner
            expected_output=f"A detailed {days}-day curriculum for learning {topic}."
        )
    ]

    print("\nStarting the EduAgent+ multi-agent process...\n")
    result = crew.kickoff()

    print("\n===== Final Output =====")
    print(result)
