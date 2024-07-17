import os
import maya.cmds as cmds
import maya.mel as mel

#notes:
    #file -force -options "v=0;" -typ "FBX export" -pr -es "C:/Users/west/Downloads/SK_Shockwave.fbx";
    #Consider moving options to .mel file
    #mel.eval('"source ExportOptions.mel;"') # source of the file
    #mel.eval("Animation;") #name of the function 
    #may move export def to funct in mel

def CharacterExporter():

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

def AnimationExporter():
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

def BatchExporter():
    #By file set, not folder.
    print("Batch Exporter (Incomplete)")

def RemoveNamespace():
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

def ReAddNamespace():
    #Put namespace back
    cmds.namespace( set=':')
    cmds.namespace( rel=False )

def FBXOption(animation = "false"):
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

def GetFilepath():
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


