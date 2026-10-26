#!/usr/bin/python3
"""
This module defines a class BaseGeometry
"""


class BaseGeometry:
    """A class representing BaseGeometry with area and validation logic."""

    def area(self):
        """Calculate the area
        Raises:
            Exception: Indicates area() is not implemented yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer and its grater than 0
        Args:
            name: the name of the value
            value: the parameter value to validate

        Raise:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
