#!/usr/bin/python3
"""
This module provides the `text_indentation` function.
It prints text with two new lines after every `.`, `?`, and `:` character,
stripping leading and trailing spaces on each formatted line.
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Flag to skip spaces at the beginning of each printed line
    skip_space = True

    for char in text:
        if skip_space and char == ' ':
            continue

        print(char, end="")
        skip_space = False

        if char in ['.', '?', ':']:
            print("\n")
            skip_space = True
