import openai
from openai import OpenAI 



class ChatWithAI:
    """
    A class to interact with a large language model (LLM) using the OpenAI API.
    """ 
    def __init__(self, prompt: str, api_key: str, model: str ='gpt-3.5-turbo'): 
        self.__prompt = prompt
        self.__api_key = api_key
        self.model = model
    
    def get_response_from_llm(self):
        """
        Gets a response from a large language model (LLM) using the OpenAI API.

        Args:
            prompt (str): The prompt to send to the LLM.
            api_key (str): The API key to use to authenticate with the OpenAI API.
        Returns:
            str: The response from the LLM.
        """
        client = OpenAI(api_key=self.__api_key)
        
        try:
            completion = client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {
                        "role": "user",
                        "content": self.__prompt
                    }
                ]
            )

            # text response from the ai 
            answer = completion.choices[0].message.content 
            return answer

        except Exception as e:
            print("Error:", e)
            