#!/usr/bin/python3
if __name__ != "__main__":
    exit()
import sys

if len(sys.argv) == 1:
    print("0 arguments.")
    exit()
elif len(sys.argv) == 2:
    print("{} argument:".format(len(sys.argv) - 1))
else:
    print("{} arguments:".format(len(sys.argv) - 1))
for i in range(1, len(sys.argv)):
    print("{}: {}".format(i, sys.argv[i]))
