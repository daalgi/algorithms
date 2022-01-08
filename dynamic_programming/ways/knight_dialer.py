"""
https://leetcode.com/problems/knight-dialer/

The chess knight has a unique movement, it may move two 
squares vertically and one square horizontally, or two 
squares horizontally and one square vertically (with both 
forming the shape of an L). The possible movements of 
chess knight are shown in this diagaram:

A chess knight can move as indicated in the chess diagram below:

We have a chess knight and a phone pad as shown below, 
the knight can only stand on a numeric cell (i.e. blue cell).

Given an integer n, return how many distinct phone numbers of 
length n we can dial.

You are allowed to place the knight on any numeric cell 
initially and then you should perform n - 1 jumps to dial 
a number of length n. All jumps should be valid knight jumps.

As the answer may be very large, return the answer modulo 109 + 7.

Example 1:
Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, 
so placing the knight over any numeric cell of 
the 10 cells is sufficient.

Example 2:
Input: n = 2
Output: 20
Explanation: All the valid number we can dial are 
[04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 
60, 61, 67, 72, 76, 81, 83, 92, 94]

Example 3:
Input: n = 3131
Output: 136006598
Explanation: Please take care of the mod.

Constraints:
1 <= n <= 5000
"""
from functools import lru_cache
from typing import List


def sequences(n: int) -> List[int]:
    def yield_sequences(start: int, num_hoops: int, sequence: List[int]):
        if num_hoops == 0:
            yield "".join(str(s) for s in sequence)
            return

        for neighbor in neighbors[start]:
            yield from yield_sequences(neighbor, num_hoops - 1, sequence + [neighbor])

    neighbors = {
        1: (6, 8),
        2: (7, 9),
        3: (4, 8),
        4: (3, 9, 0),
        5: tuple(),
        6: (1, 7, 0),
        7: (2, 6),
        8: (1, 3),
        9: (4, 2),
        0: (4, 6),
    }
    res = []
    for nei in neighbors:
        res += yield_sequences(nei, n - 1, [nei])

    return res


def brute_force(n: int) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(2^n)
    # Space complexity: O(1)
    pass


def dp_memoization(n: int) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(10n) = O(n)
    # Space complexity: O(10n) = O(n)

    @lru_cache(maxsize=None)
    def dfs(r: int, c: int, left: int) -> int:
        # Depth First Search recursive function

        # Base cases
        # Out-of-bounds or invalid move
        if not 0 <= r < 4 or not 0 <= c < 3 or (r == 3 and c != 1):
            return 0

        if left == 0:
            return 1

        left -= 1
        # Explore the new moves
        count = 0
        for dr, dc in moves:
            count += dfs(r + dr, c + dc, left)
        return count

    # Knight valid relative moves (row, col)
    # Note: since here the grid is very limited in size,
    # we can predict the valid next moves for each cell,
    # and avoid exploring all the possible moves
    # (see `dp_memoization2`)
    moves = (
        (1, 2),
        (1, -2),
        (-1, 2),
        (-1, -2),
        (2, 1),
        (2, -1),
        (-2, 1),
        (-2, -1),
    )
    # Loop over the possible starting keys
    count = 0
    for r in range(4):
        for c in range(3):
            if r == 3 and c != 1:
                continue
            count += dfs(r, c, n - 1)

    return count % 1000000007


def dp_memoization2(n: int) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n)
    # Space complexity: O(n)

    @lru_cache(maxsize=None)
    def dfs(key: int, left: int) -> int:
        # Depth First Search recursive function

        # Base case
        # No moves left
        if left == 0:
            return 1

        left -= 1
        count = 0
        for nei in neighbors[key]:
            count += dfs(nei, left)
        return count

    # For each key we can return the valid next moves
    # manually in a dictionary
    neighbors = {
        1: (6, 8),
        2: (7, 9),
        3: (4, 8),
        4: (3, 9, 0),
        5: tuple(),
        6: (1, 7, 0),
        7: (2, 6),
        8: (1, 3),
        9: (4, 2),
        0: (4, 6),
    }
    count = 0
    for nei in neighbors:
        count += dfs(nei, n - 1)
    return count % 1000000007


def dp_tabulation(n: int) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(n)
    # Space complexity: O(n)

    # For each key we can return the valid next moves
    # manually in a dictionary
    neighbors = {
        1: (6, 8),
        2: (7, 9),
        3: (4, 8),
        4: (3, 9, 0),
        5: tuple(),
        6: (1, 7, 0),
        7: (2, 6),
        8: (1, 3),
        9: (4, 2),
        0: (4, 6),
    }

    # Table to keep track of the counts for each move (row)
    # and starting from each key (column)
    dp = [[0] * 10 for _ in range(n)]
    # For one move, we can exactly reach only one key,
    # the one we start from
    dp[0] = [1] * 10

    for move in range(1, n):
        for start in range(10):
            for neighbor in neighbors[start]:
                dp[move][neighbor] += dp[move - 1][start]

    return sum(dp[-1]) % 1000000007


def dp_tabulation_opt(n: int) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Strategy: space optimization taking into account that we only
    # need the results from the previous `move` iteration

    # For each key we can return the valid next moves
    # manually in a dictionary
    neighbors = {
        1: (6, 8),
        2: (7, 9),
        3: (4, 8),
        4: (3, 9, 0),
        5: tuple(),
        6: (1, 7, 0),
        7: (2, 6),
        8: (1, 3),
        9: (4, 2),
        0: (4, 6),
    }

    # Instead of a 2d table, we can use two rows to keep track
    # of the previous and the current count.
    # `prev` initialize to ones
    prev = [1] * 10
    curr = prev
    for moves in range(1, n):
        curr = [0] * 10
        for start in range(10):
            for neighbor in neighbors[start]:
                curr[neighbor] += prev[start]

        # Update the reference to the arrays
        prev = curr
    return sum(curr) % 1000000007


if __name__ == "__main__":
    print("-" * 60)
    print("Knight dialer")
    print("-" * 60)

    test_cases = [
        # (n, solution)
        (1, 10),
        (2, 20),
        (3, 46),
        (13, 180288),
        (25, 715338219),
        (5000, 406880451),
    ]

    for n, solution in test_cases:

        print("n:", n)
        if n < 4:
            print("Sequences:")
            seq = sequences(n)
            seq_str = str(sorted(seq))
            if len(seq_str) > 60:
                seq_str = seq_str[:55] + " ...]"
            print(seq_str)

        if n < 100:
            result = dp_memoization(n)
            output = f"      dp_memoization = "
            output += " " * (10 - len(output))
            test_ok = solution == result
            output += str(result)
            output += " " * (50 - len(output))
            output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
            print(output)

            result = dp_memoization2(n)
            output = f"     dp_memoization2 = "
            output += " " * (10 - len(output))
            test_ok = solution == result
            output += str(result)
            output += " " * (50 - len(output))
            output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
            print(output)

        result = dp_tabulation(n)
        output = f"       dp_tabulation = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation_opt(n)
        output = f"   dp_tabulation_opt = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
