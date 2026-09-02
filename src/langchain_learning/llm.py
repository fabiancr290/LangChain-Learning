from langchain_ollama import ChatOllama

from langchain_learning.config import OLLAMA_MODEL


def get_llm() -> ChatOllama:
    return ChatOllama(
        model=OLLAMA_MODEL,
        temperature=0,
    )
