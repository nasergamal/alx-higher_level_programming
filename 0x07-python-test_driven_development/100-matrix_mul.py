#!/usr/bin/python3
'''matrces multiplication'''


def matrix_mul(m_a, m_b):
    '''multiplies two matrices

    Args:
        m_a (list): list of lists
        m_b (list): list of lists

    raise:
        TypeError: if matrix is empty var or not list in list
        TypeError: items in lists not int/float
        TypeError: if matrix rows not equal
        ValueError: if the 2 matrices can't be multiplied

    return:
        a matrix with the results
    '''
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(n, (int, float)) for i in m_a for n in i):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(n, (int, float)) for i in m_b for n in i):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("if len(m_a[0]) != len(m_b):")
    newmatrix = []
    newlist = []
    for i in range(len(m_a)):
        newlist = []
        a = 0
        for length in range(len(m_b[0])):
            for n in range(len(m_b)):
                a += m_a[i][n] * m_b[n][length]
            newlist.append(a)
            a = 0
        newmatrix.append(newlist)
    return newmatrix
