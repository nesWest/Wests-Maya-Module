import maya.cmds as cmds
import os  

class InstallWindow:       
    def __init__(self, modulePath):
        self.modulePath = modulePath
        self.VersionNumber = "0.1"
        self.paths = os.environ['MAYA_MODULE_PATH'].split(";")
        
        #Gets Paths
        print("-------Found Paths------------------------------")
        for path in self.paths:
            print(path)
        print("------------------------------------------------")
        print("\n")

        #options Menu
        cmds.window("ModuleInstallPath")
        cmds.showWindow("ModuleInstallPath")
        cmds.columnLayout()

        self.options = cmds.optionMenu(label="Possible Paths")
        cmds.optionMenu(self.options, edit=1)

        for path in self.paths:
            cmds.menuItem( label=path )

        def buttonCallback(arg):
            SelectedPath = cmds.optionMenu(self.options, query=True, value=True)
            FinishInstall(SelectedPath,"WestsMayaModule", self.modulePath, self.VersionNumber)

        cmds.text("Finishing the process will restart Maya")    
        cmds.button(label="Finish", command = buttonCallback)


def FinishInstall(selectedPath, moduleName, modulePath, versionNumber):
    print("-----------------Making .Mod---------------------")
    print("Final Selected Path " + selectedPath)
    modFile = open(selectedPath + "/WestsModules.mod", "x")
    line = "+ " + moduleName + " " + versionNumber + " " + modulePath
    modFile.write(line)
    modFile.close()

    print("Making Shelf Tools")

    print("Restarting Maya")
    maya_executable = os.environ['MAYA_LOCATION'] + "/bin/maya.exe" #EXE location
    filename = cmds.file(q=True, sn=True) #current file name to try and relaunch
    cmds.savePrefs() #save user prefs
    os.spawnl(os.P_NOWAIT, maya_executable, '-file', filename) #Launches Maya
    cmds.quit()      #prompt user to save the maya file


