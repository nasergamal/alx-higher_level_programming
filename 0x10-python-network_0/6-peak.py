#!/usr/bin/python3
"""finding peak in an unsorted array """


def find_peak(list_of_integers):
    """find peak"""
    if not list_of_integers:
        return None
    return max(list_of_integers)
