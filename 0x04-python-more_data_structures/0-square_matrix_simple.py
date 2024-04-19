#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """_summary_

    Args:
        matrix (list).

    Returns:
        _type_: new_matrix : the results of  multiplying each element in matrix.
    """
    new_matrix = [0] * len(matrix)
    if len(matrix) == 0:
        return new_matrix
    for i in range(0, len(matrix)):
        for j in range(0, i):
            new_matrix[i][j] = matrix[i][j] * matrix[i][j]
    
    return new_matrix
