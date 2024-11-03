## Data Format 

The following data formats is to used for effective retrieval from a vector database. 
Metadata is utilized to improve re-ranking for best match.




```bash
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


```bash
[
    {
        "unique_id": 18,
        "text": "The blog explains how to take care of you pet.....",
        "pet_type": "hamsters",
        "blog_topic": "How to take care of a hamster?",
        # "pet_breed": "golden retriever", # no breed
        # "category": "Diet and exercise", # no category
        # "author": "Miranda Jose", # optional 
        "source": "https://petmd.com/hamsters", 
        "keywords": ["care", "hamsters", "diet"],
        # "pet_age_group": "adult"  no age group
    },
    {
        ...
    }
]
```

