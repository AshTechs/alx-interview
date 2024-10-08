#!/usr/bin/python3
"""
Rotate a 2D matrix by 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate the given n x n 2D matrix by 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): The matrix to rotate.

    Returns:
        None: The matrix is modified in place.
    """
    # Transpose the matrix
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
