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

    def __str__(self):
        '''return rectangle dimenstions'''
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        '''return rectangle area'''
        return self.__width * self.__height
