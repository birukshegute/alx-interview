#!/usr/bin/python3
"""
Rotaing a matrix 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2d matrix 90 degree clockwise
    """
    for i, j in enumerate(zip(*reversed(matrix))):
        matrix[i] = list(j)
