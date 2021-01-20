"""
Determine which pair or pairs of elements have the smallest 
absolute difference between them.
"""
def closest_numbers(arr):
    n = len(arr)

    # Sort the array
    s = sorted(arr)
    
    # identify the minimum diference
    mini = s[1] - s[0]
    for i in range(2, n):
        if mini > s[i] - s[i-1]:
            mini = s[i] - s[i-1]
            
    # identify pairs of minimum difference
    res = []
    for i in range(1, n):
        if s[i] - s[i-1] == mini:
            res.extend([s[i-1], s[i]])
            
    return res


if __name__ == '__main__':
    print('-' * 60)
    print('Closest numbers')
    print('-' * 60)

    test_cases = [
        ([-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854], [-20, 30]),
        ([-5, 15, 25, 71, 63], [63, 71]),
        ([9, 7, 2, -8, 18], [7, 9])
    ]
    
    for array, solution in test_cases:
        
        array_string = str(array[:6])
        if len(array) > 6:
            array_string = array_string[:-1] + ', ...]'

        result = closest_numbers([*array])
        string = f'closest_numbers({array_string}) = {str(result)}'
        string += ' ' * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
    print()