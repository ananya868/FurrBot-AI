from abc import ABC, abstractmethod
import os, time
from typing import List, Dict, Any, Optional


class DB(ABC):
    @abstractmethod
    def __init__(self):
        pass


class PineconeDB(DB):
    """
    Pinecone vector database class

    - Uses Index host uri to connect.
    - Doesn't support updating or deleting vectors.
    - Supports query operations.

    NOTE : To upsert vectors, please refer to 'shift_database.ipynb' notebook in this repo
    """
    def __init__(self):
        from pinecone import Pinecone 
        assert os.getenv('PINECONE_API_KEY') is not None, "Pinecone API key not found"

        # Initialize Pinecone client
        try:
            self.client = Pinecone(
                api_key = os.getenv('PINECONE_API_KEY')
            )
        except Exception as e:
            raise Exception(f"Failed to initialize Pinecone client: {e}")

        # Initialize index
        try: 
            assert os.getenv('PINECONE_INDEX_HOST') is not None, "Pinecone index name not found"
            self.index = self.client.Index(host = os.getenv('PINECONE_INDEX_HOST'))
        except Exception as e:
            raise Exception(f"Failed to initialize Pinecone index: {e}")

    def check_connection(self) -> bool:
        """
        Check if the connection to the Pinecone index is valid.

        Returns:
            bool: True if the connection is valid, False otherwise.
        """
        try:
            self.index.describe_index_stats()
            return True
        except Exception as e:
            raise Exception(f"Database connection error: {e}")

    def query(
        self, 
        query: str, 
        namespace: str, 
        top_k: int = 10, 
        top_n: int = 3, 
        re_ranker_model: str = "bge-reranker-v2-m3"
    ) -> Any: 
        """
        Query the Pinecone index with a given query string.

        Args:
            query (str): The query string.
            namespace (str): The namespace to search in.
            top_k (int): The number of top results to return.
            top_n (int): Final no. of re-ranked points.
            re_ranker_model (str): The model to use for re-ranking.
        
        Returns:
            Any: The results of the query.
        """
        # Init time
        s = time.time()

        # Similarity search
        results = None
        try:
            results = self.index.search(
                namespace = namespace, 
                query = {
                    "inputs": {
                        "text": query,                        
                    }, 
                    "top_k": top_k,
                },
                rerank = {
                    "model": re_ranker_model, 
                    "top_n": top_n, 
                    "rank_fields": ["chunk_text"]
                },
                fields=["chunk_text"]
            )
        except Exception as e:
            raise Exception(f"Failed to query Pinecone index: {e}")

        # End time
        e = time.time()
        return results, e - s   


    

    

