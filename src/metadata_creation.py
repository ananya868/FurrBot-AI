from abc import ABC, abstractmethod 




class MetadataCreation(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def create_metadata(self):
        pass



# Define a class to create a metadata 'keywords' field
class KeywordsMetadataCreation(MetadataCreation):
    def __init__(self, text: str) -> list:
        self.text = text 

    def create_metadata(self, keywords):
        """   
        Create a metadata 'keywords' field
        Args:
            text (str): Text content of the pdf file
        Returns:
            list: List of keywords 
        """
            
