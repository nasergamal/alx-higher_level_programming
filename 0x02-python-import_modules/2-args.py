#!/usr/bin/python3
if __name__ != "__main__":
    exit()
import sys

if len(sys.argv) == 1:
    print("0 arguments.")
    exit()
print("{} arguments:".format(len(sys.argv) - 1))
for i in range(1, len(sys.argv)):
    print("{}: {}".format(i, sys.argv[i]))
