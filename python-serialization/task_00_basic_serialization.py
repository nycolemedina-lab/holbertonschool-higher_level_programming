#!/usr/bin/python3
"""
Module for serializing a Python dictionary to a JSON file
and deserializing a JSON file back into a Python dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python object to JSON and writes it to a file.
    If the output file already exists, it is overwritten.

    Args:
        data (dict): The Python dictionary containing data.
        filename (str): The path or name of the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Reads a JSON file and deserializes it back into a Python object.
    Args:
        filename (str): The path or name of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary from the file.
    """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
