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

    # Extra method to merge short elements in a list of text elements
    def merge_short_elements(self, item_list: list, text: list):
        """
        Merge short elements in a list of text elements
        About: Some elements in the list of texts (extracted from pdf) might be short, identify those and pass
                them to this function to merge them with their consecutive elements. 
        """
        for t in text:
            for i in range(len(item_list) - 1):
                if t in item_list[i]:
                    # Copy this 
                    content = item_list[i]
                    item_list.pop(i)
                    # Add the new content to next item 
                    item_list[i] = content + " " + item_list[i]
                    break 

        return item_list

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
