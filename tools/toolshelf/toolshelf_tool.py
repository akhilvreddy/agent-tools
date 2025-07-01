import os

# Change this to your specifc tools, or add dynamic implementation here.
AVAILABLE_TOOLS = [
    "/search", "/email", "/discord", "/refine",
    "/summarize", "/plan", "/reask", "/critique",
    "/extract", "/memory", "/file-utils", "/log", "/timestamp"
]

def list_tools() -> list[str]:
    """Return a list of all available tools."""
    return AVAILABLE_TOOLS