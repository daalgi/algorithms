"""
https://www.lintcode.com/problem/1042/?_from=collection&fromId=18

A matrix is Toeplitz if every diagonal from top-left to bottom-right 
has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

- matrix will be a 2D array of integers.
- matrix will have a number of rows and columns in range [1, 20].
- matrix[i][j] will be integers in range [0, 99].

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512
In the above grid, the diagonals are 
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", 
and in each diagonal all elements are the same, so the answer is True.

Example 2:
Input: matrix = [[1,2],[2,2]]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.
"""
from typing import List


def solution1(matrix: List[List[int]]) -> bool:
    # Time complexity: O(m*n)
    # Space complexity: O(m+n)

    rows, cols = len(matrix), len(matrix[0])
    # Lists with the first row and column for each diagonal check
    row_indices = [i for i in range(rows - 1, 0, -1)] + [0] * (cols - 1)
    col_indices = [0] * rows + [j for j in range(1, cols - 1)]

    # Loop over the diagonals
    diagonals = len(row_indices)
    for d in range(diagonals):

        # First element in the diagonal `d`
        row, col = row_indices[d], col_indices[d]
        ref = matrix[row][col]

        # Check next elements in the diagonal against `ref`
        row += 1
        col += 1
        while row < rows and col < cols:
            if matrix[row][col] != ref:
                return False
            row += 1
            col += 1

    return True


def solution2(matrix: List[List[int]]) -> bool:
    # Time complexity: O(m*n)
    # Space complexity: O(1)

    rows, cols = len(matrix), len(matrix[0])
    diagonals = rows + cols - 1
    # Loop over the diagonals
    for d in range(diagonals):

        # First element in the diagonal `d`
        row = max(0, rows - d - 1)
        col = 0 if row > 0 else d - rows + 1
        ref = matrix[row][col]

        # Check next elements in the diagonal against `ref`
        row += 1
        col += 1
        while row < rows and col < cols:
            if matrix[row][col] != ref:
                return False
            row += 1
            col += 1

    return True


if __name__ == "__main__":
    print("-" * 60)
    print("Toeplitz matrix")
    print("-" * 60)

    test_cases = [
        ([[1]], True),
        ([[1, 2, 3]], True),
        ([[1, 2], [2, 2]], False),
        ([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True),
        ([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 1]], False),
        ([[1, 2, 3, 4, 8], [5, 1, 2, 3, 4], [9, 5, 1, 2, 3]], True),
    ]

    for matrix, solution in test_cases:

        output = f"Matrix: {matrix}"
        if len(output) > 60:
            output = output[:60] + " ...]]"
        print(output)

        result = solution1(matrix)
        output = f"\t   solution1 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = solution2(matrix)
        output = f"\t   solution2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
