#first of all import the socket library
import socket

#create a socket object
s = socket.socket()
print ("socket successfully created")

#reserve a port on your computer in our case it is 40674 but it can be anything
port = 40674

#next bind to the port
#we have not typed any ip in the ip field
#instead we have inputrd an empty string
#this makes the server listen to requests
#coming from other computers on the network

s.bind(('',port))#'':ip address open:take request from any machine in the network,bind()--->2 params:
print("socket binded to %s" %(port))

#put the socket into listening mode

s.listen(5)

print("Socket is listening")
while True:
    c, addr = s.accept()
    print('Got connection from ',addr)
    c.send(b'Thank you for connection')
    c.close()

