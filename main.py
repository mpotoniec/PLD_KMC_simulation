'''Main file of program'''

import platform
import sys

def main():
    
    print('Program do symulacji Napylania laserowego PLD metodą Kinetic Monte Carlo')
    print('Obecna maszyna to:',platform.platform())
    print('Wersja Pythona to')
    print(sys.version)

if __name__ == '__main__':
    main()