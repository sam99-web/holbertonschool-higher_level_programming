#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        s = ord(str[i])
        if s >= 97 and s <= 122:
            s = s - 32
        print("{}".format(chr(s)), end="")
    print()
