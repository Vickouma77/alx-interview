#!/usr/bin/env python3
"""Rotate 2d matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise in-place.
    
    This function takes a 2D matrix as input and modifies it in-place by rotating
    the elements 90 degrees clockwise.
    
    :param matrix: The n x n 2D matrix to be rotated.
    :type matrix: List[List[int]]
    :return: None (The matrix is modified in-place)
    
    Example:
    >>> matrix = [[1, 2, 3],
    ...           [4, 5, 6],
    ...           [7, 8, 9]]
    >>> rotate_2d_matrix(matrix)
    >>> print(matrix)
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
