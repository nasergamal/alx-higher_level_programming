#!/usr/bin/python3
'''appending file to a list in json file'''
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    items = load_from_json_file('add_item.json')
except Exception as e:
    items = []
items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")
