"""
https://leetcode.com/problems/max-area-of-island/

You are given an m x n binary matrix grid. An island is a 
group of 1's (representing land) connected 4-directionally 
(horizontal or vertical.) You may assume all four edges of 
the grid are surrounded by water.

The area of an island is the number of cells with a value 1 
in the island.

Return the maximum area of an island in grid. If there is 
no island, return 0.

Example 1:
Input: grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The answer is not 11, because the island 
must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
from typing import List
from copy import deepcopy


def print_matrix(grid: List[List[int]]):
    print()
    for row in grid:
        print("   " + " ".join(f"{v:>3}" for v in row))
    print()


def dfs_recursion(grid: List[List[int]]) -> int:
    # Time complexity: O(mn)
    # Space complexity: O(1)

    def dfs(r: int, c: int) -> int:
        # Base case: out-of-bounds or water
        if not 0 <= r < rows or not 0 <= c < cols or not grid[r][c]:
            return 0

        # Mark the current grid with a zero
        # so we don't visit it again
        grid[r][c] = 0

        # Current path size
        size = 1
        for dr, dc in moves:
            # Explore neighboring cells
            size += dfs(r + dr, c + dc)

        return size

    #
    max_size = 0

    # Define the possible moves
    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))

    # Loop over the cells of the grid
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if not grid[r][c]:
                continue
            size = dfs(r, c)
            if size > max_size:
                max_size = size

    return max_size


def dfs_recursion2(grid: List[List[int]]) -> int:
    # Time complexity: O(mn)
    # Space complexity: O(1)
    
    def dfs(r: int, c: int) -> int:
        # Base case: out-of-bounds or water
        if not 0 <= r < rows or not 0 <= c < cols or not grid[r][c]:
            return 0

        grid[r][c] = 0
        return 1 + sum(dfs(r + dr, c + dc) for dr, dc in moves)

    rows, cols = len(grid), len(grid[0])
    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
    return max(dfs(r, c) for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    print("-" * 60)
    print("Max area of island")
    print("-" * 60)

    test_cases = [
        # (grid, solution)
        (
            [
                [0],
            ],
            0,
        ),
        (
            [
                [0, 1, 0],
                [0, 0, 0],
                [0, 1, 1],
            ],
            2,
        ),
        (
            [
                [1, 1],
                [1, 1],
            ],
            4,
        ),
        (
            [
                [1, 1, 1, 1, 0],
                [1, 1, 0, 1, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            9,
        ),
        (
            [
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 1],
            ],
            4,
        ),
        (
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ],
            6,
        ),
    ]

    for i, (grid, solution) in enumerate(test_cases):

        print("\nGrid:")
        print_matrix(grid)

        result = dfs_recursion(deepcopy(grid))
        output = f"        dfs_recursion = "
        output += " " * (15 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dfs_recursion2(deepcopy(grid))
        output = f"       dfs_recursion2 = "
        output += " " * (15 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
