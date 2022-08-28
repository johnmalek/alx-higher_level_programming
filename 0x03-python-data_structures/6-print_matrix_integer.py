#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    """
    Prints a matrix of integers
    """

    for row in matrix:
        row_length = len(row)
        for i in range(row_length):
            print("{:d}".format(row[i]), end=" " if i+1 < len(row) else "")
        print()
