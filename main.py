# Import Modules
import os
import socket
from requests import get

# Create another script for windows

# Test if the installation has been made before and redirect...
try:
    f = open('start.py')
    f.close()
    os.system("sudo python3.7 start.py") # Redirection
    os.system("sudo rm main.py")
    exit()
except FileNotFoundError:
    try:
        f = open('bukstart.py')
        f.close()
        os.system("sudo python3.7 bukstart.py")
        os.system("sudo rm main.py")
        exit()
    except FileNotFoundError:
        print("Starting script...")
        os.system("clear")

# Ask for bukkit
os.system("clear")
print("[AVAIABLE MODES]")
print("1: Vanilla")
print("2: Bukkit")
print("3: Forge Server")
mode = input("What mode do you want? ")
if mode == "1":
    os.system("cp /opt/MCSS/vanilla.py .")
    os.system("sudo python3.7 vanilla.py")
elif mode == "2":
    os.system("cp /opt/MCSS/bukkit.py .")
    os.system("sudo python3.7 bukkit.py")
elif mode == "3":
    os.system("clear")
    print("Not supported yet...")
else:
    print("Default: Vanilla")
    os.system("cp /opt/MCSS/vanilla.py .")
    os.system("sudo python3.7 vanilla.py")

# Self destruction of the file
os.system("sudo rm main.py")
