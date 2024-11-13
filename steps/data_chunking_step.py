from src.data_chunking import (
    DataChunkingFactory,
    ParagraphBasedChunking,
    FixedLengthChunking
)




def data_chunking_step(data_dict: dict, chunking_method: str='para', chunk_length: int=None) -> dict:
    """  
    Data chunking step
    This function is responsible for chunking the pre-processed data using specific chunking method
    Validates the correct data format and structure.
    Args:
        data_dict: dict: Dictionary containing the pre-processed data
        chunk_length: int: Length of the chunk
    Returns:
        dict: Dictionary of chunks
    """

    assert isinstance(data_dict, dict), "Input data must be a dictionary"
    assert any(data_dict.values()), "Data dict is empty!"

    # pipeline of data chunking steps
    data_chunking_pipeline = {
        'para': ParagraphBasedChunking, 
        'fixed': FixedLengthChunking
        # .... 
    }

    for method, chunking_class in data_chunking_pipeline.items():
        if method == chunking_method:
            chunker = DataChunkingFactory(strategy=chunking_class(data_dict))
            chunks = chunker.chunk_data()        
    # check for data in chunks
    assert any(chunks.values()), "Chunked data is empty!"
    return chunks



# Sample data from this step:
# {
#     'Cats': [
#         {
#             'text': 'I have a cat. My cat is very cute. I love my cat.', 
#             'topic': 'cat', 
#             'blog_name': 'cat_lover'
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
#     .... 
# }