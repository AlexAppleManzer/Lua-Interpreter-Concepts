# C:\Program Files\Java\jdk-11.0.2\bin
import sys
import socket
import subprocess
import os

HOST = ""
PORT = 8888

os.system('compilejava.bat')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

p = subprocess.Popen(["java", "TestSocket"])

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print("Bind failed.")
    print("Error code: "+str(msg[0]))
    print("Message: "+str(msg[1]))
    sys.exit()
print("Socket bind complete")

s.listen(10)
print("Socket now listening")

while 1:
    conn, addr = s.accept()
    print("Connected with: "+addr[0])
    print(str(addr[1]))
    data = conn.recv(1024)
    if not data:
        break
    print('Received', repr(data))

    conn.sendall(data)

s.close()