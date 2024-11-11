from abc import ABC, abstractmethod 
from chat_with_ai import ChatWithAI
import uuid 
# Short unique id 
from shortuuid import ShortUUID


class MetadataCreation(ABC):
    """
        Utilize LLM to create metadata fields. 
        based on the provided text content. 
    """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_metadata(self):
        pass



# Define a class to create a metadata 'unique id' field 
class UniqueIdMetadataCreation(MetadataCreation):
    def __init__(self): 
        pass
    def create_metadata(self):
        return str(ShortUUID().random(length=6))


# Define a class to create a metadata 'keywords' field
class KeywordsMetadataCreation(MetadataCreation):
    def __init__(self, text: str, api_key: str) -> list:
        self.text = text 
        self.api_key = api_key

    def create_metadata(self):
        """   
        Create a metadata 'keywords' field
        Args:
            text (str): Text content of the pdf file
        Returns:
            list: List of keywords 
        """
        # prompt for the LLM to generate keywords 
        prompt = f"""Given para is a blog about a pet, written by pet veterans. 
                    You are a keyword extractor who focus on extracting top 5 keywords 
                    from the blog, which represent overall topic of the content. 
                    Para: {self.text} 
                    Make sure to only answer in this format and only return the answer, no extra text.
                    [keyword1, keyword2, keyword3, keyword4, keyword5]
                    """
        chat = ChatWithAI(prompt=prompt, api_key=self.api_key, model='gpt-3.5-turbo') 
        keywords = chat.get_response_from_llm() # str
        # pre-process to return list of keywords
        keywords = keywords.replace('[', '').replace(']', '').replace(' ', '').split(',')
        
        return keywords


# Define a class to create a metadata 'age group' field
class AgeGroupMetadataCreation(MetadataCreation):
    def __init__(self, text: str, api_key: str) -> list:
        self.text = text
        self.api_key = api_key
    
    def create_metadata(self):
        """
        Create a metadata 'age group' field
        Args:
            text (str): Text content of the pdf file
        Returns:
            list: List of age groups
        """
        # prompt for the LLM to generate age groups
        prompt = f"""Given para is a blog about a pet, written by pet veterans. 
                    You are a age group classifier who focus on classifying the age group of the animal described in the para by reading the para thoroughly.
                    If you can't classify the age group, return 'unknown', else 'baby' or 'young' or 'adult' or 'old'. 
                    Para: {self.text} 
                    Make sure to only answer in this format and only return the answer, no extra text.
                    'age_group'
                    """
        chat = ChatWithAI(prompt=prompt, api_key=self.api_key, model='gpt-3.5-turbo') 
        age_group = chat.get_response_from_llm() # str
        # pre-process to return age group string
        age_group = age_group.replace("'", '').replace(' ', '')
        
        return age_group


# Define a class to create a metadata 'topic' field 


# Define a class to create a metadata 'word_count'


# Define a class to create a metadata 'chunk_size




# Define Factory class to create metadata fields 
class MetadataFactory:
    def __init__(self, strategy: MetadataCreation):
        self.strategy = strategy
    
    def set_strategy(self, strategy: MetadataCreation): 
        self.strategy = strategy
    
    def create_field(self):
        """  
        Create a metadata field using the strategy
        """  
        return self.strategy.create_metadata()
