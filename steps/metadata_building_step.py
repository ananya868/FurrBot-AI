from src.metadata_creation import (
    MetadataFactory,
    UniqueIdMetadataCreation, 
    KeywordsMetadataCreation, 
    AgeGroupMetadataCreation 
)
import re
from tqdm import tqdm



def metadata_creation_step(data_dict: dict, api_key: str)-> dict: 
    """
    Metadata creation step 
    This function is responsible for creating metadata for the pre-processed data
    Args: 
        data_dict: dict: Dictionary containing the pre-processed data
    Returns:
        dict: Dict containing metadata
    """
    assert isinstance(data_dict, dict), "Input data must be a dictionary"
    assert any(data_dict.values()), "Data dict is empty!"

    # Loop into the data dict and create metadata for each data
    for pet_type, chunk in data_dict.items():
        for items in tqdm(chunk): 
            # items -> dict 
            # items['unique_id'] = MetadataFactory(strategy=UniqueIdMetadataCreation()).create_field()

            # if 'metadata' not in items:
            #     items['metadata'] = {}

            # Create metadata fields
            items['pet'] = pet_type
            # items['metadata']['keywords'] = MetadataFactory(strategy=KeywordsMetadataCreation(text=items.get('text'), api_key=api_key)).create_field()
            # items['metadata']['age_group'] = MetadataFactory(strategy=AgeGroupMetadataCreation(text=items.get('text'), api_key=api_key)).create_field()
            items['word_count'] = len(items.get('text').split())
            items['chunk_size'] = len(re.findall(r'\w+|\S\w*', items['text']))
        
        print(f"[info] --Metadata created for: {pet_type}--")

    assert any(data_dict.values()), "Metadata dict is empty!"

    return data_dict

# Sample data from this step:
# {
#     'Cats': [
#         {
            # 'unique_id': '123456',
            # 'text': 'This is a cat',
            # 'metadata': {
            #     'keywords': ['cat', 'pet', 'cute'],
            #     'age_group': 'adult',
            #     'word_count': 3,
            #     'chunk_size': 3
            # }
#         },
#         {
#             ....
#         }
#     ],
#     'Dogs': [
#         {
#             ....
#         }
#         ....
#     ],
# }    