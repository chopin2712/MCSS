# Ouvrir server.jar sans output
# Clear
# Ecrire:

import os
import socket
from requests import get

# Get status
file = open("status.txt", "r")
status = file.read()
file.close()
print(status)

print("[SERVER IS RUNNING]")
print("List of IP addresses:")
print("For you: localhost")
private = socket.getfqdn()
print("For your local network: ", private)

if status == '1':
    public = get('https://api.ipify.org').text
    print("World-wide: ", public)

# Start server
os.system("java -jar server.jar >/dev/null")
