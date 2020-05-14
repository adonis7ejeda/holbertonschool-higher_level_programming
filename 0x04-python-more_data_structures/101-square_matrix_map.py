#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return(list(map(lambda _: list(map(lambda x: x**2, _)), matrix)))
