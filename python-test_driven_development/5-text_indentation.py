#!/usr/bin/python3
"""
Module for text indentation.

This module contains a function that prints text with 2 new lines
after each of these characters: . ? :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text: The text to print (must be a string)

    Raises:
        TypeError: If text is not a string

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Start with empty result
    i = 0
    while i < len(text):
        # Print current character
        print(text[i], end="")
        
        # If we hit a special character, print 2 newlines
        if text[i] in '.?:':
            print("\n")
            
            # Skip any spaces after the special character
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        
        i += 1
