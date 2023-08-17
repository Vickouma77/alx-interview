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
    left, right = 0, n - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # Save top left value
            topLeft = matrix[top][left + i]
            # Move bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]
            # Move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # Move top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            # Move top left to top right
            matrix[top + i][right] = topLeft
        right -= 1
        left += 1
