from InstallWindow import InstallWindow
import InstallShelf
import maya.cmds as cmds
import os

def onMayaDroppedPythonFile(obj):
    #Path found here so that we know the correct path to module
    PathToModule = os.path.dirname(__file__)
    InstallShelf.InstallShelf()
    InstallWindow(PathToModule +"/WestsMayaModule")

