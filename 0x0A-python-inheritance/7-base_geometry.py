#!/usr/bin/python3
'''Still empty'''


class BaseGeometry:
    '''placeholder'''

    def area(self):
        '''to be added: area calculation'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''int checke'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
