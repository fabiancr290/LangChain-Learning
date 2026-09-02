from langchain_ollama import ChatOllama

from langchain_learning.llm import get_llm


def test_get_llm():
    llm = get_llm()

    assert isinstance(llm, ChatOllama)
