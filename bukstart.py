import os
import socket
from requests import get

# Get status
os.system("clear")
file = open("status.txt", "r")
status = file.read()
file.close()

print("[SERVER IS RUNNING]")
print("List of IP addresses:")
print("For you: localhost")
private = socket.getfqdn()
print("For your local network: ", private)

if status == '1':
    public = get('https://api.ipify.org').text
    print("World-wide: ", public)

# Start server
os.system("sudo sh craftbukkit.sh >/dev/null")
