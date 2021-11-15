"""
MERGE SORT
Running time: O(n log2(n))
"""
from random import randint
import time
import cProfile


def merge_sort(a: list) -> list:
    def _merge(b: list, c: list) -> list:
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
        # print(b, c, a)
        return a

    def _merge_sort(a: list):

        n = len(a)
        # Base case
        if n < 2:
            return a

        # Divide and conquer
        half = n // 2
        b = _merge_sort(a[:half])
        c = _merge_sort(a[half:])
        return _merge(b, c)

    return _merge_sort(a)


def merge_sort2(arr: list) -> list:
    def _merge(arr: list, left: int, mid: int, right: int):
        helper = [*arr]

        left_pointer, right_pointer = left, mid + 1
        current = left_pointer

        # Loop over the two halves of the array using two pointers,
        # until one of the pointers reaches its boundary
        while left_pointer <= mid and right_pointer <= right:
            if helper[left_pointer] <= helper[right_pointer]:
                arr[current] = helper[left_pointer]
                left_pointer += 1
            else:
                arr[current] = helper[right_pointer]
                right_pointer += 1
            current += 1

        # If there're elements in the left half of the array,
        # add them
        remaining = mid - left_pointer + 1
        for i in range(remaining):
            arr[current + i] = helper[left_pointer + i]

        # If there're elements in the right half of the array,
        # add them
        current += remaining
        remaining = right - right_pointer
        for i in range(remaining):
            arr[current + i] = helper[right_pointer + i]

    def _merge_sort(arr: list, left: int, right: int):
        # Base case
        if left >= right:
            # If the indices cross each other, finish
            return

        mid = (left + right) // 2
        _merge_sort(arr, left, mid)
        _merge_sort(arr, mid + 1, right)
        _merge(arr, left, mid, right)

    _merge_sort(arr, 0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    print("-" * 60)
    print("Merge sort")
    print("-" * 60)

    test_cases = [
        ([1, 2], [1, 2]),
        ([3, 2], [2, 3]),
        ([4, 3, 1, 2], [1, 2, 3, 4]),
        ([1, 4, 3, 5, 6, 2], [1, 2, 3, 4, 5, 6]),
        ([1, 3, 2], [1, 2, 3]),
        ([9, 8, 9, 8], [8, 8, 9, 9]),
        (["c", "f", "b", "a"], ["a", "b", "c", "f"]),
    ]

    for array, solution in test_cases:
        array_string = str(array[:6])
        if len(array) > 6:
            array_string = array_string[:-1] + ", ...]"

        result = merge_sort([*array])
        string = f" merge_sort({array_string}) = {str(result)}"
        string += " " * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = merge_sort2([*array])
        string = f"merge_sort2({array_string}) = {str(result)}"
        string += " " * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

    # case = 2
    # arr = [*test_cases[case][0]]
    # print(arr)
    # print(merge_sort2(arr))

    size = 20000
    print(f"\n>>> Performance test - Random array size: {size}")
    arr = [randint(0, size) for _ in range(size)]
    t = time.time()
    merge_sort([*arr])
    # cProfile.run("merge_sort([*arr])")
    t = time.time() - t
    print(f"Method 1: {t*1e3:>8.0f} ms")
    t = time.time()
    merge_sort2([*arr])
    # cProfile.run("merge_sort2([*arr])")
    t = time.time() - t
    print(f"Method 2: {t*1e3:>8.0f} ms")
