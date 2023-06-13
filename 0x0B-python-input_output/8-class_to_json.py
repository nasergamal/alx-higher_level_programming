#!/usr/bin/python3
'''description returning function'''


def class_to_json(obj):
    '''return dictionary description for JSON serialization of an object'''
    return obj.__dict__
