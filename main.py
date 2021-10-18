'''Main file of program'''

import platform
import sys
import os

import KMCmodel.engine
import KMCmodel.parameters

def main():

    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
    else:
        print('Nieznana maszyna')
        return -1

    print('Program do symulacji Napylania laserowego PLD metodą Kinetic Monte Carlo')
    print('Obecna maszyna to:',platform.platform())
    print('Wersja Pythona to')
    print(sys.version)

    print('Uruchamianie programu:')
    engine = KMCmodel.engine.Engine()

    engine.startCalculations()


    #parameters = KMCmodel.parameters.Parameters()
    #print(parameters)
    print('Ukończono')

    return 0

if __name__ == '__main__':
    main()