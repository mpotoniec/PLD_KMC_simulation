'''File with 3D point class'''

class Point3D():
    '''Class representing point 3D in space'''
    def __init__(self,x,y,z) -> None:
        self.__x = x
        self.__y = y
        self.__z = z
        
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self,y):
        self.__y = y

    @property
    def z(self):
        return self.__z
    
    @z.setter
    def z(self,z):
        self.__z = z