# 
import socket

socketObject = socket.socket()

port= "12345"

socketObject.bind(('',port))    # My current IP: 192.168.1.226 if "" -> 127.0.0.1

socketObject.listen(5)

connection, addr = socketObject.accept()



connection.recv(1024)     # The argument will be the data limit to receive

connection.close()

