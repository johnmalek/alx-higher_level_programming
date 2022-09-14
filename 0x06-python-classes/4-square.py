#!/usr/bin/python3
"""
defines a class square
"""


class Square:
    """
    A square
    """
    def __init__(self, size=0):
        """The __init__ method for Square class
        Args:
            size: size of the square
        """
        self.__size = size

    @property
    def size(self):
        """Call the function to checking property
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """check errors and setter for size attribute
        Args:
            value: Value to checking errors
        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates the area of the square
        Returns:
            The area of the square
        """

        return self.__size ** 2
