from config import PATHS
import json

def parlament_conversion():
    hyp = []
    
    # Opening the json.
    path = PATHS['parlament_gt']
    f = open(path)
    data = json.load(f)

    for item in data:
        # we need to divide it by 1000 because its in ms.
        instance = (item["Speaker"], item["Start"], item["End"])
        hyp.append(instance)
    return hyp

hyp = parlament_conversion()
