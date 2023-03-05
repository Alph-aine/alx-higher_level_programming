#!/usr/bin/python3
"""
    Module 2-matrix_divided.py- contains program to divide all of a matrix
    -with a provided number and returns a new_matrix, to 2 decimal places
"""


def matrix_divided(matrix, div):
    if not isintance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(msg)

    new_matrix = []
    samelen = len(matrix[0])

    for rows in matrix:
        if type(rows) is not list:
            raise TypeError(msg)
        if len(rows) != samelen:
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for i in rows:
            if not isintance(i, (int, float)):
                raise TypeError(msg)
            new_list.append(round(i/div, 2))
        new_matrix.append(new_list)
    return new_matrix
