import os
import subprocess
import time

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
    except subprocess.SubprocessError:
        print('I have problems with your wifi card')
    print('Scan wifi stations')
    os.system('airodump-ng wlan0mon')
    time.sleep(30)
    print('Scan finished')



hack()