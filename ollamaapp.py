from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# creating my prompts
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question: {question}")
    ]
)

st.title('Langchain demo Chat app with gemma2:2b')
input_text = st.text_input('Write your prompt:')

# ollama LLM model
llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()

# LCEL chain
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text}) 
    st.write(response)
