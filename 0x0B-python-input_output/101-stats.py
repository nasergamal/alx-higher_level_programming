#!/usr/bin/python3
'''parsing data'''
from sys import stdin


def printcycle(size, ptstuff):
    '''print data'''
    print(f"File size: {size}")
    for k in sorted(ptstuff):
        print(f"{k}: {ptstuff[k]}")


size = 0
possible_code = ['200', '301', '400', '401', '403', '404', '405', '500']
c = 0
printable_stuff = {}
try:
    for line in stdin:
        li = line.split()

        try:
            size += int(li[-1])
        except Exception as e:
            pass
        if li[-2] in possible_code:
            if printable_stuff.get(li[-2], 0) == 0:
                printable_stuff[li[-2]] = 0
            printable_stuff[li[-2]] += 1

        if c == 9:
            c += 1
            printcycle(size, printable_stuff)
            c = 1
        else:
            c += 1
    printcycle(size, printable_stuff)
except KeyboardInterrupt:
    printcycle(size, printable_stuff)
    raise
