import os
import subprocess

os.chdir(os.environ["APPDATA"] + "\.minecraft\mods")
os.system("git pull")