from streamlit_src.home_page import home
from streamlit_src.feed_page import feed
from streamlit_src.chat_page import chat
import streamlit as st
from annotated_text import annotated_text
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



# Sidebar s
st.sidebar.image("assets/ai_art.png", width=250, use_column_width=True)
st.sidebar.markdown("""
            <p style='text-align: left; 
                color: white; font-size: 20px;
                background: linear-gradient(to right, #f32170, #ff6b08, #cf23cf, #eedd44); 
                    -webkit-text-fill-color: transparent; 
                    -webkit-background-clip: text;  
                font-family: monospace ;'><b>Explore the Chatbot</b> 🐰</p>
        """, unsafe_allow_html=True)

st.sidebar.markdown(
    """ 
        *Please provide your openai api key*
        *(Don't Worry! This app doesn't store api key)*
    """,
)

# streamlit input box, also output success if api key entered 

api_key = st.sidebar.text_input("Enter your OpenAI API Key", help="Please enter your OpenAI API key here", type="password")
# if api_key:
    # st.sidebar.success("API key entered successfully!")

default_api_key = "gemini api"

def check_openai_api_key(api_key):
    client = openai.OpenAI(api_key=api_key)
    try:
        client.models.list()
    except openai.AuthenticationError:
        return False
    else:
        return True

# st.sidebar.write(os.environ.get("gigi"))
# set to .env
if os.environ.get("OPENAI_API_KEY") == None:   
    if api_key:
        # st.sidebar.write("Checking API key ...")
        with st.sidebar.container():
            with st.spinner('checking your API key ...'):
                if check_openai_api_key(api_key):
                    st.sidebar.markdown(
                        """
                            <p style="text-align: center;"><b>Api Key Working</b> ✅<br> Key added Successfully! </p>
                        """, unsafe_allow_html=True
                    )
                    # set to env variable
                    os.environ["OPENAI_API_KEY"] = api_key
                else:
                    st.sidebar.markdown(
                        """
                            <p style="text-align: center;"><b>Invalid Api Key</b> ⚠️</p>
                        """, unsafe_allow_html=True
                    )
        
else: 
    st.sidebar.markdown(
        """
            <p style="text-align: center;"><b>Key already set</b> ✅<br> </p>
        """, unsafe_allow_html=True 
    )

st.sidebar.markdown(
    """
        or create a **.env** file in root dir, add your key:
        ```bash
        OPENAI_API_KEY="sk-14saq2f********"
        ```
    """
)
model = st.sidebar.selectbox(
    "You can also choose LLM model -",
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

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.sidebar.button("Home", help="Click here to go to the home page", use_container_width=True):
            st.session_state.page = "home"
            st._experimental_rerun()
    with col2:
        if st.sidebar.button("Feed", help="Click here to go to the feed page", use_container_width=True):
            st.session_state.page = "feed"
            st._experimental_rerun()
    with col3:
        if st.sidebar.button("Chatbot", help="Click here to go to the chatbot", use_container_width=True):
            st.session_state.page = "chat"
            st._experimental_rerun()
