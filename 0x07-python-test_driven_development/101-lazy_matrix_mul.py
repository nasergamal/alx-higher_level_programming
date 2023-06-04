#!/usr/bin/python3
'''numpy'''
import numpy


def lazy_matrix_mul(m_a, m_b):
    '''matrix multiplication using numpy
    Args:
        m_a (list): 1st array
        m_b (list): 2nd array
    '''
    return numpy.matmul(m_a, m_b)
