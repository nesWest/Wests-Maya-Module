"""
	file        utilities.py

	date        07/21/2024

	authors     West Foulks (WestFoulks@gmail.com)

	brief       Contains a set of functions to help with mutliple varied maya 
                tasks. Should Eventually be moved into scripts that more relate to the functions.
"""
import os
import maya.cmds as cmds
import maya.mel
import random


"""
    Name        ShowIcons
    Desc        Finds .png and .jpeg ins speciific Icon Directorys and displays 
                them all in a window with their name as a annotation
"""
def ShowIcons() -> None:
    iconsWindow = cmds.window("Icons", widthHeight=(200, 55))
    scrollLayout = cmds.scrollLayout( horizontalScrollBarThickness=16, verticalScrollBarThickness=16)
    cmds.gridLayout( numberOfColumns=40, cellWidthHeight=(40, 40) )

    paths = os.environ['XBMLANGPATH'].split(";")

    for path in paths:
        print(path.replace("/","\\") + "\\")
        
        try :
            for f in os.listdir(path.replace("/","\\")):
                if f.endswith(".png") or f.endswith(".jpeg"):
                    cmds.image( image=f, annotation=f)
        except:
            print("EOF")
            
    cmds.showWindow("Icons")

"""
    Name        Restart Maya
    Desc        Restarts Maya after saving user preferences.
                This is slightly unstable and needs improving
"""
def RestartMaya() -> None:
    print("Restarting Maya")
    maya_executable = os.environ['MAYA_LOCATION'] + "/bin/maya.exe" #EXE location
    filename = cmds.file(q=True, sn=True) #current file name to try and relaunch
    cmds.savePrefs() #save user prefs
    os.spawnl(os.P_NOWAIT, maya_executable, '-file', filename) #Launches Maya
    cmds.quit()      #prompt user to save the maya file

"""
    Name        RNDTest
    Desc        Random test function to fill Shelf at the moment will remove in the future.
"""
def RndTest() -> None:
    cube = cmds.polyCube()
    array = []

    for i in range(0,10):
        for j in range(0,10):
            y = random.uniform(0,2)
            object = cmds.duplicate(cube)
            cmds.move(i,y/2,j, object)
            cmds.scale(1,y,1, object)
            array.append(object)
            
    cmds.delete(cube)

