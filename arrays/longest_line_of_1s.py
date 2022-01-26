"""
https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

Given an m x n binary matrix mat, return the length 
of the longest line of consecutive one in the matrix.

The line could be horizontal, vertical, diagonal, 
or anti-diagonal.

Example 1:
Input: mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
Output: 3

Example 2:
Input: mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
Output: 4

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 10^4
1 <= m * n <= 10^4
mat[i][j] is either 0 or 1.
"""
from typing import List
from copy import deepcopy


def print_matrix(mat):
    print()
    for row in mat:
        print("   " + "".join(f"{v:>2}" for v in row))
    print()


def brute_force(mat: List[List[int]]) -> int:
    # Time complexity: O(mn)
    # Space complexity: O(1)
    rows, cols = len(mat), len(mat[0])
    max_ones = 0

    # Check horizontal lines
    for r in range(rows):
        curr_ones = 0
        for c in range(cols):
            if mat[r][c]:
                curr_ones += 1
                if curr_ones > max_ones:
                    max_ones = curr_ones
            else:
                curr_ones = 0

    # Check vertical lines
    if max_ones < rows:
        for c in range(cols):
            curr_ones = 0
            for r in range(rows):
                if mat[r][c]:
                    curr_ones += 1
                    if curr_ones > max_ones:
                        max_ones = curr_ones
                else:
                    curr_ones = 0

    # Check diagonals
    min_dir = min(cols, rows)
    if max_ones < min_dir:
        r_starts = list(range(rows - 1 - max_ones)) + [0] * (cols - max_ones)
        c_starts = [0] * (rows - 1 - max_ones) + list(range(cols - max_ones))
        for i in range(len(r_starts)):
            r, c = r_starts[i], c_starts[i]
            curr_ones = 0
            while r < rows and c < cols:
                if mat[r][c]:
                    curr_ones += 1
                    if curr_ones > max_ones:
                        max_ones = curr_ones
                else:
                    curr_ones = 0
                r, c = r + 1, c + 1

    # Check anti-diaogonals
    if max_ones < min_dir:
        r_starts = list(range(rows - 1 - max_ones, -1, -1)) + [0] * (
            cols - 1 - max_ones
        )
        c_starts = [cols - 1] * (rows - max_ones) + list(range(cols - 1, max_ones, -1))
        for i in range(len(r_starts)):
            r, c = r_starts[i], c_starts[i]
            curr_ones = 0
            while r < rows and c > -1:
                # print(r, c)
                if mat[r][c]:
                    curr_ones += 1
                    if curr_ones > max_ones:
                        max_ones = curr_ones
                else:
                    curr_ones = 0
                r, c = r + 1, c - 1

    return max_ones


def dp3d_iter(mat: List[List[int]]) -> int:
    # Dynamic programming - Iterative
    # Time complexity: O(mn)
    # Time complexity: O(mn)

    rows, cols = len(mat), len(mat[0])

    # 3D matrix to store the max num of 1s
    # dp[i][j][0] stores the max num of horizontal 1s so far
    # dp[i][j][1] stores the max num of vertical 1s so far
    # dp[i][j][2] stores the max num of diagonal 1s so far
    # dp[i][j][3] stores the max num of anti-diagonal 1s so far
    dp = [[[0] * 4 for _ in range(cols)] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if mat[r][c]:
                # Horizontal
                dp[r][c][0] = 1 + (dp[r][c - 1][0] if c > 0 else 0)
                # Vertical
                dp[r][c][1] = 1 + (dp[r - 1][c][1] if r > 0 else 0)
                # Diagonal
                dp[r][c][2] = 1 + (dp[r - 1][c - 1][2] if r > 0 and c > 0 else 0)
                # Anti-diagonal
                dp[r][c][3] = 1 + (dp[r - 1][c + 1][3] if r > 0 and c < cols - 1 else 0)

    return max([max(v) for col in dp for v in col])


def dp2d_iter(mat: List[List[int]]) -> int:
    # Dynamic programming - Iterative
    # Time complexity: O(mn)
    # Time complexity: O(n)

    rows, cols = len(mat), len(mat[0])

    # In `dp3d_iter` we only used the last row of the `dp` 3d-matrix,
    # so we can optimize the space using a
    # 2D matrix to store the max num of 1s
    # dp[c][0] stores the max num of horizontal 1s so far
    # dp[c][1] stores the max num of vertical 1s so far
    # dp[c][2] stores the max num of diagonal 1s so far
    # dp[c][3] stores the max num of anti-diagonal 1s so far
    dp = [[0, 0, 0, 0] for _ in range(cols)]

    max_ones = 0
    for r in range(rows):
        prev = 0
        for c in range(cols):
            if mat[r][c]:
                # Horizontal
                dp[c][0] = 1 + (dp[c - 1][0] if c > 0 else 0)
                # Vertical
                dp[c][1] = 1 + (dp[c][1] if r > 0 else 0)
                # Diagonal
                # (prev value stored in `prev`, to avoid conflicts
                # with the horizontal check, which uses `c-1` as well)
                curr = dp[c][2]
                dp[c][2] = 1 + (prev if r > 0 and c > 0 else 0)
                prev = curr
                # Anti-diagonal
                dp[c][3] = 1 + (dp[c + 1][3] if r > 0 and c < cols - 1 else 0)
                max_ones = max(max_ones, *dp[c])
            else:
                prev = dp[c][2]
                dp[c] = [0, 0, 0, 0]

    return max_ones


if __name__ == "__main__":
    print("-" * 60)
    print("Longest line of consecutive one in matrix")
    print("-" * 60)

    test_cases = [
        ([[0]], 0),
        ([[1]], 1),
        ([[1, 0, 1]], 1),
        ([[1, 1, 1]], 3),
        ([[1], [1], [1]], 3),
        ([[0, 0, 1], [0, 1, 1], [0, 1, 1]], 3),
        ([[0, 0, 1], [0, 1, 1], [1, 1, 1]], 3),
        ([[0, 0, 1], [1, 0, 1], [1, 1, 1]], 3),
        ([[1, 0, 1], [1, 1, 0], [0, 1, 1]], 3),
        ([[0, 0, 1], [1, 1, 0], [1, 0, 1]], 3),
        (
            [
                [0, 1, 0, 1, 1],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 1, 0],
                [1, 0, 1, 1, 1],
                [1, 0, 0, 0, 1],
            ],
            3,
        ),
        (
            [
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 1, 0, 0, 0, 1],
                [0, 0, 0, 1, 1, 0, 0, 1],
                [1, 1, 0, 1, 0, 1, 0, 1],
                [0, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 1, 1, 0, 0, 0, 1],
            ],
            5,
        ),
    ]

    for mat, solution in test_cases:

        print("Matrix:")
        print_matrix(mat)

        result = brute_force(deepcopy(mat))
        output = f"     brute_force = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp3d_iter(deepcopy(mat))
        output = f"       dp3d_iter = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp2d_iter(deepcopy(mat))
        output = f"       dp2d_iter = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
