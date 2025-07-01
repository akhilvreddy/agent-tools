import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_text(text: str) -> str:
    """Summarizes input text using OpenAI."""
    prompt = f"""Summarize the following input in clear bullet points:

{text}
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )
    return response["choices"][0]["message"]["content"].strip()