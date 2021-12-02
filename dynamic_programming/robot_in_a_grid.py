"""
CRACKING THE CODING INTERVIEW
8.2 Robot in a grid:
Imagine a robot sitting on the upper left corner of a grid with
r rows and c columns. The robot can only move in two directions,
right and down, but certain cells are "off limits" such that 
the robot cannot step on them. Design an algorithm to find
a path for the robot from the top left to the bottom right.
"""
from collections import defaultdict


def brute_force(grid: list) -> list:
    # Time complexity: O(2^(r+c)),
    # where r and c are the rows and columns
    # (each path has r+c steps and there are two choices
    # we can make at each step).

    # Start from the last cell, and work backwards to
    # find a path from the origin
    rows = len(grid)
    if grid is None or len(grid) == 0:
        return None
    cols = len(grid[0])

    def get_path(grid: list, row: int, col: int, path: list) -> list:
        # Recursive function

        # Base case: boundary and obstacle check
        if row < 0 or col < 0 or grid[row][col] == 0:
            return False

        is_origin = row == 0 and col == 0

        if (
            is_origin
            or get_path(grid, row, col - 1, path)
            or get_path(grid, row - 1, col, path)
        ):
            path.append((row, col))
            # print(f"{row,col} -> {path}")
            return True

        return False

    path = list()
    if get_path(grid, rows - 1, cols - 1, path):
        return path

    return None


def dp_recursion(grid: list) -> list:
    # Time complexity: O(r+c)
    # Optimizes the previous exponential algorithm
    # by finding duplicate work.
    # Strategy: same as brute force, but keeping track
    # of the cells already visited to avoid revisiting them
    # and reduce the time complexity.

    if grid is None or len(grid) == 0:
        return None

    memo = defaultdict(bool)

    def get_path(grid: list, row: int, col: int, path: list) -> list:
        # Recursive function

        # Base case: boundary and obstacle checking
        if row < 0 or col < 0 or grid[row][col] == 0:
            return False

        # Check if the current cell has already been visited
        if (row, col) in memo:
            return memo[(row, col)]

        # Check if the current cell is the origin or
        # belong to a path to the origin
        is_origin = row == 0 and col == 0
        if (
            is_origin
            or get_path(grid, row, col - 1, path)
            or get_path(grid, row - 1, col, path)
        ):
            # print(f"{row,col} -> {path}")
            memo[(row, col)] = True
            path.append((row, col))
            return True

        # If the current cell doesn't belong to a path
        # to the origin, register it in the hashtable
        # and return false
        memo[(row, col)] = False
        return False

    path = list()
    rows, cols = len(grid), len(grid[0])

    # Call the recursive function
    if get_path(grid, rows - 1, cols - 1, path):
        return path

    return None


def dp_iterative(grid: list) -> list:
    pass


if __name__ == "__main__":
    print("-" * 60)
    print("Robot in a grid")
    print("-" * 60)

    test_cases = [
        ([[1, 1], [0, 1]], [(0, 0), (0, 1), (1, 1)]),
        ([[1, 1, 0], [0, 1, 1], [0, 0, 1]], [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]),
        ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]),
        ([[1, 0, 0], [0, 1, 1], [0, 0, 1]], None),
    ]

    for grid, solution in test_cases:

        string = f" brute_force = "
        string += " " * (25 - len(string))
        result = brute_force(grid)
        string += str(result)
        string += " " * (65 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"dp_recursion = "
        string += " " * (25 - len(string))
        result = dp_recursion(grid)
        string += str(result)
        string += " " * (65 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        # string = f"dp_iterative({num}) = "
        # string += " " * (25 - len(string))
        # result = dp_iterative(num)
        # string += str(result)
        # string += " " * (60 - len(string))
        # print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
