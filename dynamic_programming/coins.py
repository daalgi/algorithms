"""
CRACKING THE CODING INTERVIEW
8.11 Coins:
Given an infinite number of quarters (25 cents), dimes (10 cents),
nickels (5 cents), and pennies (1 cent), write code to calculate
the number of ways of representing n cents.


https://leetcode.com/problems/coin-change-2/
You are given an integer array coins representing coins of 
different denominations and an integer amount representing 
a total amount of money.

Return the number of combinations that make up that amount. 
If that amount of money cannot be made up by any combination 
of the coins, return 0.

You may assume that you have an infinite number of each kind 
of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1

Constraints:
1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
"""
from typing import List
from functools import lru_cache


def brute_force(n: int, coins: List[int]) -> int:
    # Time complexity: O(2^max(n, n/min(coins)))
    # Space complexity: O(max(n, n/min(coins)))

    num_coins = len(coins)

    def dfs(target: int, coin_index: int = 0) -> int:
        # DFS - recursive function
        # `coin_index` represents the current index in the coin list,
        # to avoid repeated solutions (in different order),
        # i.e.:
        # 1 + 1 + 5
        # 5 + 1 + 1

        # Base cases
        if target == 0:
            return 1
        if target < 0:
            return 0

        count = 0
        for i in range(coin_index, num_coins):
            count += dfs(target - coins[i], i)

        return count

    return dfs(n, 0)


def dp_recursion(n: int, coins: List[int]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n * ncoins)
    # Space complexity: O(n * ncoins)

    # Memoization as a dictionary (hashtable):
    # { (target, coin_index): count }
    memo = dict()

    num_coins = len(coins)

    def dfs(target: int, coin_index: int = 0) -> int:
        # DFS recursive function
        # `coin_index` keeps track of the index of the current
        # coin in the list `coins`, used to avoid repeated
        # solutions with elements in different order
        # i.e.:
        # 1 + 1 + 5
        # 5 + 1 + 1

        # Base cases
        if target == 0:
            return 1
        if target < 0:
            return 0

        # Check if the solution has been already computed
        if (target, coin_index) in memo:
            return memo[(target, coin_index)]

        # Current count of coins
        count = 0

        # Loop over the coins from the passed `coin_index`
        # to the last
        for i in range(coin_index, num_coins):
            count += dfs(target - coins[i], i)

        # Store the result in the `memo` list to avoid
        # repeated work later on
        memo[(target, coin_index)] = count
        return count

    return dfs(n, 0)


def dp_recursion2(n: int, coins: List[int]) -> int:
    @lru_cache(maxsize=None)
    def dfs(target: int, coin_index: int) -> int:
        # DFS recursive function using python built-in memoization

        # Base cases
        if target == 0:
            return 1
        if target < 0 or coin_index < 0:
            return 0

        # To avoid duplicated solutions with the coins in
        # different order (i.e.: 1 + 5, 5 + 1),
        # explore the possible solutions:
        return (
            # using the current coin coin[coin_index]
            dfs(target - coins[coin_index], coin_index)
            # not using the current coin and passing to the next
            # one: coin_index - 1
            + dfs(target, coin_index - 1)
        )

    return dfs(n, len(coins) - 1)


def dp_iterative(n: int, coins: List[int]) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(n * ncoins)
    # Space complexity: O(n)

    # Table to store partial results
    table = [0] * (n + 1)
    table[0] = 1
    # Loop over the coins.
    # If looping over the amount `n`, there will
    # be duplicate ways, i.e.:
    # 1 + 1 + 3, 1 + 3 + 1, 3 + 1 + 1
    for coin in coins:
        # For each coin, loop over the
        # indices of the table where `coin`
        # can help reach the target `n`,
        # that is from `coin` to `n+1`
        for i in range(coin, n + 1):
            table[i] += table[i - coin]

    # Return the counts registered in the last element
    # of `table` (the ones that summed up `n`)
    return table[-1]


if __name__ == "__main__":
    print("-" * 60)
    print("Coins")
    print("-" * 60)

    coins = [1, 5, 10, 25]
    # coins = [25, 10, 5, 1]

    test_cases = [
        (0, coins, 1),
        (1, coins, 1),
        (2, coins, 1),
        (5, coins, 2),
        (7, coins, 2),
        (10, coins, 4),
        (86, coins, 163),
        (125, coins, 424),
    ]

    print("Coins:", coins, "\n")

    for n, coins, solution in test_cases:

        string = f"  brute_force({n}) = "
        string += " " * (25 - len(string))
        result = brute_force(n, coins)
        string += str(result)
        string += " " * (65 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f" dp_recursion({n}) = "
        string += " " * (25 - len(string))
        result = dp_recursion(n, coins)
        string += str(result)
        string += " " * (65 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f"dp_recursion2({n}) = "
        string += " " * (25 - len(string))
        result = dp_recursion2(n, coins)
        string += str(result)
        string += " " * (65 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        string = f" dp_iterative({n}) = "
        string += " " * (25 - len(string))
        result = dp_iterative(n, coins)
        string += str(result)
        string += " " * (65 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
