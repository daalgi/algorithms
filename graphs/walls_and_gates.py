"""
https://www.lintcode.com/problem/663/

You are given a m x n 2D grid initialized 
with these three possible values.
    -1 - A wall or an obstacle.
    0 - A gate.
    INF - Infinity means an empty room. 
    We use the value 2^31 - 1 = 2147483647 to 
    represent INF as you may assume that the 
    distance to a gate is less than 2147483647.

Fill each empty room with the distance to its 
nearest gate. If it is impossible to reach a 
Gate, that room should remain filled with INF.

Example1
Input:
[
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]
]
Output:
[
    [3,-1,0,1],
    [2,2,1,-1],
    [1,-1,2,-1],
    [0,-1,3,4]
]
Explanation:
the 2D grid is:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
the answer is:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

Example2
Input:
[
    [0,-1],
    [2147483647,2147483647]
]
Output:
[
    [0,-1],
    [1,2]
]
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
    # Space complexity: O(mn)

    def explore_neighbors(row: int, col: int) -> None:
        # BFS iterative algorithm to explore the neighbors
        # Queue (dist, row, col)
        q = deque([(0, row, col)])
        while q:
            dist, r, c = q.popleft()
            dist += 1
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if (
                    # Check boundaries
                    0 <= nr < rows
                    and 0 <= nc < cols
                    # Check that the next cell wasn't reached
                    # before by a closer door
                    and grid[nr][nc] > dist
                ):
                    grid[nr][nc] = dist
                    q.append((dist, nr, nc))

    moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
    # Loop over the cells of the grid
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 0:
                # If it's a gate, BFS to explore the neighboring 
                # cells and update the distance of each reachable
                # cell (only if there's no closer gate)
                explore_neighbors(row, col)
    return grid


if __name__ == "__main__":
    print("-" * 60)
    print("Walls and gates")
    print("-" * 60)

    test_cases = [
        # (grid, solution)
        # 0: gate
        # -1: wall/obstacle
        # "x":  empty room
        # (later transformed into float("inf") for the algorithm)
        (
            [
                [0, -1],
                ["x", "x"],
            ],
            [
                [0, -1],
                [1, 2],
            ],
        ),
        (
            [
                [0, -1, "x"],
                [-1, -1, "x"],
                [0, "x", "x"],
            ],
            [
                [0, -1, 4],
                [-1, -1, 3],
                [0, 1, 2],
            ],
        ),
        (
            [
                ["x", "x", "x", -1, 0],
                ["x", "x", 0, -1, "x"],
                ["x", "x", "x", "x", "x"],
                [0, -1, -1, -1, 0],
            ],
            [
                [3, 2, 1, -1, 0],
                [2, 1, 0, -1, 1],
                [1, 2, 1, 2, 1],
                [0, -1, -1, -1, 0],
            ],
        ),
    ]

    for i, (grid, solution) in enumerate(test_cases):

        print("\nGrid:")
        if i == 0 or test_cases[i - 1][0] != grid:
            print_matrix(grid)

        grid = [
            [v if isinstance(v, int) else float("inf") for v in row] for row in grid
        ]
        result = bfs_iterative(deepcopy(grid))
        output = f"        bfs_iterative = "
        output += " " * (40 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print("\nAfter the conquer:")
        print_matrix(result)

        print()
