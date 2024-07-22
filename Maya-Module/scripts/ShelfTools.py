"""
	file        ShelfTools.py

	date        07/21/2024

	authors     West Foulks (WestFoulks@gmail.com)

	brief       Contains a set of functions to help create and manage this modules shelf tools
                TODO: Create XML or Json File for shelf information
"""
import os
import maya.cmds as cmds
import maya.mel

"""
    Name        RefeshShelves
    Desc        When Clicked will Refesh all shelves adding new icons where needed.
    Input       Shelf Information file Name
"""
def RefreshShelves(settings = "shelfsettings_01.txt") -> None:

    #TODO ensure it updates correctly
    #TODO add mutli shelf functionality and xml functionality

    with open(os.path.dirname(__file__)+ "\\" + settings, "r") as file:
        shelfname=file.readline().replace("\n","")
        
        gShelfTopLevel = maya.mel.eval("global string $gShelfTopLevel;$tmp_1=$gShelfTopLevel;")

        if cmds.shelfLayout(shelfname,p=gShelfTopLevel, ex=1):
            if cmds.shelfLayout(shelfname, q=1, ca=1):
                for each in cmds.shelfLayout(shelfname, q=1, ca=1):
                    cmds.deleteUI(each) 
        else:
            cmds.shelfLayout(shelfname, p=gShelfTopLevel)

        for line in file:
            splitContent = line.split(",")
            shelf_edit = cmds.shelfButton(parent=shelfname, label = splitContent[0], annotation=splitContent[1], image1=splitContent[2], command=splitContent[3] )


