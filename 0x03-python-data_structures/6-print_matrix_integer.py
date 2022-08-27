#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    """
    Prints a matrix of integers
    """

    for row in matrix:
        row_length = len(row)
        for i in range(row_length):
            if i != row_length - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]), end=" ")
        print()
