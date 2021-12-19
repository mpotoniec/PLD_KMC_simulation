import KMCmodel.color
import KMCmodel.diffusion

from collections import Counter

class Cell():
    def __init__(self, x, y, z) -> None:
        self.__x = x
        self.__y = y
        self.__z = z
        self.__energy = 0
        self.__colorIndex = 0

        #self.__neighbourhood = [None for _ in range(26)]
        self.__neighbourhood = []


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
    def colorIndex(self):
        return self.__colorIndex
    @colorIndex.setter
    def colorIndex(self, colorIndex):
        self.__colorIndex = colorIndex

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

    def __hash__(self) -> int:
        return hash((self.__x, self.__y, self.__z))