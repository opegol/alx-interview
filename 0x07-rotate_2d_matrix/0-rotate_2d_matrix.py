#!/usr/bin/python3

"""Given an n x n 2D matrix, rotate it 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise in-place.
    """
    # mat = [[matrix[i][j] for i in range(len(matrix))]
    # for j in range(len(matrix[0]))]
    lm = len(matrix)
    m = int(lm / 2)
    for i in range(lm):
        for j in range(i, lm):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        for i in range(m):
            tmp = row[i]
            row[i] = row[lm-i-1]
            row[lm-i-1] = tmp
