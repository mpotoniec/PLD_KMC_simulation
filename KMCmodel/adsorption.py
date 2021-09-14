'''asdasd'''
import KMCmodel.event
import KMCmodel.cell
import KMCmodel.parameters

class Adsorption(KMCmodel.event.Event):
    '''adss'''
    def __init__(self, cell: KMCmodel.cell.Cell, adsorption_probability) -> None:
        super().__init__()
        self.__cell = cell
        self.__probability = adsorption_probability

    @property
    def cell(self):
        return self.__cell
    @cell.setter
    def cell(self, cell):
        self.__cell = cell 
    @property
    def probability(self):
        return self.__probability  
    @probability.setter
    def probability(self, probability):
        self.__probability = probability

    def __str__(self) -> str:
        return (
        "ADSORPCJA: w komórce o wsp: [x = " 
        + str(self.__cell.x) + ", y = " 
        + str(self.__cell.y) + ", z = " 
        + str(self.__cell.z) + "]. Z prawdopodowbieństwem: " 
        + str(self.__probability) + ". " 
        + str(self.__cell.color))