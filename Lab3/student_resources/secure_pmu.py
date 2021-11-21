 
#!/usr/bin/python
 
import sys
import socket
import ssl
 
 
CERTIFICATE = sys.argv[1] #certchain path .pem
KEY_PATH = sys.argv[2] #.key
HOST = "localhost"
PORT = 5003
 
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(CERTIFICATE, KEY_PATH)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((HOST, PORT))
    sock.listen(5) #not sure what number in here is
    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
    

        print("enter loop")
        command = ""
        while True: 
            data = conn.recv(15) 
            #obv would need to do more procesisng in case we receive the command ints several packets..
            print(data.decode())
            if not data: 
                break
            if(data.decode() == "CMD_short:0"):
                print("sending reply")
                conn.send(("This is PMU data 0").encode())

        conn.close()
