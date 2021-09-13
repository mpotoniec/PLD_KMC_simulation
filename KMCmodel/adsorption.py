'''asdasd'''
import KMCmodel.event
import KMCmodel.cell
import KMCmodel.parameters

class Adsorption(KMCmodel.event.Event):
    '''adss'''
    def __init__(self, cell: KMCmodel.cell.Cell) -> None:
        super().__init__()
        self.__cell = cell
        self.__probability = KMCmodel.parameters.Parameters.adsorption_probability

    @property
    def cell(self):
        return self.__cell
    
    @property
    def probability(self):
        return self.__probability