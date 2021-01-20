"""
INSERTION SORT
Running time: O(n*(n-1)/2) = O(n^2)
"""
def insertion_sort(arr: list, verbose: bool = False):
    pass_num = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            current = arr[i]
            j = i - 1
            while j > -1 and arr[j] > current:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = current
            if verbose:
                pass_num += 1
                print(f'Pass {pass_num}: {arr}')

    return arr

def swaps_count(arr: list):
    swaps = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            current = arr[i]
            j = i - 1
            while j > -1 and arr[j] > current:
                arr[j+1] = arr[j]
                j -= 1
                swaps += 1
            arr[j+1] = current

    return swaps


if __name__ == '__main__':
    print('-' * 60)
    print('Insertion sort')
    print('-' * 60)

    test_cases = [
        ([1, 2], [1, 2]),
        ([3, 2], [2, 3]),
        ([4, 3, 1, 2], [1, 2, 3, 4]),
        ([5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5]),
        ([1, 4, 3, 5, 6, 2], [1, 2, 3, 4, 5, 6]),
        ([1, 3, 2], [1, 2, 3]),
        ([9, 8, 9, 8], [8, 8, 9, 9]),
        (['c', 'f', 'b', 'a'], ['a', 'b', 'c', 'f'])
    ]
    
    for array, solution in test_cases:
        
        array_string = str(array[:6])
        if len(array) > 6:
            array_string = array_string[:-1] + ', ...]'

        result = insertion_sort([*array])
        string = f'insertion_sort({array_string}) = {str(result)}'
        string += ' ' * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
    print()

    array = test_cases[3][0]
    print(f'--> Verbose example:\n Array: {array}')
    insertion_sort([*array], verbose=True)