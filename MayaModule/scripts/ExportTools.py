"""
	file        ExportTools.py

	date        07/21/2024

	authors     West Foulks (WestFoulks@gmail.com)

	brief       Contains a set of functions to help ease export process In maya via Shelf Tools
                
                #file -force -options "v=0;" -typ "FBX export" -pr -es "C:/Users/west/Downloads/SK_Shockwave.fbx";
                #Consider moving options to .mel file
                #mel.eval('"source ExportOptions.mel;"') # source of the file
                #mel.eval("Animation;") #name of the function 
                #may move export def to funct in mel
"""
import os
import maya.cmds as cmds
import maya.mel as mel

"""
    Name        Character Export
    Desc        Helps streamline exporting a character rig
"""
def CharacterExporter() -> None:

    #Select Correct Objects
    cmds.select('game_root')
    cmds.select('*_Meshes', add=True)

    savePath = GetFilepath()

    if not savePath :
        return

    #TODO Add Checks for forced naming conventions here

    options = "v={0}"
    FBXOption("false")
    cmds.file(savePath, force=True, op=options, typ="FBX export", pr=True, es=True)
    print("Character Exporter (InProgress)")

"""
    Name        Animation Export
    Desc        Helps streamline exporting a animation for a character rig
"""
def AnimationExporter() -> None:
    #Deletes namespace
    RemoveNamespace()

    #Select Correct Objects
    cmds.select('game_root')
    cmds.select('*_Meshes', add=True)

    savePath = GetFilepath()

    if not savePath :
        ReAddNamespace() #gotta abort so readd
        return

    #TODO Add Checks for forced naming conventions here

    options = "v={0}"
    FBXOption("true")
    cmds.file(savePath, force=True, op=options, typ="FBX export", pr=True, es=True)
    
    #Re Add Namespace to rig
    ReAddNamespace()

    #- Button to put namespace back
    print("Animation Exporter (InProgress)")

"""
    Name        Batch Export
    Desc        batch export files / animations
    TODO        Fill Function
"""
def BatchExporter() -> None:
    #By file set, not folder.
    print("Batch Exporter (Incomplete)")


"""
    Name        RemoveNamespace
    Desc        removes name Space From Selelction
                TODO: should remove cals to cmds.select inside of this function
                      could cause issues down the line
"""
def RemoveNamespace() -> None:
    #get namespace
    cmds.select('*:game_root')
    gameRootName = []
    gameRootName = cmds.ls(sl=True, sn=True)
    cmds.select(clear=True)
    #Delete namespace
    myNameSpace = (gameRootName[0].split(':'))[0]
    cmds.namespace( set=':')
    cmds.namespace( set=myNameSpace)
    cmds.namespace( rel=True )
    cmds.select ("game_root")

"""
    Name        reAddNamespace
    Desc        adds a namespace to Selection
                TODO: Rename to AddNamespace
"""
def ReAddNamespace() -> None:
    #Put namespace back
    cmds.namespace( set=':')
    cmds.namespace( rel=False )

"""
    Name        RefeshShelves
    Desc        Sets FBX export Options for animation or Character Rig
    Input       If the export options needed are for animations.
"""
def FBXOption(animation = "false") -> None:
    #TODO could store settings in file
    mel.eval("FBXExportSmoothMesh -v true")
    mel.eval("FBXExportUseSceneName -v false")
    mel.eval("FBXExportCameras -v false")
    mel.eval("FBXExportLights -v false")
    mel.eval("FBXExportCacheFile -v false")
    mel.eval("FBXExportBakeComplexAnimation -v " + animation)
    mel.eval("FBXExportConstraints -v false")
    mel.eval("FBXExportSkins -v true")
    mel.eval("FBXExportSmoothMesh -v false")
    mel.eval("FBXExportSmoothingGroups -v false")
    mel.eval("FBXExportUpAxis y")

"""
    Name        GetFilepath
    Desc        prompts user for filepath
    return      string that contains the full filepath includes name of file to save.
"""
def GetFilepath() -> str:
    #Assume file and name
    fileName = cmds.file(q=True, sn=True).replace(".*", "")
    lastDirectoryUsed = 'C:/Users/west/Downloads/' + fileName #Specific to This Function

    #aensure its correct
    singleFilter = "*.fbx"
    savePath = cmds.fileDialog2(fileFilter=singleFilter, dialogStyle=2, startingDirectory=lastDirectoryUsed)

    #check for cancel
    if not savePath:
        return None 

    savePath = savePath[0].replace('*', 'fbx')
    return savePath


