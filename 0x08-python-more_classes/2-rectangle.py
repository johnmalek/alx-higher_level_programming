#!/usr/bin/python3
"""
Defines a class rectangle
"""

class Rectangle:
    """
    A rectangle
    """
    def __init__(self, width=0, height=0):
        """
        The __init__ method for the class
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        A method to access the width attribute of the rectangle
        Returns:
            The width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        A method to access the height attribute of the rectangle
        Returns:
            The height of the rectangle
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        A method to set the value of the width and check for errors
        Args:
            value: value to the set the width as
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than zero
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        A method to set the value of the height and check and for errors
        Args:
            value: value to set the height as
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than zero
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle
        Returns:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle
        Returns:
            The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        perimeter = 2 * (self.__width + self.__height)
        return perimeter
