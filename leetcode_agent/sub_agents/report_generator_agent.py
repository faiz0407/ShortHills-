"""Report Generator Agent — assembles the final structured learning guide."""

from google.adk.agents import Agent

from ..tools.format_learning_plan import format_learning_plan


report_generator_agent = Agent(
    name="ReportGeneratorAgent",
    model="groq/llama-3.3-70b-versatile",
    description="Formats and assembles the final structured LeetCode learning guide from all collected information.",
    instruction="""
You are a report formatting specialist.

You will receive information gathered by other agents:
- A list of recommended LeetCode problems (from ProblemResearchAgent)
- Tutorial summaries (from TutorialFinderAgent)
- A 7-day practice schedule (from PracticeRecommenderAgent)

Your job:

1. Use the `format_learning_plan` tool to combine everything into a polished guide.
   - Pass the topic name as `topic`
   - Pass the problems list as `problems`
   - Pass the tutorial summaries as `tutorials`
   - Pass the practice schedule as `schedule`

2. Present the formatted output as-is — do not add extra commentary.

The final output should be a complete, self-contained learning guide that
a user can follow from start to finish.
""",
    tools=[format_learning_plan],
)