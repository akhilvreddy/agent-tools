import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_structured_data(raw_text: str) -> str:
    """Extract structured JSON from messy input using LLM."""
    prompt = f"""Extract structured JSON data from the following input:
{raw_text}

Only return JSON. No explanations.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response["choices"][0]["message"]["content"].strip()