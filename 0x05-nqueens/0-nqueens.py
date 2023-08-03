#!/usr/bin/env python3
""" N queens problem """

import sys


def printBoard(board):
    """ Print board """
    for row in board:
        print(row)


def isSafe(board, row, col):
    """ Check if a queen can be placed on board[row][col] """
    for c in range(col):
        if board[row][c] == 1:
            return False
    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False
    for r, c in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False
    return True


def solveNQUtil(board, col):
    """ Solve N queen problem """
    if col == len(board):
        printBoard(board)
        return True
    res = False
    for row in range(len(board)):
        if isSafe(board, row, col):
            board[row][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[row][col] = 0
    return res


def solveNQ(n):
    """ Solve N queen problem """
    if n < 4:
        print("N must be at least 4")
        return False
    board = [[0 for i in range(n)] for j in range(n)]
    solveNQUtil(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solveNQ(n)

