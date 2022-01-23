from copy import deepcopy
from random import randint


def test_determinant(test_number: int):
    test_0 = [[10]]  # Single
    # ans: 10
    test_1 = [[1, 0],  # Identity
              [0, 1]]
    # ans: 1
    test_2 = [[2, 0, 0],  # Diagonal
              [0, 3, 0],
              [0, 0, 2]]
    # ans: 12
    test_3 = [[1, 4, 8],  # Full matrix
              [2, 3, 6],
              [2, 6, 3]]
    # ans: 45
    test_4 = [[2, 3, 7, 1],  # Full matrix
              [7, 1, 9, 8],
              [8, 6, 1, 4],
              [0, 1, 4, 2]]
    # ans: 681
    test_5 = [[2, 3, 7, 1, 9],  # Full matrix
              [7, 1, 9, 8, 3],
              [8, 6, 1, 4, 1],
              [0, 1, 4, 2, 13],
              [22, 7, 3, 9, 18]]
    # ans: 41997
    test_6 = [[randint(0, 10) for i in range(10)] for j in range(10)]
    test_6[6] = [0 for k in range(10)]

    tests = [test_0, test_1, test_2, test_3, test_4, test_5, test_6]
    det = compute_determinant(tests[test_number])
    print("Determinant of the test matrix is:", det)


def compute_determinant(matrix: list):
    """
    Precondition: <matrix> is a two-dimensional, square list of real numbers.
    :return: computes and returns the determinant of the matrix
    """
    size = len(matrix)
    if size == 1:
        return matrix[0][0]
    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    matrix_determinant = 0
    with_most_zeros = find_most_zeros(matrix)
    for i in range(size):
        if with_most_zeros[0]:  # A row has the most 0's
            row = with_most_zeros[1]

            cofactor = (-1) ** (row + i) * matrix[row][i]

            if cofactor == 0:  # Skip if cofactor is 0
                continue

            new_matrix = deepcopy(matrix[:row] + matrix[row + 1:])

            for j in range(size - 1):
                new_matrix[j].pop(i)
        else:  # A column has the most 0's
            col = with_most_zeros[1]

            cofactor = (-1) ** (i + col) * matrix[i][col]

            if cofactor == 0:  # Skip if cofactor is 0
                continue

            new_matrix = deepcopy(matrix[:i] + matrix[i + 1:])

            for j in range(size - 1):
                new_matrix[j].pop(col)

        matrix_determinant += cofactor * compute_determinant(new_matrix)
    return matrix_determinant


def find_most_zeros(matrix):
    with_most_zeros = [0, True, 0]  # True for False has most, True otherwise
    size = len(matrix)

    # Rows
    for i in range(size):
        num_zeros = matrix[i].count(0)
        if num_zeros > with_most_zeros[0]:
            with_most_zeros = [num_zeros, True, i]

    # Columns
    current_column = list()
    for j in range(size):
        for k in range(size):
            current_column.append(matrix[k][j])
        num_zeros = current_column.count(0)
        if num_zeros > with_most_zeros[0]:
            with_most_zeros = [num_zeros, False, j]

    return with_most_zeros[1:]


def is_number(n):
    """
    Returns true iff n is a real number.
    """
    try:
        float(n)
        return True
    except ValueError:
        return False


def main():
    size_of_matrix = str((input("Size of square matrix (1 through 99): ")))
    while not (size_of_matrix.isdigit()) or \
            not (1 <= int(size_of_matrix) <= 99):
        size_of_matrix = \
            str(input("Please enter a size in-between 1 and 99: "))
    size_of_matrix = int(size_of_matrix)
    matrix = list()
    for i in range(size_of_matrix):
        ith_row = list()
        print("Enter the entries for row " + str(i + 1) + ": ")
        for j in range(size_of_matrix):
            entry = input("Entry (" + str(i + 1) +
                          ", " + str(j + 1) + "): ")
            while not (is_number(entry)):
                entry = input("Entry (" + str(i + 1) +
                              ", " + str(j + 1) + "): ")
            ith_row.append(float(entry))
        matrix.append(ith_row)

    print("\nInputted matrix:")
    for i in range(size_of_matrix):
        print(matrix[i])
    print("\nComputing determinant...")
    det = compute_determinant(matrix)
    print("Determinant of the inputted matrix is:", det)


if __name__ == "__main__":
    main()
    # test_determinant(3)
