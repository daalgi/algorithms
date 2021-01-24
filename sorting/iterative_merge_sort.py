"""
MERGE SORT
Running time: O(n log2(n))

source:
https://www.baeldung.com/cs/non-recursive-merge-sort
"""
def merge(a: list, left1: int, right1: int, left2: int, right2: int):
    temp = [0] * (right2 - left1 + 1)

    i = 0
    while left1 <= right1 and left2 <= right2:
        if a[left1] <= a[left2]:
            temp[i] = a[left1]
            left1 += 1
        else:
            temp[i] = a[left2]
            left2 += 1
        i += 1

    while left1 <= right1:
        temp[i] = a[left1]
        left1 += 1
        i += 1

    while left2 <= right2:
        temp[i] = a[left2]
        left2 += 1
        i += 1

    return temp
    
def iterative_merge_sort(a: list):
    n = len(a)
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
            temp = merge(a, left1, right1, left2, right2)

            # Copy the elements into their respective places 
            # in the original array
            for j in range(right2 - left1 + 1):
                a[i + j] = temp[j]
            
            i += 2 * size

        # Double the size of a single part of the array
        size *= 2

    return a


if __name__ == '__main__':
    print('-' * 60)
    print('Iterative merge sort')
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

        result = iterative_merge_sort(array)
        string = f'iterative_merge_sort({array_string}) = {str(result)}'
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
    print()