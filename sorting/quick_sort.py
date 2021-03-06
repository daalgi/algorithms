"""
QuckSort operates on the input array only thruogh repeated 
swaps of pairs of elements, so it only allocates a miniscule
amount of additional memory for intermediate computations.

Running time: O(n log(n))

Step 1: Choose a pivot element.
Step 2: Rearrange the input array around the pivot.
"""
import random


PIVOT_METHOD = 'median' #'median', 'random', 'first', 'last'
VERBOSE = 0

def partition(a: list, start: int, end: int):
    """
    Takes as input an array `a` but operates only on
    the subarray of elements a[start], ..., a[end],
    where `start` and `end` are given parameters.
    
    Swaps elements of the subarray.

    Returns the final pivot position.
    """
    """
    # Choose a random pivot
    pivot_index = random.randint(start, end)
    #a[start], a[pivot_index] = a[pivot_index], a[start]
    #pivot = a[start]
    pivot = a[pivot_index]

    # Index `i` keeps track of the boundary
    # between processed elements that are less
    # than and greater than the pivot.   
    i = start + 1

    # Loop through the elements of the subarray
    for j in range(start+1, end+1):
        # Swap if the jth element is less than the pivot
        if a[j] < pivot:
            a[j], a[i] = a[i], a[j]
            i += 1
    
    # Swap the pivot
    a[start], a[i-1] = a[i-1], a[start]

    # Report the final pivot position
    return i -1
    """
    pivot_index = choose_pivot(start, end)
    pivot = a[pivot_index]
    
    if VERBOSE:
        print(f'Method: {PIVOT_METHOD},\tPivot index: {pivot_index},\tPivot value: {pivot}')

    while True:
        while a[start] < pivot:
            start += 1
        while a[end] > pivot:
            end -= 1
        if start >= end:
            return end
        swap(a, start, end)
        

def swap(a: list, i: int, j: int):
    if VERBOSE:
        print(f'Swap: {i, j}')
        print(a)
    a[i], a[j] = a[j], a[i]
    if VERBOSE:
        print(a)


def choose_pivot(start: int, end: int):
    if PIVOT_METHOD == 'median':
        return (start + end) // 2
    elif PIVOT_METHOD == 'random':
        return random.randint(start, end)
    elif PIVOT_METHOD == 'first':
        return start
    elif PIVOT_METHOD == 'last':
        return end
    else:
        return (start + end) // 2


def quicksort(a: list, start: int, end: int):
    # 0- or 1-element subarray
    if start >= end:
        return

    if VERBOSE:
        print(f'\nQuicksort call interval: {start, end}')

    # Rearrange the elements across the pivot
    pivot_index = partition(a, start, end)

    # Recursive calls at both parts of the pivot
    quicksort(a, start, pivot_index - 1)
    quicksort(a, pivot_index + 1, end)


def main(a: list):
    quicksort(a, 0, len(a) - 1)
    return a


if __name__ == '__main__':
    print('\n'+ '-' * 60)
    print('Quicksort')
    print('-' * 60)

    test_cases = [
        #([1], [1]),
        #([1, 2], [1, 2]),
        #([8, 7], [7, 8]),
        #([3, 2, 1, 4], [1, 2, 3, 4]),
        ([1, 8, -3, -8, 1, 1], [-8, -3, 1, 1, 1, 8]),
        #([0.1, -0.8, -2, 3.8], [-2, -0.8, 0.1, 3.8]),
        #([-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1]),
        #([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        #([1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1])
    ]
    
    for array, solution in test_cases:
        string = f'quicksort({str(array)}) = {str(main(array))}'
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == array else "NOT OK"}')      
    print()
    