#!/usr/bin/python3
'''content writing function'''


def write_file(filename="", text=""):
    '''write content into file'''
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
