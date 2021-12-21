"""
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many 
distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:

1 <= n <= 45
"""
from functools import lru_cache


def brute_force(n: int) -> int:
    # Brute force
    # Time complexity: O(2^n)
    pass


@lru_cache(maxsize=None)
def dp_memoization(n: int) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n)
    # Time complexity: O(n)

    # Base cases
    if n <= 3:
        return n
    return dp_memoization(n - 1) + dp_memoization(n - 2)


def dp_tabulation(n: int) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Base case
    if n <= 3:
        return n

    # Table to keep partial results
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    # Loop over up to the steps
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


def dp_tabulation_opt(n: int) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Space complexity optimization, keeping track only of the
    # two previous steps instead of the whole `dp` list

    # Base case
    if n <= 3:
        return n

    # Table to keep partial results
    prev = 2  # step 2
    curr = 3  # step 3

    # Loop over up to the steps
    for _ in range(4, n + 1):
        curr, prev = curr + prev, curr

    return curr


if __name__ == "__main__":
    print("-" * 60)
    print("Climbing stairs")
    print("-" * 60)

    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (5, 8),
        (8, 34),
        (13, 377),
        (25, 121393),
        (45, 1836311903),
        (50, 20365011074),
    ]

    for n, solution in test_cases:

        result = dp_memoization(n)
        output = f"    dp_memoization({n}) = "
        output += " " * (45 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation(n)
        output = f"     dp_tabulation({n}) = "
        output += " " * (45 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation_opt(n)
        output = f" dp_tabulation_opt({n}) = "
        output += " " * (45 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
