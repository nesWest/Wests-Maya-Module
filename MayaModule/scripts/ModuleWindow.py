'''
	file        pyqt_tests.py

	date        08/06/2024

	authors     West Foulks (WestFoulks@gmail.com)

	brief       Window to show information regarding this module allow reinstallation upon updates
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

class ModuleWindow(MayaQWidgetDockableMixin, QtWidgets.QDialog):
    
    win_instance = None

    def __init__(self, parent=maya_main_window()) -> None:
        super().__init__(parent)
        self.setWindowTitle("West's Maya Tools")
        self.setMinimumSize(200,300)

        #Possible Intall Locations
        self.location_dropdown = QtWidgets.QComboBox()
        self.location_dropdown.addItems(self._getEnvPaths())
        self.location_dropdown.setContentsMargins(0,0,0,0)
    
        #Possible Shelves to Install
        self.shelfChecks = []
        for shelf in JsonReader.GetShelves().keys():
            self.shelfChecks.append(QtWidgets.QCheckBox(shelf))
            

        #reinstall uninstall Buttons
        self.install_button = QtWidgets.QPushButton('(Re)Install')
        self.uninstall_button = QtWidgets.QPushButton('Uninstall')
        
        #Sub layout Shelves
        layout_form = QtWidgets.QFormLayout()
        layout_form.addRow('Install Locations (of .mod)', self.location_dropdown)
        layout_form.setContentsMargins(0,0,0,0)
        for shelf in self.shelfChecks:
            layout_form.addRow('', shelf) 

        
        #Subl Layout (re)Install uninstall
        layout_installUninstall = QtWidgets.QHBoxLayout()
        layout_installUninstall.setContentsMargins(0,0,0,0)
        layout_installUninstall.addWidget(self.install_button)
        layout_installUninstall.addWidget(self.uninstall_button)
        
        #Main Layout
        layout_main = QtWidgets.QVBoxLayout()
        layout_main.addLayout(layout_form)
        layout_main.addLayout(layout_installUninstall)
        
        self.setLayout(layout_main)

        #Connect Buttons
        self.install_button.clicked.connect(self._reInstall)
        self.uninstall_button.clicked.connect(self._unInstall)

    def _getEnvPaths(self) -> list:
        paths = os.environ['MAYA_MODULE_PATH'].split(';')
        paths.pop()
        return paths
    
    def _reInstall(self) -> None:
        #Create .Mod File
        selectedPath = self.location_dropdown.currentText()
        moduleName = JsonReader.GetModuleName()
        versionNumber = str(JsonReader.GetVersionNumber())

        filename = selectedPath + '/WestsModules.mod'
        print(filename)
        if os.path.exists(filename):
            os.remove(filename)

        modFile = open(filename, 'x')
        line = '+ ' + moduleName + ' ' + versionNumber + ' ' + JsonReader.UserData_GetModulePath()
        modFile.write(line)
        modFile.close()

        #create Shelves
        for shelf in self.shelfChecks:
            if shelf.checkState():
                ShelfTools.AddShelf(shelf.text()) #also updates shelf
            else:
                ShelfTools.RemoveShelf(shelf) #remove shelf if it exists

        #Restart Maya
        Utilities.RestartMaya()
    
    def _unInstall(self) -> None:
        #Remove .Mod Files
        paths = self._getEnvPaths()

        for path in paths:
            filename = path + '/WestsModules.mod'
            if os.path.exists(filename):
                os.remove(filename)

        #Remove Shelves
        ShelfTools.RemoveAllShelves()

        Utilities.RestartMaya()

    @classmethod    
    def showWindow(cls) -> None:
        if cls.win_instance == None:
            cls.win_instance = ModuleWindow()
        
        if cls.win_instance.isHidden():
            cls.win_instance.show(dockable=True)
        else:
            cls.win_instance.raise_()

        


