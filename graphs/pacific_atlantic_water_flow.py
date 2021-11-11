"""
https://leetcode.com/problems/pacific-atlantic-water-flow/
There is an m x n rectangular island that borders both the 
Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches 
the island's left and top edges, and the Atlantic Ocean touches 
the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are 
given an m x n integer matrix heights where heights[r][c] represents 
the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to 
neighboring cells directly north, south, east, and west if the 
neighboring cell's height is less than or equal to the current 
cell's height. Water can flow from any cell adjacent to an ocean 
into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] 
denotes that rain water can flow from cell (ri, ci) to both the 
Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 
Constraints:
m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""


def recursion_dfs(heights: list) -> list:
    # Check if the matrix is empty
    if not heights:
        return []

    # size of the matrix
    m, n = len(heights), len(heights[0])

    # Sets of tuples to keep track in which locations
    # water can flow to a given ocean
    atlantic = set()
    pacific = set()

    # Tuple of possible movement directions
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def dfs(x: int, y: int, ocean: set) -> bool:
        # Recursive DFS

        # Base case
        if (x, y) in ocean:
            # If the node's been visited
            return

        # Add the current location
        ocean.add((x, y))

        # Loop over all the directions of possible movements
        for dx, dy in directions:
            # Coordinates of the neighbor node
            new_x, new_y = x + dx, y + dy
            # Check if the new node can be added to the set
            if 0 <= new_x < m and 0 <= new_y < n:
                # If it's within the grid boundaries
                if heights[new_x][new_y] >= heights[x][y]:
                    # If the new node's height is >= than the
                    # current, the water can flow from
                    # the new to the current.
                    # In that case, call dfs with the new location.
                    dfs(new_x, new_y, ocean)

    # Checking if every single node in the grid
    # can reach both ocean: brute force O((nm)^2). From each node
    # we have to check if the neighbour's height is lower or equal,
    # and then try to reach both oceans.

    # Alternatively, we can check from the nodes touching
    # each the ocean, what other nodes are reachable
    # (higher or equal height). Then, if a node is reachable
    # from both seas, return it.

    # Loop over vertical borders
    for row in range(m):
        dfs(row, 0, pacific)
        dfs(row, n - 1, atlantic)

    # Loop over horizontal borders
    for col in range(n):
        dfs(0, col, pacific)
        dfs(m - 1, col, atlantic)

    # The intersection of both sets are the nodes
    # from which the water can flow to both oceans
    return list(atlantic & pacific)


if __name__ == "__main__":
    print("-" * 60)
    print("Pacific Atlantic water flow")
    print("-" * 60)

    test_cases = [
        # (matrix, solution)
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            [(0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), (4, 0)],
        ),
        (
            [
                [2, 1],
                [1, 2],
            ],
            [(0, 0), (0, 1), (1, 0), (1, 1)],
        ),
        (
            [
                [2, 2, 4],
                [2, 1, 3],
                [4, 3, 3],
            ],
            [(0, 2), (2, 0)],
        ),
        (
            [
                [2, 2, 4],
                [2, 5, 3],
                [4, 3, 3],
            ],
            [(0, 2), (2, 0), (1, 1)],
        ),
    ]

    for i, (mat, solution) in enumerate(test_cases):

        res = recursion_dfs(mat)

        result = sorted(res)
        solution = sorted(solution)
        string = f"recursion({i}) = "
        string += " " * (15 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
