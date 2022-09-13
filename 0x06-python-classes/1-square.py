#!/usr/bin/python3

class Square:
    """
    A square class that defines a square by 
    - Private instance attribute: size
    - Instantiation with size (no type/value verification)
    """
    def __init__(self, size):
        """
        The __init__ method for the square class
        """
        self.__size = size
