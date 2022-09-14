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
        The __init__ method for the square class
        Args:
            size (int): The size of the square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        A method the access the attribute size
        Returns:
            The attribute size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        A method to set the value of size
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
        A method to access the attribute position
        Returns:
            The attribute position
        """
    @position.setter
    def position(self, value):
        """
        check errors and setter for size attribute
        Args:
            value: Value to checking errors
        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than zero
        """
        if type(value) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
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
        Prints in stdout
        Returns:
            Prints in stdout the square with the character #
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
