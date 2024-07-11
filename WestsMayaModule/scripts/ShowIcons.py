import os
import maya.cmds as cmds

iconsWindow = cmds.window("Icons", widthHeight=(200, 55))
scrollLayout = cmds.scrollLayout( horizontalScrollBarThickness=16, verticalScrollBarThickness=16)
cmds.gridLayout( numberOfColumns=40, cellWidthHeight=(40, 40) )

paths = os.environ['XBMLANGPATH'].split(";")

for path in paths:
    print(path.replace("/","\\") + "\\")
    
    try :
        for f in os.listdir(path.replace("/","\\")):
            if f.endswith(".png"):
                cmds.image( image=f, annotation=f)
    except:
        print("Err")
        
cmds.showWindow("Icons")