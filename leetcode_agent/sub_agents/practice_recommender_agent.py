"""Practice Recommender Agent — generates structured practice schedules."""

from google.adk.agents import Agent

from ..tools.generate_practice_schedule import generate_practice_schedule


practice_recommender_agent = Agent(
    name="PracticeRecommenderAgent",
    model="groq/llama-3.3-70b-versatile",
    description="Generates a structured 7-day practice schedule with progressive difficulty for a given DSA topic.",
    instruction="""
You are a study plan specialist for LeetCode preparation.

When given a topic:

1. Use the `generate_practice_schedule` tool to create a 7-day schedule.
2. Present the schedule in a clear, day-by-day format.

**Output format:**
For each day, include:
- **Day X: [Theme]**
- Tasks to complete (as a bullet list)
- Daily goal

Add a brief motivational note at the end encouraging consistent practice.
Do NOT modify the schedule structure — present it as returned by the tool.
""",
    tools=[generate_practice_schedule],
)