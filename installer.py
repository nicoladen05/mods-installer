import requests
import subprocess
import os
import urllib.request
import ctypes

def is_git_installed():
    try:
        subprocess.run(["git", "--version"], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except subprocess.CalledProcessError:
        return False

def install_git():
    if not is_git_installed():
        # Download Git for Windows
        os.system("curl -O https://github.com/git-for-windows/git/releases/download/v2.30.2.windows.1/Git-2.30.2-64-bit.exe")

        # Run the installer
        subprocess.run(["Git-2.30.2-64-bit.exe", "/S"])


# URL der .exe-Datei
url = "https://maven.fabricmc.net/net/fabricmc/fabric-installer/0.11.1/fabric-installer-0.11.1.exe"

# Herunterladen der Datei
response = requests.get(url)
open("fabric-installer.exe", "wb").write(response.content)

# Benutzer auffordern, im sich öffnenden Fenster auf "Installieren" zu klicken
print("\033[1;31;40m Bitte im sich öffnenden Fenster auf 'Installieren' klicken und dieses nach der Installation schließen! \033[0m")

# Ausführen der heruntergeladenen .exe-Datei
subprocess.run(["fabric-installer.exe"])

install_git()

# Navigate to the .minecraft folder
os.chdir(os.environ["APPDATA"] + "/.minecraft")

# Delete the mods folder
# Set the path to the mods folder
mods_path = os.environ["APPDATA"] + "\.minecraft\mods"

# Check if the mods folder exists
if os.path.exists(mods_path):
    # Print a warning message
    print("Achtung: Du hast berreits einen mods order in %appdata%/minecraft. Dieses Script löscht diesen bei der Installation.")
    print("Soll das Programm fortfahren? Schreibe j oder n und drücke auf enter.")

    # Get the user's input
    confirm = input()

    # If the user confirms, delete the mods folder
    if confirm.lower() == "j":
        # Construct the full path to cmd.exe
        cmd_path = os.path.join(os.environ["WINDIR"], "system32", "cmd.exe")

        # Run cmd.exe with the /c option and the rd command with the /S and /Q options
        # as a single string, using the shell argument
        
        subprocess.run([cmd_path, "/c", f"rd /S /Q {mods_path}"], shell=True) 
        print("Der Ordner wurde gelöscht.")
    else:
        print("Das Programm wird sich nun schließen.")
        exit()

# Klonen des Git-Repositories in den Ordner "mods"
minecraft_folder = os.path.join(os.environ["appdata"], ".minecraft")
mods_folder = os.path.join(minecraft_folder, "mods")
if not os.path.exists(mods_folder):
    os.makedirs(mods_folder)

repo_url = "https://github.com/nicoladen05/minecraft-mods"
subprocess.run(["git", "clone", repo_url, mods_folder])