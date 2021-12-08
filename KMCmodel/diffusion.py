import KMCmodel.cell

import math

class Diffusion():
    def __init__(self, originCell, targetCell) -> None:
        
        self.__probability = 0
        self.__originCell: KMCmodel.cell.Cell = originCell
        self.__targetCell: KMCmodel.cell.Cell = targetCell

    def calculateProbability(self, kT, diff_prob_initial_params):

        if self.__originCell.colorIndex == 0 or self.__targetCell.colorIndex != 0:
            self.__probability = 0
            return self.__probability

        energyDiff = self.__targetCell.energy - self.__originCell.energy
        self.__probability = math.exp(-energyDiff / kT) * diff_prob_initial_params

        return self.__probability


    @property
    def originCell(self):
        return self.__originCell
    @originCell.setter
    def originCell(self, cell):
        self.__originCell = cell
    @property
    def targetCell(self):
        return self.__targetCell
    @targetCell.setter
    def targetCell(self, cell):
        self.__targetCell = cell
    @property
    def probability(self):
        return self.__probability
    @probability.setter
    def probability(self, probability):
        self.__probability = probability

    def __eq__(self, event: object) -> bool:
        if not(isinstance(event, Diffusion)): return False
        else:
            diff: Diffusion = event
            if diff.originCell == self.__originCell and diff.targetCell == self.__targetCell: return True
            else: return False

    def __str__(self) -> str:
        return (
        "DYFUZJA: o komórce początkowej: [x = " 
        + str(self.__originCell.x) + ", y = " 
        + str(self.__originCell.y) + ", z = " 
        + str(self.__originCell.z) + "] i komórce docelowej: [x = " 
        + str(self.__targetCell.x) + ", y = " 
        + str(self.__targetCell.y) + ", z = " 
        + str(self.__targetCell.z) + "]. Z prawdopodowbieństwem: " 
        + str(self.__probability))

    def __hash__(self) -> int:
        return hash((self.originCell, self.targetCell))