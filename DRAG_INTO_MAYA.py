from InstallWindow import InstallWindow
from MayaModule.scripts.ShelfTools import RefreshShelves
import maya.cmds as cmds
import os

def onMayaDroppedPythonFile(obj):
    #Path found here so that we know the correct path to module
    PathToModule = os.path.dirname(__file__)
    InstallWindow(PathToModule +"/MayaModule")
    RefreshShelves()

