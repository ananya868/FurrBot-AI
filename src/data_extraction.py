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







