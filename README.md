# 📘 LeetCode Learning Assistant

A multi-agent AI system built with [Google ADK](https://google.github.io/adk-docs/) that generates comprehensive, structured LeetCode learning guides for any DSA topic.

## Architecture

```
LeetCodeLearningAssistant (Root Orchestrator — Gemini 2.0 Flash)
├── ProblemResearchAgent     → Gemini + google_search + custom tools
├── TutorialFinderAgent      → Gemini + google_search + custom tools
├── PracticeRecommenderAgent → Groq/Llama 3 70B + custom tools
└── ReportGeneratorAgent     → Groq/Llama 3 70B + custom tools
```

**Models used:**
- **Gemini 2.0 Flash** — for agents using the built-in `google_search` tool
- **Groq / Llama 3 70B** — for reasoning-heavy agents (via LiteLLM)

**Tools:**
| Tool | Type | Used By |
|------|------|---------|
| `google_search` | Built-in (ADK) | ProblemResearchAgent, TutorialFinderAgent |
| `search_web` | Custom | ProblemResearchAgent, TutorialFinderAgent |
| `extract_problem_links` | Custom | ProblemResearchAgent |
| `generate_practice_schedule` | Custom | PracticeRecommenderAgent |
| `format_learning_plan` | Custom | ReportGeneratorAgent |

## Quick Start

### 1. Clone & Setup

```bash
git clone <repo-url>
cd shorthills-adk
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Environment

Create a `.env` file with both API keys:

```env
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

- **Groq API key:** [console.groq.com](https://console.groq.com/)
- **Google API key:** [aistudio.google.com](https://aistudio.google.com/apikey)

### 3. Run

```bash
adk web
```

Open the browser URL shown in the terminal, select **LeetCodeLearningAssistant**, and try:

> "Create a learning guide for dynamic programming"

## Project Structure

```
shorthills-adk/
├── leetcode_agent/
│   ├── agent.py                          # Root orchestrator agent
│   ├── sub_agents/
│   │   ├── problem_research_agent.py     # Google Search + curated problems
│   │   ├── tutorial_finder_agent.py      # Tutorial discovery via search
│   │   ├── practice_recommender_agent.py # 7-day schedule generation
│   │   └── report_generator_agent.py     # Final report formatting
│   └── tools/
│       ├── search_web.py                 # Custom web search (any LLM backend)
│       ├── extract_problem_links.py      # Curated LeetCode problem mapping
│       ├── generate_practice_schedule.py # Structured practice planner
│       └── format_learning_plan.py       # Markdown report formatter
├── requirements.txt
├── .env
└── README.md
```

## Supported Topics

The agent works with **any DSA topic**, but has curated problem sets for:
Binary Search · Two Pointers · Dynamic Programming · Trees · Graphs · Linked List · Sliding Window · Stack · Heap · Backtracking

## License

MIT
