import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def reask_for_clarity(question_context: str) -> str:
    """Generate a clarifying question if the agent is uncertain."""
    prompt = f"""You are an assistant helping an agent clarify its goal.

The current context is:
{question_context}

If the goal is unclear or ambiguous, ask a single clarifying question.
If it's already clear, reply: 'No clarification needed.'
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response["choices"][0]["message"]["content"].strip()