"""Custom web search tool compatible with any LLM backend (Groq, OpenAI, Gemini, etc.).

Replaces google.adk.tools.google_search which only works with Gemini models.
Uses googlesearch-python for lightweight, API-key-free web searching.
"""

from googlesearch import search


def search_web(query: str, num_results: int = 5) -> list[dict]:
    """Search the web for a given query and return structured results.

    Args:
        query: The search query string.
        num_results: Number of results to return (default: 5, max: 10).

    Returns:
        A list of dicts, each containing 'title' and 'url' keys.
        Returns a helpful fallback message if the search fails or returns
        no results.
    """
    num_results = min(max(num_results, 1), 10)

    results = []
    try:
        for url in search(query, num_results=num_results, advanced=False):
            # Extract a readable title from the URL
            path_segment = url.rstrip("/").split("/")[-1]
            title = path_segment.replace("-", " ").replace("_", " ").title() if path_segment else url
            results.append({"url": url, "title": title})
    except Exception as e:
        return [{
            "url": f"https://www.google.com/search?q={query.replace(' ', '+')}",
            "title": f"Google search link for: {query}",
            "note": f"Automated search failed ({type(e).__name__}). Use the URL above to search manually.",
        }]

    if not results:
        return [{
            "url": f"https://www.google.com/search?q={query.replace(' ', '+')}",
            "title": f"Google search link for: {query}",
            "note": "No automated results found. Use the URL above to search manually.",
        }]

    return results
