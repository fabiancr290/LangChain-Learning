from langchain_core.prompt_values import StringPromptValue

from langchain_learning.prompts import BASIC_PROMPT


def test_basic_prompt():
    prompt = BASIC_PROMPT.invoke({"question": "What is TCP/IP?"})

    assert isinstance(prompt, StringPromptValue)
    assert "What is TCP/IP?" in prompt.text
