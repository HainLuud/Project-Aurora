import os, sys
import subprocess
import pathlib

scriptPath = pathlib.Path(__file__).parent.absolute()

# Install all requirements
requrements = open("requirements.txt", "r", encoding="utf-8").read().split("\n")

for requrement in requrements:
    subprocess.check_call([sys.executable, "-m", "pip", "install", requrement])

# Start the program
os.startfile(os.path.join(scriptPath, "main.pyw"))

# Extract path of python.exe
pythonPath = sys.path[1].split("\\")
user = pythonPath[2]
pythonExe = os.path.join(os.sep.join(pythonPath[:len(pythonPath) - 1]), "python.exe")

scriptPath = pathlib.Path(__file__).parent.absolute()

# Make autorun batch file
autorunFile = open("autorun.bat", "w", encoding="utf-8")
autorunFile.write('"' + pythonExe + '" "' + os.path.join(scriptPath, 'src', 'main.pyw"'))
autorunFile.close()

# Make batch file that will be moved to startup folder, to have the script started at startup
auroraStartupFile = open("auroraStartup.bat", "w", encoding="utf-8")
auroraStartupFile.write('wscript.exe "' + os.path.join(scriptPath, 'invisible.vbs') + '" "' + os.path.join(scriptPath, 'autorun.bat"'))
auroraStartupFile.close()

# Move batch file to startup folder
startupfolderPath = os.path.join("C:" + os.sep, "Users", user, "Appdata", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
os.rename(os.path.join(scriptPath, "auroraStartup.bat"), os.path.join(startupfolderPath, "auroraStartup.bat"))