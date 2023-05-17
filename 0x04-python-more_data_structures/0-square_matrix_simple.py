#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    return(list(map(lambda a: list(map(lambda b: b ** 2, a)), matrix)))
