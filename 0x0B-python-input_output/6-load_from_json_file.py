#!/usr/bin/python3
'''load json representation from file'''
import json


def load_from_json_file(filename):
    '''create an object from json file'''
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
