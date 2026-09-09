from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable

from langchain_learning.chains import get_basic_chain


def test_get_basic_chain():
    chain = get_basic_chain()

    assert isinstance(chain, Runnable)


def test_str_output_parser():
    parser = StrOutputParser()

    result = parser.invoke("Hello LangChain")

    assert isinstance(result, str)
    assert result == "Hello LangChain"
