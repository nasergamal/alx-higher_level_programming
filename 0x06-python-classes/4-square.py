#!/usr/bin/python3
'''Empty class'''


class Square:
    '''Square class'''
    def __init__(self, size=0):
        '''initialization

        Args:
            size (int): square size
        '''
        Square.check(size)
        self.__size = size

    @property
    def size(self):
        '''return square size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''set square size'''
        Square.check(value)
        self.__size = value

    def check(size):
        '''check for invalid type/value in size'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''return square area'''
        return self.__size ** 2
