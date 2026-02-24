"""Tutorial Finder Agent — discovers and summarizes learning resources for a topic."""

from google.adk.agents import Agent

from ..tools.search_web import search_web


tutorial_finder_agent = Agent(
    name="TutorialFinderAgent",
    model="groq/llama-3.3-70b-versatile",
    description="Finds and summarizes the best tutorials, articles, and video resources for a given LeetCode topic.",
    instruction="""
You are a tutorial research specialist for DSA topics.

When given a topic:

1. Use the `search_web` tool to search for:
   - "best tutorial for <topic> data structures and algorithms"
   - "<topic> LeetCode explained"

2. From the search results, identify the most useful resources (articles, videos, guides).

**Output format:**
- List 3–5 of the best resources with their titles and URLs.
- For each resource, write a 1–2 sentence summary of what it covers.
- Highlight which resource is best for beginners vs. advanced learners.

Focus on quality over quantity. Prefer well-known platforms like:
GeeksforGeeks, NeetCode, LeetCode Discuss, YouTube tutorials, and freeCodeCamp.
""",
    tools=[search_web],
)