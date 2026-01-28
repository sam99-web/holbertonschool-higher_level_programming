#!/usr/bin/python3
"""
This module contains the definition of class 'Rectangle'
"""

class Rectangle:
    """
    Class to define a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        __init__ Constructor to build the instance

        Args:
            width (int, optional): Rectangle width. Defaults to 0.
            height (int, optional): Rectangle height. Defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        width Get the width of the rectangle

        Returns:
            int: size of the rectangle (width length)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width Define the width of the rectangle

        Args:
            value (int): size of the rectangle (width length)

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        height Get the height of the rectangle

        Returns:
            int: size of the rectangle (height length)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height Define the height of the rectangle

        Args:
            value (int): size of the rectangle (height length)

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


    def area(self):
        """
        Compute and return the area of the rectangle.

        Returns:
            int: Area (width * height)
        """
        return self.width * self.height

    def perimeter(self):
        """
        Compute and return the perimeter of the rectangle.

        Returns:
            int: Perimeter (2 * (width + height)), or 0 if width or height is 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
