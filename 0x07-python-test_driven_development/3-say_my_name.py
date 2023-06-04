#!/usr/bin/python3
'''a function that print names'''


def say_my_name(first_name, last_name=""):
    '''say_my_name takes two arguments and print them

    Args:
        first_name (str): the first name
        last_name (str): last name (not obligatory)

    Raise:
        TypeError: if first_name or last_name not str

    Return:
        My name is <first name> <last name>
    '''
    if not first_name or not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
