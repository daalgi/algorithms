"""
MERGE SORT
Running time: O(n log2(n))
"""
def merge(b: list, c: list):
    m = len(b) + len(c)
    a = [None] * m
    i = j = 0
    for k in range(m):
        if i == len(b):
            a[k] = c[j]
            j += 1
        elif j == len(c):
            a[k] = b[i]
            i += 1
        elif b[i] < c[j]:
            a[k] = b[i]
            i += 1
        else:
            a[k] = c[j]
            j += 1
    #print(b, c, a)
    return a
    
def merge_sort(a: list):
    n = len(a)
    # Base case
    if n < 2: 
        return a
        
    # Divide and conquer
    half = n // 2
    b = merge_sort(a[:half])
    c = merge_sort(a[half:])
    return merge(b, c)


if __name__ == '__main__':
    print('-' * 60)
    print('Merge sort')
    print('-' * 60)
    
    test_cases = [
        ([1, 2], [1, 2]),
        ([3, 2], [2, 3]),
        ([4, 3, 1, 2], [1, 2, 3, 4]),
        ([1, 4, 3, 5, 6, 2], [1, 2, 3, 4, 5, 6]),
        ([1, 3, 2], [1, 2, 3]),
        ([9, 8, 9, 8], [8, 8, 9, 9]),
        (['c', 'f', 'b', 'a'], ['a', 'b', 'c', 'f'])
    ]
    
    for array, solution in test_cases:
        array_string = str(array[:6])
        if len(array) > 6:
            array_string = array_string[:-1] + ', ...]'

        result = merge_sort(array)
        string = f'merge_sort({array_string}) = {str(result)}'
        string += ' ' * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
    print()