#!/usr/bin/python3
"""
Defines a function
"""


def read_file(filename=""):
    """
    A function taht reads a text file and prints it to stdou
    Args:
        filename: The file to be read
    """
    with open(filename, mode="r", encoding="utf-8") as text_file:
        content = text_file.read()
        print(content)
