import MayaModule.scripts.ModuleWindow as MW
import maya.cmds as cmds
import os

def onMayaDroppedPythonFile(obj):
    #Path found here so that we know the correct path to module
    PathToModule = os.path.dirname(__file__)
    MW.win.setModulePath(PathToModule)
    MW.ShowWindow()
    

