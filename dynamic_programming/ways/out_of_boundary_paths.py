"""
https://leetcode.com/problems/out-of-boundary-paths/

There is an m x n grid with a ball. The ball is initially at the 
position [startRow, startColumn]. You are allowed to move the 
ball to one of the four adjacent cells in the grid (possibly 
out of the grid crossing the grid boundary). You can apply at 
most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, 
return the number of paths to move the ball out of the grid 
boundary. Since the answer can be very large, 
return it modulo 10^9 + 7.

Example 1:
Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6

Example 2:
Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12

Constraints:
1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow < m
0 <= startColumn < n
"""
from functools import lru_cache


def brute_force(m: int, n: int, max_moves: int, start_row: int, start_col: int) -> int:
    # Time complexity: O(4^N),
    # Space complexity: O(N)
    # where `N` is the size of the moves allowed `max_moves`,
    # and 4 is the possible choices at every point
    pass


def dp_memoization(
    m: int, n: int, max_moves: int, start_row: int, start_col: int
) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mnN)
    # Space complexity: O(mnN)
    # where m x n is the size of the grid, and N is `max_moves`

    @lru_cache(maxsize=None)
    def dfs(r: int, c: int, moves_left: int) -> int:
        # Base cases
        # No moves left
        if moves_left < 0:
            return 0
        # Out of boundary
        if not (0 <= r < m) or not (0 <= c < n):
            return 1

        count = 0
        for dr, dc in moves:
            count += dfs(r + dr, c + dc, moves_left - 1)
        return count

    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
    return dfs(start_row, start_col, max_moves) % 1000000007


def dp_tabulation(
    m: int, n: int, max_moves: int, start_row: int, start_col: int
) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(mnN)
    # Space complexity: O(mnN)
    # where m x n is the size of the grid, and N is `max_moves`
    # TODO
    pass


if __name__ == "__main__":

    print("-" * 60)
    print("Target sum")
    print("-" * 60)

    test_cases = [
        # (rows, cols, max_moves, start_row, start_col, solution)
        (2, 2, 2, 0, 0, 6),
        (1, 3, 3, 0, 1, 12),
        (5, 10, 50, 3, 5, 142902352),
        (50, 50, 50, 13, 13, 475390182),
    ]

    for rows, cols, max_moves, start_row, start_col, solution in test_cases:

        print(f"Grid: {rows}x{cols}")
        print(f"Start: {start_row, start_col}")
        print(f"Max moves: {max_moves}")

        result = dp_memoization(rows, cols, max_moves, start_row, start_col)
        string = f"dp_memoization = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        test_ok = solution == result
        string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(string)

        # result = dp_tabulation(nums, target)
        # string = f" dp_tabulation = "
        # string += " " * (25 - len(string))
        # string += str(result)
        # string += " " * (60 - len(string))
        # test_ok = solution == result
        # string += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        # print(string)

        print()
