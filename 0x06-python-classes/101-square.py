#!/usr/bin/python3
'''Empty class'''


class Square:
    '''Square class'''
    def __init__(self, size=0, position=(0, 0)):
        '''initialization

        Args:
            size (int): square size
            position (int, int): square position
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''return square size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''set square size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        '''return square position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''set square position'''
        if (len(value) != 2 or not isinstance(value, tuple)
                or not isinstance(value[0], int) or
                not isinstance(value[1], int)
                or value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        '''return square area'''
        return self.__size ** 2

    def sqr(self):
        '''make a printable copy of square'''
        if self.__size == 0:
            return "\n"
        sqr = ""
        for m in range(self.__position[1]):
            sqr += '\n'
        for i in range(self.__size):
            for b in range(self.__position[0]):
                sqr += " "
            for n in range(self.__size):
                sqr += "#"
            sqr += "\n"
        return sqr

    def __str__(self):
        return self.sqr()[:-1]

    def my_print(self):
        '''
        print a square based on the size using # as filler
        and preceded by space based on position value
        '''
        print(sqr(), end="")
