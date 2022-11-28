import socket
hostname = socket.gethostname()
#import os
#print (os.system("ipconfig"))
ipadd = socket.gethostbyname(hostname)
print (ipadd)