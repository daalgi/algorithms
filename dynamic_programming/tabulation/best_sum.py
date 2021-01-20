"""
The function `best_sum(target_sum, numbers)` takes in a 
target_sum and an array of numbers as arguments.

Returns an array containing the shortest combination of 
numbers that add up to exactly the target_sum.

If there is a tie for the shortest combination,
you may return any one of the shortest.

-----------------
Analysis

m = target_sum
n = len(numbers)

Complexity:
    time: O(m^2 * n)
    space: O(m^2)
"""
def best_sum(target_sum: int, numbers: list):
    table = [[]] + [None] * (target_sum)
    for i in range(target_sum + 1):
        if table[i] is not None:
            for number in numbers:
                if i + number < target_sum + 1:
                    if not table[i + number] or len(table[i + number]) > len(table[i]) + 1:
                        table[i + number] = [*table[i], number]
                
    return table[target_sum]


if __name__ == "__main__":
    from datetime import datetime
    target_sum = 7
    numbers = [2, 3, 4]
    print('\n' + '-' * 10, f'how_sum({target_sum}, ', numbers, ')', '-' * 10)    
    
    time = datetime.now()
    res = best_sum(target_sum, numbers)
    time = (datetime.now() - time).total_seconds() * 1000
    print(f'O(m^2 * n) time:   {time:10.0f} ms, solution:', res)
    
    print('\n' + '-' * 10, 'tests', '-' * 10)
    test_cases = [
        (7, [5, 3, 4, 7], [7]),
        (8, [2, 3, 5], [3, 5]),
        (8, [1, 4, 5], [4, 4]),
        (100, [1, 2, 5, 25], [25, 25, 25, 25]),
        (100, [25, 2, 4, 18], [25, 25, 25, 25]),
        (888, [3, 5, 178, 256, 32], None)
    ]
    for target_sum, numbers, solution in test_cases:
        res = best_sum(target_sum, numbers)
        print(f'best_sum({target_sum}, ', numbers, ') = ', res,
            f'\tTest: {res == solution if solution is not None else "?"}')
    print()