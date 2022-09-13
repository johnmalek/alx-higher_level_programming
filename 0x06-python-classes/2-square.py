#!/usr/bin/python3

class Square:
    """
    A class Square that defines a square by: 
    - Private instance attribute: size
    - Instantiation with optional size: def __init__(self, size=0):
    """
    def __init__(self, size=0):
        """
        The __init__ method for the square class
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

