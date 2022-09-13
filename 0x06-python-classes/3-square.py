#!/usr/bin/python3

class Square:
    """
    A class Square that defines a square
    """
    def __init__(self, size=0):
        """
        The __init__ method for the square class
        Args:
            size: (:obj: 'int', optional): A private instance size
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates the area of the square
        Returns:
            The area of the square
        """
        return self.__size ** 2
