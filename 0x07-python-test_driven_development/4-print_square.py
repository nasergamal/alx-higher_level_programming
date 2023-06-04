#!/usr/bin/python3
'''print square function'''


def print_square(size):
    '''define printing square function
    Args:
        size (int): square size

    Raise:
        TypeError; if size is not int
        ValueError: if size is less than 0
    '''

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        [print("#", end="")for n in range(size)]
        print()
