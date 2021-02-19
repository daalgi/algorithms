"""
DYNAMIC PROGRAMMING - TILING PROBLEMS
https://www.youtube.com/watch?v=gQszF5qdZ-0&list=PLDV1Zeh2NRsAsbafOroUBnNV8fhZa7P4u&index=1&ab_channel=WilliamFiset

In how many ways can you tile a board of a given `length` with
red tiles of length 1, and blue tiles of length 2?
"""
def top_down(length: int):
    if length < 0:
        return 0
    if length == 0:
        return 1
    return top_down(length - 1) + top_down(length - 2)


memo = {}
def top_down_memo(length: int):
    if length in memo:
        return memo[length]

    if length < 0:
        return 0
    if length == 0:
        return 1

    memo[length] = top_down_memo(length - 1) + top_down_memo(length - 2)

    return memo[length]


def bottom_up(length: int):
    if length == 0 or length == 1:
        return 1

    table = [0] * (length + 1)
    table[0] = 1
    table[1] = 1
    for i in range(2, length + 1):
        table[i] = table[i-1] + table[i-2]
    
    return table[length]

    
if __name__ == "__main__":
    print('-' * 60)
    print('Dynamic programming - Tiling problem')
    print('-' * 60)
    
    test_cases = [
        (5, 8),
        (11, None),
        (28, None),
        (33, None),
    ]
    
    for length, solution in test_cases:
        
        res = top_down(length)
        string = f'Top down:'
        string += ' ' * (30 - len(string)) + f'length = {length}'
        string += ' ' * (50 - len(string)) + f'Number of ways = {res}'
        string += ' ' * (75 - len(string))
        if solution:
            string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string)

        memo = {}
        res = top_down_memo(length)
        string = f'Top down with memo:'
        string += ' ' * (30 - len(string)) + f'length = {length}'
        string += ' ' * (50 - len(string)) + f'Number of ways = {res}'
        string += ' ' * (75 - len(string))
        if solution:
            string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string)
        
        res = bottom_up(length)
        string = f'Bottom up (tabulation):'
        string += ' ' * (30 - len(string)) + f'length = {length}'
        string += ' ' * (50 - len(string)) + f'Number of ways = {res}'
        string += ' ' * (75 - len(string))
        if solution:
            string += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(string)

        print()