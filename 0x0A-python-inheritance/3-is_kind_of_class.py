#!/usr/bin/python3
'''check if object is inhert or from same class'''


def is_kind_of_class(obj, a_class):
    '''check if the 2 arguments are related'''
    return (type(obj).__name__ == a_class.__name__)
