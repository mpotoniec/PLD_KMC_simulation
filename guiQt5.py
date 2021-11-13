'''
Podstawowe gui stworzone przy pomocy biblioteki PyQt5. Możliwość wizualizacji OpenGl #TODO w przyszłości
Brak możliwości wykonania kodu przy pomocy kompilatora JIT PYPY3. PYPY3 nie ma PyQt5
'''
import PyQt5.QtWidgets as qtw

import parameters
import KMCmodel.engine

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(qtw.QGridLayout())

        simulation_parameters = parameters.Parameters()
        simulations_list = []

        #Creating labes
        space_size_label = qtw.QLabel('Space size')
        substrate_temperature_label = qtw.QLabel('Substrate temperature') 
        melting_temperature_label = qtw.QLabel('Melting temperature')
        boltzman_constant_label = qtw.QLabel('Boltzman contstant')
        vibration_frequency_label = qtw.QLabel('Vibration frequency')  
        n_label = qtw.QLabel('n')
        energyAA_label = qtw.QLabel('EnergyAA')
        energy_vapour_label = qtw.QLabel('Energy vapour') 
        deposition_rate_diffusion_label = qtw.QLabel('Deposition rate diffusion')
        cell_dim_label = qtw.QLabel('Cell dim')
        nano_second_label = qtw.QLabel('Nano second')
        deposition_rate_label = qtw.QLabel('Deposition rate')

        self.layout().addWidget(space_size_label)
        self.layout().addWidget(substrate_temperature_label)
        self.layout().addWidget(melting_temperature_label)
        self.layout().addWidget(boltzman_constant_label)
        self.layout().addWidget(vibration_frequency_label)
        self.layout().addWidget(n_label)
        self.layout().addWidget(energyAA_label)
        self.layout().addWidget(energy_vapour_label)
        self.layout().addWidget(deposition_rate_diffusion_label)
        self.layout().addWidget(cell_dim_label)
        self.layout().addWidget(nano_second_label)
        self.layout().addWidget(deposition_rate_label)

        #Creating text fields
        space_size_entry = qtw.QLineEdit()
        space_size_entry.setText(str(simulation_parameters.space_size))

        substrate_temperature_entry = qtw.QLineEdit()
        substrate_temperature_entry.setText(str(simulation_parameters.substrate_temperature))

        melting_temperature_entry = qtw.QLineEdit()
        melting_temperature_entry.setText(str(simulation_parameters.melting_temperature))

        boltzman_constant_entry = qtw.QLineEdit()
        boltzman_constant_entry.setText(str(simulation_parameters.boltzman_constant))

        vibration_frequency_entry = qtw.QLineEdit() 
        vibration_frequency_entry.setText(str(simulation_parameters.vibration_frequency))

        n_entry = qtw.QLineEdit()
        n_entry.setText(str(simulation_parameters.n))

        energyAA_entry = qtw.QLineEdit()
        energyAA_entry.setText(str(simulation_parameters.energyAA))

        energy_vapour_entry = qtw.QLineEdit()
        energy_vapour_entry.setText(str(simulation_parameters.energy_vapour))

        deposition_rate_diffusion_entry = qtw.QLineEdit()
        deposition_rate_diffusion_entry.setText(str(simulation_parameters.deposition_rate_diffusion))

        cell_dim_entry = qtw.QLineEdit()
        cell_dim_entry.setText(str(simulation_parameters.cell_dim))

        nano_second_entry = qtw.QLineEdit()
        nano_second_entry.setText(str(simulation_parameters.nano_second))

        deposition_rate_entry = qtw.QLineEdit()
        deposition_rate_entry.setText(str(simulation_parameters.deposition_rate))

        self.layout().addWidget(space_size_entry, 0,1)
        self.layout().addWidget(substrate_temperature_entry, 1,1)
        self.layout().addWidget(melting_temperature_entry, 2,1)
        self.layout().addWidget(boltzman_constant_entry, 3,1)
        self.layout().addWidget(vibration_frequency_entry, 4,1)
        self.layout().addWidget(n_entry, 5, 1)
        self.layout().addWidget(energyAA_entry, 6,1)
        self.layout().addWidget(energy_vapour_entry, 7,1)
        self.layout().addWidget(deposition_rate_diffusion_entry, 8,1)
        self.layout().addWidget(cell_dim_entry, 9,1)
        self.layout().addWidget(nano_second_entry, 10,1)
        self.layout().addWidget(deposition_rate_entry, 11,1)

        #Creating buttons
        start_simulations_button = qtw.QPushButton('Start simulations', clicked = lambda: start_simulations())
        queue_up_simulation_button = qtw.QPushButton('Queue up simulation', clicked = lambda: queue_up_simulations())

        self.layout().addWidget(start_simulations_button, 12,0)
        self.layout().addWidget(queue_up_simulation_button, 12,1)

        Queued_simulations = qtw.QLabel('Number of queued simulations = 0')
        self.layout().addWidget(Queued_simulations, 0,2)

        def queue_up_simulations():
            simulations_list.append(make_parameters_for_simulation())
            number_of_simulations = int(Queued_simulations.text().split('=')[1])
            number_of_simulations += 1
            Queued_simulations.setText('Number of queued simulations = ' + str(number_of_simulations))

        def make_parameters_for_simulation():
            simulation_parameters = parameters.Parameters()

            simulation_parameters.create_new_parameters(space_size_entry.text(), substrate_temperature_entry.text(),melting_temperature_entry.text(),
            boltzman_constant_entry.text(),vibration_frequency_entry.text(),n_entry.text(),energyAA_entry.text(),energy_vapour_entry.text(),
            deposition_rate_diffusion_entry.text(),cell_dim_entry.text(),nano_second_entry.text(),deposition_rate_entry.text())

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
                Queued_simulations.setText('Number of queued simulations = 0')


        self.show()