#!/usr/bin/python3
"""
Defines a class square
"""


class Square:
    """
    A square
    """
    def __init__(self, size=0, position=(0, 0)):
            """
            The __init__ method for the class
            Args:
                size (int): defines the size of the square
                position (tuple): defines the position of the square
            """
            self.__size = size
            self.__position = position

    @property
    def size(self):
        """
        A method to access the size of the square
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ 
        Checks errors and setter for the size attribute
        Args:
            value: value to checking errors
        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than zero
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        A method to access the position attribute
        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Checks errors and setter for the postion attribute
        Args:
            value: value to checking errors
        Raises:
            TypeError: Exception if size is not an integer
            ValueErrr: Exception if size is less than zero
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise Valueerror("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not tuple or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        Calculates the area of the square
        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints a square using # character
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(end=" ")
                for k in range(self.size):
                    print("#", end="")
                print()
