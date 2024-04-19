#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """_summary_

    Args:
        matrix (list).

    Returns:
        _type_: new_matrix : the results of  multiplying each element in matrix.
    """
    new_matrix = []
    if len(matrix) == 0:
        return new_matrix

    new_matrix = [[i*i for i in j] for j in matrix]
    return new_matrix
