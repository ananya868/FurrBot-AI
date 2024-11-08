from abc import ABC, abstractmethod 
from src.data_ingestion import DataIngestionFactory, TextDataIngestion, CSVDataIngestion #... (add more)



def data_ingestion_step(source: str, type: str='pdf') -> dict: 
    """  
    Data Ingestion Step   
    This function is responsible for ingesting data from various sources storing it to a data structure.
    Also, validating the correct data format and structure. 

    Key points: 
        - 'data' is the primary folder to store all the data 
        - 'source' is the folder name containing the data, e.g. 'pdf', 'csv', 'api'
        - 'type' is the type of data to ingest, e.g. 'pdf', 'csv', 'api'
    Args: 
        source (str): The folder name containing the data
    """  

    # Basic checks 
    assert os.path.exists(os.path.join('data', source)), f"{source} not found, please keep the data in the 'data' folder."
    assert type in ['pdf', 'csv', 'api', 'json', 'text'], f"Invalid data type: {type}. Please choose from 'pdf', 'csv', 'api', 'json', 'text'."

    # Ingestor Initialization
    if type == 'pdf':
        ingestor = DataIngestionFactory(strategy=TextDataIngestion(folder_name=source))
    elif type == 'csv':
        ingestor = DataIngestionFactory(strategy=CSVDataIngestion(folder_path=source))
    elif type == 'api':
        print("API ingestion not implemented yet.")
    elif type == 'json':
        print("JSON ingestion not implemented yet.")
    elif type == 'text':
        print("Text ingestion not implemented yet.")
    else:
        raise NotImplementedError(f"Data ingestion step failed for type: {type}")
     
    # Data Ingestion
    try:
        data = ingestor.ingest_data()
    except Exception as e: 
        raise Exception(f"Data ingestion failed with error: { str(e) }")        

    assert any(data.values()), f"No data found in the source: {source}"

    return data 


