#!/usr/bin/python3
"""
module contains function rotate_2d_matrix that rotates a 2D matrix
"""

def rotate_2d_matrix(matrix):
    """
    rotates a 2D matrix
    """
    # transpose
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse
    for i in range(len(matrix)):
        matrix[i].reverse()
