class Rectangle:
    """
    Class that defines a rectangle by its width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): new width value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.

        Returns:
            int: the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): new height value

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Return the area of the rectangle.

        Returns:
            int: area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.

        Returns:
            int: perimeter of the rectangle,
                 or 0 if width or height is 0
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Return the string representation of the rectangle
        using the character '#'.

        Returns:
            str: rectangle drawing or empty string
        """
        if self.width == 0 or self.height == 0:
            return ""

        rectangle = []
        for _ in range(self.height):
            rectangle.append("#" * self.width)
        return "\n".join(rectangle)
