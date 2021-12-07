import KMCmodel.cell

class Adsorption():
    def __init__(self, cell: KMCmodel.cell.Cell, adsorption_probability) -> None:
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

    def __eq__(self, adsorption: object) -> bool:
        if self.__cell.x == adsorption.cell.x and self.__cell.y == adsorption.cell.y and self.__cell.z == adsorption.cell.z: return True
        else: return False

    def __str__(self) -> str:
        return (
        "ADSORPCJA: w komórce o wsp: [x = " 
        + str(self.__cell.x) + ", y = " 
        + str(self.__cell.y) + ", z = " 
        + str(self.__cell.z) + "]. Z prawdopodowbieństwem: " 
        + str(self.__probability) + ". " 
        + str(self.__cell.color))

    def __hash__(self) -> int:
        return hash((self.__cell, self.__probability))