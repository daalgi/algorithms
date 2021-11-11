"""
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map 
of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting 
adjacent lands horizontally or vertically. You may assume all 
four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""


def recursion_dfs(matrix: list) -> int:
    # Time complexity: O(m * n)
    # Worst case: O(m * n + m * n)
    # Space complexity: O(m * n)

    # Size of the matrix
    rows, cols = len(matrix), len(matrix[0])

    # Tuple of possible movement directions
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    # Set of tuples to keep track of the visited cells
    visited = set()

    def dfs(r: int, c: int) -> int:
        # Recursive DFS

        # Base case: already visited cell
        if (r, c) in visited:
            return

        # Register the location as visited to avoid future revisits
        visited.add((r, c))

        # Loop over the possible movements from the current cell
        for dr, dc in directions:
            # New cell location
            nr, nc = r + dr, c + dc

            # Check the new location
            if 0 <= nr < rows and 0 <= nc < cols:
                # If the new location is within the boundaries
                if matrix[nr][nc] == 1:
                    # If the new location is earth,
                    # continue the exploration for the current path
                    dfs(nr, nc)

    # Loop over the rows and columns of the grid to identify
    # the number of islands
    ans = 0
    for row in range(rows):
        for col in range(cols):
            if (row, col) not in visited and matrix[row][col] == 1:
                # If the current cell hasn't been visited and
                # is earth, call the recursive function to visit
                # the contiguous earth-cells
                dfs(row, col)
                # Add one island
                ans += 1

    return ans


if __name__ == "__main__":
    print("-" * 60)
    print("Number of islands")
    print("-" * 60)

    test_cases = [
        # (matrix, solution)
        (
            [
                [1],
            ],
            1,
        ),
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
            1,
        ),
        (
            [
                [1, 1, 1, 1, 0],
                [1, 1, 0, 1, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            1,
        ),
        (
            [
                [1, 1, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 1],
            ],
            3,
        ),
    ]

    for i, (mat, solution) in enumerate(test_cases):

        result = recursion_dfs(mat)
        string = f"recursion({i}) = "
        string += " " * (15 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
