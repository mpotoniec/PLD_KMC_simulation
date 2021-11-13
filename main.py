'''Main file of program'''
import platform
import sys
import os

import parameters
import KMCmodel.engine

def clear_console():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')
    else:
        print('Nieznana maszyna')
        return -1

def print_machine_info():
    print('Obecna maszyna to:',platform.platform())
    print('Wersja Pythona to')
    print(sys.version)

def make_calculation_without_gui():
    print('Uruchamianie programu:')
    engine = KMCmodel.engine.Engine(parameters.Parameters())

    engine.startCalculations()

    print('Ukończono')

def make_calculations_with_guiQt5():
    import PyQt5.QtWidgets as qtw
    from guiQt5 import MainWindow

    app = qtw.QApplication([])
    mw = MainWindow()
    app.exec_()

def make_calculations_with_guiTkinter():
    from guiTkinter import MainWindow

    main_window = MainWindow()

def main():

    clear_console()
    print_machine_info()

    #make_calculation_without_gui()
    #make_calculations_with_guiQt5()
    make_calculations_with_guiTkinter()

    return 0

if __name__ == '__main__':
    main()