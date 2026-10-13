#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(len(i)):
            print("{:d}".format(row[i]), end=" " if i != len(row) - 1 else "")
        print()
