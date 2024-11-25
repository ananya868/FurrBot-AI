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

    try:
        theme_dict = st_theme()
        base = theme_dict.get('base') 
    except:
        print("--")
        
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
            


   