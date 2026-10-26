#!/usr/bin/python3
"""
this module defins a class rectanglr that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using BaseGeometry validation"""
    def __init__(self, width, height):
        """initialize a new Rectangle instance
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        seld.integer_validator("height", height)
        self.__height = height
