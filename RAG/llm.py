# Script to generate answers using context and query 
from openai import OpenAI
import google.generativeai as genai
import os 
import streamlit as st

# Main OpenAI Answer Generation function
def stream_gen(model_name: str, previous_conversation: list, context: str, user_query: str):
    """
    Generate an answer from a large language model (LLM) using the OpenAI API.
    """     
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )
    
    # convert the conversation to string
    conversation = str(previous_conversation)
    # prompt 
    prompt = f"""
        You are a pet Care chatbot. You have to chat with the user, about pets using a RAG system. The conversation so far is:
        {conversation}
        
        Here is some information I retrieved that might help you answer the user's query:
        {context}
        
        User's query: {user_query}
        
        If the user is simply greeting you, then greet them back in a friendly manner, dont use the context. 
        Otherwise, Based on the conversation and the retrieved information, generate the next response. 
        If the query is related to a previous part of the conversation, feel free to provide a follow-up response, otherwise answer using the retrieved context.

        Also, Your answer should be in a friendly way, make sure to use some markdown formatting like making the important points bold, or give point wise answer for better clearness, use emojis in most sentences to represent emotions (must do).
    """
    try: 
        message_placeholder = st.empty()
        answer = ""
        for response in client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": "Your are a LLM used in RAG chatbot to improve answers using the context and a query provided"},
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            stream=True
        ):  
            answer += response.choices[0].delta.content or ""
            message_placeholder.markdown(answer + "|")
        message_placeholder.markdown(answer)
        return answer
    except Exception as e:
        print("Error:", e)



def gen_gemini(context: str, query: str):
    """  
    This function generates a response to a query based on the provided context.
    """
    prompt = f"""
        Given the query and the context please generate a response for the query using the context. 
        Since, the query comes from chatbot, make sure your answers are not too long, and is suitable for chatbot.
        Make sure to write a clear and concise answer without losing much information, also answer exactly what the user is querying. 
        Only answer using the context, dont answer it by your own.

        Context: {context}
        Query: {query}
    """

    genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Res 
    response = model.generate_content(prompt)
    text = response.text

    return text 
    
