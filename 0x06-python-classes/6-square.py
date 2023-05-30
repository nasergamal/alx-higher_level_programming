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
        Square.check(size)
        self.__size = size
        self.__position = position

    @property
    def size(self):
        '''return square size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''return square size'''
        Square.check(value)
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

    def check(size):
        '''check for invalid type/value in size'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        '''return square area'''
        return self.__size ** 2

    def my_print(self):
        '''
        print a square based on the size using # as filler
        and preceded by space based on position value
        '''
        if self.__size == 0:
            print("")
            return
        [print("") for m in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for m in range(0, self.__position[0])]
            [print("#", end="") for n in range(0, self.__size)]
            print("")
