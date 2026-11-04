#!/usr/bin/python3
"""
This module defines the function 'write_file' that writes a string
to a text file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Write text in the file and returns the number of characters written.
    Args:
        filename: The name of the file to write in.
        text: the text to write in the file.
    """
    with open(filename, "w") as f:
        f.write(text)
    return len(text)
