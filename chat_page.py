import streamlit as st 
import streamlit_extras 
from openai import OpenAI
import google.generativeai as genai 
from annotated_text import annotated_text 
from streamlit_theme import st_theme 
from dotenv import load_dotenv

from RAG.llm import ( 
    stream_gen,
    gen_gemini
)
from RAG.qdrant_database import QdrantDatabase
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


# Main Chat Page
def chat(model: str = 'gpt-3.5-turbo'):
    st.set_page_config(
        page_title="chat",
        page_icon="",
        # layout="wide",
        initial_sidebar_state="expanded",
    )

    # theme_dict = st_theme() 
    # theme = theme_dict.get('base')
    model = os.environ['model']
        # st.markdown(
        #     """
        #     > *:rainbow[Start Chatting with the AI assistant!]* 🤖
        #     """
        # )
    # st.title(model)
    # Sidebar with a button to delete chat history4
    # if st.button(":rainbow[clear chat] 🗑️"):
    #     st.session_state.messages = []
    #     save_chat_history([])
    st.markdown("""
        <p style='text-align: left; 
            color: white; font-size: 20px;
            background: linear-gradient(to right, #f32170, #ff6b08, #cf23cf, #eedd44); 
                -webkit-text-fill-color: transparent; 
                -webkit-background-clip: text;  
            font-family: monospace ;'><b><i>Start Chatting!</i></b></p>
    """, unsafe_allow_html=True)

    USER_AVATAR = "👨🏻‍🚀"
    BOT_AVATAR = "🐰"


    # Model Client
    if model=="gemini-1.5-flash":
        genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
        client = genai.GenerativeModel(model)
        current_model = "gemini"
    elif "gpt" in model:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        current_model = "openai"

    # Qdrant Database client
    qdrant = QdrantDatabase(
        cluster_uri="https://904197e5-0ed4-48c7-9642-0611912311c7.us-east4-0.gcp.cloud.qdrant.io:6333", 
        api=os.getenv("DB_API")
    )

    """Session State Vars"""
    # Ensure openai_model is initialized in session state
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    # Initialize or load chat history
    if "messages" not in st.session_state:
        st.session_state.messages = load_chat_history()

    
    if 'initial_message_shown' not in st.session_state:
        st.session_state.initial_message_shown = False
    
    if not st.session_state.initial_message_shown:
        initial_message = "Hi. FurrBot Welcomes you! 🐰 How can i help you?"
        st.session_state.messages.append({"role": "assistant", "content": initial_message})
        st.session_state.initial_message_shown = True

    # Display chat messages
    for message in st.session_state.messages:
        avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])


    # Main chat interface
    if prompt := st.chat_input("Message FurrBot"):

        # User Message : prompt
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar=USER_AVATAR):
            st.markdown(f"**{prompt}**")

        # Ai Message : response
        with st.chat_message("assistant", avatar=BOT_AVATAR):

            # Do Retrieval (takes 1.3 seconds)
            matches = qdrant.query_db(collection_name='furr_bot', limits=2, query=prompt)
            # Get context from the matches
            context = ""
            for match in matches: 
                context += " " + match.get('text')
            answer = stream_gen(model, st.session_state.messages, context, prompt)
    
        st.session_state.messages.append({"role": "assistant", "content": answer})

        # Save chat history after each interaction
        save_chat_history(st.session_state.messages)


    

