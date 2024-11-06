from abc import ABC, abstractmethod
import re


class DataPreProcessingBase(ABC): 
    @abstractmethod 
    def __init__(self):
        pass

    @abstractmethod 
    def process(self):
        pass 


# Define a class to remove irrelevant links from the text
class RemoveLinks(DataPreProcessingBase):
    def __init__(self, link_prefixes: list, text: list):
        self.link_prefixes = link_prefixes
        self.text = text

    def process(self):
        """ 
        Remove links from the text
        """
        for i in range(len(self.text)):
            pattern = r'\b(?:' + '|'.join([re.escape(prefix) for prefix in self.link_prefixes]) + r')\S*'
            self.text[i] = re.sub(pattern, '', self.text[i])
        
        return self.text


# Define a class to remove irrelevant date/time from the text
class RemoveDateTime(DataPreProcessingBase):
    def __init__(self, text: list):
        self.text = text

    def process(self):
        """ 
        Remove date/time from the text
        """
        for i in range(len(self.text)):
            date_pattern = r'\b\d{2}/\d{2}/\d{2}\b' # Date pattern
            time_pattern = r'\b\d{1,2}:\d{2} (?:AM|PM)\b' # time pattern
            # Combine all patterns using the OR operator '|'
            combined_pattern = f"{date_pattern}|{time_pattern}"
            self.text[i] = re.sub(combined_pattern, '', self.text[i])

        return self.text


# Define a class to remove irrelevant special sentences from the text
class RemoveIrrelevantSentences(DataPreProcessingBase):
    def __init__(self, text: list, sentences: list=None):
        self.text = text
        self.sentences = sentences

    def process(self):
        """
        Remove irrelevant sentences from the text
        - these sentences need to be found out by manually analysis the text corpus
        """
        # Special case for repeating title across blogs
        title = self.text[0].split("petmd.com")[0][:-1]
        # Remove title from text
        pattern_1 = rf'\b{re.escape(title)}\b[.!?]?'
        for i in range(1, len(self.text)):
            self.text[i] = re.sub(pattern_1, "", self.text[i])

        # General case 
        if self.sentences is None:
            return self.text
        for sentence in self.sentences:
            for i in range(0, len(self.text)):
                pattern = rf'\b{re.escape(sentence)}\b[.!?]?'  # Define pattern with boundaries and optional punctuation
                self.text[i] = re.sub(pattern, "", self.text[i])

        return self.text 


# Define a class to Remove page numbers from the text 
class RemovePageNumbers(DataPreProcessingBase):
    def __init__(self, text: list):
        self.text = text

    def process(self):
        """
        Remove page numbers from the text
        """
        for i in range(len(self.text)):
            pattern = r'\b\d+/\d+\b' # Define pattern for page numbers
            self.text[i] = re.sub(pattern, "", self.text[i])

        return self.text


# Define a class to lowercase the text and remove extra spaces
class LowerCaseAndRemoveExtraSpaces(DataPreProcessingBase):
    def __init__(self, text: list):
        self.text = text
    
    def process(self):
        """
        Lowercase the text and remove extra spaces
        """
        for i in range(len(self.text)):
            self.text[i] = self.text[i].lower()
            self.text[i] = re.sub(r'\s+', ' ', self.text[i])

        return self.text



# Factory class for Data Pre-Processing 
class DataPreProcessingFactory: 
    def __init__(self, strategy=DataPreProcessingBase):
        """  
        Initialize the strategy
        """
        self.strategy = strategy
    
    def set_strategy(self, strategy):
        """  
        Switch the strategy for data pre-processing
        """
        self.strategy = strategy

    def process_data(self):
        """
        Process the text using the strategy
        """
        return self.strategy.process()
    


