"""
SUMMARY OF SORTING ALGORITHSM

Non-comparison based sorting algorithms:
Insertion sort: O(n + k)
Counting sort: O(n + k)
Radix sort: O(nk))

Comparison-based sorting algorithms:
Heap-sort: O(n log2(n))
Merge-sort: O(n log2(n))
Quick-sort: O(n log2(n))
"""
from typing import List
from random import randint

import time


def insertion_sort(a: List[int]) -> List[int]:
    n = len(a)
    for i in range(1, n):
        ref, j = a[i], i - 1
        while j > -1 and a[j] > ref:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = ref
    return a


def counting_sort(a: List[int]) -> List[int]:
    mini, maxi = min(a), max(a)
    r = maxi - mini + 1
    count = [0] * r
    for num in a:
        count[num - mini] += 1

    for i in range(1, r):
        count[i] += count[i - 1]

    for i in range(r):
        count[i] -= 1

    for i in range(r):
        pass

    return a


def radix_sort(a: List[int]) -> List[int]:
    def _counting_sort(a: List[int], place: int) -> None:
        output = [0] * n
        count = [0] * base

        for i in range(n):
            index = a[i] // place
            count[index % base] += 1

        for i in range(1, base):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = a[i] // place
            output[count[index % base] - 1] = a[i]
            count[index % base] -= 1
            i -= 1

        for i in range(n):
            a[i] = output[i]

    n = len(a)
    maxi = max(a)
    place = 1
    base = 10
    while maxi // place > 0:
        _counting_sort(a, place)
        place *= 10
    return a


def merge_sort(a: List[int]) -> List[int]:
    def _mergesort(a: List[int], left: int, right: int) -> None:
        if right - left < 2:
            return
        mid = (right + left) // 2
        _mergesort(a, left, mid)
        _mergesort(a, mid, right)
        _merge(a, left, mid, right)

    def _merge(a: List[int], left: int, mid: int, right: int) -> None:
        buffer = a[left:mid]
        buffer_size = mid - left
        read_left, write, read_right = 0, left, mid

        while read_left < buffer_size and read_right < right:
            if a[read_right] < buffer[read_left]:
                a[write] = a[read_right]
                read_right += 1
            else:
                a[write] = buffer[read_left]
                read_left += 1
            write += 1

        while read_left < buffer_size:
            a[write] = buffer[read_left]
            read_left += 1
            write += 1

    _mergesort(a, 0, len(a))
    return a


def quicksort(a: List[int]) -> List[int]:
    def _quicksort(a: List[int], left: int, right: int) -> None:
        if left < right:
            p = _partition(a, left, right)
            _quicksort(a, left, p)
            _quicksort(a, p + 1, right)

    def _partition(a: List[int], left: int, right: int) -> int:
        pivot = a[(right + left) // 2]
        while True:
            while a[left] < pivot:
                left += 1
            while a[right] > pivot:
                right -= 1
            if left >= right:
                return right
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1

    _quicksort(a, 0, len(a) - 1)
    return a


if __name__ == "__main__":
    print("-" * 60)
    print("Sorting algorithms")
    print("-" * 60)

    arrays = [
        [i for i in range(100)],
        [i for i in range(10000)],
        [i for i in range(1000000)],
        [i for i in range(100, -1, -1)],
        [i for i in range(10000, -1, -1)],
        [i for i in range(1000000, -1, -1)],
        [randint(0, 100) for _ in range(100)],
        [randint(0, 10000) for _ in range(10000)],
        [randint(0, 1000000) for _ in range(1000000)],
        [randint(max(0, i - 10), i + 10) for i in range(100)],
        [randint(max(0, i - 100), i + 100) for i in range(10000)],
        [randint(max(0, i - 1000), i + 1000) for i in range(1000000)],
        [randint(max(0, i - 10), i + 10) if i % 10 == 0 else i for i in range(100)],
        [
            randint(max(0, i - 100), i + 100) if i % 100 == 0 else i
            for i in range(10000)
        ],
        [
            randint(max(0, i - 1000), i + 1000) if i % 10000 == 0 else i
            for i in range(1000000)
        ],
    ]

    infos = [
        "100-element array already sorted",
        "10k-element array already sorted",
        "1M-elements array already sorted",
        "100-element array completely unsorted",
        "10k-element array completely unsorted",
        "1M-elements array completely unsorted",
        "100-random elements array",
        "10k-random elements array",
        "1M-random elements array",
        "100-random partially sorted elements array",
        "10k-random partially sorted elements array",
        "1M-random partially sorted elements array",
        "100-random almost sorted elements array",
        "10k-random almost sorted elements array",
        "1M-random almost sorted elements array",
    ]
    test_cases = [(i, a) for i, a in zip(infos, arrays)]

    TEST_POS, TIME_POS = 55, 68
    LARGE_ARRAY_TESTS = set([5, 8])

    for i, (info, array) in enumerate(test_cases):

        print(info)
        output = str(array)
        if len(output) > 65:
            output = output[:60] + " ...]"
        print(output)

        if i not in LARGE_ARRAY_TESTS:
            t = time.time()
            result = insertion_sort([*array])
            t = time.time() - t
            result_str = str(result)
            if len(result_str) > 25:
                result_str = result_str[:20] + " ...]"
            output = f"   insertion_sort = {result_str}"
            test_ok = result == sorted(array)
            output += " " * (TEST_POS - len(output))
            output += f'Test: {"OK" if test_ok else "NOT OK"}'
            output += " " * (TIME_POS - len(output)) + f"{t*1e3:>8.0f} ms"
            print(output)

        t = time.time()
        result = radix_sort([*array])
        t = time.time() - t
        result_str = str(result)
        if len(result_str) > 25:
            result_str = result_str[:20] + " ...]"
        output = f"       radix_sort = {result_str}"
        test_ok = result == sorted(array)
        output += " " * (TEST_POS - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        output += " " * (TIME_POS - len(output)) + f"{t*1e3:>8.0f} ms"
        print(output)

        t = time.time()
        result = merge_sort([*array])
        t = time.time() - t
        result_str = str(result)
        if len(result_str) > 25:
            result_str = result_str[:20] + " ...]"
        output = f"       merge_sort = {result_str}"
        test_ok = result == sorted(array)
        output += " " * (TEST_POS - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        output += " " * (TIME_POS - len(output)) + f"{t*1e3:>8.0f} ms"
        print(output)
        t = time.time()
        result = quicksort([*array])
        t = time.time() - t
        result_str = str(result)
        if len(result_str) > 25:
            result_str = result_str[:20] + " ...]"
        output = f"        quicksort = {result_str}"
        test_ok = result == sorted(array)
        output += " " * (TEST_POS - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        output += " " * (TIME_POS - len(output)) + f"{t*1e3:>8.0f} ms"
        print(output)

        print()
