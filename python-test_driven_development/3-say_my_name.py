#!/usr/bin/python3
"""
This module provides the "say_my_name" function.
Prints the string pass to the function
"""


def say_my_name(first_name, last_name=""):
    """Prints "My name is" followed by first_name, last_name
    Args:
        first_name: first string to print
        last_name: second string to print
    Returns:
        void
    Raises:
        TypeError: if first_name or last_name are not strings
"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
