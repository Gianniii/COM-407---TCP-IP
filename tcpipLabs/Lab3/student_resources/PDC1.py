 
#!/usr/bin/python
 
import sys
import socket
 
 
 
HOST = sys.argv[1]
PORT = int(sys.argv[2])
COMMAND = sys.argv[3]
 
 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST,PORT))
 
 
#print("sending:", COMMAND)
sock.sendall(COMMAND.encode())
 
#todo tread the 2 diff commands differenty....
#prob just the way your print the buffer....
received = 0
receiving = True
buffer = ""
while True:
   data = sock.recv(10000)
   
   if(data):
       data = data.decode()
       buffer += data
   else:
       break
 
if(COMMAND == "CMD_short:0" or COMMAND == "CMD_short:1" ):
    newbuffer = buffer.split("This")
    if(len(newbuffer)> 2):
        print("This" + newbuffer[1])
    
    if(len(newbuffer) > 3):
        for str in newbuffer[2:]:
            print("This" + str)
else:
    print(buffer, flush=True)
 
sock.close()
