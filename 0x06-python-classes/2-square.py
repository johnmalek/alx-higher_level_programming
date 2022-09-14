#!/usr/bin/python3
"""
Defines a class square
"""


class Square:
    """
    A square
    """
    def __init__(self, size=0):
        """
        The __init__ method for the square class
        Args:
            size: size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
