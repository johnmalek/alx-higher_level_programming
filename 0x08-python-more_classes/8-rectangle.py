#!/usr/bin/python3
"""
Defines a class rectangle
"""


class Rectangle:
    """
    A rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        The __init__ method for the class
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        A method to access the width attribute of the rectangle
        Returns:
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        A method to check for errors and set the value for the width
        Args:
            value (int): The value to set the width as
        Raises:
            TypeError: if the width is not an integer
            ValueError: if the width is less than zero
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        A method to access the attribute height of rectangle
        Returns:
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        A method to check for errors and set the value of the height
        Args:
            value (int): The value to set the height as
        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than zero
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
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Print the string with the character #
        Return:
            string (str): string with #
        """
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle += str(self.print_symbol)
            if i < self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """
        String representation of the rectangle
        Return:
            string (str): string to get
        """
        return "Rectangle(" + str(self.__width) + "," + str(self.__height) +\
            ")"

    def __del__(self):
        """
        Deletes an instance of the rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Gets the biggest rectangle based on the area
        Args:
            rect_1: First rectangle
            rect_2: Second rectangle
        Raises:
            TypeError: if rect_1 and rect_2 are not instances of Rectangle
        Returns:
            The biggest rectangle based on area
            rect_1 if both have the same area
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() > rect_2.area():
                return rect_1
            elif rect_2.area() > rect_1.area():
                return rect_2
            else:
                return rect_1
