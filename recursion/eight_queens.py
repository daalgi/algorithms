"""
CRACKING THE CODING INTERVIEW
8.12 Eight Queens:
Write an algorithm to print all ways of arranging eight queens
on an 8x8 chess board so that none of them share the same row,
column, or diagonal. In this case, "diagonal" means all diagonals,
not just the two that bisect the board.

https://leetcode.com/problems/n-queens/
The n-queens puzzle is the problem of placing n queens on an 
n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the 
n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of 
the n-queens' placement, where 'Q' and '.' both indicate a 
queen and an empty space, respectively.

Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 
4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]
"""
from typing import List


def print_board(size: int, queens: List[int] = None, initial_space: int = 20):
    if not queens:
        queens = []

    for r in range(size):
        s = " " * initial_space
        for c in range(size):
            row = -1 if c not in queens else queens.index(c)
            s += " X " if row == r else " . "
        print(s)
    print()


def backtrack(size: int) -> int:
    # `size` = board size (rows and cols), and number of queens
    # Backtrack
    # Each row will have a queen. We can recursively find
    # the appropriate columns (instead of recursively looking
    # for the correct tuples (row, column)).

    # Time complexity: O()
    # Space complexity: O()

    # List of lists to keep track of the valid solutions
    # [ [3, 2, 0, 1, ...], ... ], where each int in the
    # list of lists represents a column number of the location
    # of a queen, and its index the row number.
    res = list()

    def is_valid(row: int, col: int, columns: List[int]) -> bool:
        # If there're no other queens yet, it's a valid location
        if not columns:
            return True

        # Check compatibility with the location of the rest
        # of the queens
        for r in range(len(columns)):

            # Same row --> no need to check it,
            # not possible to repeat a row with this algorithm
            # if row == r: return False

            # Same column
            if columns[r] == col:
                return False

            # Diagonal
            if abs(row - r) == abs(col - columns[r]):
                return False

        # If all tests passed, it's a valid location
        return True

    def _backtrack(row: int, columns: List[int]):

        # Base case: all the queens placed
        if len(columns) == size:
            res.append(columns[:])
            return

        for col in range(size):
            # print('Location:', (row, col), columns)
            if is_valid(row, col, columns):

                # New valid candidate
                columns.append(col)
                # print('>>Valid location:', (row, col))

                # Explore solution
                _backtrack(row + 1, columns)

                # Revert last choice
                # (done implicitly in the new iteration)
                columns.pop()

    _backtrack(0, [])
    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Eight Queens")
    print("-" * 60)

    test_cases = [
        (1),
        (2),
        (3),
        (4),
        # (5),
        # (6),
        # (7),
        # (8),
        # (9),
    ]

    for size in test_cases:

        print(f">>> Board size: {size}x{size}")
        print_board(size)

        result = backtrack(size)

        if not result:
            print("> No solution\n\n")

        for i, columns in enumerate(result):
            print(f"\n> Solution {i:>3}:", columns, "\n")
            print_board(size, columns)
