
## Travel Guide Demo with Ollama and Streamlit
## This script creates a simple travel guide application using Ollama's LLM and Streamlit.
## Requirements:
## - langchain-ollama
## - streamlit
## To run the app, use the command: streamlit run 02_Travelguide_Demo.py
ç
from langchain_ollama import ChatOllama
import streamlit as st
from langchain.prompts import PromptTemplate

llm  = ChatOllama(model="mistral", base_url="http://localhost:11434")

prompt_template = PromptTemplate(
    input_variables=["city","month","language","budget"],
    template="""Welcome to the {city} travel guide!
    If you're visiting in {month}, here's what you can do:
    1. Must visit attractions.
    2. Local cuisine you must try.
    3. Useful phrases in {language}.
    4. Try out local cuisine and delicacies.
    5. Tips for traveling on a {budget} budget.
    Enjoy your trip!
    """)

st.title("Travel Guide")

city = st.text_input("Enter the city: ")
month = st.text_input("Enter the month of visit: ")
language = st.selectbox("Language:", ["English", "Spanish", "French", "German", "Italian"], index=0)
budget = st.selectbox("Travel Budget:", ["Low", "Medium", "High"], index=0)
if city and month and language and budget:
    response = llm.invoke(prompt_template.format(
        city=city,
        month=month,
        language=language,
        budget=budget))
    st.write(response.content)
