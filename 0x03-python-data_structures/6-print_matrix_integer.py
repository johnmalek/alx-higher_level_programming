#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    """
    Prints a matrix
    """

    for row in matrix:
        row_length = len(row)
        for i in range(row_length):
            if i != row_length - 1:
                print("{}".format(row[i]), end=" ")
            else:
                print("{}".format(row[i]), end=" ")
        print()
