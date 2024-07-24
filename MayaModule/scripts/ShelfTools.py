'''
	file        ShelfTools.py

	date        07/21/2024

	authors     West Foulks (WestFoulks@gmail.com)

	brief       Contains a set of functions to help create and manage this modules shelf tools
                TODO: Create XML or Json File for shelf information
'''
import os
import maya.cmds as cmds
import maya.mel
from JsonReader import GetShelves

'''
    Name        RefeshShelves
    Desc        When Clicked will Refesh all shelves adding new icons where needed.
    Input       Shelf Information file Name
'''
def RefreshShelves() -> None:
    shelves = GetShelves()

    shelfname = 'WestTestShelf'
    shelf = shelves[shelfname]
    RefreshShelf(shelfname, shelf)

def RefreshShelf(selfName : str, shelf : dict) -> None:
    gShelfTopLevel = maya.mel.eval('global string $gShelfTopLevel;$tmp_1=$gShelfTopLevel;')

    if cmds.shelfLayout(selfName,p=gShelfTopLevel, ex=1):
        if cmds.shelfLayout(selfName, q=1, ca=1):
            for each in cmds.shelfLayout(selfName, q=1, ca=1):
                cmds.deleteUI(each) 
    else:
        cmds.shelfLayout(selfName, p=gShelfTopLevel)

    for button in shelf:
        shelf_edit = cmds.shelfButton(parent=selfName, 
                                      label = button['label'], 
                                      annotation=button['annotation'], 
                                      image1=button['image1'], 
                                      command=button['command'],
                                      enableCommandRepeat=button['enableCommandRepeat'] )