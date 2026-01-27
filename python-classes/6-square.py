#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    # ---------- size ----------
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    # ---------- position ----------
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not isinstance(value[0], int) or
            not isinstance(value[1], int) or
            value[0] < 0 or
            value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    # ---------- area ----------
    def area(self):
        return self.__size ** 2

    # ---------- my_print ----------
    def my_print(self):
        if self.__size == 0:
            print()
            return

        # position[1] = nombre de lignes vides avant le carré
        for i in range(self.__position[1]):
            print()

        # impression du carré
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
