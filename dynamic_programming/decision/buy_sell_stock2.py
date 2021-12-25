"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

You are given an integer array prices where prices[i] is the price 
of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can 
only hold at most one share of the stock at any time. However, 
you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), 
profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), 
profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), 
profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we 
never buy the stock to achieve the maximum profit of 0.

Constraints:
1 <= prices.length <= 3 * 10^4
0 <= prices[i] <= 10^4
"""
from typing import List
from functools import lru_cache


def brute_force(prices: List[int]) -> int:
    # Brute force
    # Time complexity: O(2^n)
    # Space complexity: O(1)
    pass


def peak_valley(prices: List[int]) -> int:
    # Approach: consider every peak after a valley
    # to maximize the profit, given that there's no limit
    # in the number of transactions we can do.
    # Time complexity: O(n)
    # Space complexity: O(1)

    valley = peak = prices[0]
    curr_profit = max_profit = 0
    days = len(prices)
    for day in range(1, days):
        if prices[day - 1] >= prices[day]:
            # If the price goes down in the current `day`,
            # keep track of the new local minimum `valley`
            valley = prices[day]
            if curr_profit > 0:
                # If we reached a peak in the previous `day`,
                # take profits
                max_profit += curr_profit
                # Set the previous profit to zero
                curr_profit = 0

        elif prices[day - 1] < prices[day]:
            # If the prices goes up in the current `day`,
            # keep track of the new local maximum `peak`
            peak = prices[day]
            # Calculate the current profit from the previous `valley`
            curr_profit = peak - valley

    # If the last day is a `peak`, take profits
    if curr_profit > 0:
        return max_profit + curr_profit
    return max_profit


def one_pass(prices: List[int]) -> int:
    # Approach: given that we can sell and buy the same day,
    # we take profits every single day that the prices go up
    # Time complexity: O(n)
    # Space complexity: O(1)
    profit = 0
    days = len(prices)
    for day in range(1, days):
        if prices[day - 1] < prices[day]:
            profit += prices[day] - prices[day - 1]

    return profit


def dp_memoization(prices: List[int]) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(n²)
    # Space complexity: O(n)

    @lru_cache(maxsize=False)
    def dfs(day: int, holding: bool) -> int:
        if day == days:
            return 0

        if holding:
            # If we're holding a stock, we can either
            # sell or continue hodling
            return max(
                # Option 1: sell
                prices[day] + dfs(day + 1, False),
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
            # Option 2: buy (we previously had to sell)
            sell[day - 1] - prices[day],
        )
        sell[day] = max(
            # Option 1: hold
            sell[day - 1],
            # Option 2: sell (we previously had to buy)
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
    # we just sold the stock
    sell = 0

    for day in range(1, days):
        buy = max(
            # Option 1: wait
            buy,
            # Option 2: buy (we previously had to sell)
            sell - prices[day],
        )
        sell = max(
            # Option 1: hold
            sell,
            # Option 2: sell (we previously had to buy)
            buy + prices[day],
        )

    return sell


if __name__ == "__main__":
    print("-" * 60)
    print("Best time to buy a sell stock II")
    print("-" * 60)

    test_cases = [
        ([3, 3, 5, 0, 0, 3, 1, 4], 8),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([7, 6, 9, 3, 1, 3, 1, 8, 2, 20], 30),
    ]

    for prices, solution in test_cases:

        output = f"Prices: {prices}"
        if len(output) > 60:
            output = output[:60] + " ...]]"
        print(output)

        result = peak_valley(prices)
        output = f"\t        peak_valley = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = one_pass(prices)
        output = f"\t           one_pass = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
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
