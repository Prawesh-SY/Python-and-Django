# cLIENT
import socket



port = 12345 

server_ip = "192.168.1.221"
connect = True


# CLIENT - SEND MESSAGE
s = socket.socket()

s.connect((server_ip,port))
print("connected to server")

while connect:
    message = input("Me(press n to exit): ")
    s.send(message.encode('utf-8'))
    
    
    if message.lower() == "n":
        connect = False


s.close()
    
# Threading to be used for duplex communication  