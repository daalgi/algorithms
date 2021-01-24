"""
MERGE SORT -- COUNT INVERSIONS
Running time: O(n log2(n))

Iterative merge sort tutorial:
https://www.baeldung.com/cs/non-recursive-merge-sort
"""
def merge(a: list, left1: int, right1: int, left2: int, right2: int, verbose: bool = False):
    temp = [0] * (right2 - left1 + 1)
    inversions = 0
    i = 0

    string = ''
    if verbose:
        size1 = right1 - left1 + 1
        string = f'--> {str(a[left1:right1+1])}, {str(a[left2:right2+1])},'
        string += f'\tsize1: {size1},\tindices: {left1, right1, left2, right2}'
        
    while left1 <= right1 and left2 <= right2:
        if a[left1] <= a[left2]:
            temp[i] = a[left1]
            left1 += 1
        else:
            temp[i] = a[left2]
            inversions += right1 - left1 + 1

            if verbose:
                string += f'\n\ti: {i}\t\tleft1: {left1}\tright1: {right1}\tleft2: {left2}'
                string += f'\tinversions: {right1 - left1 + 1}'

            left2 += 1            
            
        i += 1

    if verbose:
        string += f'\n\tTotal inversions: {inversions}'
        print(string)

    while left1 <= right1:
        temp[i] = a[left1]
        left1 += 1
        i += 1

    while left2 <= right2:
        temp[i] = a[left2]
        left2 += 1
        i += 1

    return temp, inversions
    
def iterative_merge_sort(a: list, verbose: bool = False):
    n = len(a)
    inversions = 0
    # Size of each part of the array that the algorithm handles at each step
    size = 1    
    while size < n:

        # Iterate over all parts of the array
        i = 0
        while i < n:

            # Set the indices of the two parts to be sorted
            left1 = i
            right1 = i + size - 1
            left2 = i + size
            right2 = i + 2 * size - 1
            
            # When left2 reaches the outside of the array, done
            if left2 >= n:
                break

            # Adjust right2 when it reaches the outside of the array,
            # meaning that this part contains less elements than `size`
            if right2 >= n:
                right2 = n - 1
            
            # Merge both parts of the array
            temp, merge_inversions = merge(a, left1, right1, left2, right2, verbose)
            inversions += merge_inversions

            # Copy the elements into their respective places 
            # in the original array
            for j in range(right2 - left1 + 1):
                a[i + j] = temp[j]
            
            i += 2 * size

        # Double the size of a single part of the array
        size *= 2

    if verbose:
        print('--> Array total inversions:', inversions)

    return inversions


if __name__ == '__main__':
    print('-' * 60)
    print('Count inversions in iterative merge sort')
    print('-' * 60)
    
    test_cases = [
        ([1, 2], 0),
        ([3, 2], 1),
        ([4, 3, 1, 2], 5),
        ([1, 4, 3, 5, 6, 2], 5),
        ([5, 4, 3, 6, 2, 1, 3], 15),
        ([1, 3, 2], 1),
        ([9, 8, 9, 8], 3),
        ([1, 1, 1, 2, 2], 0),
        ([2, 1, 3, 1, 2], 4),
        ([1, 5, 3, 7], 1),
        ([7, 5, 3, 1], 6),
        ([1, 3, 5, 7], 0),
        ([3, 2, 1], 3),
        ([9492052, 241944, 5743396, 5758608, 6053545], 4),
        ([5, 1, 2, 4, 9, 3], 6),
        (['c', 'f', 'b', 'a'], 5)
    ]
    
    for array, solution in test_cases:
        array_string = str(array[:6])
        if len(array) > 6:
            array_string = array_string[:-1] + ', ...]'

        result = iterative_merge_sort([*array])
        string = f'iterative_merge_sort({array_string}) = {str(result)}'
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
    print()


    array = test_cases[4][0]
    print(f'>>> Verbose example:\nArray: {array}')
    iterative_merge_sort([*array], verbose=True)