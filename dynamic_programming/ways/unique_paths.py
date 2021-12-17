"""
https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid 
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point 
in time. The robot is trying to reach the bottom-right 
corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to 
reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Example 3:
Input: m = 7, n = 3
Output: 28

Example 4:
Input: m = 3, n = 3
Output: 6

Constraints:
1 <= m, n <= 100
It's guaranteed that the answer will be less than or 
equal to 2 * 10^9.
"""


def bf_recursion(rows: int, cols: int) -> int:
    # Brute force - recursion
    # Time complexity: O(2^(m+n))
    # Space complexity: O(m+n))

    def recursion(r: int, c: int) -> int:
        # Recursive function

        # Base cases
        if r >= rows or c >= cols:
            # Out-of-bounds
            return 0
        if r == rows - 1 and c == cols - 1:
            # Destination reached
            return 1

        return recursion(r + 1, c) + recursion(r, c + 1)

    # Call the recursive function
    return recursion(0, 0)


def dp_recursion(rows: int, cols: int) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(m*n)
    # Space complexity: O(m*n)
    memo = dict()

    def recursion(r: int, c: int) -> int:
        # Recursive function

        # Base cases
        if r >= rows or c >= cols:
            # Out-of-bounds
            return 0
        if r == rows - 1 and c == cols - 1:
            # Destination reached
            return 1
        if (r, c) in memo:
            return memo[(r, c)]

        memo[(r, c)] = recursion(r + 1, c) + recursion(r, c + 1)
        return memo[(r, c)]

    # Call the recursive function
    return recursion(0, 0)


def dp_iter(rows: int, cols: int) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(m*n)
    # Space complexity: O(m*n)

    # Table to keep track of the results
    table = [[0] * cols for _ in range(rows)]
    # Loop over the rows
    for row in range(rows):
        # Loop over the columns
        for col in range(cols):
            # Number of paths to move from (0, 0) to (row, col)
            if row == 0 and col == 0:
                # If at the origin, 1
                table[row][col] = 1
            elif row == 0:
                # If at row 0, the same as in the previous column
                # (there's no other way you can get there
                # with only down-right valid movements)
                table[row][col] = table[row][col - 1]
            elif col == 0:
                # If at col 0, the same as the previous row
                table[row][col] = table[row - 1][col]
            else:
                # Any other cell, combination of both:
                # - cell at the top (row - 1)
                # - cell at the left (col - 1)
                table[row][col] = table[row - 1][col] + table[row][col - 1]

    # Return the value at the bottom right cell
    return table[rows - 1][cols - 1]


def dp_iter_opt(rows: int, cols: int) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(m*n)
    # Space complexity: O(n)
    # Space optimiaztion: since we only need access
    # to the previous two rows for a given cell, we can reduce
    # the space complexity by storing only two rows
    # instead of the whole matrix.

    # Table to keep track of the results
    curr, prev = [0] * cols, [0] * cols
    # Loop over the rows
    for row in range(rows):
        # Loop over the columns
        for col in range(cols):
            # Number of paths to move from (0, 0) to (row, col)
            if row == 0 and col == 0:
                # If at the origin, 1
                curr[col] = 1
            elif row == 0:
                # If at row 0, the same as in the previous column
                # (there's no other way you can get there
                # with only down-right valid movements)
                curr[col] = curr[col - 1]
            elif col == 0:
                # If at col 0, the same as the previous row
                curr[col] = prev[col]
            else:
                # Any other cell, combination of both:
                # - cell at the top (row - 1)
                # - cell at the left (col - 1)
                curr[col] = prev[col] + curr[col - 1]

        # The current row `curr` now becomes `prev` for the
        # next iteration
        prev = curr[:]

    # Return the value at the bottom right cell
    return curr[-1]


if __name__ == "__main__":
    print("-" * 60)
    print("Unique paths")
    print("-" * 60)

    test_cases = [
        (1, 1, 1),
        (2, 1, 1),
        (2, 2, 2),
        (7, 3, 28),
        (3, 7, 28),
        (7, 7, 924),
    ]

    for rows, cols, solution in test_cases:

        result = bf_recursion(rows, cols)
        string = f" bf_recursion{rows, cols} = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = dp_recursion(rows, cols)
        string = f" dp_recursion{rows, cols} = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = dp_iter(rows, cols)
        string = f"      dp_iter{rows, cols} = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = dp_iter_opt(rows, cols)
        string = f"  dp_iter_opt{rows, cols} = "
        string += " " * (25 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
