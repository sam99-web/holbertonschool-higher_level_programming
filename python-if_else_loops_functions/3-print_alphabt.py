#!/usr/bin/python3

for i in range(26):
    if chr(97 + i) != 'q' and chr(97 + i) != 'e':
        print("{}".format(chr(97 + i)), end="")
