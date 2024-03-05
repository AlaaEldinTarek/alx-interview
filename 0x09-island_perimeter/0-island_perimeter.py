#!/usr/bin/python3
"""
Function to determine a perimeter in a grid
"""


def island_perimeter(grid):
    """
    Search land cell and counts the water cells around it
    """
    LAND = 1
    WATER = 0
    perimeter = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == LAND:
                # print("land in [x= {:d} y= {:d}]".format(x, y))
                # left
                if y == 0 or grid[y - 1][x] == WATER:
                    perimeter += 1
                # right
                if y == len(grid) - 1 or grid[y + 1][x] == WATER:
                    perimeter += 1
                # up
                if x == 0 or grid[y][x - 1] == WATER:
                    perimeter += 1
                # down
                if x == len(row) - 1 or grid[y][x + 1] == WATER:
                    perimeter += 1
    return perimeter
