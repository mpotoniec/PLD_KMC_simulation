'''File contains class with parameters of simulation'''

class Parameters():
    '''Class with parameters of program'''
    def __init__(self) -> None:
        self.__space_size = 10 #70
        self.__substrate_temperature = 700
        self.__melting_temperature = 2930
        self.__boltzman_constant = 8.617333262 * 10e-5
        self.__vibration_frequency = 1e13
        self.__n = 1
        self.__energyAA = 0.8
        self.__energy_vapour = 1000
        self.__deposition_rate_diffusion = 0.05
        self.__cell_dim = 1e-9
        self.__nano_second = 1e-9

        self.__deposition_rate = 90.0e-9 / 1800.0

        self.__adsorption_probability = self.__deposition_rate / self.__cell_dim
        self.__Tr = self.__substrate_temperature
        self.__Tn = pow(self.__Tr, self.__n)
        self.__kT = self.__Tr * self.__boltzman_constant
        self.__attempt_rate = self.__vibration_frequency

    @property
    def space_size(self): 
        return self.__space_size
    @space_size.setter
    def space_size(self, space_size):
        self.__space_size = space_size
    @property
    def substrate_temperature(self): 
        return self.__substrate_temperature        
    @substrate_temperature.setter
    def substrate_temperature(self, substrate_temperature):
        self.__substrate_temperature = substrate_temperature    
    @property
    def melting_temperature(self): 
        return self.__melting_temperature       
    @melting_temperature.setter
    def melting_temperature(self, melting_temperature):
        self.__melting_temperature = melting_temperature
    @property
    def boltzman_constant(self): 
        return self.__boltzman_constant       
    @boltzman_constant.setter
    def boltzman_constant(self, boltzman_constant):
        self.__boltzman_constant = boltzman_constant
    @property
    def vibration_frequency(self): 
        return self.__vibration_frequency       
    @vibration_frequency.setter
    def vibration_frequency(self, vibration_frequency):
        self.__vibration_frequency = vibration_frequency
    @property
    def n(self): 
        return self.__n       
    @n.setter
    def n(self, n):
        self.__n = n
    @property
    def energyAA(self): 
        return self.__energyAA      
    @energyAA.setter
    def energyAA(self, energyAA):
        self.__energyAA = energyAA
    @property
    def energy_vapour(self): 
        return self.__energy_vapour     
    @energy_vapour.setter
    def energy_vapour(self, energy_vapour):
        self.__energy_vapour = energy_vapour
    @property
    def deposition_rate_diffusion(self):
        return self.__deposition_rate_diffusion
    @deposition_rate_diffusion.setter
    def deposition_rate_diffusion(self, deposition_rate_diffusion):
        self.__deposition_rate_diffusion = deposition_rate_diffusion
    @property
    def cell_dim(self): 
        return self.__cell_dim       
    @cell_dim.setter
    def cell_dim(self, cell_dim):
        self.__cell_dim = cell_dim
    @property
    def nano_second(self): 
        return self.__nano_second      
    @nano_second.setter
    def nano_second(self, nano_second):
        self.__nano_second = nano_second
    @property
    def deposition_rate(self):
        return self.__deposition_rate
    @property
    def adsorption_probability(self): 
        return self.__adsorption_probability
    @property
    def Tr(self): 
        return self.__Tr
    @property
    def Tn(self): 
        return self.__Tn 
    @property
    def kT(self): 
        return self.__kT
    @property
    def attempt_rate(self): 
        return self.__attempt_rate

    def __str__(self) -> str:

        to_print =  str(f"Wymiar przestrzenii = {self.__space_size:,}\n")
        to_print += str(f"Temperatura substratu = {self.__substrate_temperature:,}\n")
        to_print += str(f"Temperatura topnienia = {self.__melting_temperature:,}\n")
        to_print += str(f"Stała Boltzmana = {self.__boltzman_constant:,}\n")
        to_print += str(f"Częstość wibracji = {self.__vibration_frequency:,}\n")
        to_print += str(f"N = {self.__n:,}\n")
        to_print += str(f"Energia AA = {self.__energyAA:,}\n")
        to_print += str(f"Energia mgiełki plazmy = {self.__energy_vapour:,}\n")
        to_print += str(f"Wskaźnik depozycji dyfuzji = {self.__deposition_rate_diffusion:,}\n")
        to_print += str(f"Rozmiar komórki = {self.__cell_dim:,}\n")
        to_print += str(f"Nano sekunda = {self.__nano_second:,}\n")
        to_print += str(f"Wskaźnik depozycji = {self.__deposition_rate:,}\n")
        to_print += str(f"Prawdopodobieństwo adsorpcji = {self.__adsorption_probability:,}\n")
        to_print += str(f"Tr = {self.__Tr:,}\n")
        to_print += str(f"Tn = {self.__Tn:,}\n")
        to_print += str(f"kT = {self.__kT:,}\n")
        to_print += str(f"Wskaźnik prób = {self.__attempt_rate:,}\n")

        return to_print

    def __hash__(self) -> int:
        return 0