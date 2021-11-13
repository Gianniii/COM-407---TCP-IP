 
#!/usr/bin/python
 
import sys
import socket
 
 
 
GROUP = sys.argv[1]
PORT = int(sys.argv[2])
SCIPER = sys.argv[3] 
 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 32)

txt = input("enter message: ")
print(txt)

byte_sciper = bytes(SCIPER, 'utf-8')
first6 = byte_sciper[0:6]
strFirst6 = first6.decode('utf-8')
data = strFirst6 + txt

sock.sendto(data.encode(),(GROUP, PORT))
 



 
sock.close()