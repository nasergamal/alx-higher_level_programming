#!/usr/bin/python3

if __name__ != "__main__":
    exit()
from calculator_1 import add, sub, mul, div
import sys
if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
if sys.argv[2] not in "+-*/":
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
a, b, c = int(sys.argv[1]), int(sys.argv[3]), sys.argv[2]
if c == "+":
    print("{} + {} = {}".format(a, b, add(a, b)))
if c == "-":
    print("{} - {} = {}".format(a, b, sub(a, b)))
if c == "*":
    print("{} * {} = {}".format(a, b, mul(a, b)))
if c == "/":
    print("{} / {} = {}".format(a, b, div(a, b)))
