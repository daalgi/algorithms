"""
COUNT SORT for integer lists. 
Efficient as long as the range of values is not much larger than the size of the array.

Running time: O(n+k) 
where `n` is the number of elements in the array
and `k` is the range of the input.
"""
def count_sort(arr: list, verbose: bool = False):
    n = len(arr)
    maxi = max(arr)
    mini = min(arr)

    # Create frequency array
    m = maxi - mini + 1
    freq = [0] * m
    for i in range(n):
        freq[arr[i] - mini] += 1

    if verbose:
        print(f'Frequency array:', freq)

    # Define sorted array from the frequency array
    res = []
    for i in range(m):
        if freq[i] != 0:
            for j in range(freq[i]):
                res.append(i + mini)
        
    return res


if __name__ == '__main__':
    print('-' * 60)
    print('Count sort')
    print('-' * 60)

    test_cases = [
        ([1, 2], [1, 2]),
        ([3, 2], [2, 3]),
        ([4, 3, 1, 2], [1, 2, 3, 4]),
        ([5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5]),
        ([1, 4, 3, 5, 6, 2], [1, 2, 3, 4, 5, 6]),
        ([1, 3, 2], [1, 2, 3]),
        ([9, 8, 9, 8], [8, 8, 9, 9]),
        #(['c', 'f', 'b', 'a'], ['a', 'b', 'c', 'f'])
    ]
    
    for array, solution in test_cases:
        
        array_string = str(array[:6])
        if len(array) > 6:
            array_string = array_string[:-1] + ', ...]'

        result = count_sort([*array])
        string = f'count_sort({array_string}) = {str(result)}'
        string += ' ' * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
    print()

    array = test_cases[3][0]
    print(f'--> Verbose example:\n Array: {array}')
    count_sort([*array], verbose=True)