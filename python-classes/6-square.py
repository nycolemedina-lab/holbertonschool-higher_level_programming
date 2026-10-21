#!/usr/bin/python3
"""
this module provides the square class
"""


class Square:
    """Represent a square shape

    """
    def __init__(self, size=0, position=(0, 0)):
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

        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not all (isintance(i, int) for i in position) or
                not all (i >= 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position


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

    @property
    def position(self):
        """return the current position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter for position
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all (i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculate the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """print the square
        """
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
