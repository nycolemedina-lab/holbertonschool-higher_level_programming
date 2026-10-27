#!/usr/bin/python3
"""
This module defines an abstract base class 'Shape'
with concrete subclasses 'Circle' and 'Rectangle'.
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        ...

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        ...

class Circle(Shape):
    """Circle class inheriting from Shape."""

    def __init__(self, radius):
        """Initializes a new instance of Circle."""
        self.__radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return 3.1415 * (self.__radius ** 2)

    def perimeter(self):
        """Calculates the perimeter of the circle."""
        return 2 * 3.1415 * self.__radius

class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""

    def __init__(self, width, height):
        """Initializes a new instance of Rectangle."""
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)

def shape_info(shape):
    """Print the area and perimeter of the shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
