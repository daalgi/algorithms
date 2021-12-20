"""
https://leetcode.com/problems/domino-and-tromino-tiling/

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. 
You may rotate these shapes.

Given an integer n, return the number of ways to tile an 2 x n board. 
Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are 
different if and only if there are two 4-directionally adjacent cells 
on the board such that exactly one of the tilings has both squares 
occupied by a tile.

Example 1:
Input: n = 3
Output: 5
Explanation: The five different ways are show above.

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 1000
"""
from functools import lru_cache


def brute_force(n: int) -> int:
    # Time complexity: O(6^n), 6 dominos/trominos possible choices
    # Space complexity: O(n)
    pass


def dp_memoization(n: int) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n)
    # Space complexity: O(n)

    @lru_cache(maxsize=None)
    def dfs(i: int, previous_gap: bool = False) -> int:
        # Base cases
        if i < 0:
            # Dominos/trominos placed outside of the board, not valid
            return 0
        if i == 0:
            # Return 1 if there's no gap; 0 if there's gap
            # equivalent to: return 1 if not previous_gap else 0
            return not previous_gap

        if previous_gap:
            # If there's a gap
            # tromino  xx --> i - 1 tiles, without gap (gap closed)
            #           x
            # h.domino xx --> i - 1 tiles, with gap (one gap closed, other opened)
            return dfs(i - 1) + dfs(i - 1, True)

        # If there's no gap:
        #   v.domino x    --> i - 1 tiles, no gap
        #            x
        #   2h.dominos xx --> i - 2 tiles, no gap
        #              xx
        #   tromino xx    --> i - 2 tiles, gap
        #           x
        #   tromino    x  --> i - 2 tiles, gap
        #              xx
        return dfs(i - 1) + dfs(i - 2) + 2 * dfs(i - 2, True)

    MOD = 1000000007
    return dfs(n, False) % MOD


def dp_tabulation(n: int) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Base cases
    if n < 3:
        return n

    # f[k]: number of ways to "fully cover a board" of width k
    f = [0] * (n + 1)
    # p[k]: number of ways to "partially cover a board" of width k
    p = [0] * (n + 1)

    # Initialize f and p with results for the base case scenarios
    f[1] = 1  # 1v.domino
    f[2] = 2  # 2v.dominoes, 2h.dominoes
    p[2] = 1  # 1tromino (leaving a gap)

    for k in range(3, n + 1):
        f[k] = f[k - 1] + f[k - 2] + 2 * p[k - 1]
        p[k] = p[k - 1] + f[k - 2]

    MOD = 1000000007
    return f[n] % MOD


if __name__ == "__main__":
    print("-" * 60)
    print("Domino and tromino tiling")
    print("-" * 60)

    test_cases = [
        (1, 1),
        (2, 2),
        (3, 5),
        (4, 11),
        (50, 451995198),
        (200, 627399438),
        (888, 970198824),
        (1000, 979232805),
    ]

    for size, solution in test_cases:

        print(f"Board shape: 2x{size}")

        if size < 300:
            result = dp_memoization(size)
            output = f"     dp_memoization = "
            output += " " * (25 - len(output))
            output += str(result)
            output += " " * (60 - len(output))
            test_ok = solution == result
            output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
            print(output)

        result = dp_tabulation(size)
        output = f"      dp_tabulation = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
