"""
You are working at the cash counter at a fun-fair, 
and you have different types of coins available to you in infinite quantities. 
The value of each coin is already given. Can you determine the number of ways 
of making change for a particular number of units using the given types of coins?
"""
def memoization_wrong(change: int, coins: list, memo: dict = None):
    # NOTE: 
    # this solution counts twice combinations of coins like (2, 1) and (1, 2)
    if len(coins) == 0: return 0
    if not memo: memo = {}
    if change in memo: return memo[change]
    if change == 0: return 1    
    if change < 0: return None

    count = 0
    for coin in coins:
        remainder = change - coin
        currentWays = memoization(remainder, coins, memo)
        if currentWays:
            if remainder not in memo:            
                memo[remainder] = currentWays
            else:
                memo[remainder] += currentWays
            count += currentWays
    
    memo[change] = count
    return count


def memoization(change: int, coins: list, memo: dict = None):
    num_coins = len(coins)
    if num_coins == 0: return 0
    if not memo: memo = {}
    if (change, num_coins) in memo: return memo[(change, num_coins)]
    if change == 0: return 1    
    if change < 0: return None

    count = 0
    for i in range(num_coins):
        coin = coins[i]
        if coin <= change:
            remainder = change - coin
            # Pop out the current coin in the recursive call
            # to avoid counting twice the combinations of coins,
            # that is, to avoid the counting the same combination
            # of coins but in different order.
            current_ways = memoization(remainder, coins[i:], memo)
            if current_ways:
                # Save the combinations already computed (change, num_coins)
                memo[(remainder, num_coins)] = current_ways
                count += current_ways
    
    memo[(change, num_coins)] = count
    return count


def tabulation(change: int, coins: list):
    table = [1] + [0] * change
    for coin in coins:
        for i in range(coin, change + 1):
            table[i] += table[i-coin]
    return table[change]


if __name__ == "__main__":
    from datetime import datetime
    change = 1986
    coins = [2, 5, 3]
    #change = 4
    #coins = [1, 2, 3]
    title = 'NUMBER OF WAYS TO RETURN CHANGE'
    print('\n' + '-' * 10, f'{title}', '-' * 10)
    print(f'({change},', coins, ')')
    
    time = datetime.now()
    res = memoization(change, coins)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Memoization, O(n * m) time: {time:10.0f} ms, solution:', res)
        
    time = datetime.now()
    res = tabulation(change, coins)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Tabulation, O(n * m) time:  {time:10.0f} ms, solution:', res, '\n')

    print('\n' + '-' * 10, 'tests', '-' * 10)
    
    test_cases = [
        #(change, coins, result)
        (2, [1, 2], 2),        
        (3, [1, 2, 3], 3),     
        (4, [1, 2, 3], 4),     
        (5, [1, 2, 3], 5),     
        (4, [1, 2], 3),        
        (4, [2, 3], 1),        
        (5, [2, 3], 1),        
        (6, [2, 3], 2),        
        (7, [2, 3], 1),        
        (8, [2, 3], 2),        
        (9, [2, 3], 2),        
        (4, [3], 0),           
        (7, [2, 3, 5], 2),     
        (10, [2, 5, 3, 6], 5),
        (166, [5, 37, 8, 39, 33, 17, 22, 32, 13, 7, 10, 35, 40, 2, 43, 49, 46, 19, 41, 1, 12, 11, 28], 96190959),
        (888, [5, 158, 91], None)
    ]
    for change, coins, result in test_cases:
        res = tabulation(change, coins)
        print(f'tabulation({change},', coins, ') = ', 
            res, f'\tTest: {res == result if result is not None else "?"}')