#!/usr/bin/python3
"""
inheriting lists for MyList class
"""


class MyList(list):
    """defining My List class"""
    def __init__(self):
        """initialization of mylist instance"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
