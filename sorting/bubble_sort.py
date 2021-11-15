"""
BUBBLE SORT
Running time: O(n^2)
"""
from random import randint
import time


def bubble_sort(arr: list):
    # Sorted in-place
    # No early stop
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def bubble_sort2(arr: list, verbose: bool = False):
    # Sorted in-place
    # Early stop
    n = len(arr)
    swapped = True
    pass_num = 0
    # Loop over the elements of the array as long as
    # `swapped` is True. If last pass didn't swap any
    # element, the algorithms stops.
    while swapped:
        swapped = False
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        # The n-th pass finds the n-th largest element
        # and puts it into its final place,
        # so the inner loop can avoid looking at the last n-1 element
        n -= 1
        if verbose:
            pass_num += 1
            print(f"Pass {pass_num}: {arr}")
    return arr


if __name__ == "__main__":
    print("-" * 60)
    print("Bubble sort")
    print("-" * 60)

    test_cases = [
        ([1, 2], [1, 2]),
        ([3, 2], [2, 3]),
        ([4, 3, 1, 2], [1, 2, 3, 4]),
        ([5, 4, 3, 2, 1, 0], [0, 1, 2, 3, 4, 5]),
        ([1, 4, 3, 5, 6, 2], [1, 2, 3, 4, 5, 6]),
        ([1, 3, 2], [1, 2, 3]),
        ([9, 8, 9, 8], [8, 8, 9, 9]),
        (["c", "f", "b", "a"], ["a", "b", "c", "f"]),
    ]

    for array, solution in test_cases:

        array_string = str(array[:6])
        if len(array) > 6:
            array_string = array_string[:-1] + ", ...]"

        result = bubble_sort([*array])
        string = f" bubble_sort({array_string}) = {str(result)}"
        string += " " * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = bubble_sort2([*array])
        string = f"bubble_sort2({array_string}) = {str(result)}"
        string += " " * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

    array = test_cases[3][0]
    print(f">>> Verbose example:\nArray: {array}")
    bubble_sort2([*array], verbose=True)

    size = 5000
    print(f"\n>>> Performance test - Random array size: {size}")
    arr = [randint(0, size) for _ in range(size)]
    t = time.time()
    bubble_sort([*arr])
    t = time.time() - t
    print(f"No early stop: {t*1e3:>8.0f} ms")
    t = time.time()
    bubble_sort2([*arr])
    t = time.time() - t
    print(f"Early stop:    {t*1e3:>8.0f} ms")
