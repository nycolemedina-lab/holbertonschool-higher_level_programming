#!/usr/bin/python3
"""
This module provides the 'print_square' function.
It prints a square with the `#` character based on the given size.
"""


def print_square(size):
    """Prints a square with '#'
    Args:
        size: The height and width of the square.
    Raises:
        TypeError: If size is not an integer or if size is a float < 0.
        ValueError: If size is an integer < 0.
"""
# Catch float < 0 specifically to raise TypeError per project requirements
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Exclude booleans explicitly since bool inherits from int in Python
    if not isinstance(size, int) or type(size) is bool:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
