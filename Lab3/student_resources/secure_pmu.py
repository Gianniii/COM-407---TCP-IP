 
#!/usr/bin/python
 
import sys
import socket
import ssl
 
 
CERTIFICATE = sys.argv[1]
KEY = sys.argv[2]
HOST = "localhost"
PORT = 5003
 



 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen()

newSocket, addr = sock.accept()

newSocket = ssl.wrap_socket(newSocket, certfile = CERTIFICATE, keyfile=KEY)
newSocket.bind((HOST, PORT))

COMMAND = newSocket.listen()
 
while True: 
    data = newSocket.recv(1024)
    if not data: 
        break
    if(data.decode() == "CMD_SHORT:0"):
        newSocket.send("This is PMU data 0")

newSocket.close()