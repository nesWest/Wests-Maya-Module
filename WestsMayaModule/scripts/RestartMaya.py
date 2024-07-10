import maya.cmds as cmds
import os

print("Restarting Maya")
maya_executable = os.environ['MAYA_LOCATION'] + "/bin/maya.exe" #EXE location
filename = cmds.file(q=True, sn=True) #current file name to try and relaunch
cmds.savePrefs() #save user prefs
os.spawnl(os.P_NOWAIT, maya_executable, '-file', filename) #Launches Maya
cmds.quit()      #prompt user to save the maya file