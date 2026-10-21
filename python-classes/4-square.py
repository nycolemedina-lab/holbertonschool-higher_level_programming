#!/usr/bin/python3
"""
this module provides the square class

"""


class Square:
    """Represent a square shape

    """
    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size: Side length of the square.
        Raises:
            TypeError: If size not an integer
            ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """return the current value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter for size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value


    def area(self):
        """calculate the area of the square
        """
        return self.__size ** 2
