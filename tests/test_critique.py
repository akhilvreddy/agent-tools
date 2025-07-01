from tools.critique.critique_tool import critique_output

def test_critique_output_returns_string():
    dummy_output = "The agent said the capital of France is Berlin."
    result = critique_output(dummy_output)
    assert isinstance(result, str)
    assert "Paris" in result or "incorrect" in result.lower()

# checks if OPENAI_API_KEY is set