#!/usr/bin/python3
def uppercase(str):
    for c in str:
        # If character is lowercase, convert to uppercase
        if 97 <= ord(c) <= 122:
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()
