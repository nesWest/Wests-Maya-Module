from MayaModule.scripts.ModuleWindow import ModuleWindow as MW
import MayaModule.scripts.JsonReader as JsonReader
import maya.cmds as cmds
import os

def onMayaDroppedPythonFile(obj):
    #Path found here so that we know the correct path to module
    PathToModule = os.path.dirname(__file__)
    JsonReader.UserData_SetModulePath( PathToModule + "/MayaModule/")
    MW.showWindow()

