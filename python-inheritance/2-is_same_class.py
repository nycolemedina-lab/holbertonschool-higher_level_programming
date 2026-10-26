#!/usr/bin/python3
"""
This module defines the function is_same_class the returns true if an object is
an instance of a class or flase otherwise.
"""


def is_same_class(obj, a_class):
    """Check is an object is an instance of a specified class

    Args:
        obj: the object to check
        a_class: the class to check in
    Returns:
        True: if the object is from the class
        False: if the object is not from the class
    """
    return type(obj) is a_class
