import os
from abc import ABC, abstractmethod 
from typing import Any, Optional
from pydantic import BaseModel, Field


class LLM(ABC):
    """Abstract base class for LLMs."""
    @abstractmethod
    def generate_text(self, prompt: str, **kwargs: Any) -> str:
        """Generate text from the LLM."""
        pass

    @classmethod
    def init_llm(cls, provider_name: str, model: str = None) -> 'LLM':
        """Factory method to get the right provider."""
        provider = {
            "openai": OpenAILLM,
            "google": GoogleLLM,
            "anthropic": AnthropicLLM,
            "mistral": MistralLLM 
        }
        if provider_name.lower() not in provider:
            raise ValueError(f"Provider {provider_name} not supported.")
        
        if model: 
            return provider[provider_name.lower()](model)
        else:
            return provider[provider_name.lower()]()


# Output Schema 
class OutputSchema(BaseModel):
    answer: str = Field(..., description="The answer to the question.")
    followup: Optional[str] = Field(..., description="Follow-up question to suggest to the user.")


class OpenAILLM(LLM):
    def __init__(self, model: str = "gpt-4o") -> None: 
        from openai import OpenAI
        try:
            self.client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))
        except Exception as e:
            print(f"Error initializing OpenAI client: {e}")
            raise Exception(f"Error: {e}")
        
        assert model in ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-3.5-turbo"], f"Incompatible model {model}."
        self.model = model
    
    def generate_text(self, prompt: str, **kwargs: Any) -> str:
        """
        Generate text from OpenAI LLM.
        """
        assert isinstance(prompt, str), "Prompt must be a string."
        assert isinstance(kwargs, dict), "kwargs must be a dictionary."
        try:
            response = self.client.beta.chat.completions.parse(
                model = self.model,
                messages = [{
                    "role": "user",
                    "content": prompt
                }],
                response_format = OutputSchema, 
                temperature = kwargs.get("temperature", 0.8),
                max_tokens = kwargs.get("max_tokens", 1624),
            )
        except Exception as e:
            print(f"Error generating text: {e}")
            raise Exception(f"Error: {e}")
        return response.choices[0].message.content


class GoogleLLM(LLM):
    def __init__(self, model: str = "gemini-2.5-pro-exp-03-25") -> None:
        from google import genai 
        try:
            self.client = genai.Client(api_key = os.getenv("GOOGLE_API_KEY"))
        except Exception as e:
            print(f"Error initializing Google client: {e}")
            raise Exception(f"Error: {e}")

        assert model in ["gemini-2.5-pro-exp-03-25"], f"Incompatible model {model}."
        self.model = model # latest google lux model 

    def generate_text(self, prompt: str, **kwargs: Any) -> str:
        """
        Generate text from Google LLM.
        """
        assert isinstance(prompt, str), "Prompt must be a string."
        assert isinstance(kwargs, dict), "kwargs must be a dictionary."
        temperature = kwargs.get("temperature", 0.8)
        max_tokens = kwargs.get("max_tokens", 1624)
        try:
            response = self.client.models.generate_content(
                model = self.model, 
                contents = prompt
            )
        except Exception as e:
            print(f"Error generating text: {e}")
            raise Exception(f"Error: {e}")
        return response.text


class AnthropicLLM(LLM):
    def __init__(self, model: str = "claude-3-7-sonnet-20250219") -> None:
        import anthropic
        try: 
            self.client = anthropic.Anthropic(
                api_key = os.getenv("ANTHROPIC_API_KEY")
            )
        except Exception as e:
            print(f"Error initializing Anthropic client: {e}")
            raise Exception(f"Error: {e}")
        
        assert model in ["claude-3-7-sonnet-20250219"], f"Incompatible model {model}."
        self.model = model 
    
    def generate_text(self, prompt: str, **kwargs: Any) -> str:
        """
        Generate text from Anthropic LLM.
        """
        assert isinstance(prompt, str), "Prompt must be a string."
        assert isinstance(kwargs, dict), "kwargs must be a dictionary."
        try:
            response = self.client.messages.create(
                model = self.model, 
                max_tokens = kwargs.get("max_tokens", 1624),
                messages = [{
                    "role": "user",
                    "content": prompt
                }], 
                temperature = kwargs.get("temperature", 0.8)
            )
        except Exception as e:
            print(f"Error generating text: {e}")
            raise Exception(f"Error: {e}")
        return response.content


class MistralLLM(LLM):
    def __init__(self, model: str = "mistral-large-latest") -> None:
        from mistralai import Mistral 
        try:
            self.client = Mistral(
                api_key = os.getenv("MISTRAL_API_KEY")
            )
        except Exception as e:
            print(f"Error initializing Mistral client: {e}")
            raise Exception(f"Error: {e}")
        
        assert model in ["mistral-large-latest"], f"Incompatible model {model}."
        self.model = model
    
    def generate_text(self, prompt: str, **kwargs: Any) -> str:
        """
        Generate text from Mistral LLM.
        """
        assert isinstance(prompt, str), "Prompt must be a string."
        assert isinstance(kwargs, dict), "kwargs must be a dictionary."
        temperature = kwargs.get("temperature", 0.8)
        max_tokens = kwargs.get("max_tokens", 1624)
        try:
            response = self.client.chat.complete(
                model = self.model, 
                messages = [{
                    "role": "user",
                    "content": prompt
                }],
                temperature = temperature,
                max_tokens = max_tokens
            )
        except Exception as e:
            print(f"Error generating text: {e}")
            raise Exception(f"Error: {e}")
        return response.choices[0].message.content




# Example Usage 
if __name__ == "__main__":
    llm = LLM.init_llm("openai", "gpt-4o")

    prompt = "Write a 20 words para on france? give followups as well!"
    response = llm.generate_text(prompt)
    print(response)  # Should print the answer to the question.