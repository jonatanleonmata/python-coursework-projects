# Class: CSE 1321L
# Section: BW2
# Term: Fall 2026
# Instructor: Hunter Osborne
# Name: Jonatan Leon Mata
# Assignment: 5C


def display_matrix(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            print(matrix[row][column], end=" ")
        print()


rows_a = int(input("Enter rows for Matrix A: "))
columns_a = int(input("Enter columns for Matrix A: "))
print()

rows_b = int(input("Enter rows for Matrix B: "))
columns_b = int(input("Enter columns for Matrix B: "))
print()

if columns_a != rows_b:
    print("Matrix multiplication is not possible.")
    print("Number of columns in Matrix A must equal number of rows in Matrix B.")
else:
    print("Enter Matrix A values (comma-separated):")
    values_a = input().split(",")
    print()

    print("Enter Matrix B values (comma-separated):")
    values_b = input().split(",")
    print()

    matrix_a = []
    value_index = 0
    for row in range(rows_a):
        matrix_row = []
        for column in range(columns_a):
            matrix_row.append(int(values_a[value_index]))
            value_index = value_index + 1
        matrix_a.append(matrix_row)

    matrix_b = []
    value_index = 0
    for row in range(rows_b):
        matrix_row = []
        for column in range(columns_b):
            matrix_row.append(int(values_b[value_index]))
            value_index = value_index + 1
        matrix_b.append(matrix_row)

    resulting_matrix = []
    for row in range(rows_a):
        result_row = []
        for column in range(columns_b):
            total = 0
            for value in range(columns_a):
                total = total + matrix_a[row][value] * matrix_b[value][column]
            result_row.append(total)
        resulting_matrix.append(result_row)

    print("Matrix A:")
    display_matrix(matrix_a)
    print()

    print("Matrix B:")
    display_matrix(matrix_b)
    print()

    print("Resulting Matrix:")
    display_matrix(resulting_matrix)
