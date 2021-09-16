#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    z = []
    for j in matrix:
        y = []
        for x in j:
            y.append(x*x)
        z.append(y)
    return z
