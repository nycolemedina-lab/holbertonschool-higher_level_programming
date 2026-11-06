#!/usr/bin/python3
"""
This module defines the function "pascal_triangle" that returns
a list of lists of integers representing the Pascal's triangle of n:
"""


def pascal_triangle(n):
    """Creat tha list of integers."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        # Start each new row with 1
        current_row = [1]

        # Calculate middle values by summing adjacent elements from the previous row
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        # End each row with 1
        current_row.append(1)
        triangle.append(current_row)

    return triangle
