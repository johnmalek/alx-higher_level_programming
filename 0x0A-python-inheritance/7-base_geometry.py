#!/usr/bin/python3
"""
Defines a class
"""


class BaseGeometry:
    """
    A class BaseGeometry
    """
    def __init__(self):
        """
        Initializes the class
        """

    def area(self):
        """
        A method to calculate the area
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        A method that validates value
        Args:
            name: name
            value: value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than zero
        """

        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
