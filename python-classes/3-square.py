#!/usr/bin/python3
"""
This module defines a Square class.
"""
class Square:
    """
    This class defines a square with a private size attribute.
    """

    def __init__(self, size=0):
        """
        Initialise a new Square instance.

        Args:
        size (int) the size of the square.

        Raise:
        TypeError (size must be an integer)
        ValueError (size must be >=0)
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size <0:
            raise ValueError("size must be >=0")
        self.__size = size        

    """ Public intance methode that return the square area."""
    def area(self):
        return self.__size ** 2
