#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    else:
        for row in matrix:
            if len(row) == 0:
                print()
            for col in row:
                print("{:d}".format(col), end=" " if col != row[-1] else "\n")
