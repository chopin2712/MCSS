import os
import socket
from requests import get

# Test if the installation has been made before and redirect...
try:
    f = open('start.py')
    f.close()
    os.system("sudo python3.7 start.py") # Redirection
    os.system("sudo rm main.py")
    exit()
except FileNotFoundError:
    print("Starting script...")
    os.system("clear")

# 1: Get minecraft version
version = input("What Minecraft version do you want? ")

# Supported versions
if version == '':
    print("Getting latest version...")
    os.system("wget https://launcher.mojang.com/v1/objects/d0d0fe2b1dc6ab4c65554cb734270872b72dadd6/server.jar")
elif version == "1.14.3":
    os.system("wget https://launcher.mojang.com/v1/objects/d0d0fe2b1dc6ab4c65554cb734270872b72dadd6/server.jar")

# 
else:
    print("Oops your version seems to not be detected")
    URL = input("Can you give us the download URL? ")
    URL = "wget " + URL
    os.system(URL)
    next = "0"
    while next == "0":
        try:
            f = open('server.jar')
            f.close()
            print("FILE FOUND!")
            next = "1"
        except FileNotFoundError:
            os.system("clear")
            input("Please put the server.jar file into this directory then press enter... ")

# Run the file and get eula
os.system("chmod +x server.jar")
os.system("java -jar server.jar >/dev/null")
os.system("cp /opt/MCSS/server/* .")

# 2: Modify Server.properties
os.system("clear")
next = input("Do you want to modify properties [Y, n] ")
if next == 'Y' or next == 'y':
    os.system("atom server.properties")
    status = input("When you finished press enter... ")

# 3: Ip addresses informations
os.system("clear")
print("[SERVER IS ALMOST READY]")
print("This is your IP address")
print("For you : localhost")
private = socket.getfqdn()
print("For your local network: ", private)


# Public
public = input("Do you want to be avaiable world wide? [Y, n] ")
if public == 'Y' or public == 'y':
    print("Open http://192.168.1.1")
    print("Create a new portmap with 25565 as port and ", private, "as IP address")
    input("Press enter when you finished: ")
    public = get('https://api.ipify.org').text
    print(public)
    status = 1
    file = open("status.txt", "w")
    file.write('1')
    file.close()
else:
    os.system("clear")
    print("[SERVER IS READY]")
    print("This is your IP address")
    print("For you : localhost")
    print("For your local network: ", private)
    file = open("status.txt", "w")
    file.write('0')
    file.close()

# 4: Play!
os.system("clear")
print("[SERVER IS READY]")
print("This is your IP address")
print("For you : localhost")
print("For your local network: ", private)
if status == 1:
    print("WORLD WIDE: ", public)
os.system("java -jar server.jar >/dev/null")

# Copy the start script
os.system("sudo cp /opt/MCSS/start.py .")
# Ask
os.system("sudo rm main.py")
