"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

You are given an array prices where prices[i] is the price of a given 
stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many 
transactions as you like, but you need to pay the transaction fee 
for each transaction.

Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

Constraints:
1 <= prices.length <= 5 * 10^4
1 <= prices[i] < 5 * 10^4
0 <= fee < 5 * 10^4
"""
from typing import List
from functools import lru_cache


def dp_memoization(prices: List[int], fee: int) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(kn)
    # Space complexity: O(kn)

    @lru_cache(maxsize=False)
    def dfs(day: int, holding: bool) -> int:
        if day == days:
            return 0

        if holding:
            # If we're holding a stock, we can either
            # sell or continue hodling
            return max(
                # Option 1: sell
                prices[day] - fee + dfs(day + 1, False),
                # Option 2: continue holding
                dfs(day + 1, True),
            )

        # If not holding a stock, we can either
        # buy or wait
        return max(
            # Option 1: buy
            # Note: no fee for buying, only when the transaction is completed,
            # that is, when selling.
            -prices[day] + dfs(day + 1, True),
            # Option 2: wait
            dfs(day + 1, False),
        )

    days = len(prices)
    return dfs(0, holding=False)


def dp_tabulation(prices: List[int], fee: int) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(n)
    # Space complexity: O(n)

    days = len(prices)

    # `buy` is a list that represents the maximum profit for a given
    # `day` assuming we just bought the stock
    buy = [0] * days
    # Assume we buy the first day
    buy[0] = -prices[0]
    # `sell` is a list that represents the maximum profit for a given
    # `day` assuming we just sold the stock
    sell = [0] * days

    for day in range(1, days):
        buy[day] = max(
            # Option 1: wait
            buy[day - 1],
            # Option 2: buy (previously we had to sell)
            sell[day - 1] - prices[day],
        )
        sell[day] = max(
            # Option 1: hold
            sell[day - 1],
            # Option 2: sell (previously we had to buy)
            buy[day - 1] + prices[day] - fee,
        )

    return sell[-1]


def dp_tabulation_opt(prices: List[int], fee: int) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(n)
    # Space complexity: O(1)

    days = len(prices)

    # `buy` is an integer that represents the maximum profit assuming
    # we just bought the stock
    # Assume we buy the first day
    buy = -prices[0]

    # `sell` is an integer that represents the maximum profit assuming
    # we just sold the stock
    sell = 0

    for day in range(1, days):
        buy = max(
            # Option 1: wait
            buy,
            # Option 2: buy (before we had to sell)
            sell - prices[day],
        )
        sell = max(
            # Option 1: hold
            sell,
            # Option 2: sell (before we had to buy)
            buy + prices[day] - fee,
        )

    return sell


if __name__ == "__main__":
    print("-" * 60)
    print("Best time to buy a sell stock with transaction fee")
    print("-" * 60)

    test_cases = [
        # (prices, fee, solution)
        ([3, 3, 5, 0, 0, 3, 1, 4], 2, 2),
        ([1, 2, 3, 4, 5], 1, 3),
        ([1, 2, 3, 4, 5], 2, 2),
        ([7, 6, 4, 3, 1], 1, 0),
        ([7, 6, 9, 3, 1, 3, 1, 8, 2, 20], 2, 22),
    ]

    for prices, fee, solution in test_cases:

        output = f"Prices: {prices}"
        if len(output) > 60:
            output = output[:60] + " ...]]"
        output += f"\nSelling fee: {fee}"
        print(output)

        result = dp_memoization(prices, fee)
        output = f"\t     dp_memoization = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation(prices, fee)
        output = f"\t      dp_tabulation = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation_opt(prices, fee)
        output = f"\t  dp_tabulation_opt = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)
        print()
