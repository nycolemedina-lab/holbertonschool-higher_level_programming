#!/usr/bin/python3
"""
This module defines the function "to_json_string" that
returns the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """Converts an object into JSON representation.
    Args:
        my_obj: the object to convert.

    Return: JSON representation of an object.
    """
    return json.dumps(my_obj)
