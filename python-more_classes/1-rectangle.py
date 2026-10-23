#!/usr/bin/python3
"""
this module defines a class rectangle
"""


class Rectangle:
    """Represent a square shape
    """
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle
        Args:
            width: the width of the rectanglr
            height: the height of the rectaglr
        """
        self.__width = width
        self.__height =height

    @property
    def width(self):
        """returns current width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width
        """
        if not isintance(value, int):
            raise TypeError("width must be an integer")
        if int(value) < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    @property
    def height(self):
        """returns current height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height
        """
        if not isintance(value, int):
            raise TypeError("height must be an integer")
        if int(value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

