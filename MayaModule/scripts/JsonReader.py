import json
import os

moduleDataName = 'module-data.json'
userDataName = 'user-data.json'

def GetPath(file : str) -> str:
    path = os.path.dirname(__file__).replace('MayaModule\\scripts','') #depends on where this is called from urg
    path += file
    return path

def GetData(file : str = moduleDataName ) -> dict:
    path = GetPath(file)

    with open(path, 'r') as file:
        data = json.load(file)
        file.close()

    return data

def GetShelves() -> dict:
    return GetData()['Shelves']

def GetVersionNumber() -> float :
    return GetData()['Info']['VersionNumber']

def UserData_NewExport(dictionary : dict) :
    return