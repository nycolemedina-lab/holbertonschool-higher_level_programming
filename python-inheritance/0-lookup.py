#!/usr/bin/python3
"""
This module contains a function that returns the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj: the object to inspect.

    Returns:
        list: a lis of strings containing the attributes and methods.
    """
    return dir(obj)
