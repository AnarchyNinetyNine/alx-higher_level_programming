#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return None
    new_matrix = [list(map(lambda x: x * x, row)) for row in matrix]
    return new_matrix
