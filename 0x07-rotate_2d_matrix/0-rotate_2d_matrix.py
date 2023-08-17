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
            top, bottom = left, right
            # save topleft  value
            topLeft = matrix[top][left + i]
            # move bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]
            # move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # move top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            # move top left to top right
            matrix[top + i][right] = topLeft
        right -= 1
        left += 1
