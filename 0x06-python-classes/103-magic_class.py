#!/usr/bin/python3
'''circle'''


class MagicClass:
    '''MagicClass'''
    def __init__(self, radius):
        '''initialization'''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        '''return area'''
        return ((self.__radius ** 2) * pi)

    def circumference(self):
        '''return circumference'''
        return (2 * pi * self.__radius)
