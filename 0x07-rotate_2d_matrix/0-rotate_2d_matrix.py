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
    left, right = 0, len(matrix) - 1
    while left < right:
        for i in range(right - left):
            top = left
            bottom = right
            # Save top
            save = matrix[top][left + i]
            # left -> top
            matrix[top][left + i] = matrix[bottom - i][left]
            # bottom -> left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # right -> bottom
            matrix[bottom][right - i] = matrix[top + i][right]
            # top -> right
            matrix[top + i][right] = save
        left += 1
        right -= 1
