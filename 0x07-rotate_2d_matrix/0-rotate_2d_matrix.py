#!/usr/bin/env python3
"""Rotate 2d matrix
"""


def rotate_2d_matrix(matrix: list) -> None:
    """
    Rotate a given n x n 2D matrix 90 degrees clockwise in-place.
    This function takes a 2D matrix as input and modifies
    it in-place by rotating the elements 90 degrees clockwise.
    :param matrix: The n x n 2D matrix to be rotated.
    :type matrix: List[List[int]]
    :return: None (The matrix is modified in-place)
    """
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
