"""LeetCode Learning Assistant — Root Agent.

A multi-agent system built with Google ADK that generates structured
LeetCode learning guides using Groq/Llama 3 70B for inference.
"""

from dotenv import load_dotenv

# Load environment variables before agent initialization
load_dotenv()

from google.adk.agents import Agent  # noqa: E402

from .sub_agents.problem_research_agent import problem_research_agent  # noqa: E402
from .sub_agents.tutorial_finder_agent import tutorial_finder_agent  # noqa: E402
from .sub_agents.practice_recommender_agent import practice_recommender_agent  # noqa: E402
from .sub_agents.report_generator_agent import report_generator_agent  # noqa: E402


root_agent = Agent(
    name="LeetCodeLearningAssistant",
    model="groq/llama-3.3-70b-versatile",
    description="Orchestrates multiple specialist agents to generate a comprehensive, structured LeetCode learning guide for any DSA topic.",
    instruction="""
You are the LeetCode Learning Assistant — an orchestrator that coordinates
multiple specialist agents to create comprehensive study guides.

When a user provides a DSA topic (e.g., "dynamic programming", "binary search",
"graphs", "two pointers"):

**Step 1:** Delegate to `ProblemResearchAgent` to find relevant LeetCode problems.
**Step 2:** Delegate to `TutorialFinderAgent` to find and summarize tutorials.
**Step 3:** Delegate to `PracticeRecommenderAgent` to generate a 7-day practice schedule.
**Step 4:** Send ALL gathered information to `ReportGeneratorAgent` to format the final guide.

**Important rules:**
- Always run Steps 1–3 before Step 4.
- Pass the complete output from each agent to ReportGeneratorAgent.
- If a user asks a general question (not a topic request), answer directly.
- If the topic is unclear, ask the user to clarify.

**Example interaction:**
User: "Create a learning guide for binary search"
→ You delegate to each sub-agent in order, then return the final formatted guide.
""",
    sub_agents=[
        problem_research_agent,
        tutorial_finder_agent,
        practice_recommender_agent,
        report_generator_agent,
    ],
)