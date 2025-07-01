import os
from duckduckgo_search import DDGS

def search_web(query: str, max_results: int = 3) -> list[str]:
    """Performs a web search using DuckDuckGo."""
    results = []
    with DDGS() as ddgs:
        search_results = ddgs.text(query, max_results=max_results)
        results = [r['body'] for r in search_results]
    return results