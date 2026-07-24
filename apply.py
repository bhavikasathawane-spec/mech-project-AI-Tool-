from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#creating prompts
prompt = ChatPromptTemplate.from_messages(
[
    ("system","you.are helpfull assistant . please respond to the question asked"),
    ("user","Quesation:{quesation}")
   ]
)

#fronttend UI design using streamlit framework
st.title("My GPT")
input_text = st.input("Ask your question")

# ollama model integration 
llm = Ollama(model="gemma2:latest")
output_parser = StrOutputParser()
chain = prompt| llm | output_parser


#input validation
st.write(chain.invoke({"question":input_text}))