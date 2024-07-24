import json
import os

dataName = 'module-data.json'

def GetShelves() -> dict:
    path = os.path.dirname(__file__).replace("MayaModule\\scripts","") 
    path += dataName

    with open(path, 'r') as file:
        data = json.load(file)
        file.close()

    return data['shelves']

