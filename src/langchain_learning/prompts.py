from langchain_core.prompts import PromptTemplate

BASIC_PROMPT = PromptTemplate.from_template(
    "Answer the following question clearly and concisely:\n\n{question}"
)
