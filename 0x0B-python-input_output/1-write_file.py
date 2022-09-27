#!/usr/bin/python3
"""
Defines a function
"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file 
    Args:
        filename: The file to be written to
        text: The text to write to the file
    Returns:
        The number of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as text_file:
        content = text_file.write(text)
        return len(text)
