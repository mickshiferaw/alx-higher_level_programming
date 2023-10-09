#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for inMatrix in matrix:
        if len(inMatrix) < 1:
            print()
        for x in range(len(inMatrix)):
            print('{:d}'.format(inMatrix[x]),
                  end='\n' if x is len(inMatrix) - 1 else ' ')
