#!/usr/bin/python3

def add_integer(a, b=98):
    """ 
    this module provides a fonction to add two integers.

    Adds two integers and returns the result.
     
    Args:
        a: the first integer (int or float)
        b: the second integer (int or float)
    Returns:
        the sum of a and b as an integer

    Raises:
        TypeError: if a or b is not an integer or float
    """
    
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    
    return a + b
