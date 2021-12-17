"""
https://leetcode.com/problems/unique-paths-ii/

A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of 
the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. 
How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""
from typing import List
from functools import lru_cache


def print_grid(grid: List[List[int]], initial_space: int = 5):
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        line = " " * initial_space
        for j in range(cols):
            line += " . " if grid[i][j] == 0 else " x "
        print(line)
    print()


def dp_memoization(grid: List[List[int]]) -> int:
    # Dynamic programming - memoization
    # Time complexity: O(m*n)
    # Space complexity: O(m*n)

    @lru_cache(maxsize=None)
    def dfs(r: int, c: int) -> int:
        # Recursive function

        # Base cases
        if r == rows or c == cols or grid[r][c] == 1:
            return 0
        if r == rows - 1 and c == cols - 1:
            return 1

        return dfs(r + 1, c) + dfs(r, c + 1)

    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return 0

    return dfs(0, 0)


def dp_tabulation(grid: List[List[int]]) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(m*n)
    # Space complexity: O(m*n)

    rows, cols = len(grid), len(grid[0])

    # No solution if the start of the end has an obstacle
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return 0

    # Table to keep track of the results
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    # Initialize the cell corresponding to grid[0][0]
    # with `1` (paths from origin to (0,0))
    dp[0][1] = 1

    # Loop over the rows
    for i in range(1, rows + 1):
        # Loop over the columns
        for j in range(1, cols + 1):
            if grid[i - 1][j - 1] == 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # Return the value at the bottom right cell
    return dp[-1][-1]


def dp_tabulation_opt(grid: List[List[int]]) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(m*n)
    # Space complexity: O(n)

    rows, cols = len(grid), len(grid[0])

    # No solution if the start of the end has an obstacle
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return 0

    # Space optimiaztion: since we only need access
    # to last two rows for a given cell, we can reduce
    # the space complexity by storing only two rows
    # instead of the whole matrix.
    dp = [[0] * (cols + 1)] * 2
    # Initialize the cell corresponding to grid[0][0]
    # with `1` (paths from origin to (0,0))
    dp[0][1] = 1

    # Loop over the rows
    for i in range(1, rows + 1):
        # Loop over the columns
        for j in range(1, cols + 1):
            if grid[i - 1][j - 1]:
                dp[i & 1][j] = 0
            else:
                # Note: Use bitwise operations to access
                # row 0 when `i` is even, and
                # row 1 when `i` is odd
                dp[i & 1][j] = dp[(i - 1) & 1][j] + dp[i & 1][j - 1]

    # Return the value at the bottom right cell
    return dp[rows & 1][-1]


if __name__ == "__main__":
    print("-" * 60)
    print("Unique paths II ")
    print("-" * 60)

    test_cases = [
        ([[0, 1]], 0),
        ([[1, 0]], 0),
        ([[1, 1]], 0),
        ([[0, 0]], 1),
        ([[0, 0], [0, 0]], 2),
        ([[0, 1], [0, 0]], 1),
        ([[0, 1], [1, 0]], 0),
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 6),
        ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
        ([[0, 0, 0], [1, 1, 1], [0, 0, 0]], 0),
    ]

    for grid, solution in test_cases:

        print("Grid:")
        print_grid(grid)

        result = dp_memoization(grid)
        string = f"     dp_memoization = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        result = dp_tabulation(grid)
        string = f"      dp_tabulation = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        result = dp_tabulation_opt(grid)
        string = f"  dp_tabulation_opt = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        print("\n")
