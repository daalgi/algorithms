"""
The function `best_sum(target_sum, numbers)` takes in
a target_sum and an array of numbers as arguments.

The function returns an array containing shortest combination of
numbers that add up to exactly the target_sum. 

If there is a tie for the shortest combination, it returns
any of the shortest.

m = target sum
n = len(numbers)

Brute force:
time: O(n^m * m)
space: O(m^2)

Memoized:
time: O(n * m^2)
space: O(m^2)
"""
def best_sum_slow(target_sum: int, numbers: list):
    if target_sum == 0: return []
    if target_sum < 0: return None

    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum_slow(remainder, numbers)
        if remainder_combination is not None:
            combination = remainder_combination + [num]
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination
            
    return shortest_combination


def best_sum0(target_sum: int, numbers: list, memo: dict = None):
    if not memo: memo = {}
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None

    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum0(remainder, numbers, memo)
        if remainder_combination is not None:
            combination = remainder_combination + [num]
            #memo[target_sum] = combination
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination
    
    memo[target_sum] = shortest_combination
    return shortest_combination


def best_sum1(target_sum: int, numbers: list, memo: dict = None):
    if not memo: memo = {}
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None

    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum1(remainder, numbers, memo)
        if remainder_combination is not None:
            combination = remainder_combination + [num]
            memo[target_sum] = combination
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination
    
    #memo[target_sum] = shortest_combination
    return shortest_combination


def best_sum(target_sum: int, numbers: list, memo: dict = None):
    if not memo: memo = {}
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None

    shortest_combination = None
    for num in numbers:
        remainder = target_sum - num
        remainder_combination = best_sum(remainder, numbers, memo)
        if remainder_combination is not None:
            combination = remainder_combination + [num]
            memo[target_sum] = combination
            if shortest_combination is None or len(combination) < len(shortest_combination):
                shortest_combination = combination
    
    memo[target_sum] = shortest_combination
    return shortest_combination


if __name__ == "__main__":
    from datetime import datetime
    target_sum = 80
    numbers = [2, 5, 25]
    #numbers = [2, 4]
    #numbers = [2, 3, 5]
    #numbers = [7, 14]
    print('\n' + '-' * 10, f'best_sum({target_sum},', numbers, ')' + '-' * 10)
    
    time = datetime.now()
    res = best_sum0(target_sum, numbers)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming0, O(n * m^2) time:  {time:10.0f} ms, solution:', res)
    
    time = datetime.now()
    res = best_sum1(target_sum, numbers)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming1, O(n * m^2) time:  {time:10.0f} ms, solution:', res)
    
    time = datetime.now()
    res = best_sum(target_sum, numbers)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming, O(n * m^2) time:   {time:10.0f} ms, solution:', res)
    """
    time = datetime.now()
    res = best_sum_slow(target_sum, numbers)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Brute force, O(m * n^m) time:          {time:10.0f} ms, solution:', res, '\n')
    """
    print('\n' + '-' * 10, 'tests', '-' * 10)
    test_cases = [
        (7, [5, 3, 4, 7]),
        (8, [2, 3, 5]),
        (8, [1, 4, 5]),
        (100, [1, 2, 5, 25]),
        (888, [5, 158, 91])
    ]
    for target_sum, numbers in test_cases:
        print(f'best_sum({target_sum},', numbers, ') = ', best_sum(target_sum, numbers))