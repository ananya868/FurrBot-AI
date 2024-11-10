from src.data_pre_processing import (
    DataPreProcessingFactory,
    RemoveLinks,
    RemoveDateTime,
    RemovePageNumbers,
    RemoveIrrelevantSentences, 
    LowerCaseAndRemoveExtraSpaces
)



def data_pre_processing_step(data_dict: dict) -> dict:
    """  
    Data pre-processing step  
    This function is responsible for pre-processing the raw text data
    Validates the correct data format and structure.
    Args:
        data_dict: dict: Dictionary containing the raw text data
    Returns:
        dict: Dictionary of pre-processed data
    """  
    assert isinstance(data_dict, dict), "Invalid data format. Please provide a dict object" 
    assert any(data_dict.values()), "Data dict is empty!"

    # pipeline of data pre-processing steps
    data_pre_processing_pipeline = [
        RemoveLinks,
        RemoveDateTime,
        RemoveIrrelevantSentences,
        RemovePageNumbers,
        LowerCaseAndRemoveExtraSpaces
    ]

    # process the data using the pipeline
    processed_data = {}
    for step in data_pre_processing_pipeline:
        # loop in data dict
        for pet_type, blog_list in data_dict.items():
            processed_data[pet_type] = []
            for blog in blog_list:
                processor = DataPreProcessingFactory(strategy=step(blog.get('text')))
                processed_text = processor.process_data()
                processed_data[pet_type].append(
                    {
                        "text": processed_text,
                        "topic": blog.get('topic'),
                        "blog_name": blog.get('blog_name')
                    }
                )
    
    # check for data in processed data 
    assert any(processed_data.values()), "Processed data is empty!"
    # check if text topic and blog_name keys are present
    for k, v in processed_data.items():
        assert all([i.get('text') for i in v]), "Text key not found in the pre-processed data"
        assert all([i.get('topic') for i in v]), "Topic key not found in the pre-processed data"
        assert all([i.get('blog_name') for i in v]), "Blog name key not found in the pre-processed data"
        
    return processed_data






        


