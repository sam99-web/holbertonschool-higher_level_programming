#!/usr/bin/python3

"""

Adds two intergers and returns the result.
 
 Args:
    a: the first interger (int or float)
    b: the second interger (int or float)
Returns:
    the sum of a and b as an interger

Raises:
    TypeError: if a or b is not an interger or float
"""

if not isinstance(a, (int, float)):
    raise TypeError("a must be an integer")
if not isinstance(b, (int, float)):
    raise TypeError("b must be an integer")

if isinstance(a, float):
    a = int (a)
if isinstance (b, float):
    b = int (b)
return a + b 