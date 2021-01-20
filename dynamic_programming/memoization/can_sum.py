"""
The function `can_sum(target_sum, numbers)` takes in
a target_sum and an array of numbers as arguments.

The function returns a boolean indicating whether or not
it is possible to generate the target_sum using numbers
from the array.

An element of the array can be used as many times as needed.

All input numbers are non-negative.
"""
def can_sum_slow(target_sum: int, numbers: list):
    if target_sum == 0: return True
    if target_sum < 0: return False
    for num in numbers:
        remainder = target_sum - num
        if can_sum_slow(remainder, numbers):
            return True
    return False

def can_sum(target_sum: int, numbers: list, memo: dict = None):
    if not memo: memo = {}
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return True
    if target_sum < 0: return False
    for num in numbers:
        remainder = target_sum - num
        if can_sum(remainder, numbers):
            memo[remainder] = True
            return True
    memo[target_sum] = False
    return False


if __name__ == "__main__":
    from datetime import datetime
    target_sum = 300
    #numbers = [5, 3, 4, 7]
    #numbers = [2, 4]
    #numbers = [2, 3, 5]
    numbers = [7, 14]
    print('\n' + '-' * 10, f'can_sum({target_sum}, [{",".join(str(n) for n in numbers)}])', '-' * 10)

    time = datetime.now()
    res = can_sum(target_sum, numbers)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming, O(m*n) time:  {time:10.0f} ms, solution: {res}')    
    
    time = datetime.now()
    res = can_sum_slow(target_sum, numbers)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Brute force, O(n^m) time:          {time:10.0f} ms, solution: {res}\n')