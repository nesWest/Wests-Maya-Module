import os
import maya.cmds as cmds
import random

def ShowIcons():
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
            print("Err")
            
    cmds.showWindow("Icons")

def RestartMaya():
    print("Restarting Maya")
    maya_executable = os.environ['MAYA_LOCATION'] + "/bin/maya.exe" #EXE location
    filename = cmds.file(q=True, sn=True) #current file name to try and relaunch
    cmds.savePrefs() #save user prefs
    os.spawnl(os.P_NOWAIT, maya_executable, '-file', filename) #Launches Maya
    cmds.quit()      #prompt user to save the maya file

def RndTest():
    cube = cmds.polyCube()
    array = []

    for i in range(0,10):
        for j in range(0,10):
            y = random.uniform(0,2)
            object = cmds.duplicate(cube)
            cmds.move(i,y/2,j, object)
            cmds.scale(1,y,1, object)
            array.append(object)
            
    #cmds.combine()
            
    cmds.delete(cube)