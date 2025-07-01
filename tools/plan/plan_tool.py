import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_plan(goal: str) -> str:
    """Generate a step-by-step plan using an LLM."""
    prompt = f"""You are a helpful AI planner.
Your goal: {goal}

Break this into clear, numbered steps for an agent to follow.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )
    return response["choices"][0]["message"]["content"].strip()