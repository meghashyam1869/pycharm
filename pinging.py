
from netmiko import ConnectHandler
import os
from warnings import filterwarnings
class Ping_test():
  def __init__(self):
# First create the device object using a dictionary
    # CSR = {
      # "device_type": "cisco_ios",
      # "ip": "sandbox-iosxe-latest-1.cisco.com",
      # "username": "developer",
      # "password": "C1sco12345"
    # }

    # Next establish the SSH connection
   # net_connect = ConnectHandler(**CSR)

    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
      print( hostname, 'is up!')
    else:
      print (hostname, 'is down!')
    #net_connect.disconnect()


hostname = "www.google.com"  # example
filterwarnings("ignore")
myPing_test=Ping_test()

