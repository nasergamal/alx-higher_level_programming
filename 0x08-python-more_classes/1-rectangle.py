#!/usr/bin/python3
'''rectangle class'''


class Rectangle:
    '''Rectangle class

    Args:
        width (int): rectangle width
        height (int): rectangle height

    Raise:
        TypeError: if width or height is not int
        ValueError: if width or height is less than 0
    '''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Return width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Return height'''
        return self.__height

    @width.setter
    def height(self, value):
        '''Set height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
