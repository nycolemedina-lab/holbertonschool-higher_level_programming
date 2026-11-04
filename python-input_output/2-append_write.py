#!/usr/bin/python3
"""
This module defines the function 'append_write' that appends string
at the end of a text file and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Writes the 'text' at the end of 'filename'.
    Args:
        filename: the file to be added to.
        text: the text to add to 'filename'.
    Return: the number of characters that was added.
    """
    with open(filename, "a") as f:
        f.write(text)
    return len(text)
