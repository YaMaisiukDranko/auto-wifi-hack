import os
print('auto wifi hack')

def hack():
    print('Turn off NetworkManager')
    os.system('systemctl stop NetworkManager')
    print('Killing processes')
    os.system('airmon-ng check kill')
    print('Checking wifi card')
    os.system('ifconfig')
    try:
        os.system('airmon-ng start wlan0')
    except SystemError:
        print('I have problems with your wifi card')




hack()