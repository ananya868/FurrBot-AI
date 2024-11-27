## Data Format 

The following data formats is to used for effective retrieval from a vector database. 
Metadata is utilized to improve re-ranking for best match.




```bash
[
    {
        'Dogs': [
            {
                'unique_id': 12,
                'text': "para-para para para ....",
                'pet_type': '',
                'blog_name': 'Labrador',
                'topic': 'Labrador training',
                'word_count': 180,
                'chunk_size': 155,
                'age_group': 'adult'
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


```bash
[
    {
        'birds': [
            { 
                'unique_id': 1,
                'text': "para-para para para ....",
                'pet_type': 'birds',
                'blog_name': 'Diet for birds',
                'topic': 'is wheat good for birds?',
                'word_count': 200, 
                'chunk_size': 180,
            }, 
            {
                'unique_id': 2,
                # .... 
            }
        ],

        'Rats': [
            # ....
        ]
    }
]
```

