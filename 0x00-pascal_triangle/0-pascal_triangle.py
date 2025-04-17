#!/usr/bin/python3
"""
Function that returns a list of lists of integers
representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
    Creates a list of lists of integers representing
    Pascal's triangle of n.
    """
    if n <= 0:
        return []

    pascal = [[1]]
    for i in range(n - 1):
        temp = [0] + pascal[-1] + [0]
        row = []
        for j in range(len(pascal[-1]) + 1):
            row.append(temp[j] + temp[j + 1])
        pascal.append(row)
    return pascal
