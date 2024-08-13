'''
	file        pyqt_tests.py

	date        08/06/2024

	authors     West Foulks (WestFoulks@gmail.com)

	brief       Script file for testing pyqt as a I learn.
'''
try:
    from PySide2 import QtCore, QtWidgets #in 2024 QT5
    from shiboken2 import wrapInstance
except:
    from PySide6 import QTCore, QtWidgets #in 2025 QT6
    from shiboken6 import wrapInstance

try: #To use DRAG_INTO_MAYA is there a better way?
    import JsonReader
    import ShelfTools 
    import Utilities
except:
    import MayaModule.scripts.JsonReader as JsonReader
    import MayaModule.scripts.ShelfTools as ShelfTools
    import MayaModule.scripts.Utilities as Utilities

import os   
import maya.cmds as cmds
import maya.OpenMayaUI as omui
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin


#gets maya window
def maya_main_window():
    maya_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(maya_window_ptr),QtWidgets.QWidget)

class HelloQTWindow(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super().__init__(parent)
        self.setWindowTitle("West's Maya Tools")
        self.setMinimumSize(200,300)
        self.setModulePath("")

        #Possible Intall Locations
        self.location_dropdown = QtWidgets.QComboBox()
        self.location_dropdown.addItems(self.getEnvPaths())
        self.location_dropdown.setContentsMargins(0,0,0,0)
    
        #Possible Shelves to Install
        self.Shelf_titles = []
        self.shelf_Check = []

        for i in range(0,4):
            self.Shelf_titles.append("test" + str(i))
            self.shelf_Check.append(QtWidgets.QCheckBox(""))

        #Confirm Cancel Buttons
        self.install_button = QtWidgets.QPushButton("(Re)Install")
        self.cancel_button = QtWidgets.QPushButton("Uninstall")
        
        #Sub layout Shelves
        layout_form = QtWidgets.QFormLayout()
        layout_form.addRow("Install Locations (of .mod)", self.location_dropdown)

        for i in range(0,4):
            layout_form.addRow(self.Shelf_titles[i],self.shelf_Check[i])

        layout_form.setContentsMargins(0,0,0,0)

        #Subl Layout Confirm Cancel
        layout_ConfirmCancel = QtWidgets.QHBoxLayout()
        layout_ConfirmCancel.setContentsMargins(0,0,0,0)
        layout_ConfirmCancel.addWidget(self.install_button)
        layout_ConfirmCancel.addWidget(self.cancel_button)
        
        #Main Layout
        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addLayout(layout_form)
        layout_main.addLayout(layout_ConfirmCancel)
        
        self.setLayout(layout_main)

        #Connect Buttons
        self.install_button.clicked.connect(self.reInstall)
        self.cancel_button.clicked.connect(self.unInstall)

    def getName(self) -> str:
        return self.name_line_edit.text()
    
    def createCube(self):
        cube = cmds.polyCube(name=self.getName())
    
    def createSphere(self):
        cmds.polySphere(name=self.getName())

    def getEnvPaths(self) -> list:
        paths = os.environ['MAYA_MODULE_PATH'].split(';')
        paths.pop()
        return paths
    
    def setModulePath(self, path):
        self.modulePath = path + "/MayaModule/"

    def reInstall(self):
        #Create .Mod File
        selectedPath = self.location_dropdown.currentText()
        moduleName = JsonReader.GetModuleName()
        versionNumber = str(JsonReader.GetVersionNumber())

        filename = selectedPath + '/WestsModules.mod'
        print(filename)
        if os.path.exists(filename):
            os.remove(filename)

        modFile = open(filename, 'x')
        line = '+ ' + moduleName + ' ' + versionNumber + ' ' + self.modulePath
        modFile.write(line)
        modFile.close()

        #create Shelves
        ShelfTools.RefreshShelves()

        #Restart Maya
        Utilities.RestartMaya()
    
    def unInstall(self):
        #Remove .Mod Files
        paths = self.getEnvPaths()

        for path in paths:
            filename = path + '/WestsModules.mod'
            if os.path.exists(filename):
                os.remove(filename)

        #Remove Shelves
        ShelfTools.RemoveAllShelves()

        Utilities.RestartMaya()

win = HelloQTWindow()
def ShowWindow():
    if win:
        win.show(dockable=True)
    


