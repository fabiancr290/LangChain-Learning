from unittest.mock import patch

from langchain_core.runnables import RunnableGenerator

from langchain_learning.chains import stream_basic_chain


def generate_chunks(_):
    yield "Hello"
    yield " LangChain"


def test_stream_basic_chain():
    mock_chain = RunnableGenerator(generate_chunks)

    with patch("langchain_learning.chains.get_basic_chain", return_value=mock_chain):
        chunks = stream_basic_chain("What is LangChain?")

    assert list(chunks) == ["Hello", " LangChain"]
