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
    def _merge(arr: list, helper: list, left: int, mid: int, right: int):
        for i in range(left, right):
            helper[i] = arr[i]

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
        # current += remaining
        # remaining = right - right_pointer
        # for i in range(remaining):
        #     arr[current + i] = helper[right_pointer + i]

    def _merge_sort(arr: list, left: int, right: int):
        # Base case
        if left >= right:
            # If the indices cross each other, finish
            return

        mid = (left + right) // 2
        _merge_sort(arr, left, mid)
        _merge_sort(arr, mid + 1, right)
        _merge(arr, arr[:], left, mid, right)

    _merge_sort(arr, 0, len(arr) - 1)
    return arr


def merge_sort3(array: list, verbose: bool = False):
    # source:
    # https://codereview.stackexchange.com/questions/132341/merge-sort-python-implementation

    def _mergesort(array, left, right):
        if right - left <= 1:
            return

        mid = (right + left) // 2
        if verbose:
            print(">>mergesort")
            print(array[left:mid])
            print(array[mid:right])
            print()
        _mergesort(array, left, mid)
        _mergesort(array, mid, right)
        _merge(array, left, mid, right)

    def _merge(array, left, mid, right):
        buffer = array[left:mid]
        buffer_size = mid - left  # len(buffer)
        read_left = 0
        read_right = mid
        write = left
        if verbose:
            print(">>merge")
            print(buffer)
            print(array[mid:right])
            print()
        while read_left < buffer_size and read_right < right:
            if array[read_right] < buffer[read_left]:
                array[write] = array[read_right]
                read_right += 1
            else:
                array[write] = buffer[read_left]
                read_left += 1
            write += 1

        while read_left < buffer_size:
            array[write] = buffer[read_left]
            read_left += 1
            write += 1

    _mergesort(array, 0, len(array))
    return array


def merge_sort4(array: list):
    # source:
    # https://codereview.stackexchange.com/questions/132341/merge-sort-python-implementation

    def coderodde_mergesort_impl(
        source, target, source_offset, target_offset, range_length
    ):
        if range_length < 2:
            return

        half_range_length = range_length // 2

        coderodde_mergesort_impl(
            target, source, target_offset, source_offset, half_range_length
        )

        coderodde_mergesort_impl(
            target,
            source,
            target_offset + half_range_length,
            source_offset + half_range_length,
            range_length - half_range_length,
        )

        left_run_index = source_offset
        right_run_index = source_offset + half_range_length

        left_run_bound = right_run_index
        right_run_bound = source_offset + range_length

        target_index = target_offset

        while left_run_index < left_run_bound and right_run_index < right_run_bound:
            if source[right_run_index] < source[left_run_index]:
                target[target_index] = source[right_run_index]
                right_run_index += 1
            else:
                target[target_index] = source[left_run_index]
                left_run_index += 1

            target_index += 1

        while left_run_index < left_run_bound:
            target[target_index] = source[left_run_index]
            target_index += 1
            left_run_index += 1

        while right_run_index < right_run_bound:
            target[target_index] = source[right_run_index]
            target_index += 1
            right_run_index += 1

    def coderodde_mergesort_ext(array, from_index, to_index):
        range_length = to_index - from_index
        aux = array[:]
        coderodde_mergesort_impl(aux, array, 0, from_index, range_length)

    coderodde_mergesort_ext(array, 0, len(array))
    return array


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
        ([3, 8, 5, 1, 2], [1, 2, 3, 5, 8]),
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

        result = merge_sort3([*array])
        string = f"merge_sort3({array_string}) = {str(result)}"
        string += " " * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = merge_sort4([*array])
        string = f"merge_sort4({array_string}) = {str(result)}"
        string += " " * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

    # case = -2
    # arr = [*test_cases[case][0]]
    # print(arr)
    # print(merge_sort3(arr, verbose=True))

    size = int(5e5)
    print(f"\n>>> Performance test - Random array size: {size}")
    arr = [randint(0, size) for _ in range(size)]

    t = time.time()
    merge_sort([*arr])
    # cProfile.run("merge_sort([*arr])")
    t = time.time() - t
    print(f"Method 1: {t*1e3:>8.0f} ms")

    # t = time.time()
    # merge_sort2([*arr])
    # # cProfile.run("merge_sort2([*arr])")
    # t = time.time() - t
    # print(f"Method 2: {t*1e3:>8.0f} ms")

    t = time.time()
    merge_sort3([*arr])
    # cProfile.run("merge_sort3([*arr])")
    t = time.time() - t
    print(f"Method 3: {t*1e3:>8.0f} ms")

    t = time.time()
    merge_sort4([*arr])
    # cProfile.run("merge_sort4([*arr])")
    t = time.time() - t
    print(f"Method 4: {t*1e3:>8.0f} ms")
