#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance of
a class that inherited (directly or indirectly) from a specified class.
"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited from a_class.

    Args:
        obj: The object to inspect.
        a_class: The base class to check against.

    Returns:True if obj's class is a subclass of a_class, otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
