
# SERVER
import socket

s = socket.socket()
port = 12345

s.bind(('',port))

print("i am server in listening mode")
s.listen(45)

connection, addr = s.accept()
print("connection from ", addr)

print(connection.recv(1024))

connection.close()