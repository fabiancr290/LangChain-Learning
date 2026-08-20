from langchain_ollama import ChatOllama

llm = ChatOllama(model="qwen3:8b", temperature=0)

response = llm.invoke("Explain what an API is in one simple sentence.")

print(response.content)
