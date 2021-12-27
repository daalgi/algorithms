"""
https://leetcode.com/problems/maximal-square/

Given an m x n binary matrix filled with 0's and 1's, 
find the largest square containing only 1's and return its area.

 

Example 1:


Input: matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""
from typing import List
from copy import deepcopy
from functools import lru_cache


def print_matrix(mat):
    print()
    for row in mat:
        print("   " + " ".join(f"{v:>3}" for v in row))
    print()


def brute_force(matrix: List[List[int]]) -> int:
    # Time complexity: O(m²n²)
    # Space complexity: O(1)
    pass


def dp_memoization(matrix: List[List[int]]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(mn)

    @lru_cache(maxsize=None)
    def dfs(r: int, c: int) -> int:
        if r == rows or c == cols or matrix[r][c] == 0:
            return 0
        return 1 + min(dfs(r + 1, c), dfs(r, c + 1), dfs(r + 1, c + 1))

    rows, cols = len(matrix), len(matrix[0])
    max_side = 0
    for r in range(rows):
        for c in range(cols):
            current = dfs(r, c)
            if current > max_side:
                max_side = current

    return max_side * max_side


def dp_tabulation(matrix: List[List[int]]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(mn)

    rows, cols = len(matrix), len(matrix[0])

    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_side = 0
    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if matrix[r - 1][c - 1]:
                min_neighbor = min(dp[r - 1][c], dp[r - 1][c - 1], dp[r][c - 1])
                dp[r][c] = 1 + min_neighbor

                if dp[r][c] > max_side:
                    max_side = dp[r][c]

    # print_matrix(dp)
    return max_side * max_side


def dp_tabulation_opt(matrix: List[List[int]]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(1)
    # Modify the input list `matrix` to store partial results

    rows, cols = len(matrix), len(matrix[0])

    # Special cases
    if rows == 1:
        return max(matrix[0])
    if cols == 1:
        return max(row[0] for row in matrix)

    max_side = 0
    # Check for ones in the first row and columns, and initialize
    # `max_side` to 1 if so
    if any(v for v in matrix[0]) or any(row[0] for row in matrix):
        max_side = 1

    # Loop over the elements of the `matrix`, skipping the first
    # row and column (already handled)
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c]:
                matrix[r][c] = 1 + min(
                    matrix[r][c - 1], matrix[r - 1][c - 1], matrix[r - 1][c]
                )
                if matrix[r][c] > max_side:
                    max_side = matrix[r][c]
    # print_matrix(matrix)
    return max_side * max_side


if __name__ == "__main__":
    print("-" * 60)
    print("Maximal square")
    print("-" * 60)

    test_cases = [
        ([[0]], 0),
        ([[1]], 1),
        ([[0, 1, 1]], 1),
        ([[0, 1], [1, 1]], 1),
        ([[0, 1], [1, 0]], 1),
        ([[1, 1], [1, 1]], 4),
        ([[1, 1, 1], [1, 0, 0], [1, 0, 0]], 1),
        ([[0, 1, 1], [1, 0, 0], [1, 0, 0]], 1),
        ([[1, 1, 0], [1, 1, 1], [1, 1, 1]], 4),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 9),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 0]], 4),
        ([[1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 4),
        ([[1, 1, 0, 1], [0, 1, 0, 1], [1, 0, 1, 0]], 1),
        ([[1, 0, 1, 0, 0], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 0, 1, 0]], 4),
    ]

    for matrix, solution in test_cases:

        print("Matrix:")
        print_matrix(matrix)

        result = dp_memoization(deepcopy(matrix))
        output = f"\t      dp_memoization = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation(deepcopy(matrix))
        output = f"\t       dp_tabulation = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation_opt(deepcopy(matrix))
        output = f"\t   dp_tabulation_opt = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
