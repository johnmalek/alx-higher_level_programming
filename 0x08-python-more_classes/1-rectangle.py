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
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        A method to access the width of the rectangle
        Returns:
            The width of the rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        A method to access the height property of the rectangle
        Returns:
            The height of the rectangle
        """

    @width.setter
    def width(self, value):
        """
        A method to set the width of the rectangle and check for errors
        Args:
            value: value to set the width as
        Raises:
            TypeError: if the value is not an integer
            ValueError: if value is less than zero
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
        A method to set the height of the rectangle and check for errors
        Args:
            value : value to set the height as
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
