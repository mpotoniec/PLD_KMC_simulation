'''Flie that contains abstract class of event'''

class Event():
    '''Class representing events in program'''
    def __init__(self) -> None:
        self.__probability = None

    @property
    def probability(self):
        return self.__probability

    @probability.setter
    def probability(self, probability):
        self.__probability = probability