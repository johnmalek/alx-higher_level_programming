#!/usr/bin/python3

class Square:
    """
    A class that efines a square
    Args:
        size (int) : defines the size of the square
    """
    def __init__(self, size=0):
        """
        The __init__ method for the class Square
        """
        self.__size = size

    @property
    def size(self):
        """
        Method the allows access to the size attribute
        Returns: 
            The attribute size
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

    def my_print(self):
        """
        Public instance method that prints in stdout
        Returns:
            prints in stdout the square with character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
