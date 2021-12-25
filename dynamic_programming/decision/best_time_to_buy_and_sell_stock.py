"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
You are given an array prices where prices[i] is the price 
of a given stock on the ith day.

You want to maximize your profit by choosing a single 
day to buy one stock and choosing a different day in the 
future to sell that stock.

Return the maximum profit you can achieve from this 
transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
"""

def brute_force(prices: list) -> int:
    n = len(prices)
    # Result
    max_profit = 0    
    for i in range(n - 1):
        for j in range(i + 1, n):
            diff = prices[j] - prices[i]
            if diff > max_profit:
                max_profit = diff
    return max_profit

def efficient(prices: list) -> int:
    # Keep track of the current minimum and current
    # maximum profit
    min_price = 1e4
    max_profit = 0
    # Loop over the prices: O(n)
    for p in prices:
        if p < min_price:
            # If the current price is the current
            # minimum, keep track of it
            min_price = p
        else:
            # Otherwise check the difference with
            # the current minimum
            diff = p - min_price
            if diff > max_profit:
                # If the difference is larger than
                # the current max profit, store it
                max_profit = diff
    return max_profit


if __name__ == "__main__":
    print('-' * 60)
    print('Best time to buy and sell stock')
    print('-' * 60)
    
    test_cases = [
        ([1], 0),
        ([1, 1], 0),
        ([1, 0], 0),
        ([1, 2], 1),
        ([7, 1, 5, 3, 6, 4], 5),
        [[7, 6, 4, 3, 1], 0],
        [[2, 9, 1, 9, 0, 7], 8],
        [[2, 9, 3, 9, 4, 15], 13],
    ]
    
    for prices, solution in test_cases:
        
        result = brute_force(prices)        
        string = f'brute_force{prices} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = efficient(prices)        
        string = f'  efficient{prices} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()