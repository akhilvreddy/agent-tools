import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def critique_output(agent_output: str) -> str:
    """LLM-powered critique of agent output for clarity, correctness, safety."""
    prompt = f"""Critique the following agent output:
{agent_output}

Give clear suggestions for improvement, and flag any inaccuracies or hallucinations.
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6,
    )
    return response["choices"][0]["message"]["content"].strip()