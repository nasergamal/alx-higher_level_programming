#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 1:
        [print("{:d}".format(i[n]), end=' ' if n < (len(i) - 1)
               else "\n") for i in matrix for n in range(len(i))]
    else:
        print()
