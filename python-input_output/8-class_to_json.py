#!/usr/bin/python3
"""
This module defines the function "class_to_json" that returns the
dictionary representation of a class instance for JSON serialization.
"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure

    for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary representation of obj's attributes.
    """
    return obj.__dict__
