import os
print('auto wifi hack')

def hack():
    os.system('systemctl stop NetworkManager')
    os.system('airmon-ng check kill')
    os.system('ifconfig')

hack()