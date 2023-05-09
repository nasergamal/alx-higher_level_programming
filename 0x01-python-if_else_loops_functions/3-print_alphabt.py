#!/usr/bin/python3

for i in range(97, 123):
    if chr(i) in "eq":
        continue
    print("{}".format(chr(i)), end="")
