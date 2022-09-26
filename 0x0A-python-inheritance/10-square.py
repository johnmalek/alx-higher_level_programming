#!/usr/bin/python3
"""
Defines a class
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    A class square that inherits from rectangle
    """
    def __init__(self, size):
        """
        Initializes the class
        Args:
            size: size of the square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
