# This is a file to store all the global variables needed
# It's initiated only once when the mainwindow is created
# Please don't tammper with it

import os
import sys
import platform
import ctypes.wintypes
from datetime import datetime
import Scripts.Configs as cfg
from Scripts.BasicLogger import Log

#//////////////////////////////////////////#
#//#    Global Variables Declarations   #//#
#//////////////////////////////////////////#

appStartDate: str # appStartDate is the dateTime when the launcher was started, this is used to name the logs
configData: dict[str, dict[str, str]]
modPath: str # \p2mm
modFilesPath: str # \p2mm\Modfiles
configPath: str
masterDataFilePath: str # Path defined for the masterData.cfg file
dataSystemPath: str # Path defined for the data system nuts directory
# dataSystemSSFilesPath: str # Path defined for the screenshots folder for Portal 2, this is for the data system
iow: bool = False # Windows system
iol: bool = False # Linux system
iosd: bool = False # Steam Deck/Steam OS 3.0 system
nf: str = os.sep # This way the logging won't break if someone runs the app on Mac
hadtoresetconfig: bool = False
executable: str = os.path.abspath(sys.executable)
translations: dict[str, str]
AfterFunction: None

def init() -> None:
    global appStartDate, modPath, modFilesPath, configPath, masterDataFilePath, dataSystemPath, iow, iol, iosd, nf, translations

    appStartDate = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

    if (sys.platform == "win32"):
        iow = True

        # Again thanks stackOverflow for this
        # This code allows us to get the document's folder on any windows pc with any language
        CSIDL_PERSONAL = 5       # My Documents
        SHGFP_TYPE_CURRENT = 0   # Get current, not default value

        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)

        # Set the modpath to the users documents folder
        modPath = buf.value + nf + "p2mm"
        modFilesPath = buf.value + nf + "p2mm\ModFiles"
        configPath = buf.value + nf + "p2mm"
        masterDataFilePath = buf.value + nf + "p2mm"
        dataSystemPath = buf.value + nf + "p2mm\ModFiles\Portal 2\install_dlc\scripts\\vscripts\multiplayermod\datasystem"
    elif (sys.platform.startswith("linux")):
        # Both Linux and SteamOS 3.0 system platform names return as "linux"
        # We need to use the platform release name to differentiate a normal Linux distribution from SteamOS 3.0, SteamOS 3.0 includes "valve" in the release
        if ("valve" in platform.release()):
            iosd = True
            # Steam OS 3.0 has some directories set to read-only
            # We are going to install p2mm to the home\Documents directory instead of .cache and .config because of this
            # We are also gonna keep stuff together like with the Windows paths, configs will be placed into the same directory as the ModFiles
            modPath = os.path.expanduser("~") + nf + "Documents\p2mm"
            modFilesPath = os.path.expanduser("~") + nf + "Documents\p2mm\Modfiles"
            configPath = os.path.expanduser("~") + nf + "Documents\p2mm"
            masterDataFilePath = os.path.expanduser("~") + nf + "Documents\p2mm"
            dataSystemPath = os.path.expanduser("~") + nf + "Documents\p2mm\ModFiles\Portal 2\install_dlc\scripts\\vscript\multiplayermod\datasystem"
        else:
            iol = True
            # Set the modpath the to the users .cache and .config directories in the home directory
            modPath = os.path.expanduser("~") + nf + ".cache\p2mm"
            modFilesPath = os.path.expanduser("~") + nf + ".cache\p2mm\Modfiles"
            configPath = os.path.expanduser("~") + nf + ".config\p2mm"
            masterDataFilePath = os.path.expanduser("~") + nf + ".config\p2mm"
            dataSystemPath = os.path.expanduser("~") + nf + ".cache\p2mm\ModFiles\Portal 2\install_dlc\scripts\\vscript\multiplayermod\datasystem"

    else:
        # Feel sad for the poor people who are running templeOS :(
        Log("This operating system is not supported!")
        Log("We only support Windows, Linux, and SteamOS 3.0 (Steam Deck) as of current.")
        quit()

    # Check if the modpath exists, if not create it
    if not os.path.exists(modPath):
        os.makedirs(modPath)
    if not os.path.exists(configPath):
        os.makedirs(configPath)

def LoadConfig() -> None:
    global configData
    configData = cfg.ImportConfig()
    Log("Config data loaded.")
