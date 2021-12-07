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

def print_memory_ussage(info = 'Użycie pamięci'):
    print('')
    print(info)
    import os, psutil

    MB = 1048576
    GB = 1073741824

    process = psutil.Process(os.getpid())

    resident_memory = process.memory_info()[0]
    virtual_memory = process.memory_info()[1]
    shared_memory = process.memory_info()[2]
    data_memory = process.memory_info()[5]

    print(f'Pamięć rezydenta       = {round(resident_memory / MB, 2)}[MB] | {round(resident_memory / GB, 2)}[GB]')
    print(f'Pamięć wirtualna       = {round(virtual_memory / MB, 2)}[MB] | {round(virtual_memory / GB, 2)}[GB]')
    print(f'Pamięć współdzielona   = {round(shared_memory / MB, 2)}[MB] | {round(shared_memory  / GB, 2)}[GB]')
    print(f'Pamięć danych (RAM)    = {round(data_memory / MB, 2)}[MB] | {round(data_memory / GB, 2)}[GB]')
    print('')

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
    print_memory_ussage('Użycie pamięci przed utworzeniem przestrzeni do symulacji')

    #make_calculation_without_gui()
    #make_calculations_with_guiQt5()
    make_calculations_with_guiTkinter()

    return 0

if __name__ == '__main__':
    main()