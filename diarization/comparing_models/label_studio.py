import json 
from config import PATHS


def label_studio_info():
    """
    Returns a list of tuples with the speaker ID, the start time and the end time.
    
    Arguments: 
    ----------
    (void)

    Returns:
    --------
    ref: list(tuple(str, double, double)) 
        A list of tuples where each element of the list is a tuple that contains the speaker, the start time of speech and the end time.
    """        
    # Opening the json.
    path = PATHS['ground_truth']
    f = open(path)
    data = json.load(f)

    # We create the list of the ground truth (reference)
    ref = []
    
    # We go through the json and store in the list
    for segment in data[0]["label"]:
        instance = (segment["labels"][0], segment["start"], segment["end"])
        ref.append(instance)

    return ref