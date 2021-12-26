"""
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers, find a path 
from top left to bottom right, which minimizes the sum of all 
numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
"""
from typing import List
from functools import lru_cache
from copy import deepcopy


def print_matrix(matrix: List[List[int]], element_space: int = 8):
    for row in matrix:
        for col in row:
            print(f"{str(col):>{element_space}}", end="")
        print()


def dp_memoization(grid: List[List[int]]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(mn)

    @lru_cache(maxsize=None)
    def dfs(r: int, c: int) -> int:
        # Base case
        if r == rows or c == cols:
            return float("inf")

        if r == rows - 1 and c == cols - 1:
            return grid[r][c]

        return grid[r][c] + min(
            # Option 1: go down
            dfs(r + 1, c),
            # Option 2: go right
            dfs(r, c + 1),
        )

    rows, cols = len(grid), len(grid[0])
    return dfs(0, 0)


def dp_tabulation(grid: List[List[int]]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(mn)

    rows, cols = len(grid), len(grid[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    dp[1][1] = grid[0][0]

    for r in range(1, rows + 1):
        for c in range(1, cols + 1):
            if r == 1:
                dp[r][c] = grid[r - 1][c - 1] + dp[r][c - 1]
            elif c == 1:
                dp[r][c] = grid[r - 1][c - 1] + dp[r - 1][c]
            else:
                dp[r][c] = grid[r - 1][c - 1] + min(dp[r - 1][c], dp[r][c - 1])

    return dp[-1][-1]


def dp_tabulation_opt(grid: List[List[int]]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(1)

    rows, cols = len(grid), len(grid[0])
    for r in range(1, rows):
        grid[r][0] += grid[r - 1][0]

    for c in range(1, cols):
        grid[0][c] += grid[0][c - 1]

    for r in range(1, rows):
        for c in range(1, cols):
            grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

    return grid[-1][-1]


if __name__ == "__main__":
    print("-" * 60)
    print("Minimum path sum")
    print("-" * 60)

    test_cases = [
        ([[1, 2, 3], [4, 5, 6]], 12),
        ([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7),
        ([[1, 3, 1, 0], [1, 5, 7, 0], [4, 2, 5, 3]], 8),
    ]

    for grid, solution in test_cases:

        print('Grid:')
        print_matrix(grid, element_space=3)

        result = dp_memoization(deepcopy(grid))
        output = f"\t      dp_memoization = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation(deepcopy(grid))
        output = f"\t       dp_tabulation = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation_opt(deepcopy(grid))
        output = f"\t   dp_tabulation_opt = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print('\n')
