'''File that contains unique color class in model'''
import KMCmodel.color
import numpy as np

class UniqueColor():
    '''Class representing unique color in model'''
    def __init__(self) -> None:
        '''Init method creating new unique color object with empty color array'''
        self.__colors = np.empty([1,0],dtype=KMCmodel.color.Color)

    def getColorAtIndex(self,index):
        '''Method returns color under given index'''
        return self.__colors[index]

    def getIndexOfColor(self,given_color):
        '''2 metody 1 własna druga numpy sprawdzić poprawność działania i wydajność'''

        #metoda pierwsza
        '''index = 0
        for color in self.__colors:
            if color == given_color: return index
            index+=1'''

        #metoda druga
        index = np.where(self.__colors == given_color)
        if len(index[0]) > 0: return index[0][0]
        else: return False
    
    def uniqueColor(self):
        '''Method creates unique transparent color.'''
        transparent = KMCmodel.color.Color(np.ubyte(0), np.ubyte(0), np.ubyte(0))
        self.__colors = np.append(self.__colors, transparent)

    def getNewColor(self) -> int:
        '''Method creating new random color.'''
        RGB = np.ndarray([3],dtype=np.ubyte)
        A = np.ubyte(-1)

        RGB[0] = np.random.randint(0,255)
        RGB[1] = np.random.randint(0,255)
        RGB[2] = np.random.randint(0,255)

        new_color = KMCmodel.color.Color(RGB,A)
        self.__colors = np.append(self.__colors, new_color)

        return self.__colors.size
