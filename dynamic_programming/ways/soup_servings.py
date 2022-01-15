"""
https://leetcode.com/problems/soup-servings/

There are two types of soup: type A and type B. 
Initially, we have n ml of each type of soup. 
There are four kinds of operations:

1. Serve 100 ml of soup A and 0 ml of soup B,
2. Serve 75 ml of soup A and 25 ml of soup B,
3. Serve 50 ml of soup A and 50 ml of soup B, and
4. Serve 25 ml of soup A and 75 ml of soup B.

When we serve some soup, we give it to someone, 
and we no longer have it. Each turn, we will 
choose from the four operations with an equal 
probability 0.25. If the remaining volume of soup 
is not enough to complete the operation, we will 
serve as much as possible. We stop once we no longer 
have some quantity of both types of soup.

Note that we do not have an operation where all 
100 ml's of soup B are used first.

Return the probability that soup A will be empty first, 
plus half the probability that A and B become empty at 
the same time. Answers within 10-5 of the actual answer 
will be accepted.

Example 1:
Input: n = 50
Output: 0.62500
Explanation: 
If we choose the first two operations, A will become empty first.
For the third operation, A and B will become empty at the same time.
For the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half 
the probability that A and B become empty at the same time, 
is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.

Example 2:
Input: n = 100
Output: 0.71875

Constraints:
0 <= n <= 10^9
"""
from functools import lru_cache


def dp_memoization(n: int) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n)
    # Space complexity: O(n)

    @lru_cache(maxsize=None)
    def dfs(a: int, b: int) -> float:
        # Depth First Search recursive function

        # Base cases
        # `a` and `b` finished at the same time
        if a <= 0 and b <= 0:
            # Return halft the probability that A and B
            # become empty at the same time
            # (problem statement)
            return 0.5
        if a <= 0:
            return 1
        if b <= 0:
            return 0

        # 4 operations with equal probability per iteration,
        # add the probability of each opeartion and
        # multiply the result by 1/4 = 0.25
        return 0.25 * (
            dfs(a - 100, b)
            + dfs(a - 75, b - 25)
            + dfs(a - 50, b - 50)
            + dfs(a - 25, b - 75)
        )

    # Optimization based on the results seen
    # running multiple simulations of the algorithm:
    # - When `n` is large enough (4801), the probability
    # of emptying `A` first is 0.999995382315, which
    # rounded to the 5th decimal equals 1.00000
    if n > 4800:
        return 1

    return dfs(n, n)


def dp_memoization2(n: int) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n)
    # Space complexity: O(n)

    @lru_cache(maxsize=None)
    def dfs(a: int, b: int) -> float:
        if a <= 0 and b <= 0:
            return 0.5
        if a <= 0:
            return 1
        if b <= 0:
            return 0

        return 0.25 * (
            dfs(a - 4, b) 
            + dfs(a - 3, b - 1) 
            + dfs(a - 2, b - 2) 
            + dfs(a - 1, b - 3)
        )

    if n > 4800:
        return 1

    n = (n + 24) // 25
    return dfs(n, n)


def dp_tabulation(n: int) -> float:
    # Dynamic programming - Tabulation
    # Time complexity: O(n)
    # Space complexity: O(n)

    if n > 4800:
        return 1

    # Convert n from ml to servings of 25 ml
    # to simplify the problem
    n = (n + 24) // 25

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    # When `n = 0`, we have 0.5 probability of A emptying first
    dp[0][0] = 0.5

    # When soup A is 0 and soupe B isn't,
    # 100% probability that A is going to empty first
    for i in range(1, n + 1):
        dp[0][i] = 1

    servings = ((4, 0), (3, 1), (2, 2), (1, 3))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # Loop over the 4 possible servings
            for a, b in servings:
                dp[i][j] += dp[max(0, i - a)][max(0, j - b)]

            # Account for the equal probability of All 4 servings
            dp[i][j] *= 0.25

    return dp[n][n]


if __name__ == "__main__":
    print("-" * 60)
    print("Soup servings")
    print("-" * 60)

    test_cases = [
        (0, 0.5),
        (50, 0.625),
        (100, 0.71875),
        (200, 0.79688),
        (300, 0.85217),
        (500, 0.91634),
        (1000, 0.97657),
        (4800, 0.99999),
        (4801, 1),
        (8000, 1),
    ]

    for n, solution in test_cases:

        print("n:", n)

        result = dp_memoization(n)
        result = round(result * 1e5) / 1e5
        output = f"      dp_memoization = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_memoization2(n)
        result = round(result * 1e5) / 1e5
        output = f"     dp_memoization2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation(n)
        result = round(result * 1e5) / 1e5
        output = f"       dp_tabulation = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
