#!/usr/bin/python3
'''add attributes to object'''


def add_attribute(a, b, c):
    '''add_attribute function'''
    if not hasattr(a, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(a, b, c)
