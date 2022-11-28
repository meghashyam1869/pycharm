import socket
import subprocess
import sys

from datetime import datetime

#black your screen
subprocess.call('clear', shell=True)

#ask for input
remoteserver = input("Enter a remote host to scan: ")
remoteserverIP = socket.gethostbyname(remoteserver)

#print a nice banner with information on which host we are about to scan
print ("_" * 60)
print ("please wait,scanning remote host", remoteserverIP)
print ("_" *60)

#check the date and time the scan was started
t1 = datetime.now()

#using the range function to specify ports
#also we will do error handling

try:
    for port in range (1,5000):
        sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteserverIP, port))
        if result ==0:
            print ("port {}:       open".format(port))
            sock.close()
            
except keyboardInterrupt:
    print ("Hostname could not be resolved.Exiting")
    sys.exit()

except socket.error:
    print ("couldn't connect to server")
    sys.exit()    
            