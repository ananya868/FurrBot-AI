## Data Format 

The following data formats is to used for effective retrieval from a vector database. 
Metadata is utilized to improve re-ranking for best match.
Further metadata can be added to the existing database to improve retrieval.



```bash
[
    {
        'Dogs': [
            {
                'text': "para-para para para ....",
                'topic': 'Dogs',
                'blog_name': 'Diet for dogs...',
                'word_count': 180,
                'chunk_size': 155,
            },
            {
                # ...
            }
        ],
        'Cats': [
                # ... 
        ] 
    }
]
```
