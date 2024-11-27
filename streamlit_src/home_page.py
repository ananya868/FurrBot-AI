import streamlit as st 
from annotated_text import annotated_text


def home():
    st.set_page_config(
        page_title="FurrBot",
        page_icon="❄️️",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    # Create two columns
    col1, col2 = st.columns(2)  
    with col1:
        with st.container(border=True):
            st.image("assets/home_art.png", width=650) 
    with col2:
        # st.markdown("# Furr Bot 🐰")
        st.markdown("""
            <h3 style='text-align: left; 
                color: white; font-size: 40px;
                background: linear-gradient(to right, #f32170, #ff6b08, #cf23cf, #eedd44); 
                    -webkit-text-fill-color: transparent; 
                    -webkit-background-clip: text;  
                font-family: monospace ;'>Furr Bot - Ai</h3>
        """, unsafe_allow_html=True)
        st.write(
            '''   
            
            - 🐰 **Furr Bot** is your go-to-pet care assistant! It pulls advice from a knowledge base backed by pet veterans.
            - It brings you the best with lineup of **RAG techniques, bias-busting fact checks**, and **streamlined LLMOps** to keep running smoothly! 
        ''' 
        )
        with st.expander("Flow of the App!"):
            st.write('''
                This is the space for the flow diagram
            ''')
        with st.expander("Tech Stack Used"):
            st.write(
                ''' 
                    **Python** - **RAG** - **OpenAI** - **Qdrant** - **Docker** - **GitHub Actions** - **Re** - **nltk** - **Spacy** - **Jupyter** - **fitz** - **Streamlit** - **Shelve** - **Gemini** - **Markdown**
                '''
            )
        with st.expander("Demo Video"):
            st.write(
                annotated_text(
                    ("This is the space for the demo video", "", "#18545b"), 
                )
            )
        with st.expander("About Me"):
            co1, co2, co3, co4, co5= st.columns(5)
            with co1:
                st.page_link("http://www.github.com/ananya868", label="My Github", icon="🐱")
            with co2:
                st.page_link("https://www.linkedin.com/in/ananya8154/", label="My LinkedIn", icon="👥") 
            with co3:
                st.page_link("https://x.com/aiWorms", label="Twitter", icon="🐦")
            with co4: 
                st.page_link("https://huggingface.co/Ananya8154", label="huggingFace", icon="🤗")
            st.markdown(
                f"""
                    I am a recently graduated Ai Engineer, and I love building AI solutions!
                    > Contact me @ : *ananya8154@gmail.com* or feel free to reach me out on Twitter or LinkedIn
                    
                    > Do visit my Github to see my other works! Please give this repo a star if you liked it! 🌟
                """
            )
    
        if st.button("**Go to App** 📛", help="Click here to go to the chatbot", use_container_width=False):
            st.session_state.page = "chat"
            st.rerun()

    with st.container():
     
        col3, col4 = st.columns(2)
       
        with col3:
            st.write(
                '''
                    ***How to use this app? -***
                    - *Click on the **Go to App** button to start chatting with the bot.*
                    - *Fill up some basic info about your pet*
                    - *Ask the bot any question related to your pet, or any specific topic*
                    
                    via Code:
                    ```bash
                    git clone https://github.com/ananya868/FurrBot-pet-care-chatbot.git
                    cd FurrBot-pet-care-chatbot
                    ```
                    Create a virtual env, activate and install dependencies: 
                    ```bash
                    pip install -r requirements.txt
                    ```
                    Run the app:
                    ```bash
                    streamlit run app.py    
                    ```
                ''' 
            )
            
        with col4:
            st.write(
                '''
                    ***What makes this app standout? -***
                    - *Uses a knowledge base from **experienced pet veterans**, to provide **verified and reliable information**.*
                    - ***Custom RAG and Re-Ranking** methods to ensure most relevant responses*
                    - ***Automated Bias detection and Mitigation pipeline**, uses AI-Agents to improve fairness*
                    - ***Integrated LLMOps** with scheduled data updation using **CI/CD***
                    - *Data pipeline for real-time data ingestion, transformation and chunking*
                '''
            )
            st.write(
                '''
                    ***What this app offers? -***
                    - **Pet Care**: *Get advice on pet care, grooming, and training*.
                    - **Health**: *Get information on pet health, diseases, and first aid.*
                    - **Breeds**: *Get information on different pet breeds.*
                    - **Food**: *Get information on pet food and nutrition.*
                    - **Behavior**: *Get information on pet behavior and training.*
                '''
            )


# [theme]
# base="dark"
# secondaryBackgroundColor="#1b1f33"s
# font="monospace"
