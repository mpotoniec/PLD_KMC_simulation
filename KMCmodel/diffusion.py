from KMCmodel.parameters import Parameters
import KMCmodel.cell
import KMCmodel.parameters

import math

class Diffusion():
    def __init__(self, originCell, targetCell) -> None:
        
        self.__probability = 0
        self.__originCell: KMCmodel.cell.Cell = originCell
        self.__targetCell: KMCmodel.cell.Cell = targetCell

        self.__parameters = KMCmodel.parameters.Parameters()

    #TODO zrobić overide int czy coś tam

    def calculateProbability(self, cumulated_probability):
        cumulated_probability -= self.__probability

        if self.__originCell.color.A == 0:
            self.__probability = 0
            return cumulated_probability

        if self.__targetCell.color.A != 0:
            self.__probability = 0
            return cumulated_probability

        energyDiff = self.__targetCell.energy - self.__originCell.energy
        expParam = -energyDiff / self.__parameters.kT
        self.__probability = self.__parameters.Tn * self.__parameters.attempt_rate * math.exp(expParam)
        self.__probability = self.__probability / (self.__parameters.deposition_rate_diffusion / (self.__parameters.cell_dim * self.__parameters.nano_second))

        cumulated_probability += self.__probability

        return cumulated_probability



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