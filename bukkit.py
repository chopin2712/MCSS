import os
import socket
from requests import get

# Get the version
os.system("clear")
os.system("sudo cp -r /opt/MCSS/bukkit/* .")

print("Starting the compiler of Spigot")
version = input("What version do you want to get? (If you already have one press ENTER) >")
if version == '':
    print("Get your craftbukkit / spigot file.jar")
    print("Then put it into the folder")
    input("When you finished press ENTER...")
    os.system("mv *.jar craftbukkit.jar")
else:
    compile = "java -jar BuildTools.jar --rev " + version
    os.system(compile)
    os.system("clear")
    name = "spigot-" + version + ".jar"
    command = "mv " + name + " craftbukkit.jar"
    os.system(command)

# 2
os.system("clear")
next = input("Do you want to modify properties [Y, n] ")
if next == 'Y' or next == 'y':
    os.system("vim server.properties")
    status = input("When you finished press enter... ")

private = socket.getfqdn()

# Public
os.system("clear")
public = input("Do you want to be avaiable world wide? [Y, n] ")
if public == 'Y' or public == 'y':
    print("Open http://192.168.1.1")
    print("Create a new portmap with 25565 as port and ", private, "as IP address")
    input("Press enter when you finished: ")
    public = get('https://api.ipify.org').text
    status = 1
    file = open("status.txt", "w")
    file.write('1')
    file.close()
else:
    file = open("status.txt", "w")
    file.write('0')
    file.close()
    status = 0

# Informations
os.system("clear")
print("[SERVER IS READY]")
print("This is your IP address")
print("For you : localhost")
print("For your local network: ", private)
if status == 1:
    print("WORLD WIDE: ", public)

os.system("chmod +x craftbukkit.sh")
# os.system("sudo sh craftbukkit.sh >/dev/null")
os.system("sudo sh craftbukkit.sh")

os.system("sudo cp /opt/MCSS/bukstart.py .")
os.system("sudo chmod 777 -R *")
os.system("sudo rm bukkit.py")

# Needs to add start script as name bukstart.py
