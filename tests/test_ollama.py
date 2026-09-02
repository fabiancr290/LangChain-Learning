from langchain_ollama import ChatOllama


def test_ollama_connection():
    llm = ChatOllama(model="qwen3:8b", temperature=0)

    response = llm.invoke("Reply with exactly: OK")

    assert response is not None
    assert response.content
    assert isinstance(response.content, str)
