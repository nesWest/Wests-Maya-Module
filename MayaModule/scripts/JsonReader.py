'''
	file        JsonReader.py

	date        07/24/2024

	authors     West Foulks (WestFoulks@gmail.com)

	brief       Contains a set of functions to help ease fetching data from both Module-data.json and user-data.json
              these file contain important information this module uses.
'''
import json
import os

moduleDataName = 'module-data.json'
userDataName = 'user-data.json'

'''
    Name        GetPath
    Desc        Gets the correct filepath to the file requested
    Input       String name to the specific file. example 'module-data.json'
    returns     a string path to the file requested.
'''
def GetPath(file : str) -> str:
    #if called from maya will need to remove MayaModule\Scripts
    path = os.path.dirname(__file__).replace('MayaModule\\scripts','')
    path += file
    return path

'''
    Name        GetData
    Desc        Fetches the .json data from a specific file requested by name
    Input       String name to the specific file. example 'module-data.json'
    returns     the data as a dictionary
'''
def GetData(file : str = moduleDataName ) -> dict:
    path = GetPath(file)

    try:
      with open(path, 'r') as file:
        data = json.load(file)
        file.close()
    except FileNotFoundError:
       print('No .JSON Found')
       data = {}

    return data

'''
    Name        GetShelves
    returns all shelf information as a dictionary
'''
def GetShelves() -> dict:
    return GetData()['Shelves']

'''
    Name        GetVersionNumber
    Desc        Returns the module version number as a float
'''
def GetVersionNumber() -> float :
    return GetData()['Info']['VersionNumber']

'''
    Name        UserData_NewExport
    Desc        Saves the File path for the corrisponding export
    Input       {'ExportType':'filepath'}
'''
def UserData_NewExport(dictionary : dict) -> None:
    data = GetData(userDataName)

    try:
      data['ExportLocations'].update(dictionary)
    except:
       data.update({'ExportLocations':dictionary})

    path = GetPath(userDataName)
    with open(path, 'w') as file:
      json.dump(data, file, indent=4)
      file.close()

    return

'''
    Name        UserData_GetExportLocation
    Desc        returns the file path for the correct exporttype
    Input       export type
'''
def UserData_GetExportLocation(exportInfo : str) -> str:
    data = GetData(userDataName)

    try:
      data = str( data['ExportLocations'][exportInfo] )
    except:
      data = ''

    return data

