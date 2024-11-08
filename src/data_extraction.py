from abc import ABC, abstractmethod
import fitz
import os 


# Define abstract base class for Data Extraction 
class DataExtractionBase(ABC):
    @abstractmethod
    def __init__(self):
        pass 

    @abstractmethod
    def extract(self):
        pass



# Class for extracting text from PDF files
class PDFTextExtractorForBreeds(DataExtractionBase):
    def __init__(self, pdf_file_path):
        self.pdf_file_path = pdf_file_path

    # Extract method for extracting text from PDF files 
    def extract(self):
        """
        Extract text from a PDF file
        """
        # Open the PDF file using PyMuPDF
        pdf_reader = fitz.open(self.pdf_file_path)

        # list for storing text
        text_list = []
        subheadings = []

        # Iterate through each page in the PDF file
        for i in range(pdf_reader.page_count):
            page = pdf_reader[i]
            blocks = page.get_text("dict")["blocks"] 

            for block in blocks:
                if "lines" in block:
                    for line in block["lines"]:
                        for span in line["spans"]:
                            text = span["text"].strip()
                            font_size = span["size"]
                            font_flags = span["flags"]
                            
                            # Condition
                            if font_size > 12:
                                text_list.append(text)
                                subheadings.append(text)
                            else:
                                # If not a new section, add it to the current section
                                if text_list and not text_list[-1].endswith("\n"):
                                    text_list[-1] += " " + text
                                else:
                                    text_list.append(text) # Starts new section
        
        text_list_01 = text_list.copy()
        # Iterate through the list and merge items containing "FAQ" with the next item
        i = 0
        while i < len(text_list_01) - 1: 
            if "FAQ" in text_list_01[i] and "References" not in text_list_01[i]:
                # Merge current item with the next item unless the next item contains "References"
                if "References" not in text_list_01[i + 1]:
                    text_list_01[i] = text_list_01[i] + " " + text_list_01[i + 1]
                    # Remove the next item (since it's now merged)
                    text_list_01.pop(i + 1)
                else:
                    i += 1  # Move to the next item if the next one contains "References"
            else:
                i += 1  # Only move to the next item if no merge happened or if "References" was encountered
        
        return text_list_01, subheadings 
        

# Class for merging shorter elements in a list of text elements 
class MergeShortElements(DataExtractionBase):
    def __init__(self, item_list: list, subheadings: list, threshold: int = 16):
        self.item_list = item_list
        self.subheadings = subheadings
        self.threshold = threshold

    # method to merge short elements in a list of text elements
    def extract(self):
        """
        Merge short elements in a list of text elements
        About: Some elements in the list of texts (extracted from pdf) might be short, identify those and pass
                them to this function to merge them with their consecutive elements. 
        """
        # Extract short elements from the list 
        # text = [e for e in self.item_list if len(e.split(" ")) < self.threshold]
        items, indexes = [], []
        for e, item in enumerate(self.item_list): 
            # if item is shorter than the threshold, add it to the next item, also merge the same subheading with that index
            if len(item.split(" ")) < self.threshold:
                items.append(item)
                indexes.append(e) 

        # Merge the short elements with the next element, also the subheading with the next subheading
        for i in indexes: 
            if i < len(self.item_list) - 1:
                self.item_list[i] = self.item_list[i] + " " + self.item_list[i + 1]
                self.subheadings[i] = self.subheadings[i] + " " + self.subheadings[i + 1]
                self.item_list.pop(i + 1)
                self.subheadings.pop(i + 1)
                
        return self.item_list, self.subheadings
    


# Factory class for Data Extraction 
class DataExtractionFactory:
    def __init__(self, strategy: DataExtractionBase):
        """ 
        Initialize the factory with a strategy
        """
        self.strategy = strategy

    def set_strategy(self, strategy: DataExtractionBase):
        """
        Set the strategy for data extraction
        """
        self.strategy = strategy
    
    def extract(self):
        """
        Extract data using the set strategy
        """
        return self.strategy.extract()
