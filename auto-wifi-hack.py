import os
print('auto wifi hack')

def hack():
    print('Enabling root terminal')
    os.system('sudo su')
    print('Turn off NetworkManager')
    os.system('systemctl stop NetworkManager')
    print('Killing processes')
    os.system('airmon-ng check kill')
    print('Checking wifi card')
    os.system('ifconfig')

hack()