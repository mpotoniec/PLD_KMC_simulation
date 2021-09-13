'''ads'''

class Size3D():
    '''asd'''
    def __init__(self,width,height,depth) -> None:
        '''asds'''
        self.__width = width
        self.__height = height
        self.__depth = depth

        self.__volume_size = self.__width * self.__height * self.__depth

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width
        self.__volume_size = self.__width * self.__height * self.__depth

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        self.__volume_size = self.__width * self.__height * self.__depth

    @property
    def depth(self):
        return self.__depth

    @depth.setter
    def depth(self, depth):
        self.__depth = depth
        self.__volume_size = self.__width * self.__height * self.__depth

    @property
    def volume_size(self):
        return self.__volume_size