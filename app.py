#Imporing libraries
import os
from apiKey import apiKey

import streamlit as st
import pandas as pd

from langchain.llms import OpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from dotenv import load_dotenv, find_dotenv


#Main
st.title("AI Assistance for Data Science")
st.header("Data Analysis Part")
st.subheader("Solution")
st.write("This AI assistant can help you with data analysis. Please input your data and the question you have in mind.")
