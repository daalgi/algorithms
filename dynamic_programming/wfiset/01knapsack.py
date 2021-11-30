"""
0/1 KNAPSACK
https://www.youtube.com/watch?v=cJ21moQpofY&list=PLDV1Zeh2NRsAsbafOroUBnNV8fhZa7P4u&index=7

Given a set of objects which have both a value and a weight (vi, wi),
what is the maximum value we can obtain by selecting a subset of
these objects such as the sum of weights does not exceed a certain
capacity?
"""
def knapsack(capacity: int, values: list, weights: list):
    n = len(values)

    # Table:
    # rows - represent each item
    # columns - represent knapsack capacity
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

    # Loop through the items
    for i in range(1, n+1):
        v = values[i-1]
        w = weights[i-1]

        # Loop through the capacities (columns in the table)
        for c in range(1, capacity+1):

            # Consider not picking the current element
            dp[i][c] = dp[i-1][c]

            # Consider including the current element if it's more valuable
            if c >= w and dp[i-1][c-w] + v > dp[i][c]:
                dp[i][c] = dp[i-1][c-w] + v
    
    # Using the info in the table, backtrack and determine which
    # items were selected
    selected_items = []
    c = capacity
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i-1][c]:
            item_index = i - 1
            selected_items.append(item_index)
            c -= weights[item_index]

    return dp[n][capacity], selected_items
    
        
if __name__ == "__main__":
    print('-' * 60)
    print('0/1 knapsack problem')
    print('-' * 60)
    
    test_cases = [
        ((4, [1, 2, 3], [4, 5, 1]), (3, [2])),
        ((3, [1, 2, 3], [4, 5, 6]), (0, [])),
        ((10, [1, 4, 8, 5], [3, 3, 5, 6]), None),
        ((7, [2, 2, 4, 5, 3], [3, 1, 3, 4, 2]), None),
        ((27, [2, 2, 4, 5, 3], [3, 1, 3, 4, 2]), None),
    ]
    
    for (capacity, v, w), solution in test_cases:        
        res = knapsack(capacity, v, w)
        string = f'Capacity: {capacity}\n'
        string += f'Values = {v}\n'
        string += f'Weights = {w}\n'
        string += f'Maximum value: {res[0]}\n'
        string += f'Selected items: {res[1]}\n'
        if solution is not None:
            string += f'Test: {"OK" if res == solution else "NOT OK"}\n'
        print(string)