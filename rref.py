from typing import List


def reduced_row_echelon_form(matrix: List[List[float]]) -> None:
    """
    :param matrix: A two dimensional list of real numbers.
    :return: Row reduces the given matrix in place.
    """
    lead = 0
    num_of_rows = len(matrix)
    num_columns = len(matrix[0])
    for row in range(num_of_rows):
        if num_columns <= lead:
            return

        i = row
        while matrix[i][lead] == 0:
            i += 1
            if num_of_rows == i:
                i = row
                lead += 1
                if num_columns == lead:
                    return

        # Swap rows i and r
        matrix[i], matrix[row] = matrix[row], matrix[i]

        if matrix[row][lead] != 0:
            new_row = []
            for elem in matrix[row]:
                new_row.append(elem / matrix[row][lead])
            matrix[row] = new_row

        for j in range(num_of_rows):
            if j != row:
                new_row = []
                for k, elem in enumerate(matrix[row]):
                    new_row.append(matrix[j][k] - (matrix[j][lead] * elem))
                matrix[j] = new_row
        lead += 1
    return


def matrix_to_string(matrix: List[List[float]]) -> str:
    matrix_string = "["
    for row in matrix:
        matrix_string += "["
        for elem in row:
            matrix_string += str(elem + 0) + ", "
        matrix_string = matrix_string[:-2]
        matrix_string += "]"
        matrix_string += "\n"
    matrix_string = matrix_string[:-1]
    matrix_string += "]"
    return matrix_string


def main():
    matrix_rows = str((input("Number of matrix rows: ")))
    while not (matrix_rows.isdigit()) or \
            not (1 <= int(matrix_rows)):
        matrix_rows = \
            str(input("Please enter a positive integer: "))
    matrix_rows = int(matrix_rows)

    matrix_cols = str((input("Number of matrix columns: ")))
    while not (matrix_cols.isdigit()) or \
            not (1 <= int(matrix_cols)):
        matrix_cols = \
            str(input("Please enter a positive integer: "))
    matrix_cols = int(matrix_cols)

    matrix = list()
    for i in range(matrix_rows):
        ith_row = list()
        print("Enter the entries for row " + str(i + 1) + ": ")
        for j in range(matrix_cols):
            ith_row.append(float(input("Entry (" + str(i + 1) +
                                       ", " + str(j + 1) + "): ")))
        matrix.append(ith_row)

    print("\nInputted matrix:")
    for i in range(matrix_rows):
        print(matrix[i])

    print("\nRow reducing...")
    reduced_row_echelon_form(matrix)
    for i in range(matrix_rows):
        for j in range(matrix_cols):
            matrix[i][j] += 0
    for i in range(matrix_rows):
        print(matrix[i])


def test_rref(test_num):
    L1 = [[1, 2, -1, -4],
         [2, 3, -1, -11],
         [-2, 0, -3, 22]]
    L2 = [[2, 8, 4, 2],
          [2, 5, 1, 5],
          [4, 10, -1, 1]]
    L3 = [[3, 4],
          [2, 3]]
    tests = [L1, L2, L3]
    reduced_row_echelon_form(tests[test_num - 1])
    s1 = matrix_to_string(tests[test_num - 1])
    print(s1)


if __name__ == "__main__":
    main()
    # test_rref(2)
