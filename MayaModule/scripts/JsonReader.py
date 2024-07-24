import json
import os

moduleDataName = 'module-data.json'
userDataName = 'user-data.json'

def GetPath(file : str) -> str:
    #if called from maya will need to remove MayaModule\Scripts
    path = os.path.dirname(__file__).replace('MayaModule\\scripts','')
    path += file
    return path

def GetData(file : str = moduleDataName ) -> dict:
    path = GetPath(file)

    try:
      with open(path, 'r') as file:
        data = json.load(file)
        file.close()
    except FileNotFoundError:
       print("No .JSON Found Writing New")
       data = {}

    return data

def GetShelves() -> dict:
    return GetData()['Shelves']

def GetVersionNumber() -> float :
    return GetData()['Info']['VersionNumber']

def UserData_NewExport(dictionary : dict) :
    data = GetData(userDataName)

    data["ExportLocations"].update(dictionary)

    path = GetPath(userDataName)
    with open(path, 'w') as file:
      json.dump(data, file, indent=4)
      file.close()

    return

def UserData_GetExportLocation(exportInfo : str) -> str:
    data = GetData(userDataName)

    try:
      data = str( data["ExportLocations"][exportInfo] )
    except:
      data = ""

    return data