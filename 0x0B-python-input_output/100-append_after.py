#!/usr/bin/python3
'''appending mid file'''


def append_after(filename="", search_string="", new_string=""):
    '''append given string whenever a string match required string'''
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    li = ""
    for line in lines:
        li += line
        if search_string in line:
            li += new_string
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(li)
