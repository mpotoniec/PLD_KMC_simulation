'''File that contains basic color in model'''
import numpy as np

class Color():
    '''Class representing basic color in model'''
    def __init__(self,R,G,B,A) -> None:
        '''First init method that get four np.ubyte values R, G, B and A'''

        self.__R: np.ubyte = R
        self.__G: np.ubyte = G
        self.__B: np.ubyte = B
        self.__A: np.ubyte = A

    @property
    def R(self):
        return self.__R
    @R.setter
    def R(self,R):
        self.__R = R
    @property
    def G(self):
        return self.__G
    @G.setter
    def G(self,G):
        self.__G = G
    @property
    def B(self):
        return self.__B
    @B.setter
    def B(self,B):
        self.__B = B
    @property
    def A(self):
        return self.__A
    @A.setter
    def A(self,A):
        self.__A = A
        
    def __eq__(self, color: object) -> bool:
        '''Method check if two colors are equal'''
        if self.__R == color.R and self.__G == color.G and self.__B == color.B and self.__A == color.A: return True
        else: return False

    def __hash__(self) -> int:
        #return ((self.__R, self.__G, self.__B, self.__A))
        return 1

    def __str__(self) -> str:
        return (
        "Kolor o wartościach RGB: [R = "
        + str(self.__R) + ", G = "
        + str(self.__G) + ", B = "
        + str(self.__B) + "], A = "
        + str(self.__A))

#Do zrobienia ewentualny drugi konstruktor
#Ustalić czy przeciążenie == jest potrzebne
