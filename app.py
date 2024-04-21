#Imporing libraries
import os
from apiKey import apiKey

import streamlit as st
import pandas as pd

from langchain_openai import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv

# openai key
os.environ["OPENAI_API_KEY"] = apiKey
load_dotenv(find_dotenv())

#Main Titles
st.title("AI Assistance for Data Science 🤖")
st.write("This AI assistant can help you with data analysis.👋 Please input your data and the question you have in mind.")

#Explaination side bar
with st.sidebar:
    st.write('*Your Data Science Adventure Begins with an CSV File.*')
    st.caption('''*You may already know that every exciting data science journey starts with a dataset. That's why I'd love for you to upload a CSV file. Once we have your data in hand, we'll dive into understanding it and have some fun exploring it. Then, we'll work together to shape your business challenge into a data science framework. I'll introduce you to the coolest machine learning models, and we'll use them to tackle your problem.
    Sounds fun right*''')
    st.divider()
    st.caption("<p style = 'text-align:center'> Made with love ♥️ by Muneeb </p>", unsafe_allow_html=True)

# Button 
if 'clicked' not in st.session_state:
    st.session_state.clicked = {1:False}

#function to update vaue in session state
def clicked(button):
    st.session_state.clicked[button] = True

st.button("Let's get started!", on_click=clicked, args=(1,))
if st.session_state.clicked[1]:
    user_csv = st.file_uploader("Upload your CSV file", type=["csv"])

    if user_csv is not None:
        user_csv.seek(0)
        df = pd.read_csv(user_csv, low_memory=False)

        # model
        llm = OpenAI(temperature=0)

        #Function sidebar
        @st.cache_data
        def steps_eda():
            steps_eda = llm("What are the steps of EDA?")
            return steps_eda

        #pandas agent
        pandas_agent = create_pandas_dataframe_agent(llm,df, verbose=True)

        @st.cache_data
        #function main
        def function_agent():
            st.write("**Data Overview**")
            st.write("The first row of the dataset looks like this:")
            st.write(df.head())
            st.write("**Data Cleaning**")
            column_df = pandas_agent.run("What are the meaning of the columns?")
            st.write(column_df)
            missing_values_df = pandas_agent.run("What are the missing values in the dataset?")
            st.write(missing_values_df)
            duplicate_values_df = pandas_agent.run("What are the duplicate values in the dataset?")
            st.write(duplicate_values_df)
            st.write("**Data Summarisation**")
            st.write(df.describe())
            correlation_df = pandas_agent.run("What are the correlation values in the dataset?")
            st.write(correlation_df)
            outlier_df = pandas_agent.run("Identify the outliers in the dataset")
            st.write(outlier_df)
            new_feature_df = pandas_agent.run("What new features would be interesting to add?")
            st.write(new_feature_df)
            return

        st.header("Exploratory Data Analysis")
        st.subheader("General Information about the dataset")


        with st.sidebar:
            with st.expander("Steps of EDA"):
                st.write(steps_eda())

        function_agent()



        user_question = st.text_input("What variable you intersted in?")
