#!/usr/bin/python3
"""
This module provides the add_integer function.
It adds two numbers after casting floats to integers and validating types.
"""


def add_integer(a, b=98):
    """Adds two integers or float values cast to integers.

    Args:
        a: First number (int or float).
        b: Second number (int or float, defaults to 98).

    Returns:
        int: The integer addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float, or if a/b is a boolean.
        OverflowError: If a float argument is infinity or too large to convert.
    """

    if not isinstance(a, (int, float)) or type(a) is bool:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or type(b) is bool:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
