#!/usr/bin/python3
"""this is a function that multiplies 2 matrices by using the module NumPy"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """this is a function that multiplies 2 matrices by using the module NumPy
    Args:
        m_a: the first matrix
        m_b: the second matrix
    """
    return (np.matmul(m_a, m_b))
