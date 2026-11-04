#!/usr/bin/python3
"""
this module defines the function 'read_file' that reads a file
and prints it to stdout
"""


def read_file(filename=""):
    """Read a file and print it to stdout

    Args:
        filename: file to read and print
    """
    with open("filename") as f:
        for line in f:
            print(line, end="")
