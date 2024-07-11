import os
import maya.cmds as cmds
import maya.mel

def InstallShelf(settings = "shelfsettings_01.txt"):
    file = open(os.path.dirname(__file__)+ "\\" + settings, "r")
    shelfname=file.readline()
    
    dynamicshelf = None
    gShelfTopLevel = maya.mel.eval("global string $gShelfTopLevel;$tmp_1=$gShelfTopLevel;")
    if cmds.shelfLayout(shelfname, ex=True):
        # if the shelf exists, we want to delete the buttons, this is to
        # prevent a problem with buttons already existing on the shelf.
        # you may want to add better checking here if you do not wish to delete
        # buttons you are not managing for example.
        dynamicshelf = shelfname
        shelfbuttons = cmds.shelfLayout(shelfname, q=True, ca=True)
        if shelfbuttons:
            for button in shelfbuttons:
                cmds.deleteUI(button)
    else:
        dynamicshelf = cmds.shelfLayout(shelfname, p=gShelfTopLevel)



    content=file.readline()
    while content:
        splitContent = content.split(",")
        shelf_edit = cmds.shelfButton(parent=dynamicshelf, label = splitContent[0], annotation=splitContent[1], image1=splitContent[2], command=splitContent[3] )
        content=file.readline()

    #read in excel doc for shelfbuttons
    #shelf_edit = cmds.shelfButton(parent=dynamicshelf, label = "Name", annotation='Create a sphere.', image1='restart.png', command='cmds.sphere()' )


InstallShelf()