from tools.email.email_tool import send_email

def test_send_email():
    try:
        send_email(
            to="your@email.com",  # replace or mock
            subject="Test Email from pytest",
            body="This is a test email."
        )
    except Exception as e:
        assert False, f"Email failed: {e}"