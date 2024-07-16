import os
import maya.cmds as cmds
import maya.mel

def InstallShelf(settings = "shelfsettings_01.txt"):
    file = open(os.path.dirname(__file__)+ "\\" + settings, "r")
    shelfname=file.readline()
    
    dynamicshelf = None
    gShelfTopLevel = maya.mel.eval("global string $gShelfTopLevel;$tmp_1=$gShelfTopLevel;")
    if cmds.shelfLayout(shelfname, p=gShelfTopLevel, ex=True):
        dynamicshelf = shelfname
        cmds.deleteUI(gShelfTopLevel + "|" +shelfname)
    
    dynamicshelf = cmds.shelfLayout(shelfname, p=gShelfTopLevel)

    content=file.readline()
    while content:
        splitContent = content.split(",")
        shelf_edit = cmds.shelfButton(parent=dynamicshelf, label = splitContent[0], annotation=splitContent[1], image1=splitContent[2], command=splitContent[3] )
        content=file.readline()

    #read in excel doc for shelfbuttons
    #shelf_edit = cmds.shelfButton(parent=dynamicshelf, label = "Name", annotation='Create a sphere.', image1='restart.png', command='cmds.sphere()' )

