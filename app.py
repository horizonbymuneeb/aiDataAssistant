#Imporing libraries
import os
from apiKey import apiKey

import streamlit as st
import pandas as pd

from langchain.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv


#Main
st.title("AI Assistance for Data Science 🤖")
st.write("This AI assistant can help you with data analysis.👋 Please input your data and the question you have in mind.")



with st.sidebar:
    st.write('*Your Data Science Adventure Begins with an CSV File.*')
    st.caption('''*You may already know that every exciting data science journey starts with a dataset. That's why I'd love for you to upload a CSV file. Once we have your data in hand, we'll dive into understanding it and have some fun exploring it. Then, we'll work together to shape your business challenge into a data science framework. I'll introduce you to the coolest machine learning models, and we'll use them to tackle your problem.
    Sounds fun right*''')

    with st.expander("THIS IS HOW IT WORKS"):
        st.write("1. Upload your CSV file")
        st.write("2. Ask your question")
        st.write("3. Get the answer")

    st.divider()

    st.caption("<p style = 'text-align:center'> Made with love ♥️ by Muneeb </p>", unsafe_allow_html=True)

if 'clicked' not in st.session_state:
    st.session_state.clicked = {1:False}

#function to update vaue in session state
def clicked(button):
    st.session_state.clicked[button] = True

st.button("Let's get started!", on_click=clicked, args=(1,))
if st.session_state.clicked[1]:
    st.header("Data Analysis Part")
    st.subheader("Solution")

    user_csv = st.file_uploader("Upload your CSV file", type=["csv"])

    if user_csv is not None:
        user_csv.seek(0)
        df = pd.read_csv(user_csv, low_memory=False)
        



