#!/usr/bin/python3

"""Defines pascal_triangle function"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing
    the Pascal’s triangle of n:
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    t = [1]
    k = pascal_triangle(n-1)
    for i in range(n-2):
        t.append((k[-1][i] + k[-1][i+1]))
    t.append(1)
    k.append(t)
    return k
