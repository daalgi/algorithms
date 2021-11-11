"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
Given an m x n integers matrix, return the length of the longest 
increasing path in matrix.

From each cell, you can either move in four directions: 
left, right, up, or down. You may not move diagonally or move 
outside the boundary (i.e., wrap-around is not allowed).

Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
"""


def recursion_dfs(matrix: list) -> int:
    # Time complexity: O(m * n)
    # Space complexity: O(m * n)

    # size of the matrix
    rows, cols = len(matrix), len(matrix[0])

    # Tuple of possible movement directions
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    # Memo array to store the maximum increasing path length
    # starting at each cell
    memo = [[0 for j in range(cols)] for i in range(rows)]

    def dfs(r: int, c: int) -> int:
        # Recursive DFS

        # Base case
        if memo[r][c]:
            # Return the already calculated result
            return memo[r][c]

        # Lenght of the current path
        # (at least one cell can always be selected in the path)
        res = 1

        # Loop over the possible movement directions
        for dr, dc in directions:

            # Coordinates of the new cell
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                # If the new cell is within the boundaries

                if matrix[nr][nc] > matrix[r][c]:
                    # If the path is increasing, the length
                    # of the current path is the maximum of
                    # the current length and the length for the
                    # path after successive movements
                    res = max(res, dfs(nr, nc) + 1)

        # Update the current cell's maximum length
        memo[r][c] = res
        return res

    # Loop over the rows and columns and keep track
    # of the longest increasing path calling the recursive function
    ans = 0
    for row in range(rows):
        for col in range(cols):
            ans = max(ans, dfs(row, col))

    return ans


if __name__ == "__main__":
    print("-" * 60)
    print("Longest increasing path in a matrix")
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
                [9, 9, 4],
                [6, 6, 8],
                [2, 1, 1],
            ],
            4,
        ),
        (
            [
                [2, 1],
                [1, 2],
            ],
            2,
        ),
        (
            [
                [2, 2, 4],
                [2, 1, 3],
                [4, 3, 3],
            ],
            3,
        ),
        (
            [
                [3, 4, 5],
                [3, 2, 6],
                [2, 2, 1],
            ],
            4,
        ),
    ]

    for i, (mat, solution) in enumerate(test_cases):

        result = recursion_dfs(mat)
        string = f"recursion({i}) = "
        string += " " * (15 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
