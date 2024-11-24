# Script to run the streamlit app for the chatbot
from streamlit_src.llm import gen 


import streamlit as st
from dotenv import load_dotenv 
import shelve 
import os


## query provided by user -> query the db -> we get response -> 
# -> we re-rank (summarize or select based on scores, filter shorting)
# -> we create context, query -> send to llm and generate answer for chatbot ->
# it returns answer to user as a message 

# we need to check when the query db should be used in chatbot.. 





