'''Main file of program'''

import platform
import sys
import os

import KMCmodel.engine

def main():
    
    os.system('clear')
    print('Program do symulacji Napylania laserowego PLD metodą Kinetic Monte Carlo')
    print('Obecna maszyna to:',platform.platform())
    print('Wersja Pythona to')
    print(sys.version)

    print('Uruchamianie programu:')
    engine = KMCmodel.engine.Engine()
    engine.startCalculations()
    print('Ukończono')

if __name__ == '__main__':
    main()