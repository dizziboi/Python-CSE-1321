# Class: CSE 1321L
# Section: B09
# Term: Fall
# Instructor: Jui Mhatre
# Name: Caleb Brown
# Assignment: 5

def build_matrix(values, rows, cols):
    """Divide a flat list of values into rows and columns using nested loops."""
    matrix = []
    index = 0
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(values[index])
            index += 1
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    """Print a matrix in row-column format using nested loops."""
    for i in range(len(matrix)):
        line = ""
        for j in range(len(matrix[i])):
            line += str(matrix[i][j]) + " "
        print(line)


def multiply(a, b, r1, c1, c2):
    """Multiply matrix a (r1 x c1) by matrix b (c1 x c2) using nested loops."""
    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            total = 0
            for k in range(c1):
                total += a[i][k] * b[k][j]
            row.append(total)
        result.append(row)
    return result


def main():
    r1 = int(input("Enter rows for Matrix A: "))
    c1 = int(input("Enter columns for Matrix A: "))
    print()
    r2 = int(input("Enter rows for Matrix B: "))
    c2 = int(input("Enter columns for Matrix B: "))
    print()

    if c1 != r2:
        print("Matrix multiplication is not possible.")
        print("Number of columns in Matrix A must equal number of rows in Matrix B.")
        return

    print("Enter Matrix A values (comma-separated):")
    a_values = []
    for item in input().split(","):
        a_values.append(int(item.strip()))

    print()
    print("Enter Matrix B values (comma-separated):")
    b_values = []
    for item in input().split(","):
        b_values.append(int(item.strip()))

    matrix_a = build_matrix(a_values, r1, c1)
    matrix_b = build_matrix(b_values, r2, c2)
    result = multiply(matrix_a, matrix_b, r1, c1, c2)

    print()
    print("Matrix A:")
    display_matrix(matrix_a)
    print()
    print("Matrix B:")
    display_matrix(matrix_b)
    print()
    print("Resulting Matrix:")
    display_matrix(result)


main()