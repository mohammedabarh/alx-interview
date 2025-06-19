#!/usr/bin/python3
"""
Island Perimeter module
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    
    Args:
        grid (list of list): 2D grid where:
            - 0 represents water
            - 1 represents land
    
    Returns:
        int: The perimeter of the island
    """
    if not grid:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # For each land cell, start with 4 sides
                perimeter += 4
                
                # Check cell above if it exists and is land
                if i > 0 and grid[i-1][j] == 1:
                    # Subtract 2 for the shared edge (1 from current cell, 1 from above cell)
                    perimeter -= 2
                    
                # Check cell to the left if it exists and is land
                if j > 0 and grid[i][j-1] == 1:
                    # Subtract 2 for the shared edge (1 from current cell, 1 from left cell)
                    perimeter -= 2

    return perimeter
