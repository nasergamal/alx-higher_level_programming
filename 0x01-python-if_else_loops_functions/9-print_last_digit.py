#!/usr/bin/python3

def print_last_digit(number):
    ld = number % 10
    if number < 0:
        ld = 10 - ld
    print(f'{ld}', end="")
    return ld
