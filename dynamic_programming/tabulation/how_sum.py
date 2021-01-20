"""
The function `how_sum(target_sum, numbers)` takes in a 
target_sum and an array of numbers as arguments.

Returns an array containing any combination of elements that
add up to exactly the target_sum.

If there is no combination that adds up to the target_sum,
then return null.

If there are multiple combinations possible, 
return any single one.

-----------------
Analysis

m = target_sum
n = len(numbers)

Complexity:
    time: O(m^2 * n)
    space: O(m^2)
"""
def how_sum(target_sum: int, numbers: list):
    table = [None] * (target_sum + 1)
    table[0] = []
    for i in range(target_sum + 1):
        if table[i] is not None:
            for number in numbers:
                if i + number < target_sum + 1:
                    table[i + number] = [*table[i], number]
                
    return table[target_sum]

if __name__ == "__main__":
    from datetime import datetime
    target_sum = 7
    numbers = [2, 3, 4]
    print('\n' + '-' * 10, f'how_sum({target_sum}, ', numbers, ')', '-' * 10)    
    
    time = datetime.now()
    res = how_sum(target_sum, numbers)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'O(m^2 * n) time:   {time:10.0f} ms, solution:', res)
    
    print('\n' + '-' * 10, 'tests', '-' * 10)
    test_cases = [
        (7, [2, 3]),        # [3, 2, 2]
        (7, [5, 3, 4, 7]),  # [4, 3]
        (7, [2, 4]),        # None
        (8, [2, 3, 5]),     # [2, 2, 2, 2]
        (300, [7, 14]),     # None
    ]
    for target_sum, numbers in test_cases:
        print(f'how_sum({target_sum}, ', numbers, f') = {how_sum(target_sum, numbers)}')