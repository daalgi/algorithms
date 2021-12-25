"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

You are given an array prices where prices[i] is the price of a given 
stock on the ith day.

Find the maximum profit you can achieve. You may complete as many 
transactions as you like (i.e., buy one and sell one share of the 
stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day 
(i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:
Input: prices = [1]
Output: 0

Constraints:
1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""
from typing import List
from functools import lru_cache


def dp_memoization(prices: List[int]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n)
    # Space complexity: O(n)

    @lru_cache(maxsize=False)
    def dfs(day: int, holding: bool) -> int:
        if day >= days:
            return 0

        if holding:
            # If we're holding a stock, we can either
            # sell or continue hodling
            return max(
                # Option 1: sell with cooldown (1 day rest)
                prices[day] + dfs(day + 2, False),
                # Option 2: continue holding
                dfs(day + 1, True),
            )

        # If not holding a stock, we can either
        # buy or wait
        return max(
            # Option 1: buy
            -prices[day] + dfs(day + 1, True),
            # Option 2: wait
            dfs(day + 1, False),
        )

    days = len(prices)
    return dfs(0, holding=False)


def dp_tabulation(prices: List[int]) -> int:
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
            # Option 2: buy (previously we had to sell and rest a day)
            sell[day - 2] - prices[day],
        )
        sell[day] = max(
            # Option 1: hold
            sell[day - 1],
            # Option 2: sell (previously we had to buy)
            buy[day - 1] + prices[day],
        )

    return sell[-1]


def dp_tabulation_opt(prices: List[int]) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(n)
    # Space complexity: O(1)

    days = len(prices)

    # `buy` is an integer that represents the maximum profit assuming
    # we just bought the stock
    # Assume we buy the first day
    buy = -prices[0]

    # `sell` is an integer that represents the maximum profit assuming
    # we just sold the stock.
    # `prev_sell` keeps track of the sell of the ith-2 day
    prev_sell = sell = 0

    for day in range(1, days):
        buy = max(
            # Option 1: wait
            buy,
            # Option 2: buy (before we had to sell)
            prev_sell - prices[day],
        )
        prev_sell = sell
        sell = max(
            # Option 1: hold
            sell,
            # Option 2: sell (before we had to buy)
            buy + prices[day],
        )

    return sell


if __name__ == "__main__":
    print("-" * 60)
    print("Best time to buy a sell stock with cooldown")
    print("-" * 60)

    test_cases = [
        # (prices, solution)
        ([1], 0),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([1, 2, 3, 0, 2], 3),
        ([3, 3, 5, 0, 0, 3, 1, 4], 6),
        ([7, 6, 9, 3, 1, 3, 1, 8, 2, 20], 23),
        ([1, 8, 1, 7], 7),
    ]

    for prices, solution in test_cases:

        output = f"Prices: {prices}"
        if len(output) > 60:
            output = output[:60] + " ...]]"
        print(output)

        result = dp_memoization(prices)
        output = f"\t     dp_memoization = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation(prices)
        output = f"\t      dp_tabulation = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation_opt(prices)
        output = f"\t  dp_tabulation_opt = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
