from tools.discord.discord_tool import send_discord_message

def test_send_discord_message():
    response = send_discord_message("✅ test message from pytest")
    assert response is True

# keeps a test channel for this