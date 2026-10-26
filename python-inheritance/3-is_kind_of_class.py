#!/usr/bin/python3
"""
This module defince the function is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of, or inherited from, a class.

    Args:
        obj: the object to check.
        a_class: the class to check against.

    Returns: True if obj is an instance or
    inherited instance of a_class; else False.

    """
    return isinstance(obj, a_class)
