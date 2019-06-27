import os
import socket

# Get backup of precedent installation

# Get the right MC version
version = input("What Minecraft version do you want? ")
# Get MC version
os.system("wget https://launcher.mojang.com/v1/objects/d0d0fe2b1dc6ab4c65554cb734270872b72dadd6/server.jar")

# Run the file and get eula
os.system("chmod +x server.jar")
os.system("java -jar server.jar")
os.system("cp /opt/MCSS/server/* .")
os.system("java -jar server.jar")
# Write stop to server.jar

# server.properties
next = input("Do you want to modify properties [Y, n] ")
if next == 'Y' or next == 'y':
    os.system("atom server.properties")
    status = input("When you finished press enter... ")

# Update
os.system("java -jar server.jar")

os.system("clear")

# Ip addresses informations
print("[SERVER IS READY]")
print("This is your IP address")
print("For you : localhost")
private = socket.getfqdn()
print("For your local network: ", private)


# Public
public = input("Do you want to be avaiable world wide? [Y, n] ")
if public == Y or public == y:
    # get public IP
    print(public)
else:
    os.system("clear")
    print("[SERVER IS READY]")
    print("This is your IP address")
    print("For you : localhost")
    print("For your local network: ", private)

# Ask
os.system("sudo rm main.py")
