#!/usr/bin/python3
"""
Module for printing names.

This module contains a function that prints a person's full name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first name> <last name>'.

    Args:
        first_name: The first name (must be a string)
        last_name: The last name (must be a string, default is "")

    Raises:
        TypeError: If first_name is not a string
        TypeError: If last_name is not a string

    Returns:
        None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print("My name is {} {}".format(first_name, last_name))
