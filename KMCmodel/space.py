from numpy.lib.function_base import diff
import KMCmodel.size3D
import KMCmodel.cell
import KMCmodel.diffusion
import KMCmodel.color

import numpy as np

class Space():
    '''asdsa'''
    def __init__(self, size: KMCmodel.size3D.Size3D) -> None:
        '''sadsa'''
        self.__size = size
        self.__cells = np.empty((self.__size.width, self.__size.height, self.__size.depth), dtype=KMCmodel.cell.Cell, order='C')
        self.__unique_colors = np.empty((1,0), dtype=KMCmodel.color.Color, order='C')

        self.__allDiffusions = np.empty((self.__size.width, self.__size.height, self.__size.depth, (9 + 8)), dtype=KMCmodel.diffusion.Diffusion, order='C')
        self.__possibleDiffusions = []
        self.__cumulated_probability = 0.

        self.getTransparentColor()
        self.__createCells()

        print("Done.")

    def __createCells(self):
        for i in range(self.__size.width):
            for j in range(self.__size.height):
                for k in range(self.__size.depth):
                    self.__cells[i, j, k] = KMCmodel.cell.Cell(i, j, k)
        self.__makeNeighbours()

    def __makeNeighbours(self):
        for i in range(self.__size.width):
            for j in range(self.__size.height):
                for k in range(self.__size.depth):

                    neighbour = 0

                    for x in range(-1, 2, 1):
                        for y in range(-1, 2, 1):
                            for z in range(-1, 2, 1):

                                if x == 0 and y == 0 and z == 0: continue

                                a = self.__mathMod(i + x, self.__size.width)
                                b = self.__mathMod(j + y, self.__size.height)
                                c = self.__mathMod(k + z, self.__size.depth)

                                self.__cells[i, j, k].neighbourhood[neighbour] = self.__cells[a, b, c]
                                neighbour+=1


        for i in range(self.__size.width):
            for j in range(self.__size.height):
                for k in range(self.__size.depth):

                    neighbour = 0

                    for x in range(-1, 2, 1):
                        for y in range(-1, 1, 1):
                            for z in range(-1, 2, 1): 

                                if x == 0 and y == 0 and z == 0: continue
                                if j == 0 and y == -1: continue

                                a = self.__mathMod(i + x, self.__size.width)
                                b = self.__mathMod(j + y, self.__size.height)
                                c = self.__mathMod(k + z, self.__size.depth)

                                self.__allDiffusions[i, j, k, neighbour] = KMCmodel.diffusion.Diffusion(self.__cells[i, j, k], self.__cells[a, b, c])
                                neighbour+=1
                                
    def __mathMod(self, a, b):
        return (abs(a * b) + a) % b

    def __allDiffusions_handleChange(self, x, y, z):

        for i in range(-2,2+1,1):
            for j in range(-2,2+1,1):
                for k in range(-2,2+1,1):
                    
                    a = self.__mathMod(x + i, self.__cells.shape[0])
                    b = self.__mathMod(y + j, self.__cells.shape[1])
                    c = self.__mathMod(z + k, self.__cells.shape[2])

                    for l in range(0, self.__allDiffusions.shape[3], 1):
                        if self.__allDiffusions[a, b, c, l] == None: continue
                        self.__handleChange(self.__allDiffusions[a, b, c, l])

    def __handleChange(self, diffusion: KMCmodel.diffusion.Diffusion):
        pervous_probability = diffusion.probability

        result = diffusion.calculateProbability(self.__cumulated_probability)
        if result != None: self.__cumulated_probability = result

        if diffusion.probability > 0 and pervous_probability == 0: self.__possibleDiffusions.append(diffusion)
        elif pervous_probability > 0 and diffusion.probability == 0: self.__possibleDiffusions.remove(diffusion)


    def getColorAtIndex(self,index):
        '''Method returns color under given index'''
        return self.__unique_colors[index]

    def getIndexOfColor(self,given_color):
        index = np.where(self.__unique_colors == given_color)
        if len(index[0]) > 0: return index[0][0]
        else: return False
    
    def getTransparentColor(self):
        '''Method creates unique transparent color.'''
        transparent = KMCmodel.color.Color(np.ubyte(0), np.ubyte(0), np.ubyte(0), np.ubyte(0))
        self.__unique_colors = np.append(self.__unique_colors, transparent)

    def getNewColor(self) -> int:
        '''Method creating new random color.'''
        R = np.ubyte(np.random.randint(0,255))
        B = np.ubyte(np.random.randint(0,255))
        G = np.ubyte(np.random.randint(0,255))
        A = np.ubyte(-1)

        new_color = KMCmodel.color.Color(R,B,G,A)
        self.__unique_colors = np.append(self.__unique_colors, new_color)

        return self.__unique_colors.size - 1



    def cells_getColor(self, i, j, k):
        return self.__cells[i, j, k].color

    def cells_setColor(self, i, j, k, color):
        self.__cells[i, j, k].color = color
        self.__allDiffusions_handleChange(i, j, k)



    @property
    def size(self):
        return self.__size   
    @property
    def cells(self):
        return self.__cells
    @property
    def allDiffusions(self):
        return self.__allDiffusions
    @property
    def possibleDiffusions(self):
        return self.__possibleDiffusions
    @possibleDiffusions.setter
    def possibleDiffusions(self, diffusion):
        self.__possibleDiffusions.append(diffusion)
    @property
    def cumulated_probability(self):
        return self.__cumulated_probability  
    
#Dokończyć to Texture!!!!