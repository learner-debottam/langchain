## 01_Mistral_Streamlit_Demo.py
## A simple Streamlit app to interact with the Mistral model using LangChain and Ollama.
## Prerequisites:
## 1. Ensure you have Streamlit and langchain-ollama installed:
##    pip install streamlit langchain-ollama
## 2. Make sure your Ollama server is running and accessible at the specified base_url.
## 3. Run the app using the command:
##    streamlit run 01_Mistral_Streamlit_Demo.py
from langchain_ollama import ChatOllama
from langchain.globals import set_debug
import streamlit as st

set_debug(True)
print("Starting...")
llm  = ChatOllama(model="mistral", base_url="http://localhost:11434")
print("Model loaded.")



st.title("Mistral LLM Demo")
question = st.text_input("Enter your question: ")
if question:
    print("Invoking model...")
    response = llm.invoke(question)
    st.write(response.content)
print("Response received.")