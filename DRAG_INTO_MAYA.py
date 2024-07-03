import maya.cmds as cmds
import os

#should be shoved in config file
#can have shelves that can be added save in as well
#and like prefered save export locaitons for different shelf things
VersionNumber = "0.1"
PathToModule = "C:\\Users\\west\\OneDrive\\Desktop\\Maya-Module\\WestsMayaModule"

#TODO add prompts for shelves to add


#Button Callback that takes string and installs .mod file
def FinishInstall(menuCalling):
    print("-----------------Making .Mod---------------------")
    
    SelectedPath = cmds.optionMenu(menuCalling, query=True, value=True)
    print("Final Selected Path " + SelectedPath)
    modFile = open(SelectedPath + "/WestsModules.mod", "x")#should be changed to .mod

    line = "+ WestsMayaModule " + VersionNumber + " " + PathToModule
    modFile.write(line)

    modFile.close()

    print("Making Shelf Tools")

    print("Restarting Maya")
    RestartMaya()

def RestartMaya():
    maya_executable = os.environ['MAYA_LOCATION'] + "/bin/maya.exe" #EXE location
    filename = cmds.file(q=True, sn=True) #current file name to try and relaunch
    cmds.savePrefs() #save user prefs
    os.spawnl(os.P_NOWAIT, maya_executable, '-file', filename) #Launches Maya
    cmds.quit()      #prompt user to save the maya file
        

#Gets Paths
print("-------Found Paths------------------------------")
paths = os.environ['MAYA_MODULE_PATH'].split(";")
for path in paths:
    print(path)
print("------------------------------------------------")
print("\n")

#options Menu
cmds.window("ModuleInstallPath")
cmds.showWindow("ModuleInstallPath")
cmds.columnLayout()

options = cmds.optionMenu(label="Possible Paths")
cmds.optionMenu( options, edit=1)

for path in paths:
    cmds.menuItem( label=path )

cmds.text("Finishing the process will restart Maya")    
cmds.button(label="Finish", c = "FinishInstall(options)")





