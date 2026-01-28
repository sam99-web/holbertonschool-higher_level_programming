class Rectangle:
    """
    Classe Rectangle qui définit un rectangle par sa largeur et sa hauteur.
    """

    def __init__(self, width=0, height=0):
        """
        Initialise un nouveau Rectangle.

        Args:
            width (int): largeur du rectangle (par défaut 0)
            height (int): hauteur du rectangle (par défaut 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Récupère la largeur du rectangle.

        Returns:
            int: la largeur du rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Définit la largeur du rectangle.

        Args:
            value (int): nouvelle largeur

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est inférieur à 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Récupère la hauteur du rectangle.

        Returns:
            int: la hauteur du rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Définit la hauteur du rectangle.

        Args:
            value (int): nouvelle hauteur

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value est inférieur à 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """
        Calcule et retourne le périmètre du rectangle.

        Returns:
            int: le périmètre du rectangle.
                 Retourne 0 si la largeur ou la hauteur est égale à 0.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Retourne une représentation du rectangle avec le caractère '#'.

        Returns:
            str: une chaîne représentant le rectangle,
                 ou une chaîne vide si largeur ou hauteur vaut 0.
        """
        if self.width == 0 or self.height == 0:
            return ""

        lines = []
        for _ in range(self.height):
            lines.append("#" * self.width)
        return "\n".join(lines)
