# import socket programming + multithreading library
import socket

# import thread module
from _thread import *
import threading

print_lock = threading.Lock()

# thread function
def threaded(c):
    while True:

# data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')

        # lock released on exit
            print_lock.release()
            break

# reverse the given string from client
data = data[::-1]

# send back reversed string to client
c.send(data)

# connection closed
c.close()