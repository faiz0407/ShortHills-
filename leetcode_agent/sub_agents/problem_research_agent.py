"""Problem Research Agent — finds relevant LeetCode problems using web search and curated lists."""

from google.adk.agents import Agent

from ..tools.search_web import search_web
from ..tools.extract_problem_links import extract_problem_links


problem_research_agent = Agent(
    name="ProblemResearchAgent",
    model="groq/llama-3.3-70b-versatile",
    description="Finds relevant LeetCode problems for a given topic using web search and curated problem lists.",
    instruction="""
You are a LeetCode problem research specialist.

When given a DSA topic:

1. Use the `search_web` tool to search for "best LeetCode problems for <topic>".
2. Use the `extract_problem_links` tool to get curated problem recommendations.
3. Combine the search results and curated problems into a clean, organized list.

**Output format:**
- List each problem with its name, URL, and difficulty (Easy/Medium/Hard).
- Group problems by difficulty level.
- Include 5–10 problems total.

Do NOT make up problem URLs — only use URLs from the tools.
""",
    tools=[search_web, extract_problem_links],
)