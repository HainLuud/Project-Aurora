import os, sys
import subprocess

requrements = open("requirements.txt", "r", encoding="utf-8").read().split("\n")

for requrement in requrements:
    subprocess.check_call([sys.executable, "-m", "pip", "install", requrement])

os.startfile("src\\main.pyw")