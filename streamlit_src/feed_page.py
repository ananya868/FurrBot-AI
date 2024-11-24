import streamlit as st 
from annotated_text import annotated_text
import streamlit_extras
from streamlit_theme import st_theme

def feed():
    st.set_page_config(
        page_title="feed",
        page_icon="❄️️",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    
    theme_dict = st_theme()
    base = theme_dict.get('base') 

    with st.container(): 
        # Input box 
        st.markdown("""
            <h3 style='text-align: center; 
                color: white; font-size: 35px;
                background: linear-gradient(to right, #f32170, #ff6b08, #cf23cf, #eedd44); 
                    -webkit-text-fill-color: transparent; 
                    -webkit-background-clip: text;  
                font-family: monospace ;'>Flash cards for your pet!</h3>
        """, unsafe_allow_html=True)
        p1, p2 = st.columns(2)
        with p1: 
            pet_name = st.text_input("***What is your pet's name?***", help="Enter your pet name here")
        with p2:
            pet_breed = st.text_input("***What is your pet's breed?***", help="Enter your pet breed here")
        with st.container():
            col2, _, _, _, _, _, _, _, _, col1 = st.columns(10)
            with col1:
                if st.button(":rainbow[Go to Chatbot]", help="Click here to go to the chatbot page"):
                    if pet_name=="" and pet_breed=="":
                        st.error("Please enter your pet's name and breed!")
                    else:
                        st.success("Redirecting to chatbot ...")

            with col2:
                if st.button(":rainbow[Get Cards]", help="Click here to get flash cards"):
                    if pet_name=="" and pet_breed=="":
                        st.error("Please enter your pet's name and breed!")
                    else:
                        st.success("Getting flash cards ...")

    
    text = "Labradors are good for people who have a lot of interest in them. They must be fed protein with extra chicken. Salad is also a great choice for them!.They must be fed protein with extra chicken."
    white = "#ffffff"
    black = "#000000"
    # st.markdown("<h1 style='text-align: center; color: white; font-family: ;'>FEED</h1>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        with st.container(border=True, height=400):
            st.markdown(f"<h2 style='text-align: center; color: {white if base=='dark' else black}; font-family: monospace'>Nutrition for Labrador</h2>", unsafe_allow_html=True)
    
            # text = "Labradors are good for people who have a lot of interest in them. They must be fed protein with extra chicken. Salad is also a great choice for them! They must be fed protein with extra chicken and they must be fed protein with extra chicken and they must be fed protein."
            # with st.container(border=True):
            st.markdown(f"""
                <div style="text-align: center; font-family: monospace"> 
                    <p>
                        <b>{text}</b>
                    </p>
                </div>
            """, unsafe_allow_html=True)
    with c2:
        with st.container(border=True, height=400):
            st.markdown(f"<h2 style='text-align: center; color: {white if base=='dark' else black}; font-family: monospace'>Behavior tips</h2>", unsafe_allow_html=True)
            st.markdown(f"""
                <div style="text-align: center; font-family: monospace"> 
                    <p>
                        <b>{text}</b>
                    </p>
                </div>
            """, unsafe_allow_html=True)
    with c3:
        with st.container(border=True, height=400):
            st.markdown(f"<h2 style='text-align: center; color: {white if base=='dark' else black}; font-family: monospace'>Care Routine</h2>", unsafe_allow_html=True)
            st.markdown(f"""
                <div style="text-align: center; font-family: monospace"> 
                    <p>
                        <b>{text}</b>
                    </p>
                </div>
            """, unsafe_allow_html=True)
    with c4:    
        with st.container(border=True, height=400):
            st.markdown(f"<h2 style='text-align: center; color: {white if base=='dark' else black}; font-family: monospace'>Daily activities</h2>", unsafe_allow_html=True)
            st.markdown(f"""
                <div style="text-align: center; font-family: monospace"> 
                    <p>
                        <b>{text}</b>
                    </p>
                </div>
            """, unsafe_allow_html=True)

    c5, c6, c7, c8 = st.columns(4)
    with c5:
        with st.container(border=True, height=400):
            st.markdown(f"<h2 style='text-align: center; color: {white if base=='dark' else black}; font-family: monospace'>Diseases</h2>", unsafe_allow_html=True)
            st.markdown(f"""
                <div style="text-align: center; font-family: monospace"> 
                    <p>
                        <b>{text}</b>
                    </p>
                </div>
            """, unsafe_allow_html=True)
    with c6:
        with st.container(border=True, height=400):
            st.markdown(f"<h2 style='text-align: center; color: {white if base=='dark' else black}; font-family: monospace'>Training tips</h2>", unsafe_allow_html=True)
            st.markdown(f"""
                <div style="text-align: center; font-family: monospace"> 
                    <p>
                        <b>{text}</b>
                    </p>
                </div>
            """, unsafe_allow_html=True)
    with c7:
        with st.container(border=True, height=400):
            st.markdown(f"<h2 style='text-align: center; color: {white if base=='dark' else black}; font-family: monospace'>Grooming Guide</h2>", unsafe_allow_html=True)
            st.markdown(f"""
                <div style="text-align: center; font-family: monospace"> 
                    <p>
                        <b>{text}</b>
                    </p>
                </div>
            """, unsafe_allow_html=True)
    with c8:
        with st.container(border=True, height=400):
            st.markdown(f"<h2 style='text-align: center; color: {white if base=='dark' else black}; font-family: monospace'>Extra Care</h2>", unsafe_allow_html=True)
            st.markdown(f"""
                <div style="text-align: center; font-family: monospace"> 
                    <p>
                        <b>{text}</b>
                    </p>
                </div>
            """, unsafe_allow_html=True)
            


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


    st.sidebar.button("Home", help="Click here to go to the home page", use_container_width=True    )
    st.sidebar.button("Feed", help="Click here to go to the feed page", use_container_width=True)
    st.sidebar.button("Chatbot", help="Click here to go to the chatbot", use_container_width=True)

    

