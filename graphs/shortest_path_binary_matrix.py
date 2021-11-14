"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/

Given an n x n binary matrix grid, return the length of the 
shortest clear path in the matrix. If there is no clear path, 
return -1.

A clear path in a binary matrix is a path from the top-left 
cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) 
such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected 
(i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example 2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example 3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1

Constraints:
n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""


from collections import deque
from random import randint
from copy import deepcopy
import time


def print_matrix(mat):
    print()
    for row in mat:
        print(" ".join(["." if v == 0 else "#" for v in row]))
    print()


def bfs(grid: list) -> int:
    # BFS shortest path

    # Lenght of the nxn grid
    n = len(grid)
    end = n - 1

    # Edge case
    if grid[0][0] == 1 or grid[end][end] == 1:
        # The start or the end are blocked,
        # no path
        return -1

    # 8 possible directions from a given node (including diagonals)
    udir = [-1, 0, 1]
    directions = [(x, y) for x in udir for y in udir if x != 0 or y != 0]
    # directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    # Queue of tuples: (x, y, distance)
    queue = deque([(0, 0, 1)])

    # Update the starting node as visited (obstacle)
    grid[0][0] = 2

    # Loop over until the queue is empty
    while queue:
        x, y, dist = queue.popleft()

        if x == end and y == end:
            return dist

        # Loop over the possible next steps
        for dx, dy in directions:
            # New location (nx, ny)
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:

                # Update the grid in the current new node
                # with a 2 (visited) to avoid
                # the need of an additional list of visited nodes
                # grid[x][y] = 2 # NOO!
                #   --> neighbors can be visited multiple times
                #       until they're popped from the queue
                grid[nx][ny] = 2

                # If the new location is within the boundaries,
                # and there's no obstacle,
                # add the new node to the queue
                queue.append((nx, ny, dist + 1))

    # If the end wasn't reached, it's inaccessible
    return -1


def bfs2(grid: list) -> int:
    # BFS shortest path

    # Lenght of the nxn grid
    n = len(grid)
    end = n - 1

    # Edge case
    if grid[0][0] == 1 or grid[end][end] == 1:
        # The start or the end are blocked,
        # no clear path
        return -1

    # 8 possible directions from a given node (including diagonals)
    udir = [-1, 0, 1]
    directions = [(x, y) for x in udir for y in udir if x != 0 or y != 0]
    # directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

    # Queue of tuples: (x, y)
    queue_x = deque([0])
    queue_y = deque([0])
    # Resulting distance at a given BFS layer
    dist = 0
    # Update the starting node as visited (obstacle)
    grid[0][0] = 2

    # Loop over until the queue is empty
    while queue_x:

        # Size and travelled distance for the current layer in the queue
        size = len(queue_x)
        dist += 1

        for _ in range(size):
            x, y = queue_x.popleft(), queue_y.popleft()

            if x == end and y == end:
                return dist

            # Loop over the possible next steps
            for dx, dy in directions:
                # New location (nx, ny)
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    # Update the grid in the current new node
                    # with a 2 (visited) to avoid
                    # the need of an additional list of visited nodes
                    # grid[x][y] = 2 # NOO!
                    #   --> neighbors can be visited multiple times
                    #       until they're popped from the queue
                    grid[nx][ny] = 2

                    # If the new location is within the boundaries,
                    # and there's no obstacle,
                    # add the new node to the queue
                    queue_x.append(nx)
                    queue_y.append(ny)

    # If the end wasn't reached, it's inaccessible
    return -1


if __name__ == "__main__":
    print("-" * 60)
    print("Shortest path in binary matrix")
    print("-" * 60)

    test_cases = [
        # ( matrix, solution )
        ([[1]], -1),
        ([[0]], 1),
        ([[0, 1], [1, 0]], 2),
        ([[0, 0, 0], [0, 1, 1], [0, 0, 0]], 4),
        ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
        ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
    ]

    for i, (matrix, solution) in enumerate(test_cases):

        result = bfs(deepcopy(matrix))
        string = f" bfs({i}) = "
        string += " " * (5 - len(string))
        string += f"{result:>4}"
        string += " " * (60 - len(string))
        string += f'\t\tTest: {"OK" if solution == result else "NOT OK"}'
        print(string)

        result = bfs2(deepcopy(matrix))
        string = f"bfs2({i}) = "
        string += " " * (5 - len(string))
        string += f"{result:>4}"
        string += " " * (60 - len(string))
        string += f'\t\tTest: {"OK" if solution == result else "NOT OK"}'
        print(string)

        print()

    print("\n>> Graphical example:")

    size = 40
    nodes = size * size
    random_grid = [[0 for i in range(size)] for j in range(size)]
    for i in range(nodes * 3 // 5):
        random_grid[randint(0, size - 1)][randint(0, size - 1)] = 1
    random_grid[0][0] = 0
    random_grid[size - 1][size - 1] = 0

    print_matrix(random_grid)

    t = time.time()
    res = bfs(deepcopy(random_grid))
    t = time.time() - t
    print("BSF  - Steps needed:", res, f"\t{t*1e6:>5.0f} μs")

    t = time.time()
    res = bfs2(deepcopy(random_grid))
    t = time.time() - t
    print("BSF2 - Steps needed:", res, f"\t{t*1e6:>5.0f} μs")
