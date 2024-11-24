import streamlit as st 
import streamlit_extras 
from openai import OpenAI
from annotated_text import annotated_text 
from streamlit_theme import st_theme 
from dotenv import load_dotenv
import shelve 
import os 

load_dotenv()


# Functions
def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])

def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages

def chat():
    st.set_page_config(
        page_title="chat",
        page_icon="",
        # layout="wide",
        initial_sidebar_state="expanded",
    )

    theme_dict = st_theme() 
    theme = theme_dict.get('base')
    
    with st.container():
        st.markdown(
            """
            > *:rainbow[Start Chatting with the AI assistant!]* 🤖
            """
        )

    USER_AVATAR = "👨🏻‍🚀"
    BOT_AVATAR = "🐰"
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Ensure openai_model is initialized in session state
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"


    # Load chat history from shelve file
    def load_chat_history():
        with shelve.open("chat_history") as db:
            return db.get("messages", [])


    # Save chat history to shelve file
    def save_chat_history(messages):
        with shelve.open("chat_history") as db:
            db["messages"] = messages


    # Initialize or load chat history
    if "messages" not in st.session_state:
        st.session_state.messages = load_chat_history()

    # Sidebar with a button to delete chat history
    # with st.sidebar:
    #     if st.button("Delete Chat History"):
    #         st.session_state.messages = []
    #         save_chat_history([])

    # Display chat messages
    for message in st.session_state.messages:
        avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])

    # Main chat interface
    if prompt := st.chat_input("How can I help?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar=USER_AVATAR):
            st.markdown(f"**:rainbow[{prompt}]**")

        with st.chat_message("assistant", avatar=BOT_AVATAR):
            message_placeholder = st.empty()
            full_response = ""
            for response in client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=st.session_state["messages"],
                stream=True,
            ):
                full_response += response.choices[0].delta.content or ""
                message_placeholder.markdown(full_response + "|")
            message_placeholder.markdown(full_response)

        st.session_state.messages.append({"role": "assistant", "content": full_response})

        # Save chat history after each interaction
        save_chat_history(st.session_state.messages)




    # sidebar 
    st.sidebar.image("assets/ai_art.png", width=250, use_column_width=True)

    st.sidebar.markdown(
        """
            ## Explore the Chatbot ☃️
            
            *Since this app use openai client, please provide your openai api key*
            *(This app doesn't store api key or any type of secret keys)*
        """,
    )
    # streamlit input box, also output success if api key entered 

    api_key = st.sidebar.text_input("Enter your OpenAI API Key", help="Please enter your OpenAI API key here", type="password")
    if api_key:
        st.sidebar.success("API key entered successfully!")

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


    if st.sidebar.button("Home", help="Click here to go to the home page", use_container_width=True):
        st.session_state.page = "home"
    if st.sidebar.button("Feed", help="Click here to go to the feed page", use_container_width=True):
        st.session_state.page = "feed"
    if st.sidebar.button("Chatbot", help="Click here to go to the chatbot", use_container_width=True):
        st.session_state.page = "chat"
    
    # get current page 
    page = st.session_state.get("page", "home")
    if page == "chat":
        if st.sidebar.button("Delete chat history", help="Click here to delete chat history", use_container_width=True):
            st._experimental_rerun()
            st.session_state.messages = []
            save_chat_history([])




