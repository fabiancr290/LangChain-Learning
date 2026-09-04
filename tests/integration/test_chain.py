from langchain_learning.chains import get_basic_chain


def test_basic_chain():
    chain = get_basic_chain()

    response = chain.invoke({"question": "What is TCP/IP? Answer in one sentence."})

    assert response is not None
    assert response.content
    assert isinstance(response.content, str)
