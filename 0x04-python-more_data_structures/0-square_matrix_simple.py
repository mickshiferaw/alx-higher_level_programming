#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copymat = matrix.copy()
    for z in range(len(matrix)):
        copymat[z] = list(map(lambda x: x**2, matrix[z]))
    return (copymat)
