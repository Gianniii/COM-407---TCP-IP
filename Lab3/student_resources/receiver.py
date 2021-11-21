 
#!/usr/bin/python
 
import sys
import socket
import struct
 
 
GROUP = sys.argv[1]
PORT = int(sys.argv[2])
 
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
req = struct.pack("=4sl", socket.inet_aton(GROUP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, req)
sock.bind((GROUP,PORT))
 

received = 0
receiving = True
buffer = ""
newbuffer = ""
while True:
    data = sock.recv(1000)
    #print("something", flush=True)
    #print(data), flush=True)
    if(data):
        data = data.decode()
        buffer += data
        newbuffer = buffer.split("swcmTV")
        if(newbuffer):
            print(newbuffer[1], flush=True)
            newbuffer = ""
            buffer = ""
    else:
       break
 


 
sock.close()