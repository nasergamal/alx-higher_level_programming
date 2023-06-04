#!/usr/bin/python3
'''matrix division'''


def matrix_divided(matrix, div):
    '''divide given matrix by a given value

    Args:
        matrix (list): list of lists
        div (int/float): divisor

    raise:
        TypeError: if matrix is empty var or not list in list
        TypeError: items in lists not int/float
        TypeError: if matrix rows not equal
        TypeError: if divisor is not int/float
        ZeroDivisionError: if div == 0

    return:
        a matrix with the results
    '''
    if (not matrix or
       not isinstance(matrix, list)
       or not all(isinstance(i, list) for i in matrix)
       or not all(isinstance(n, (int, float)) for i in matrix for n in i)):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    newmatrix = [[round(n / div, 2) for n in i] for i in matrix]
    return newmatrix
