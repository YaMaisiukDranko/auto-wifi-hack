import os
print('auto wifi hack')

def hack():
    print('Turn off NetworkManager')
    os.system('systemctl stop NetworkManager')
    print('Killing processes')
    os.system('airmon-ng check kill')
    print('Checking wifi card')
    os.system('ifconfig')
    print('Turning on wlan0')
    os.system('airmon-ng start wlan0')

hack()