from abc import ABC, abstractmethod




class DataChunking(ABC):
    """
        Factory class to create data chunking objects. 
    """
    @abstractmethod
    def chunk(self):
        pass



class ParagraphBasedChunking(DataChunking):
    """  
    Works best for pdf content in our case
    Treat each paragraph as a separate chunk. 
    """  
    def __init__(self, data_dict: dict):
        self.data_dict = data_dict
    
    def chunk(self):
        """  
        Chunk the data based on paragraphs from the pdf! 
        Returns:
            dict: Dictionary of chunks
        """  
        chunks = {}
        for pet_type, blog_list in self.data_dict.items():
            chunks[pet_type] = []
            for blog in blog_list:
                text_list = blog.get('text')
                topic_list = blog.get('topic')
                blog_name = blog.get('blog_name')
                for text, topic in zip(text_list, topic_list):
                    chunks[pet_type].append(
                        {
                            "text": text,
                            "topic": topic,
                            "blog_name": blog_name
                        }
                    )
        return chunks


class FixedLengthChunking(DataChunking): 
    """
    Works best for text content.
    Treat each fixed length of text as a separate chunk. 
    """
    def __init__(self, data_dict: dict, chunk_length: int):
        self.data_dict = data_dict
        self.chunk_length = chunk_length
    
    def chunk(self):
        """
        Chunk the data based on fixed length of text.
        Returns:
            dict: Dictionary of chunks
        """
        chunks = {}
        for pet_type, blog_list in self.data_dict.items():
            chunks[pet_type] = []
            for blog in blog_list:
                text_list = blog.get('text')
                topic_list = blog.get('topic')
                blog_name = blog.get('blog_name')
                for text, topic in zip(text_list, topic_list):
                    for i in range(0, len(text), self.chunk_length):
                        chunks[pet_type].append(
                            {
                                "text": text[i:i+self.chunk_length],
                                "topic": topic,
                                "blog_name": blog_name
                            }
                        )
                    
        return chunks
        # Dont know if it works xD


class SentenceBasedChunking(DataChunking):
    pass


class BigParaChunking(DataChunking):
    pass



# Factory class to create data chunking objects  
class DataChunkingFactory:
    """
    Factory class to create data chunking objects.
    """
    def __init__(self, strategy: DataChunking):
        self.strategy = strategy
    
    def chunk_data(self):
        return self.strategy.chunk()





