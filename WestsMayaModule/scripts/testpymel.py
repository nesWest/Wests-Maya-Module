import maya.cmds as cmds
import random

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