#!/usr/bin/python3
'''File reading function'''


def read_file(filename=""):
    '''open and print file content to stdout'''
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
