## Data Format 

The following data format is to used for effective retrieval from a vector database. 
Metadata is utilized to improve re-ranking for best match.


```python
[
    {
        "unique_id": 18,
        "text": "The diet for a golden retriever is .....",
        "pet_type": "dog",
        "pet_breed": "golden retriever",
        "category": "Diet and exercise",
        "author": "Miranda Jose", 
        "source": "https://petmd.com/golden-retriever-diet",
        "keywords": ["diet", "golden-retriever", "low fat"],
        "pet_age_group": "adult"
    },
    {
        ...
    }
]
```