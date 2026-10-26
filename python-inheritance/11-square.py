#!/usr/bin/python3
"""
This module defines a class Square that inherits from the class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representing a square"""

    def __init__(self, size):
        """Initialize a new square instance
        Args:
            size: the size of the square sides
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculate the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return the printable string representation of the square"""
        return f"[Square] {self.__size}/{self.__size}"
