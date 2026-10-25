#!/usr/bin/python3
"""
this module defines a class rectangle
"""


class Rectangle:
    """Represent a square shape
    """
    number_of_instance = 0

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle
        Args:
            width: the width of the rectanglr
            height: the height of the rectaglr
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """returns current width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns current height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate the area of the rectagle
        """
        return self.__width * self.__height

    def perimeter(self):
        """calculate the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns a string representing a rectangle using "#"
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_lines = []
        for _ in range(self.__height):
            rect_lines.append("#" * self.__width)

        return "\n".join(rect_lines)

    def __repr__(self):
        """returns a string
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """delete an instance of a rectangle, and update the instance count
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
