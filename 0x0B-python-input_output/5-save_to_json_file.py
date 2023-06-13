#!/usr/bin/python3
'''create a file with json representation'''
import json


def save_to_json_file(my_obj, filename):
    '''write into a file with json representation'''
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
