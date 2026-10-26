#!/usr/bin/python3
"""
This module defines the class MyList
"""


class MyList(list):
    """A custom list class that extends built-in list functionality."""

    def print_sorted(self):
        """Print the elements of the list in sorted ascending order."""
        print(sorted(self))
