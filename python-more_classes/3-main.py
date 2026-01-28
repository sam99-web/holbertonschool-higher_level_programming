#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

myrectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(myrectangle.area(), myrectangle.perimeter()))
print(str(myrectangle))
print(repr(myrectangle))

print("--")

myrectangle.width = 10
myrectangle.height = 3
print(str(myrectangle))
print(repr(myrectangle))
