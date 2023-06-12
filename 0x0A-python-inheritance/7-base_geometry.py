#!/usr/bin/python3
"""defining BaseGeometry class for subsuqent tasks"""


class BaseGeometry:
    """start of  BaseGeometry class"""

    def area(self):
        """to be added to instance: area calculation"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer check function to validate type"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
