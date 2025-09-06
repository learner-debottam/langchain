## Travel Guide Demo with Ollama and Streamlit
## This script creates a simple travel guide application using Ollama's LLM and Streamlit.
## Requirements:
## - langchain-ollama
## - streamlit
## To run the app, use the command: streamlit run 02_Travelguide_Demo.py
from langchain_ollama import ChatOllama
import streamlit as st
from langchain.prompts import PromptTemplate

llm  = ChatOllama(model="mistral", base_url="http://localhost:11434")

prompt_template = PromptTemplate(
    input_variables=["country","no_of_paras","language"],
    template="""You are an expert in traditional cuisine. 
    You provide informatio about a specific dish from a specific country.
    Avoid giving information about fictional places. If the country is fictional or non-existent answer: I don't know.
    Answer the question: What is the traditional cuisine of {country}?
    Answer in {no_of_paras} short paragraphs in {language}.
    """)

st.title("Cuisine Info")

country = st.text_input("Enter the country: ")
no_of_paras = st.number_input("Number of paragraphs:", min_value=1, max_value=10, value=2, step=1)
language = st.selectbox("Language:", ["English", "Spanish", "French", "German", "Italian"], index=0)
if country:
    response = llm.invoke(prompt_template.format(
        country=country,
        no_of_paras=no_of_paras,
        language=language))
    st.write(response.content)
