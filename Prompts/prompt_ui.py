import os
from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

st.header('Reasearch Assistant')
user_input = st.text_input('Enter your query')

if st.button('Summarize'):
    model=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
    result=model.invoke(user_input)
    st.write(result.content)

