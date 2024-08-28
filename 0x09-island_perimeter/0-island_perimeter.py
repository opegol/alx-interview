#!/usr/bin/python3

"""Function calculates the perimeter of an island of square blocks"""


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid
        grid is a list of list of integers
        0 represents a water zone
        1 represents a land zone
        One cell is a square with side length 1.

    Args:
        grid (list): list of lists representing a rectangular block.

    Returns:
        perimeter of the connected land.
    """

    x = len(grid[0])
    y = len(grid)
    perim = 0
    ng = []
    for i in range(y + 2):
        g = []
        for j in range(x + 2):
            if (i == 0 or i == y + 1):
                g.append(0)
            elif (j == 0 or j == x + 1):
                g.append(0)
            else:
                g.append(grid[i-1][j-1])
        ng.append(g)
    for i in range(y):
        for j in range(x):
            if ng[i+1][j+1] == 1:
                zeros = (4 - (ng[i][j+1] + ng[i+2][j+1]
                         + ng[i+1][j] + ng[i+1][j+2]))
                perim += zeros
    return perim
