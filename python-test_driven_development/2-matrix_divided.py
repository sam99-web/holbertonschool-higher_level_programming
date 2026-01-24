>>> matrix_divided = __import__('2-matrix_divided').matrix_divided

# Test 1: Division normale d'une matrice
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

# Test 2: Vérifier que la matrice originale n'est pas modifiée
>>> matrix
[[1, 2, 3], [4, 5, 6]]

# Test 3: Division par 2
>>> matrix_divided([[10, 20], [30, 40]], 2)
[[5.0, 10.0], [15.0, 20.0]]

# Test 4: Division avec des floats
>>> matrix_divided([[1.5, 2.5], [3.5, 4.5]], 2)
[[0.75, 1.25], [1.75, 2.25]]

# Test 5: Division par un float
>>> matrix_divided([[10, 20], [30, 40]], 2.5)
[[4.0, 8.0], [12.0, 16.0]]

# Test 6: Division avec nombres négatifs
>>> matrix_divided([[-6, -12], [-18, -24]], 3)
[[-2.0, -4.0], [-6.0, -8.0]]

# Test 7: Erreur - division par zéro
>>> matrix_divided([[1, 2], [3, 4]], 0)
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero

# Test 8: Erreur - div n'est pas un nombre (string)
>>> matrix_divided([[1, 2], [3, 4]], "3")
Traceback (most recent call last):
    ...
TypeError: div must be a number

# Test 9: Erreur - div est None
>>> matrix_divided([[1, 2], [3, 4]], None)
Traceback (most recent call last):
    ...
TypeError: div must be a number

# Test 10: Erreur - matrix contient une string
>>> matrix_divided([[1, "hello"], [3, 4]], 2)
Traceback (most recent call last):
    ...
TypeError: matrix must be a matrix (list of lists) of integers/floats

# Test 11: Erreur - matrix n'est pas une liste
>>> matrix_divided("not a matrix", 2)
Traceback (most recent call last):
    ...
TypeError: matrix must be a matrix (list of lists) of integers/floats

# Test 12: Erreur - matrix contient un élément qui n'est pas une liste
>>> matrix_divided([1, 2, 3], 2)
Traceback (most recent call last):
    ...
TypeError: matrix must be a matrix (list of lists) of integers/floats

# Test 13: Erreur - lignes de tailles différentes
>>> matrix_divided([[1, 2, 3], [4, 5]], 2)
Traceback (most recent call last):
    ...
TypeError: Each row of the matrix must have the same size

# Test 14: Erreur - lignes de tailles différentes (autre cas)
>>> matrix_divided([[1, 2], [3, 4, 5]], 2)
Traceback (most recent call last):
    ...
TypeError: Each row of the matrix must have the same size

# Test 15: Division avec une seule ligne
>>> matrix_divided([[10, 20, 30]], 10)
[[1.0, 2.0, 3.0]]

# Test 16: Division avec inf
>>> matrix_divided([[1, 2], [3, 4]], float('inf'))
[[0.0, 0.0], [0.0, 0.0]]

# Test 17: Matrice avec des très grands nombres
>>> matrix_divided([[1000000, 2000000]], 1000)
[[1000.0, 2000.0]]

# Test 18: Erreur - matrice vide
>>> matrix_divided([], 2)
Traceback (most recent call last):
    ...
TypeError: matrix must be a matrix (list of lists) of integers/floats

# Test 19: Erreur - ligne vide dans la matrice
>>> matrix_divided([[]], 2)
Traceback (most recent call last):
    ...
TypeError: matrix must be a matrix (list of lists) of integers/floats

# Test 20: Matrice avec zéros
>>> matrix_divided([[0, 0], [0, 0]], 5)
[[0.0, 0.0], [0.0, 0.0]]
