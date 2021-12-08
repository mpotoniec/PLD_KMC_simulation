'''
Podstawowe gui stworzone przy pomocy biblioteki Tkinter. Brak możliwości wizualizacji przy pomocy OpenGl
Możliwość wykonania kody przy pomocy wydajnego kompilatora JIT PYPY3
'''
from tkinter import *

import parameters
import KMCmodel.engine

class MainWindow():
    def __init__(self) -> None:
        
        def queue_up_simulations():
            simulations_list.append(make_parameters_for_simulation())
            number_of_simulations = int(Queued_simulations.cget('text').split('=')[1])
            number_of_simulations += 1
            Queued_simulations['text'] = 'Number of queued simulations = ' + str(number_of_simulations)

        def make_parameters_for_simulation():
            simulation_parameters = parameters.Parameters()

            simulation_parameters.create_new_parameters(space_size_entry.get(), substrate_temperature_entry.get(),melting_temperature_entry.get(),
            boltzman_constant_entry.get(),vibration_frequency_entry.get(),n_entry.get(),energyAA_entry.get(),energy_vapour_entry.get(),
            deposition_rate_diffusion_entry.get(),cell_dim_entry.get(),nano_second_entry.get(),deposition_rate_entry.get())

            return simulation_parameters

        def start_simulations():
                        
            if len(simulations_list) == 0:

                make_parameters_for_simulation()
                print('Uruchamianie programu:')
                engine = KMCmodel.engine.Engine(make_parameters_for_simulation())

                engine.startCalculations()

                print('Ukończono')

            elif len(simulations_list) > 0:
                print('Uruchamianie zakolejkowanych symulacji')
                for parameter in simulations_list:
                    engine = KMCmodel.engine.Engine(parameter)
                    engine.startCalculations()
                print('Ukończono')
                simulations_list.clear()
                Queued_simulations['text'] = 'Number of queued simulations = 0'

        root = Tk()
        root.call('wm', 'iconphoto', root._w, PhotoImage(file='icon.png'))
        root.title('PLD Simulation')

        simulation_parameters = parameters.Parameters()
        simulations_list = []

        #Creating labes
        space_size_label = Label(root, text='Space size')
        substrate_temperature_label = Label(root, text='Substrate temperature')
        melting_temperature_label = Label(root, text='Melting temperature')
        boltzman_constant_label = Label(root, text='Boltzman contstant')
        vibration_frequency_label = Label(root, text='Vibration frequency') 
        n_label = Label(root, text='n')
        energyAA_label = Label(root, text='EnergyAA')
        energy_vapour_label = Label(root, text='Energy vapour')
        deposition_rate_diffusion_label = Label(root, text='Deposition rate diffusion')
        cell_dim_label = Label(root, text='Cell dim')
        nano_second_label = Label(root, text='Nano second')
        deposition_rate_label = Label(root, text='Deposition rate')


        space_size_label.grid(column=0,row=0)
        substrate_temperature_label.grid(column=0,row=1)
        melting_temperature_label.grid(column=0,row=2)
        boltzman_constant_label.grid(column=0,row=3)
        vibration_frequency_label.grid(column=0,row=4)
        n_label.grid(column=0,row=5)
        energyAA_label.grid(column=0,row=6)
        energy_vapour_label.grid(column=0,row=7)
        deposition_rate_diffusion_label.grid(column=0,row=8)
        cell_dim_label.grid(column=0,row=9)
        nano_second_label.grid(column=0,row=10)
        deposition_rate_label.grid(column=0,row=11)

        #Creating text fields
        text_fields_width = 25

        space_size_entry = Entry(root, width=text_fields_width)
        space_size_entry.insert(0, str(simulation_parameters.space_size))

        substrate_temperature_entry = Entry(root, width=text_fields_width)
        substrate_temperature_entry.insert(0, str(simulation_parameters.substrate_temperature))

        melting_temperature_entry = Entry(root, width=text_fields_width)
        melting_temperature_entry.insert(0, str(simulation_parameters.melting_temperature))

        boltzman_constant_entry = Entry(root, width=text_fields_width)
        boltzman_constant_entry.insert(0, str(simulation_parameters.boltzman_constant))

        vibration_frequency_entry = Entry(root, width=text_fields_width)
        vibration_frequency_entry.insert(0, str(simulation_parameters.vibration_frequency))

        n_entry = Entry(root, width=text_fields_width)
        n_entry.insert(0, str(simulation_parameters.n))

        energyAA_entry = Entry(root, width=text_fields_width)
        energyAA_entry.insert(0, str(simulation_parameters.energyAA))

        energy_vapour_entry = Entry(root, width=text_fields_width)
        energy_vapour_entry.insert(0, str(simulation_parameters.energy_vapour))

        deposition_rate_diffusion_entry = Entry(root, width=text_fields_width)
        deposition_rate_diffusion_entry.insert(0, str(simulation_parameters.deposition_rate_diffusion))

        cell_dim_entry = Entry(root, width=text_fields_width)
        cell_dim_entry.insert(0, str(simulation_parameters.cell_dim))

        nano_second_entry = Entry(root, width=text_fields_width)
        nano_second_entry.insert(0, str(simulation_parameters.nano_second))

        deposition_rate_entry = Entry(root, width=text_fields_width)
        deposition_rate_entry.insert(0, str(simulation_parameters.deposition_rate))

        space_size_entry.grid(column=1,row=0)
        substrate_temperature_entry.grid(column=1,row=1)
        melting_temperature_entry.grid(column=1,row=2)
        boltzman_constant_entry.grid(column=1,row=3)
        vibration_frequency_entry.grid(column=1,row=4)
        n_entry.grid(column=1,row=5)
        energyAA_entry.grid(column=1,row=6)
        energy_vapour_entry.grid(column=1,row=7)
        deposition_rate_diffusion_entry.grid(column=1,row=8)
        cell_dim_entry.grid(column=1,row=9)
        nano_second_entry.grid(column=1,row=10)
        deposition_rate_entry.grid(column=1,row=11)

        #Creating buttons
        start_simulations_button = Button(root, text='Start simulations', command = start_simulations)
        queue_up_simulation_button = Button(root, text='Queue up simulation', command = queue_up_simulations)

        start_simulations_button.grid(column=0, row=12)
        queue_up_simulation_button.grid(column=1, row=12)

        Queued_simulations = Label(root, text='Number of queued simulations = 0')
        Queued_simulations.grid(column=3, row=0)


        root.mainloop()