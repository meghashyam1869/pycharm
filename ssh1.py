#SSH to routers from devices files



#connect to multiple routers mentioned in devices.txt
from netmiko import ConnectHandler 



with open('devices.txt') as routers:
    for IP in routers:
        Router= {
            "device_type": "cisco_ios",
            "ip": "sandbox-iosxe-latest-1.cisco.com",
            "username": "developer",
            "password": "C1sco12345"
        }
        net_connect = ConnectHandler(**Router)
        
        print('Connecting to ' + IP)
        print('-'*79)
        output = net_connect.send_command('sh ip int breif')
        print(output)
        print()
        print('-'*79)
#Finally close the connection
net_connect.disconnect()