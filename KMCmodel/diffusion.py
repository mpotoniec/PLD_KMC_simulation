'''Flie that contains class of diffusion'''
from KMCmodel.parameters import Parameters
import KMCmodel.event
import KMCmodel.cell
import KMCmodel.parameters

import numpy as np

class Diffusion(KMCmodel.event.Event):
    '''Class representing diffusion in model. This class inherits from event class'''
    def __init__(self, originCell, targetCell) -> None:
        super().__init__()

        #self.__cumulated_probability = 0
        self.__originCell: KMCmodel.cell.Cell = originCell
        self.__targetCell: KMCmodel.cell.Cell = targetCell

    def equals(self, event) -> bool:
        if type(event) is not Diffusion: return False
        else:
            diff: Diffusion = event
            if diff.originCell == self.__originCell and diff.targetCell == self.__targetCell: return True
            else: return False

    #TODO zrobić overide int czy coś tam

    def handleChange(self):
        #pervous_probability = self.__probability
        pervous_probability = super().probability

        self.calculateProbability()

        if self.__probability > 0 and pervous_probability == 0: return True #self.__possibleDiffusions.append(self) 
        elif pervous_probability > 0 and self.__probability == 0: return False #self.__possibleDiffusions.remove(self)
        return None 

    def calculateProbability(self):
        #self.__cumulated_probability -= self.__probability
        self.__cumulated_probability -= super().probability

        if self.__originCell.color.A == 0:
            self.__probability = 0
            return

        if self.__targetCell.color.A != 0:
            self.__probability = 0
            return
        
        parameters = KMCmodel.parameters.Parameters()

        energyDiff = self.__targetCell.energy - self.__originCell.energy
        expParam = -energyDiff / parameters.kT
        self.__probability = parameters.Tn * parameters.attempt_rate * np.exp(expParam)
        self.__probability = self.__probability / (parameters.deposition_rate / (parameters.cell_dim * parameters.nano_second))

        self.__cumulated_probability += self.__probability



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

    '''def __str__(self) -> str:
        return (
        "DYFUZJA: o komórce początkowej: [x = " 
        + str(self.__originCell.x) + ", y = " 
        + str(self.__originCell.y) + ", z = " 
        + str(self.__originCell.z) + "] i komórce docelowej: [x = " 
        + str(self.__targetCell.x) + ", y = " 
        + str(self.__targetCell.y) + ", z = " 
        + str(self.__targetCell.z) + "]. Z prawdopodowbieństwem: " 
        + str(super().probability) + " i prawdopodowbieństwem skumulowanym: " 
        + str(self.__cumulated_probability))'''