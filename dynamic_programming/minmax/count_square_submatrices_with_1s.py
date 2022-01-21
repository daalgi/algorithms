"""
https://leetcode.com/problems/count-square-submatrices-with-all-ones/

Given a m * n matrix of ones and zeros, return how many 
square submatrices have all ones.

Example 1:
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.

Example 2:
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.

Constraints:
1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
"""
from typing import List
from copy import deepcopy


def print_matrix(mat):
    print()
    for row in mat:
        print("   " + " ".join(f"{v:>3}" for v in row))
    print()


def dp_tabulation(matrix: List[List[int]]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(1)

    rows, cols = len(matrix), len(matrix[0])

    squares = 0
    for r in range(rows):
        if matrix[r][0]:
            squares += 1

    for c in range(1, cols):
        if matrix[0][c]:
            squares += 1

    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c]:
                matrix[r][c] = 1 + min(
                    matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1]
                )
                squares += matrix[r][c]

    return squares


def dp_tabulation2(matrix: List[List[int]]) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(mn)
    # Space complexity: O(1)

    rows, cols = len(matrix), len(matrix[0])

    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c]:
                matrix[r][c] = 1 + min(
                    matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1]
                )

    # More efficient than manually updating a `squares` variable
    return sum(map(sum, matrix))


def dp_tabulation3(matrix: List[List[int]]) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(mn)
    # Space complexity: O(1)

    rows, cols = len(matrix), len(matrix[0])

    for r in range(1, rows):
        for c in range(1, cols):
            matrix[r][c] *= 1 + min(
                matrix[r - 1][c], matrix[r][c - 1], matrix[r - 1][c - 1]
            )

    return sum(map(sum, matrix))


if __name__ == "__main__":
    print("-" * 60)
    print("Count square submatrices with all ones")
    print("-" * 60)

    test_cases = [
        ([[0]], 0),
        ([[1]], 1),
        ([[0, 1, 1]], 2),
        ([[0, 1], [1, 1]], 3),
        ([[1, 1], [1, 1]], 5),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 14),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 0]], 11),
        ([[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]], 15),
        ([[1, 0, 1], [1, 1, 0], [1, 1, 0]], 7),
        (
            [
                [1, 0, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 0, 1, 1],
                [1, 0, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1],
            ],
            31,
        ),
    ]

    for matrix, solution in test_cases:

        print("Matrix:")
        print_matrix(matrix)

        result = dp_tabulation(deepcopy(matrix))
        output = f"       dp_tabulation = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation2(deepcopy(matrix))
        output = f"      dp_tabulation2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation3(deepcopy(matrix))
        output = f"      dp_tabulation3 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
