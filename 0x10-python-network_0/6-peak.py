#!/usr/bin/python3
"""finding peak in an unsorted array """


def find_peak(list_of_integers):
    """find peak"""
    if not list_of_integers:
        return None
    start, h = 0, len(list_of_integers)
    if h < 3:
        return max(list_of_integers)
    mid = h // 2
    if (list_of_integers[mid] > list_of_integers[mid - 1]
            and list_of_integers[mid] > list_of_integers[mid + 1]):
        return list_of_integers[mid]
    elif (list_of_integers[mid] < list_of_integers[mid - 1]):
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid:])
