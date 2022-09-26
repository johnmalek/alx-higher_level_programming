#!/usr/bin/python3
"""
Defines a class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class rectangle
    Inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        A method to initialize the class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Prints the rectangle
        """
        return "[Rectangle] " + str(self.__width) +  "/" + str(self.__height)
