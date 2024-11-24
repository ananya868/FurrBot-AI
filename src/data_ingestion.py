from abc import ABC, abstractmethod
import pandas as pd 
import os



# abstract class for Data Ingestion
class DataIngestion(ABC):
    @abstractmethod
    def __init__(self):
        pass 

    @abstractmethod 
    def ingest(self):
        pass


# class for ingesting Text Data from folders 
class TextDataIngestion(DataIngestion):
    def __init__(self, folder_name):
        self.folder_name = folder_name
    
    def ingest(self):
        """
        Ingest data from a folder containing text files
        
        Returns: 
            dict: A dictionary containing the text data pdf file paths
        """
        pdf_dict = {}
    
        # Walk through the directory
        for root, dirs, files in os.walk(self.folder_name):
            # Check if the current directory is not the root folder
            if root != self.folder_name:
                pdf_files = [file for file in files if file.lower().endswith('.pdf')]
                if pdf_files:
                    # Store the PDF files in the dictionary
                    pdf_dict[os.path.basename(root)] = pdf_files

        return pdf_dict


# class for ingesting data from a csv
class CSVDataIngestion(DataIngestion):
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def ingest(self):
        """
        Ingest data from a csv file 
        Returns: 
            list: A list of file paths to the csv files
        """ 
        csv_file_paths = []

        # Iterate through the directory
        for root, _, files in os.walk(self.folder_path):
            for file in files:
                if file.lower().endswith('.csv'):
                    # Construct the full file path and add to the list
                    full_path = os.path.join(root, file)
                    csv_file_paths.append(full_path)

        return csv_file_paths


# class for ingesting data from api 


# Factory Class for Data Ingestion 
class DataIngestionFactory:
    def __init__(self, strategy: DataIngestion):
        """ 
        Initialize the factory with a strategy
        """
        self.strategy = strategy

    def set_strategy(self, strategy: DataIngestion):
        """
        Set the strategy for the factory
        """
        self.strategy = strategy
    
    def ingest_data(self):
        """
        Ingest data using the strategy
        """
        return self.strategy.ingest()


    