from src.data_extraction import (
    DataExtractionFactory, 
    PDFTextExtractorForBreeds,
    MergeShortElements, 
    # ... 
)
import os



def data_extraction_step(data_dict: dict, source: str='data')-> dict:
    """  
    Data extraction step
    This function is responsible for extracting raw text and convert into structured lists
    Validates the correct data format and structure. 
    Args:
        data_dict: dict: Dictionary containing the file names
    Returns: 
        dict: Dictionary of extracted data
    """  
    # check type of data 
    # get first element of the data dict to determine the type of data
    assert isinstance(data_dict, dict), "Invalid data format. Please provide a dict object" 

    # check if dict is not empty 
    if any(data_dict.values()):
        data_type = data_dict.get(list(data_dict.keys())[0])[0].split('.')[1]

    # Create the appropriate extractor and merger based on the data type
    extracted_data = {}
    if data_type == 'pdf': 
        # Process pdf 
        for pet_type, blog_list in data_dict.items():
            extracted_data[pet_type] = []
            for blog in blog_list:
                pdf_path = os.path.join(source, 'pdf_data', pet_type, blog)
                # Extractor 
                extractor = DataExtractionFactory(strategy=PDFTextExtractorForBreeds(pdf_path))
                text, topic = extractor.extract() # text extracted
                # merge 
                merger = DataExtractionFactory(strategy=MergeShortElements(text, topic))
                text, topic = merger.extract()
                # append to the extracted data
                extracted_data[pet_type].append(
                    {
                        'text': text,
                        'topic': topic,
                        'blog_name': blog.split('.pdf')[0]
                    }
                )
    else:
        raise print(f"Data extraction not implemented for this data type: {data_type}!")
    
    # Validator
    assert any(extracted_data.values()), "Extracted data is empty!"
    # check if text topic and blog_name keys are present 
    for k, v in extracted_data.items():
        assert all([i.get('text') for i in v]), "Text key not found in the extracted data"
        assert all([i.get('topic') for i in v]), "Topic key not found in the extracted data"
        assert all([i.get('blog_name') for i in v]), "Blog name key not found in the extracted data"

    return extracted_data



# sample extracted data:
# {
#     "dog": [
#         {
#             'text': ['..', '..'],
#             'topic': ['..', '..'],
#             'blog_name': 'labrador...',
#         }, 
#         {
#             ....
#         },
#         ....
#     ],
#     "cat": [
#         {
#             'text': ['..', '..'],
#             'topic': ['..', '..'],
#             'blog_name': 'siamese...',
#         }, 
#         {
#             ....
#         },
#         ....
#     ],
#     ....
#     ...
#     .
# }