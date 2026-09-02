from langchain_ollama import ChatOllama

from langchain_learning.config import OLLAMA_MODEL


def test_ollama_connection():
    llm = ChatOllama(model=OLLAMA_MODEL, temperature=0)

    response = llm.invoke("Reply with exactly: OK")

    assert response is not None
    assert response.content
    assert isinstance(response.content, str)
