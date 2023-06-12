#!/usr/bin/python3
'''inheriting lists'''


class MyList(list):
    '''My List class'''
    def __init__(self):
        pass

    def print_sorted(self):
        print(sorted(self))
