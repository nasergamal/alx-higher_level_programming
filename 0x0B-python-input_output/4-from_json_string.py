#!/usr/bin/python3
'''Json representation of strings'''
import json


def from_json_string(my_str):
    '''return an object'''
    return json.loads(my_str)
