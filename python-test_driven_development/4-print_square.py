#!/usr/bin/python3
"""
Module for printing squares.

This module contains a function that prints a square with the character #.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: The size length of the square (must be an integer >= 0)

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0

    Returns:
        None
    """
    # Check if size is a float (before checking if it's an int)
    # because isinstance(True, int) returns True in Python
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    
    # Check if size is less than 0
    if size < 0:
        raise ValueError("size must be >= 0")
    
    # Print the square
    for i in range(size):
        print("#" * size)
