# C:\Program Files\Java\jdk-11.0.2\bin
# TLDR: 3 commands for this simple socket client Driver thing
# 1: g lineNo   this returns a long string of all of the tokens in the array separated out
# 2: c fileName this changes the file that the Lexical Server is reading
# 3: Quit       closes the server :)

import socket
import subprocess
import time

# sets up server to communicate between JVM and python code
SERVER = "localhost"
PORT = 8888

# compiles all the java code
# make sure you're setting up your enviromental variables up so javac is reconized in your path
subprocess.check_call(['javac', '*.java'])
subprocess.check_call(['javac', './lex/*.java'])
# opens up LexServer class that interpreter will be reading from
p = subprocess.Popen(["java", "lex/LexServer"])
# waits a bit to let things process
time.sleep(1)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("client: Socket created")


s.connect((SERVER, PORT))
print("client: connection complete")

s.send("hello\n".encode())
result = s.recv(1024)
print("\nclient: " + result.decode())

s.send("g 2\n".encode())
result = s.recv(1024)
print("\nclient: " + result.decode())

s.send("c test2.lua\n".encode())
result = s.recv(1024)
print("\nclient: " + result.decode())

s.send("g 2\n".encode())
result = s.recv(1024)
print("\nclient: " + result.decode())

s.send("Quit\n".encode())
result = s.recv(1024)
print("\nclient: " + result.decode())

s.close()