# Script to generate answers using context and query 
from openai import OpenAI
import os 



def gen(model_name: str, context: str, query: str):
    """
    Generate an answer from a large language model (LLM) using the OpenAI API.
    """     
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY")
    )

    # Prompt 
    prompt = f"""
        Given the query and the context please generate a response for the query using the context in a friendly way. 
        Since, the query comes from chatbot, make sure your answers are not too long, and is suitable for chatbot.
        Make sure to write a short, clear and concise answer without losing much information, also answer exactly what the user is querying. 
        Only answer using the context, dont answer it by your own.

        Context: {context}
        Query: {query}
    """
    try: 
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {
                    "role": "system",
                    "content": "Your are a LLM used in RAG chatbot to improve answers using the context and a query provided"},
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        answer = completion.choices[0].message.content
        return answer
    except Exception as e:
        print("Error:", e)



