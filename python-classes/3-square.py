#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        # Vérification du type
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        # Vérification de la valeur
        if size < 0:
            raise ValueError("size must be >= 0")
        # Attribut privé
        self.__size = size

    # Méthode publique pour calculer l'aire
    def area(self):
        return self.__size ** 2
