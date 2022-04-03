"""
https://leetcode.com/problems/surrounded-regions/

Given an m x n matrix board containing 'X' and 'O', 
capture all regions that are 4-directionally 
surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's 
in that surrounded region.

Example 1:
Input: board = [
    ["X","X","X","X"],
    ["X","0","0","X"],
    ["X","X","0","X"],
    ["X","0","X","X"]
]
Output: [
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","0","X","X"]
]
Explanation: Surrounded regions should not be 
on the border, which means that any 'O' on the 
border of the board are not flipped to 'X'. 
Any 'O' that is not on the border and it is 
not connected to an 'O' on the border will be 
flipped to 'X'. Two cells are connected if they 
are adjacent cells connected horizontally or 
vertically.

Example 2:
Input: board = [["X"]]
Output: [["X"]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""
from typing import List
from copy import deepcopy
from collections import deque


def print_matrix(grid: List[List[int]]):
    print()
    for row in grid:
        print("   " + " ".join(f"{v:>3}" for v in row))
    print()


def bfs_iterative(grid: List[List[int]]) -> List[List[int]]:
    # Time complexity: O(mn)
    # Space complexity: O(1)

    def flag_unconquerable(row: int, col: int) -> None:
        # BFS iterative algorithm
        # to explore all the neighboring 0-cells
        # and flag them as unconquerable
        grid[row][col] = UNCONQUERABLE_FLAG
        q = deque([(row, col)])
        while q:
            r, c = q.popleft()

            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if (
                    # Check boundaries
                    0 <= nr < rows
                    and 0 <= nc < cols
                    # Check cell type
                    and grid[nr][nc] == 0
                ):
                    grid[nr][nc] = UNCONQUERABLE_FLAG
                    q.append((nr, nc))

    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
    # Loop over the borders of the grid to flag
    # all the 0-cells reaching the border
    # (unconquerable)
    UNCONQUERABLE_FLAG = "#"
    rows, cols = len(grid), len(grid[0])
    for row in [0, rows - 1]:
        for col in range(cols):
            if grid[row][col] == 0:
                flag_unconquerable(row, col)

    for col in [0, cols - 1]:
        for row in range(1, rows - 1):
            if grid[row][col] == 0:
                flag_unconquerable(row, col)

    # Loop over all the cells
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == UNCONQUERABLE_FLAG:
                # Return the flagged cells to their
                # original state
                grid[row][col] = 0
            elif grid[row][col] == 0:
                # Conquer the non-flagged cells
                grid[row][col] = 1

    return grid



if __name__ == "__main__":
    print("-" * 60)
    print("Surrounded regions")
    print("-" * 60)

    test_cases = [
        # (grid, solution)
        (
            [
                [0],
            ],
            [
                [0],
            ],
        ),
        (
            [
                [1, 1],
                [1, 0],
            ],
            [
                [1, 1],
                [1, 0],
            ],
        ),
        (
            [
                [0, 1, 0],
                [0, 0, 0],
                [0, 1, 1],
            ],
            [
                [0, 1, 0],
                [0, 0, 0],
                [0, 1, 1],
            ],
        ),
        (
            [
                [1, 1, 0],
                [1, 0, 1],
                [1, 1, 1],
            ],
            [
                [1, 1, 0],
                [1, 1, 1],
                [1, 1, 1],
            ],
        ),
        (
            [
                [1, 0, 1],
                [0, 1, 0],
                [1, 0, 1],
            ],
            [
                [1, 0, 1],
                [0, 1, 0],
                [1, 0, 1],
            ],
        ),
        (
            [
                [1, 1, 1, 1, 1],
                [1, 1, 0, 1, 1],
                [1, 1, 0, 1, 0],
                [0, 0, 1, 1, 0],
            ],
            [
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [1, 1, 1, 1, 0],
                [0, 0, 1, 1, 0],
            ],
        ),
        (
            [
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0],
                [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
            ],
            [
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1],
            ],
        ),
        (
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            [
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
        ),
    ]

    for i, (grid, solution) in enumerate(test_cases):

        print("\nGrid:")
        if i == 0 or test_cases[i - 1][0] != grid:
            print_matrix(grid)

        result = bfs_iterative(deepcopy(grid))
        output = f"        bfs_iterative = "
        output += " " * (40 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print("\nAfter the conquer:")
        print_matrix(result)

        print()
