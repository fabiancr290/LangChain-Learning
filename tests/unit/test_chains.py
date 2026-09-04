from langchain_core.runnables import Runnable

from langchain_learning.chains import get_basic_chain


def test_get_basic_chain():
    chain = get_basic_chain()

    assert isinstance(chain, Runnable)
