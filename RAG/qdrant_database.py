# Script for all operations on Qdrant database (query, upserting, etc)


from qdrant_client import models, QdrantClient 
from sentence_transformers import SentenceTransformer
import os


class QdrantDatabase: 
    def __init__(self, cluster_uri: str, api: str, emb_model: str='all-MiniLM-L6-v2'):
        self.client = QdrantClient(cluster_uri, api_key=api)
        self.encoder = SentenceTransformer(emb_model)

    

    def create_collection(self, collection_name: str, distance_m: str='cosine'):
        dm = {
            'cosine': models.Distance.COSINE,
            'euclidean': models.Distance.EUCLID,
            'dot': models.Distance.DOT, 
            'manhattan': models.Distance.MANHATTAN
        }

        flag = -1
        for i in self.client.get_collections().collections: 
            if i.name == collection_name: 
                flag = 1
                print("Collection already exist! Don't need to create!")
                break
        
        if flag == -1:
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config=models.VectorParams(
                    size=self.encoder.get_sentence_embedding_dimension(),
                    distance=dm.get(distance_m),
                    on_disk=True # whether to save in memory
                )
            )
        return self.client 



    def update_collection(self, collection_name: str, distance: str, on_disk: bool):
        dm = {
            'cosine': models.Distance.COSINE,
            'euclidean': models.Distance.EUCLID,
            'dot': models.Distance.DOT,
            'manhattan': models.Distance.MANHATTAN
        }
        self.client.update_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=self.encoder.get_sentence_embedding_dimension(),
                distance=dm.get(distance),
                on_disk=True
            )
        )



    def upsert_vectors(self, collection_name: str, documents: list[dict]):
        self.client.upload_points(
            collection_name=collection_name, 
            points=[
                models.PointStruct(
                    id=idx,
                    vector=self.encoder.encode(doc['text']).tolist(),
                    payload=doc
                )
                for idx, doc in enumerate(documents)
            ]
        )

    

    def query_db(self, collection_name: str, limits: int, query: str):
        hits = self.client.query_points(
            collection_name=collection_name, 
            query=self.encoder.encode(query).tolist(),
            limit=limits 
        ).points

        res = []
        for hit in hits:
            hit.payload['score'] = hit.score 
            res.append(hit.payload)
        
        return res 
    


    def get_cluster_info(self, cluster): 
        pass
