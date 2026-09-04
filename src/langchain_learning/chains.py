from langchain_core.runnables import Runnable

from langchain_learning.llm import get_llm
from langchain_learning.prompts import BASIC_PROMPT


def get_basic_chain() -> Runnable:
    return BASIC_PROMPT | get_llm()
