import os 
import json 
import pandas as pd 



def save_data_step(data_dict: dict, path: str='vector_database/data'):
    """
    Save data step
    This function is responsible for saving the data to a file
    Args:
        data_dict: dict: Dictionary containing the data
    """

    assert isinstance(data_dict, dict), "Input data must be a dictionary"
    assert any(data_dict.values()), "Data dict is empty!"

    # check if the path exists
    if not os.path.exists(path):
        os.makedirs(path)
    
    # save the data to a file
    for pet_type, chunk in data_dict.items():
        # save the data to a file
        try:
            with open(f"{path}/{pet_type}.json", 'w') as f:
                json.dump(chunk, f)
        except Exception as e:
            print(f"Error saving json data: {e}")

    # Remove the 'metadata' key, update the keys to be compatible with csv format
    for pet_type, chunk in data_dict.items():
        for items in chunk: 
            items.update(items.pop('metadata'))
    
    # save the data to a file 
    try:
        for key, value in data_dict.items():
            df = pd.DataFrame(value)
            df.to_csv(f"{path}/{key}.csv", index=False)
    except Exception as e:
        print(f"Error saving csv data: {e}")





        
    

