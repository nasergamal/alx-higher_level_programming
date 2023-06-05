#!/usr/bin/python3
'''nqueen challenge'''
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    s = int(sys.argv[1])
except ValueError as e:
    print("N must be a number")
    exit(1)
if s < 4:
    print("N must be at least 4")
    exit(1)

newlist = []
for i in range(1, s - 1):
    y = i
    for n in range(s):
        temp = [n, y]
        newlist.append(temp)
        temp = []
        y += i + 1
        if y >= s:
            y = y - s - 1 if (y - s - 1) >= 0 else 0
    print(newlist)
    newlist = []
