## 01_Llama_Demo.py
## A simple script to interact with the Llama model using LangChain and Ollama.
## Prerequisites:
## 1. Ensure you have langchain-ollama installed:
##    pip install langchain-ollama
## 2. Make sure your Ollama server is running and accessible at the specified base_url

from langchain_ollama import ChatOllama
llm  = ChatOllama(model="llama3", base_url="http://localhost:11434")
question = input("Enter your question: \n")
response = llm.invoke(question)

if response and response.content:
    print("\nResponse: \n")
    print(response.content)