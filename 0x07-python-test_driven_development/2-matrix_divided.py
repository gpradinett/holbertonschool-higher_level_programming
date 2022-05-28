#!/usr/bin/python3
"""
this module divide all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Funtion Divide all elements of a matrix
    """

    new_matrix = []
    new_matrix2 = []

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for i in matrix:
        if len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")

        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    for i in matrix:
        try:
            if len(i) != len(matrix[1]):
                raise TypeError("Each row of the matrix must have " +
                                "the same size")
        except IndexError:
            break

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in matrix:
        for j in i:
            new_matrix2.append(round(j / div, 2))

        new_matrix.append(new_matrix2)
        new_matrix2 = []

    return new_matrix
