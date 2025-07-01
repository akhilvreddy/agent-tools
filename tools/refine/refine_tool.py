import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def refine_response(raw_output: str) -> str:
    """Use an LLM to improve or clarify an agent's output."""
    prompt = f"""You are an assistant that improves agent output.
Here's the original:
{raw_output}

Improve it for clarity, structure, and accuracy.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response["choices"][0]["message"]["content"].strip()