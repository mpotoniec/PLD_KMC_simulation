'''as'''
import numpy as np

import KMCmodel.parameters
import KMCmodel.color
import KMCmodel.diffusion

class Cell():
    '''asd'''
    def __init__(self, x, y, z) -> None:
        self.__x = x
        self.__y = y
        self.__z = z
        self.__color = KMCmodel.color.Color(0,0,0,0)
        self.__energy = 0

        self.__neighbourhood = np.empty((26), dtype=Cell, order='C')

        self.__energyAA = KMCmodel.parameters.Parameters().energyAA

    def getMostPopularColorInNeighbourhood(self):
        result = KMCmodel.color.Color(0, 0, 0, 0)
        colors = {}

        for cell in self.__neighbourhood:
            if cell.color.A == 0: continue
            if not cell.color.A in colors.keys():
                colors[cell.color] = 1
            else:
                colors[cell.color] = colors[cell.color] + 1

        maxCount = 0
        for color in colors:
            if colors[color] >= maxCount:
                maxCount = colors[color]
                result = color
        
        #if result.A == 0:
            #result = self.__uniqueColor.getColorAtIndex(self.__uniqueColor.getNewColor())

        return result



    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        self.__x = x
    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, y):
        self.__y = y
    @property
    def z(self):
        return self.__z
    @z.setter
    def z(self, z):
        self.__z = z
    @property
    def energy(self):
        return self.__energy
    @energy.setter
    def energy(self, energy):
        self.__energy = energy
    @property 
    def neighbourhood(self):
        return self.__neighbourhood
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color_to_set):

        energyAA = self.__energyAA

        if self.__color.A == 0 and color_to_set.A != 0:
            for neighbour in self.__neighbourhood:
                neighbour.energy += energyAA
        elif self.__color.A != 0 and color_to_set.A == 0:
            for neighbour in self.__neighbourhood:
                neighbour.energy -= energyAA

        self.__color = color_to_set

        '''for i in range(-2,2+1,1):
            for j in range(-2,2+1,1):
                for k in range(-2,2+1,1):
                    
                    a = self.mod(self.__x + i, self.__cells.shape[0])
                    b = self.mod(self.__y + j, self.__cells.shape[1])
                    c = self.mod(self.__z + k, self.__cells.shape[2])

                    for l in range(0, KMCmodel.diffusion.Diffusion.allDiffusionsLength(3), 1):
                        KMCmodel.diffusion.Diffusion.allDiffusions(a, b, c, l)'''
    @property
    def uniqueColor(self):
        return self.__uniqueColor

    def __eq__(self, cell: object) -> bool:
        if self.__x == cell.x and self.__y == cell.y and self.__z == cell.z:
            return True
        else: return False

    def __str__(self) -> str:
        to_print_energy = str(round(self.__energy, 2))
        if len(to_print_energy) < 3: to_print_energy = to_print_energy + '.0'
        return  (
        "Komórka o wsp: [x = " 
        + str(self.__x) + ", y = " 
        + str(self.__y) + ", z = " 
        + str(self.__z) + "]. Z energią: " 
        + to_print_energy + ". " 
        + str(self.__color))
