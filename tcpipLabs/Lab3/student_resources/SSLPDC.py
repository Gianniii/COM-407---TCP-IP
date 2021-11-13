#!/usr/bin/python
 
import sys
import socket
 
 
 
HOST = sys.argv[1]
PORT = int(sys.argv[2])
COMMAND = "RESET:20"
 
socket.setdefaulttimeout(0.5)
sock1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

 
sock2 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)



#MUST BE ABLE TO USE BOTH IPV4 AND IPV6 DEPENDING ON WHAT THE SERVER IS USING!
#print("sending:", COMMAND)
def send4():
    #print("sending ipv4")
    sock1.sendto(COMMAND.encode(), (HOST,PORT))

def send6():
    #print("sending ipv6")
    sock2.sendto(COMMAND.encode(), (HOST,PORT))
 
#todo tread the 2 diff commands differenty....
#prob just the way your print the buffer....
received = 0
receiving = True

data2 = False
data1 = False
total_attempts = 1
for i in range(60):
    buffer = ""
    attempt = 1
    data2 = False
    data1 = False
    while True:
        send4()
        try:
            data1 = sock1.recv(10)
        except:
            donothing = 0
            #print("")

        send6()
        try:
            data2 = sock2.recv(10)
        except:
            hi = 0
            #print("")

        if(data1 or data2):
            if(data1):
                data1 = data1.decode()
                buffer += data1
            else:
                data2 = data2.decode()
                buffer +=data2
            #print("")
            break
        attempt = attempt + 1
        total_attempts = total_attempts+1
    print("attempt: ")
    print(attempt)
    print(buffer, flush=True)

print("total attempts")
print(total_attempts)
sock1.close()
sock2.close()