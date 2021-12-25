"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

You are given an array prices where prices[i] is the price of a given 
stock on the ith day.

Find the maximum profit you can achieve. You may complete at most 
two transactions.

Note: You may not engage in multiple transactions simultaneously 
(i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), 
profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), 
profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), 
profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, 
as you are engaging multiple transactions at the same time. You must 
sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 105
"""
from typing import List
from functools import lru_cache


def dp_memoization(prices: List[int], transactions: int) -> int:
    # Dynamic programming - Memoization
    # Time complexity: O(kn)
    # Space complexity: O(kn)

    @lru_cache(maxsize=False)
    def dfs(day: int, remaining_trans: int, holding: bool) -> int:
        if day == days or remaining_trans == 0:
            return 0

        if holding:
            # If we're holding a stock, we can either
            # sell or continue hodling
            return max(
                # Option 1: sell
                prices[day] + dfs(day + 1, remaining_trans - 1, False),
                # Option 2: continue holding
                dfs(day + 1, remaining_trans, True),
            )

        # If not holding a stock, we can either
        # buy or wait
        return max(
            # Option 1: buy
            -prices[day] + dfs(day + 1, remaining_trans, True),
            # Option 2: wait
            dfs(day + 1, remaining_trans, False),
        )

    days = len(prices)
    return dfs(0, transactions, holding=False)


def dp_tabulation(prices: List[int], transactions: int) -> int:
    # Dynamic programming - Tabulation
    # Time complexity: O(kn)
    # Space complexity: O(kn)

    days = len(prices)
    # Special case, no prices: 0 profit
    if days == 0:
        return 0

    # Table to keep track of the profit up until day `d`
    # dp[k, d]
    dp = [[0] * days for _ in range(transactions + 1)]
    max_profit = 0
    for trans in range(1, transactions):
        for day in range(days - 1, -1, -1):
            pass

    return max_profit


if __name__ == "__main__":
    print("-" * 60)
    print("Best time to buy a sell stock III")
    print("-" * 60)

    test_cases = [
        ([3, 3, 5, 0, 0, 3, 1, 4], 6),
        ([1, 2, 3, 4, 5], 4),
        ([7, 6, 4, 3, 1], 0),
        ([7, 6, 9, 3, 1, 3, 1, 8, 2, 20], 25),
    ]

    for prices, solution in test_cases:

        output = f"Prices: {prices}"
        if len(output) > 60:
            output = output[:60] + " ...]]"
        print(output)

        result = dp_memoization(prices, transactions=2)
        output = f"\t dp_memoization = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = dp_tabulation(prices, transactions=2)
        output = f"\t  dp_tabulation = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
