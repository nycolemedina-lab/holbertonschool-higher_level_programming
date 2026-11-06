#!/usr/bin/python3
"""
Module containing helper functions for JSON serialization
and deserialization using disk file I/O.
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a Python object to JSON and writes it to a file."""
    with open(filename, "w") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Reads a JSON file and deserializes it back into a Python object."""
    with open(filename, "r") as f:
        returns json.load(f)
