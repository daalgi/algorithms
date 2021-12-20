"""
https://leetcode.com/problems/knight-probability-in-chessboard/

On an n x n chessboard, a knight starts at the cell (row, column) 
and attempts to make exactly k moves. The rows and columns are 
0-indexed, so the top-left cell is (0, 0), and the bottom-right 
cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated 
below. Each move is two cells in a cardinal direction, then one cell 
in an orthogonal direction.

Each time the knight is to move, it chooses one of eight possible moves 
uniformly at random (even if the piece would go off the chessboard) and 
moves there.

The knight continues moving until it has made exactly k moves or has moved 
off the chessboard.

Return the probability that the knight remains on the board after it has 
stopped moving.

Example 1:
Input: n = 3, k = 2, row = 0, column = 0
Output: 0.06250
Explanation: There are two moves (to (1,2), (2,1)) that will keep the 
knight on the board.
From each of those positions, there are also two moves that will keep 
the knight on the board.
The total probability the knight stays on the board is 0.0625.

Example 2:
Input: n = 1, k = 0, row = 0, column = 0
Output: 1.00000

Constraints:
1 <= n <= 25
0 <= k <= 100
0 <= row, column <= n
"""
from functools import lru_cache


def brute_force(n: int, k: int, row_start: int, col_start: int) -> int:
    # Time complexity: O(8^k), where k = total moves
    # Space complexity: O(n)
    pass


def dp_memoization(n: int, k: int, row_start: int, col_start: int) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(kn²), where k = total moves
    # Space complexity: O(n²)

    @lru_cache(maxsize=None)
    def dfs(r: int, c: int, moves_left: int) -> int:
        # Base cases
        # If goes out of the chessboard
        if not (0 <= r < n) or not (0 <= c < n):
            return 0
        # If there're no moves left
        # (and it's inside the chessboard, checked already)
        if moves_left == 0:
            return 1

        count = 0
        for dr, dc in moves:
            count += dfs(r + dr, c + dc, moves_left - 1)
        return count

    # Edge case: no moves allowed
    if k == 0:
        return 1.0

    # Knight possible moves (dr, dc)
    moves = (
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
        (2, 1),
    )

    # Probability = moves_inside / total_moves
    return dfs(row_start, col_start, k) / (8 ** k)


def dp_tabulation(n: int, moves: int, row_start: int, col_start: int) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(kn²), where k = total moves
    # Space complexity: O(n²)
    # TODO
    pass


if __name__ == "__main__":

    print("-" * 60)
    print("Knight probability in chessboard")
    print("-" * 60)

    test_cases = [
        # (board_size, moves, row_start, col_start, solution)
        (1, 0, 0, 0, 1.0),
        (3, 2, 0, 0, 0.06250),
        (25, 50, 13, 13, 0.27258),
    ]

    for board_size, moves, row_start, col_start, solution in test_cases:

        print("Board size:", board_size)
        print("Moves:", moves)
        print("Start:", (row_start, col_start))

        result = dp_memoization(board_size, moves, row_start, col_start)
        output = f"     dp_memoization = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = round(abs(solution - result) * 1e4) < 1
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        # result = dp_tabulation(board_size, moves, row_start, col_start)
        # output = f"      dp_tabulation = "
        # output += " " * (25 - len(output))
        # output += str(result)
        # output += " " * (60 - len(output))
        # test_ok = round(abs(solution - result) * 1e4) < 1
        # output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        # print(output)

        print()
