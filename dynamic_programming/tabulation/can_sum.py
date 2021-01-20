"""
The function `can_sum(target_sum, numbers)` takes in a
target_sum and an array of numbers as arguments.

The function returns a boolean indicating whether or not
it is possible to generate the target_sum using numbers 
from the array.

You may use an element of the array as many times as needed.

You may assume that all input numbers are non-negative.

--------------
Analysis:

time: O(m * n)
space: O(m)
"""
def can_sum(target_sum: int, numbers: list):
    table = [False] * (target_sum + 1)
    table[0] = True
    n = len(numbers)
    for i in range(target_sum + 1):
        if table[i] is True:
            for number in numbers:            
                if i + number < target_sum + 1:
                    table[i + number] = True
    #print(table)
    return table[target_sum]


if __name__ == "__main__":
    from datetime import datetime
    target_sum = 7
    numbers = [2, 3, 4]
    print('\n' + '-' * 10, f'can_sum({target_sum}, ', numbers, ')', '-' * 10)    
    
    time = datetime.now()
    res = can_sum(target_sum, numbers)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'O(m * n) time:   {time:10.0f} ms, solution:', res)
    
    print('\n' + '-' * 10, 'tests', '-' * 10)
    test_cases = [
        (7, [2, 3]),        # True
        (7, [5, 3, 4, 7]),  # True
        (7, [2, 4]),        # False
        (8, [2, 3, 5]),     # True
        (300, [7, 14]),     # False
    ]
    for target_sum, numbers in test_cases:
        print(f'can_sum({target_sum}, ', numbers, f') = {can_sum(target_sum, numbers)}')