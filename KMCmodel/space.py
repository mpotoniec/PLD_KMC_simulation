import KMCmodel.size3D
import KMCmodel.cell
import KMCmodel.diffusion
import KMCmodel.color

import random

class Space():
    #@profile
    def __init__(self, parameters) -> None:
        self.__parameters = parameters
        self.__size = KMCmodel.size3D.Size3D(self.__parameters.space_size, self.__parameters.space_size, self.__parameters.space_size)

        self.__cells = tuple(tuple(tuple(KMCmodel.cell.Cell(x, y, z, self.__parameters.energyAA) for z in range(self.__size.depth)) for y in range(self.__size.height)) for x in range(self.__size.width))
        self.__allDiffusions = [[[[None for _ in range((9 + 8))] for _ in range(self.__size.depth)] for _ in range(self.__size.height)] for _ in range(self.__size.width)]
        #self.__possibleDiffusions = []
        self.__possibleDiffusions = set()
        self.__adsorptionList = [None for _ in range(self.__size.width * self.__size.depth)]
        self.__unique_colors = []

        self.__cumulated_probability = 0.

        self.getTransparentColor()
        self.__makeNeighbours()
        self.__makeInitialAdsorptions()

        #self.print_diffusions()

        #self.print_memory_ussage('Użycie pamięci w funkcji init space')

    #@profile
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

                                self.__allDiffusions[i][j][k][neighbour] = KMCmodel.diffusion.Diffusion(self.__cells[i][j][k], self.__cells[a][b][c], self.__parameters.kT, self.__parameters.Tn, self.__parameters.attempt_rate, self.__parameters.deposition_rate_diffusion, self.__parameters.cell_dim, self.__parameters.nano_second)
                                neighbour+=1
                                
    def __mathMod(self, a, b):
        return (abs(a * b) + a) % b

    def __makeInitialAdsorptions(self):
        index = 0
        for i in range(self.__size.width):
            for k in range(self.__size.depth):
                self.__adsorptionList[index] = KMCmodel.adsorption.Adsorption(self.__cells[i][0][k], self.__parameters.adsorption_probability)
                index+=1

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

        if diffusion.probability > 0 and pervous_probability == 0: self.__possibleDiffusions.add(diffusion) #self.__possibleDiffusions.append(diffusion)
        
        elif pervous_probability > 0 and diffusion.probability == 0: self.__possibleDiffusions.remove(diffusion) #self.__possibleDiffusions.remove(diffusion)



    def getColorAtIndex(self,index):
        return self.__unique_colors[index]

    def getIndexOfColor(self,given_color):
        return self.__unique_colors.index(given_color)
    
    def getTransparentColor(self):
        transparent = KMCmodel.color.Color(0, 0, 0, 0)
        self.__unique_colors.append(transparent)

    def getNewColor(self) -> int:
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

    def print_diffusions(self):
            for i in range(self.__size.width):
                for j in range(self.__size.height):
                    for k in range(self.__size.depth):
                        for diffusion in self.__allDiffusions[i][j][k]:
                            print(diffusion)

    def print_memory_ussage(self, info = 'Użycie pamięci'):
        print('')
        print(info)
        import os, psutil

        MB = 1048576
        GB = 1073741824

        process = psutil.Process(os.getpid())

        resident_memory = process.memory_info()[0]
        virtual_memory = process.memory_info()[1]
        shared_memory = process.memory_info()[2]
        data_memory = process.memory_info()[5]

        print(f'Pamięć rezydenta       = {round(resident_memory / MB, 2)}[MB] | {round(resident_memory / GB, 2)}[GB]')
        print(f'Pamięć wirtualna       = {round(virtual_memory / MB, 2)}[MB] | {round(virtual_memory / GB, 2)}[GB]')
        print(f'Pamięć współdzielona   = {round(shared_memory / MB, 2)}[MB] | {round(shared_memory  / GB, 2)}[GB]')
        print(f'Pamięć danych (RAM)    = {round(data_memory / MB, 2)}[MB] | {round(data_memory / GB, 2)}[GB]')
        print('')

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
    def adsorptionList(self):
        return self.__adsorptionList
    @property
    def cumulated_probability(self):
        return self.__cumulated_probability  
    
#Dokończyć to Texture!!!!