from langchain_learning.llm import get_llm


def test_ollama_connection():
    llm = get_llm()

    response = llm.invoke("Reply with exactly: OK")

    assert response is not None
    assert response.content
    assert isinstance(response.content, str)
