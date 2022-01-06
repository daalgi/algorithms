"""
CRACKING THE CODING INTERVIEW
1.8. Zero matrix.
Write an algorithm such that if an element in an MxN matrix
is 0, its entire row and column are set to 0.

Examples:
Input:  [
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]
Output: [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 1],
]
"""
from typing import List
from copy import deepcopy


def additional_memory(matrix: list) -> list:
    # In-place modification of the matrix
    # Time complexity: O(m * n)
    # Space complexity: O(m + n)

    # Size of the matrix
    rows, cols = len(matrix), len(matrix[0])

    # Store the indices containing zeros
    row_zeros = set()
    col_zeros = set()

    # Loop over the elements of the matrix
    # to find the indices of the zeros
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_zeros.add(i)
                col_zeros.add(j)

    # Loop over the row indices with zeros:
    for row in row_zeros:
        # for col in range(n):
        #     matrix[row][col] = 0
        matrix[row] = [0] * cols

    # Loop over the col indices with zeros:
    for col in col_zeros:
        for row in range(rows):
            matrix[row][col] = 0

    return matrix


def efficient_solution(matrix: List[List[int]]) -> List[List[int]]:
    # In-place modification of the matrix
    # Time complexity: O(m * n)
    # Space complexity: O(1)
    # Strategy: use the first row and column as a flag to keep
    # track of the rows and columns to be made zero

    # Size of the matrix
    rows, cols = len(matrix), len(matrix[0])
    # Flags to indicate if the first row and col should be zero
    first_row_zero, first_col_zero = False, False

    # Check if the first row should be 0
    for row in range(rows):
        if matrix[row][0] == 0:
            first_col_zero = True
            break

    # Check if the first col should be 0
    for col in range(cols):
        if matrix[0][col] == 0:
            first_row_zero = True
            break

    # Check the rest of the cells, and store in the
    # first row and col
    for row in range(1, rows):
        for col in range(1, cols):
            if matrix[row][col] == 0:
                matrix[row][0] = 0
                matrix[0][col] = 0

    # Check the first row and column to determine which
    # cells must be made zero
    for row in range(1, rows):
        if matrix[row][0] == 0:
            for col in range(1, cols):
                matrix[row][col] = 0
    for col in range(1, cols):
        if matrix[0][col] == 0:
            for row in range(1, rows):
                matrix[row][col] = 0

    # Check if the first col is zero
    if first_col_zero:
        for row in range(rows):
            matrix[row][0] = 0

    # Check if the first row is zero
    if first_row_zero:
        for col in range(cols):
            matrix[0][col] = 0

    return matrix


if __name__ == "__main__":
    print("-" * 60)
    print("Zero matrix")
    print("-" * 60)

    test_cases = [
        ([[1]], [[1]]),
        ([[1, 2, 0], [1, 1, 1]], [[0, 0, 0], [1, 1, 0]]),
        ([[1, 0, 1], [1, 1, 1]], [[0, 0, 0], [1, 0, 1]]),
        ([[0, 1, 1], [1, 1, 1]], [[0, 0, 0], [0, 1, 1]]),
        ([[0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0]]),
        ([[1, 2, 0, 1], [1, 1, 1, 1]], [[0, 0, 0, 0], [1, 1, 0, 1]]),
        ([[1, 2, 1], [1, 1, 1]], [[1, 2, 1], [1, 1, 1]]),
        ([[1, 2, 1], [1, 2, 1], [1, 0, 1]], [[1, 0, 1], [1, 0, 1], [0, 0, 0]]),
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        ),
        (
            [
                [1, 0, 1, 2, 1],
                [1, 1, 1, 2, 1],
                [1, 1, 1, 0, 1],
                [1, 1, 1, 2, 1],
            ],
            [
                [0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1],
                [0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1],
            ],
        ),
    ]

    for matrix, solution in test_cases:

        print("Matrix:", matrix)

        result = additional_memory(deepcopy(matrix))
        output = "    additional_memory = "
        print_result = str(result)
        if len(print_result) > 30:
            print_result = print_result[:25] + " ...]]"
        output += print_result
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = efficient_solution(deepcopy(matrix))
        output = "   efficient_solution = "
        print_result = str(result)
        if len(print_result) > 30:
            print_result = print_result[:25] + " ...]]"
        output += print_result
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
