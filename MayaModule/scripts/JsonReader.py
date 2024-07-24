import json
import os

dataName = 'module-data.json'

def GetPath() -> str:
    path = os.path.dirname(__file__).replace("MayaModule\\scripts","") 
    path += dataName
    return path

def GetData() -> dict:
    path = GetPath()

    with open(path, 'r') as file:
        data = json.load(file)
        file.close()

    return data

def GetShelves() -> dict:
    return GetData()['shelves']

