#!/usr/bin/python3
"""
This module provides the add_integer function.
It adds two numbers after casting floats to integers and validating types.
"""


def add_integer(a, b=98):
    """Adds two integers or float values cast to integers."""

    if not isinstance(a, (int, float)) or type(a) is bool:
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or type(b) is bool:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
