#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    new_matrix = []
    for rows in matrix:
        new_matrix.append(list(map(lambda n: n * n, rows)))
    return new_matrix
