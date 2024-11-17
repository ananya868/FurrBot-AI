import google.generativeai as genai
import os 

try: 
    genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
except Exception as e:
    print("Error Configuring Gemini Api Key, please check if its in the .env file: ", e) 



class ChatWithGemini:
    """ 
    A class used to interact with the Gemini API for chat functionality.
    """ 
    def __init__(self, prompt: str, model: str="gemini-1.5-flash"):
        self.prompt = prompt
        self.model = model
    
    def get_response_from_llm(self):
        """
        Get a response from the Gemini Large Language Model (LLM) based on the provided prompt.

        Args:
            prompt (str): The prompt to send to the LLM.
        Returns:
        str: The response from the LLM.
        """

        try: 
            model = genai.GenerativeModel(self.model)
        except Exception as e: 
            print(f"Model init failed!: {e}")
        
        response = model.generate_content(self.prompt)

        text = response.text 

        return text

