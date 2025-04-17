#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    Returns empty list if n <= 0
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with first row

    for i in range(1, n):
        # Get the previous row
        prev_row = triangle[-1]
        # Start new row with 1
        current_row = [1]

        # Calculate middle values
        for j in range(1, i):
            current_row.append(prev_row[j-1] + prev_row[j])

        # End row with 1
        current_row.append(1)
        
        # Add row to triangle
        triangle.append(current_row)

    return triangle
