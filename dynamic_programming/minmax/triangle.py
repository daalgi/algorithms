"""
https://leetcode.com/problems/triangle/

Given a triangle array, return the minimum path sum from 
top to bottom.

For each step, you may move to an adjacent number of the 
row below. More formally, if you are on index i on the current 
row, you may move to either index i or index i + 1 on the next row.

Example 1:
Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.

Example 2:
Input: triangle = [[-10]]
Output: -10

Constraints:
1 <= triangle.length <= 200
triangle[0].length == 1
triangle[i].length == triangle[i - 1].length + 1
-10^4 <= triangle[i][j] <= 10^4
 
Follow up: Could you do this using only O(n) extra space, 
where n is the total number of rows in the triangle?
"""
from typing import List
from functools import lru_cache
from copy import deepcopy


def print_triangle(
    triangle: List[List[int]], element_space: int = 4, initial_space: int = 1
):
    max_cols = len(triangle[-1])
    for row in triangle:
        cols = len(row)
        line_initial_space = (max_cols - cols) * element_space // 2
        line = " " * (initial_space + line_initial_space)
        for col in row:
            num = str(col)
            free_space = element_space - len(num)
            left_space = right_space = free_space // 2
            line += " " * left_space + num + " " * right_space
        print(line)
    print()


def dp_memoization(triangle: List[List[int]]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(mn)

    @lru_cache(maxsize=None)
    def dfs(r: int, c: int) -> int:
        # Base case
        if r == rows or c == -1 or c == len(triangle[r]):
            return float("inf")

        if r == rows - 1:
            return triangle[r][c]

        return triangle[r][c] + min(
            # Option 1: go down left (same column)
            dfs(r + 1, c),
            # Option 2: go down right (next column)
            dfs(r + 1, c + 1),
        )

    rows = len(triangle)
    return dfs(0, 0)


def dp_tabulation(triangle: List[List[int]]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(mn)
    pass


def dp_tabulation_opt(triangle: List[List[int]]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(1)
    # Use the triangle itself to store the length of the paths
    rows = len(triangle)

    if rows == 1:
        return triangle[0][0]

    # Sides of the triangle
    for r in range(1, rows):
        triangle[r][0] += triangle[r - 1][0]
        triangle[r][r] += triangle[r - 1][r - 1]

    # Interior of the triangle
    for r in range(2, rows):
        for c in range(1, len(triangle[r]) - 1):
            triangle[r][c] += min(triangle[r - 1][c], triangle[r - 1][c - 1])

    # Minimum path at the base of the triangle
    return min(triangle[-1])


if __name__ == "__main__":
    print("-" * 60)
    print("Triangle (minimum path sum)")
    print("-" * 60)

    test_cases = [
        ([[1]], 1),
        ([[1], [2, 3]], 3),
        ([[1], [2, 3], [4, 5, 6], [1, 2, 3, 4]], 8),
        ([[1], [2, 3], [4, 15, 6], [1, 2, 3, 4], [1, -7, 3, -8, 10]], 1),
        ([[1], [2, 3], [4, 8, 6], [9, 2, 3, 4], [1, 9, 9, 9, 10]], 17),
    ]

    for triangle, solution in test_cases:

        print("Triangle:")
        print_triangle(triangle, element_space=5)

        result = dp_memoization(deepcopy(triangle))
        output = f"\t      dp_memoization = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation_opt(deepcopy(triangle))
        output = f"\t   dp_tabulation_opt = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print("\n")
