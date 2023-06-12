#!/usr/bin/python3
'''Inheritance check'''


def inherits_from(obj, a_class):
    '''check for ineheritance'''
    return issubclass(type(obj), a_class) and type(obj) != a_class
