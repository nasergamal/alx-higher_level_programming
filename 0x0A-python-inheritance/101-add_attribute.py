#!/usr/bin/python3
'''add attributes to object'''


def add_attribute(a, b, c):
    '''add_attribute function'''
    if type(a).__module__ == 'builtins':
        raise TypeError("can't add new attribute")
    setattr(a, b, c)
