#!/usr/bin/python3
'''inherting from BaseGeometry class'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle calc class'''
    def __init__(self, width, height):
        '''initializing

        Args:
            width (int): rectangle widht
            height (int): ectangle height
        '''
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height
