"""
The function `how_sum(target_sum, numbers)` takes in
a target_sum and an array of numbers as arguments.

The function returns an array containing any combination of
elements that add up to exactly the target_sum. If there is no
combination that adds up to the target_sum, then return null.

If there are multiple combinations possible, 
it returns any single one.

m = target sum
n = len(numbers)

Brute force
time: O(n^m * m)
space: O(m)

Memoized
time: O(n * m^2)
space: O(m^2)
"""
def how_sum_slow(target_sum: int, numbers: list):
    if target_sum == 0: return []
    if target_sum < 0: return None
    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum_slow(remainder, numbers)
        if remainder_result is not None:
            remainder_result.append(num)
            return remainder_result
    return None


def how_sum(target_sum: int, numbers: list, memo: dict = None):
    if not memo: memo = {}
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None
    for num in numbers:
        remainder = target_sum - num
        remainder_result = how_sum(remainder, numbers, memo)
        if remainder_result is not None:
            memo[target_sum] = remainder_result + [num]
            return memo[target_sum]
    
    memo[target_sum] = None
    return None


if __name__ == "__main__":
    from datetime import datetime
    target_sum = 21
    numbers = [5, 3, 4, 7]
    #numbers = [2, 4]
    #numbers = [2, 3, 5]
    #numbers = [7, 14]
    print('\n' + '-' * 10, f'how_sum({target_sum},', numbers, ')' + '-' * 10)
    
    time = datetime.now()
    res = how_sum(target_sum, numbers)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Dynamic programming, O(n * m^2) time:  {time:10.0f} ms, solution:', res)    
    
    time = datetime.now()
    res = how_sum_slow(target_sum, numbers)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'Brute force, O(m * n^m) time:          {time:10.0f} ms, solution:', res, '\n')