#!/usr/bin/python3
"""contains function island_perimeter"""


def island_perimeter(grid):
    """
    returns the perimeter of the island represented by 1 in a see of 0's

    Args:
    grid (array of arrays): grid containing island and water

    Returns: perimeter of island
    """
    perimeter = 0

    # traverse matrix
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j]:  # check cell above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1]:  # check  cell to left
                    perimeter -= 2
    return perimeter
