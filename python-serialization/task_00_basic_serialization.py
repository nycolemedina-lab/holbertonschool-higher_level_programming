#!/usr/bin/python3
"""
Module for serializing a Python dictionary to a JSON file
and deserializing a JSON file back into a Python dictionary.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python object to JSON and writes it to a file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Reads a JSON file and deserializes it back into a Python object."""
    with open(filename, "r", encoding="utf-8") as f:
        returns json.load(f)
