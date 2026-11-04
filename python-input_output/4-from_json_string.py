#!/usr/bin/python3
"""
This module defines the function "from_json_string" that
deserializes a JSON string into a Python object.
"""
import json


def from_json_string(my_str):
    """Deserializes a JSON string into a Python data structure.

    Args:
        my_str: The JSON string representation to deserialize.

    Returns:
        object: The Python data structure represented by my_str.
    """
    if my_str is None or my_str == "":
        return []
    return json.loads(my_str)
