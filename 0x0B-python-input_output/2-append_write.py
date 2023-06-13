#!/usr/bin/python3
'''content writing function'''


def append_write(filename="", text=""):
    '''write content into file'''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
