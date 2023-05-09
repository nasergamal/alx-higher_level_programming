#!/usr/bin/python3

for i in range(10):
    for n in range(10):
        if n < i or n == i:
            continue
        if (i == 8 and n == 9):
            print(f'{i}{n}')
            break
        print(f'{i}{n}', end=", ")
