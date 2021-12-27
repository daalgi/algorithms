"""
https://leetcode.com/problems/dungeon-game/

The demons had captured the princess and imprisoned her in 
the bottom-right corner of a dungeon. The dungeon consists 
of m x n rooms laid out in a 2D grid. Our valiant knight was 
initially positioned in the top-left room and must fight his 
way through dungeon to rescue the princess.

The knight has an initial health point represented by a 
positive integer. If at any point his health point drops 
to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by 
negative integers), so the knight loses health upon entering 
these rooms; other rooms are either empty (represented as 0) 
or contain magic orbs that increase the knight's health 
(represented by positive integers).

To reach the princess as quickly as possible, the knight 
decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can 
rescue the princess.

Note that any room can contain threats or power-ups, even 
the first room the knight enters and the bottom-right room 
where the princess is imprisoned.

Example 1:
Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at 
least 7 if he follows the optimal path: 
RIGHT-> RIGHT -> DOWN -> DOWN.

Example 2:
Input: dungeon = [[0]]
Output: 1

Constraints:
m == dungeon.length
n == dungeon[i].length
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000
"""
from typing import List
from copy import deepcopy
from functools import lru_cache


def print_matrix(mat):
    print()
    for row in mat:
        print("   " + " ".join(f"{v:>3}" for v in row))
    print()


def dp_memoization(dungeon: List[List[int]]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(mn)

    @lru_cache(maxsize=None)
    def dfs(r: int, c: int) -> int:
        # Depth First Search recursive function

        # Base cases
        # Out-of-bounds
        if r == rows or c == cols:
            return float("inf")
        # Destination reached
        if r == rows - 1 and c == cols - 1:
            return 1 if dungeon[r][c] >= 0 else -dungeon[r][c] + 1

        # Compute the current two possibilities
        go_down = dfs(r + 1, c)
        go_right = dfs(r, c + 1)

        # Current minimum health required
        min_health_req = -dungeon[r][c] + min(go_down, go_right)

        # If `min_health_req` is negative means that we found magic orbs
        # and gain health points, so we don't need extre health to
        # survive from here to the end
        if min_health_req <= 0:
            return 1
        # If `min_health_req` is positive, we need that extra health to
        # survive the path from here to the end
        return min_health_req

    rows, cols = len(dungeon), len(dungeon[0])
    return dfs(0, 0)


def dp_tabulation(dungeon: List[List[int]]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(mn)

    rows, cols = len(dungeon), len(dungeon[0])
    last_row, last_col = rows - 1, cols - 1
    # DP table that keeps track of the minimum required health to survive
    # at each cell (r, c)
    dp = [[0] * cols for _ in range(rows)]

    # Last cell (princess location)
    dp[last_row][last_col] = 1 + max(0, -dungeon[last_row][last_col])

    # Last row, coming from the last cell (we could only get there
    # by going `right`)
    for c in range(last_col - 1, -1, -1):
        dp[last_row][c] = max(1, dp[last_row][c + 1] - dungeon[last_row][c])

    # Last column, coming from the last cell (we could only get there
    # by going `down`)
    for r in range(last_row - 1, -1, -1):
        dp[r][last_col] = max(1, dp[r + 1][last_col] - dungeon[r][last_col])

    # Explore the interior cells
    for r in range(last_row - 1, -1, -1):
        for c in range(last_col - 1, -1, -1):
            needed_health = min(dp[r][c + 1], dp[r + 1][c]) - dungeon[r][c]
            dp[r][c] = max(1, needed_health)

    # print_matrix(dp)
    return dp[0][0]


def dp_tabulation2(dungeon: List[List[int]]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(mn)

    rows, cols = len(dungeon), len(dungeon[0])

    # DP table with one additional row and column to make
    # the implementation cleaner.
    # Initialize all the cells to a large number instead of 0s
    # to avoid selecting the auxiliary row and column cells
    # when doing `min(dp[r][c+1], dp[r+1][c])`
    dp = [[float("inf")] * (cols + 1) for _ in range(rows + 1)]

    # Cell below princess location
    dp[rows][cols - 1] = 1
    # Cell to the right of princess location
    dp[rows - 1][cols] = 1

    # Loop over all the cells,
    # from the princess location (last_row, last_col)
    # to the first cell (0, 0)
    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            needed_health = min(dp[r][c + 1], dp[r + 1][c]) - dungeon[r][c]
            dp[r][c] = max(1, needed_health)

    # print_matrix(dp)
    return dp[0][0]


def dp_tabulation_opt(dungeon: List[List[int]]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(mn)
    # Space complexity: O(1)
    # Modify the input list `dungeon` to store partial results

    rows, cols = len(dungeon), len(dungeon[0])

    # Last cell (princess location)
    dungeon[rows - 1][cols - 1] = 1 + max(0, -dungeon[rows - 1][cols - 1])

    # Last row
    for c in range(cols - 2, -1, -1):
        dungeon[rows - 1][c] = max(1, dungeon[rows - 1][c + 1] - dungeon[rows - 1][c])

    # Last col
    for r in range(rows - 2, -1, -1):
        dungeon[r][cols - 1] = max(1, dungeon[r + 1][cols - 1] - dungeon[r][cols - 1])

    # Rest of the cells
    for r in range(rows - 2, -1, -1):
        for c in range(cols - 2, -1, -1):
            dungeon[r][c] = max(
                1, min(dungeon[r + 1][c], dungeon[r][c + 1]) - dungeon[r][c]
            )

    # print_matrix(dungeon)
    return dungeon[0][0]


if __name__ == "__main__":
    print("-" * 60)
    print("Dungeon game")
    print("-" * 60)

    test_cases = [
        ([[0]], 1),
        ([[1]], 1),
        ([[-1]], 2),
        ([[1, 2, 3], [4, 5, 6]], 1),
        ([[1, -2, -3], [-4, -5, -1]], 6),
        ([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7),
        ([[-2, -3, 3], [-5, -10, 1], [-10, 30, -2]], 6),
    ]

    for grid, solution in test_cases:

        print("Grid:")
        print_matrix(grid)

        result = dp_memoization(deepcopy(grid))
        output = f"\t      dp_memoization = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation(deepcopy(grid))
        output = f"\t       dp_tabulation = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation2(deepcopy(grid))
        output = f"\t      dp_tabulation2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation_opt(deepcopy(grid))
        output = f"\t   dp_tabulation_opt = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
