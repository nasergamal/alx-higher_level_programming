#!/usr/bin/python3
'''integer addition function'''


def add_integer(a, b=98):
    '''return the result of the addition of the values

       the values are typecasted to int before addition

       TypeError is raised if values are not int or float
       '''

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
