# Main Script to run the streamlit app for the chatbot
import streamlit as st
from dotenv import load_dotenv, set_key
from streamlit_src.home_page import home
from streamlit_src.feed_page import feed
from chat_page import chat
from annotated_text import annotated_text, annotation
import openai
# Page settings
import time
import os 



if "page" not in st.session_state:
    st.session_state.page = "home" # default

if st.session_state.page == "home":
    home()
elif st.session_state.page == "feed":
    feed()
elif st.session_state.page == "chat":
    chat()



# Sidebar Configuration
st.sidebar.image("assets/ai_art.png", width=250, use_column_width=True)
# Sidebar Logo
st.sidebar.markdown("""
            <p style='text-align: left; 
                color: white; font-size: 20px;
                background: linear-gradient(to right, #f32170, #ff6b08, #cf23cf, #eedd44); 
                    -webkit-text-fill-color: transparent; 
                    -webkit-background-clip: text;  
                font-family: monospace ;'><b>Explore the Chatbot</b> 🐰</p>
        """, unsafe_allow_html=True)

with st.sidebar.container():
    co1, co2 = st.columns(2)
    with co1:
        st.page_link("https://github.com/ananya868/FurrBot-pet-care-chatbot", label="Src Code", icon="🖱️")
    with co2: 
        st.page_link("https://github.com/ananya868", label="My Github", icon="🐱")


# OpenAI API input
st.sidebar.markdown(
    """ 
        *Please provide your openai api key*
        *(Don't Worry! This app doesn't store api key)*
    """,
)
api_key = st.sidebar.text_input("Enter your OpenAI API Key", help="Please enter your OpenAI API key here", type="password")

default_api_key = "gemini api"

# Helper function to check Api key
def check_openai_api_key(api_key):
    client = openai.OpenAI(api_key=api_key)
    try:
        client.models.list()
    except openai.AuthenticationError:
        return False
    else:
        return True


# environment file 
env_file = '.env'
load_dotenv(env_file)

# Check for API key
if os.environ.get("OPENAI_API_KEY") == None:   
    if api_key:
        with st.sidebar.container():
            with st.spinner('checking your API key ...'):
                if check_openai_api_key(api_key):
                    st.sidebar.markdown(
                        """
                            <p style="text-align: center;"><b>Api Key Working</b> ✅<br> Key added Successfully! </p>
                        """, unsafe_allow_html=True
                    )
                    # os.environ["test_key"] = api_key # Sets in memory
                    set_key(env_file, "OPENAI_API_KEY", api_key) # Sets in .env file
                else:
                    st.sidebar.markdown(
                        """
                            <p style="text-align: center;"><b>Invalid Api Key</b> 🙅</p>
                        """, unsafe_allow_html=True
                    )       
else: 
    if check_openai_api_key(os.environ.get("OPENAI_API_KEY")):
        st.sidebar.markdown(
            """
                <p style="text-align: center;"><b>Key already set</b> ✅<br> </p>
            """, unsafe_allow_html=True 
        )
    if api_key:
        if api_key != os.environ.get("OPENAI_API_KEY"):
            if check_openai_api_key(api_key):
                set_key(env_file, "OPENAI_API_KEY", api_key)
                
# Example via code
st.sidebar.markdown(
    """
        or create a **.env** file in root dir, add your key:
        ```bash
        OPENAI_API_KEY="sk-14saq2f********"
        ```
    """
)
model_option = st.sidebar.selectbox(
    "**You can also choose LLM model** -",
    [
        "gpt-3.5-turbo",
        "gemini-1.5-flash (Free) (not recommended)",
        "gpt-4.0 (Good)",
        "gpt-4-turbo (Above Average)",
        "gpt-4o-mini (Faster)",
        "gpt-4o (Best in class)"
    ],
    help="Select the model you want to use for the chatbot",
)
# os.environ['model'] = model_option.split(" ")[0]
current_model = model_option.split(" ")[0]

if 'model' not in st.session_state:
    st.session_state.model = current_model  # Set initial model if not in session state
else:
    if st.session_state.model != current_model :
        st.session_state.model = current_model
        st.experimental_rerun()


with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.sidebar.button("Home", help="Click here to go to the home page", use_container_width=True):
            st.session_state.page = "home"
            st._experimental_rerun()
    # with col2:
    #     if st.sidebar.button("Feed", help="Click here to go to the feed page", use_container_width=True):
    #         st.session_state.page = "feed"
    #         st._experimental_rerun()
    with col3:
        if st.sidebar.button("Chatbot", help="Click here to go to the chatbot", use_container_width=True):
            st.session_state.page = "chat"
            st._experimental_rerun()
    
