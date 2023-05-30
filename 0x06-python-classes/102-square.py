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
        if not isinstance(size, int) and not isinstance(size, float):
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''return square area'''
        return self.__size ** 2

    def __lt__(self, cmp):
        '''Comparison'''
        return (self.__size ** 2) < cmp.__size ** 2

    def __le__(self, cmp):
        '''Comparison'''
        return (self.__size ** 2) <= cmp.__size ** 2

    def __gt__(self, cmp):
        '''Comparison'''
        return (self.__size ** 2) > cmp.__size ** 2

    def __ge__(self, cmp):
        '''Comparison'''
        return (self.__size ** 2) >= cmp.__size ** 2

    def __eq__(self, cmp):
        '''Comparison'''
        return (self.__size ** 2) == cmp.__size ** 2

    def __ne__(self, cmp):
        '''Comparison'''
        return (self.__size ** 2) != cmp.__size ** 2
