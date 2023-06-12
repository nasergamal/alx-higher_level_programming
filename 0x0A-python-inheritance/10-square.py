#!/usr/bin/python3
'''multi iinheritance'''
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    '''square calc'''
    def __init__(self, size):
        '''initialization

        args:
            size (int): square's size
        '''
        super().integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
