import os
import requests
from dotenv import load_dotenv

load_dotenv()
WEBHOOK = os.getenv("DISCORD_WEBHOOK_URL")

def send_discord_message(content: str):
    """Send a message to a Discord webhook."""
    payload = {"content": content}
    response = requests.post(WEBHOOK, json=payload)
    return response.status_code == 204