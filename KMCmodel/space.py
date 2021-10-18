import KMCmodel.size3D
import KMCmodel.cell
import KMCmodel.diffusion
import KMCmodel.color

import random

class Space():
    '''asdsa'''
    def __init__(self, size: KMCmodel.size3D.Size3D) -> None:
        '''sadsa'''
        self.__size = size
        self.__cells = tuple(tuple(tuple(KMCmodel.cell.Cell(x, y, z) for z in range(self.__size.depth)) for y in range(self.__size.height)) for x in range(self.__size.width))

        self.__unique_colors = []

        self.__allDiffusions = [[[[None for _ in range((9 + 8))] for _ in range(self.__size.depth)] for _ in range(self.__size.height)] for _ in range(self.__size.width)]
        self.__possibleDiffusions = []
        self.__cumulated_probability = 0.

        self.getTransparentColor()
        self.__createCells()

        print("Done.")

    def __createCells(self):
        #for i in range(self.__size.width):
        #    for j in range(self.__size.height):
        #        for k in range(self.__size.depth):
        #            self.__cells[i, j, k] = KMCmodel.cell.Cell(i, j, k)
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

                                self.__cells[i][j][k].neighbourhood[neighbour] = self.__cells[a][b][c]
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

                                self.__allDiffusions[i][j][k][neighbour] = KMCmodel.diffusion.Diffusion(self.__cells[i][j][k], self.__cells[a][b][c])
                                neighbour+=1
                                
    def __mathMod(self, a, b):
        return (abs(a * b) + a) % b

    def __allDiffusions_handleChange(self, x, y, z):

        for i in range(-2,2+1,1):
            for j in range(-2,2+1,1):
                for k in range(-2,2+1,1):
                    
                    a = self.__mathMod(x + i, len(self.__cells))
                    b = self.__mathMod(y + j, len(self.__cells[0]))
                    c = self.__mathMod(z + k, len(self.__cells[0][0]))

                    for l in range(0, len(self.__allDiffusions[0][0][0]), 1):
                        if self.__allDiffusions[a][b][c][l] == None: continue
                        self.__handleChange(self.__allDiffusions[a][b][c][l])

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
        #index = np.where(self.__unique_colors == given_color)
        #if len(index[0]) > 0: return index[0][0]
        #else: return False

        return self.__unique_colors.index(given_color)
    
    def getTransparentColor(self):
        '''Method creates unique transparent color.'''
        transparent = KMCmodel.color.Color(0, 0, 0, 0)
        self.__unique_colors.append(transparent)

    def getNewColor(self) -> int:
        '''Method creating new random color.'''
        #R = np.ubyte(np.random.randint(0,255))
        #B = np.ubyte(np.random.randint(0,255))
        #G = np.ubyte(np.random.randint(0,255))
        #A = np.ubyte(-1)

        R = random.randint(0,255)
        B = random.randint(0,255)
        G = random.randint(0,255)
        A = 255

        new_color = KMCmodel.color.Color(R,B,G,A)
        self.__unique_colors.append(new_color)

        return len(self.__unique_colors) - 1



    def cells_getColor(self, i, j, k):
        return self.__cells[i][j][k].color

    def cells_setColor(self, i, j, k, color):
        self.__cells[i][j][k].color = color
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