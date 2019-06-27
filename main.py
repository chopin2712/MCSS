import os

# Get backup of precedent installation

# Get the right MC version
version = input("What Minecraft version do you want? ")
# Get MC version

# Run the file and get eula
os.system("chmod +x server.jar")
os.system("java -jar server.jar")
os.system("cp /opt/MCSS/eula.txt .")
os.system("java -jar server.jar")
# Write stop to server.jar

# Minecraft.properties
continue = input("Do you want to modify properties [Y, n] ")
if continue == Y or continue == y:
    os.system("atom minecraft.properties")

# Update
os.system("java -jar server.jar")

os.system("clear")

# Ip addresses informations

print("[SERVER IS READY]")
print("This is your IP address")
print("For you : localhost")
# Get private
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
