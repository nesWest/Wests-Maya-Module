This repo is a collection of python scripts and plugins created for Autodesk maya
I will try and outline any complex processes in this read me through documentation.

Installation
1. Drag and Drop DRAG_INTO_MAYA.py into a Running Maya Window
2. Choose Shelf Tools to install

TODO:
make config file
add version number to config
add PathToModule to config
add shelf configuration to config
add preferred export locations to config

add prompts on install for which shelves to add

References:


library info for later:
https://help.autodesk.com/view/MAYAUL/2022/ENU/?guid=GUID-C24973A1-F6BF-4614-BC3A-9F1A51D78F4C

Path Variables 
https://help.autodesk.com/view/MAYAUL/2022/ENU/?guid=GUID-228CCA33-4AFE-4380-8C3D-18D23F7EAC72

Module Use Case Explanations 
https://learncreategame.com/techart/maya-environment-setup/#:~:text=mod%20file%20in%20a%20modules,the%20Maya%20environment%20during%20startup.
https://help.autodesk.com/view/MAYAUL/2022/ENU/?guid=Maya_SDK_Distributing_Maya_Plug_ins_DistributingUsingModules_CreatingAModulePackage_html
https://benmorgananimation.wordpress.com/2018/04/20/script-distribution-using-maya-modules/
https://techartsurvival.blogspot.com/2014/01/mayas-mildy-magical-modules.html

EXAMPLE .Mods
+ MAYAVERSION:2020 PLATFORM:win64 <ModuleName> <ModuleVersion> <ModulePath> 
MY_PLUGIN_LOCATION:= myPlugin
PATH+:=bin
MAYA_SCRIPT_PATH+:=scripts

+ MAYAVERSION:2020 PLATFORM:linux <ModuleName> <ModuleVersion> <ModulePath> 
MY_PLUGIN_LOCATION:= myPlugin
PATH+:=bin
MAYA_SCRIPT_PATH+:=scripts

+ MAYAVERSION:2020 PLATFORM:mac <ModuleName> <ModuleVersion> <ModulePath> 
MY_PLUGIN_LOCATION:= myPlugin
PATH+:=bin
MAYA_SCRIPT_PATH+:=scripts
