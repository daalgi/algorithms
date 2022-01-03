"""
QuckSort operates on the input array only thruogh repeated 
swaps of pairs of elements, so it only allocates a miniscule
amount of additional memory for intermediate computations.

Running time: O(n log(n))

Step 1: Choose a pivot element.
Step 2: Rearrange the input array around the pivot.
"""
import random
import time


def quicksort1(a: list, pivot_method: str = "median", verbose: bool = False):
    # pivot_method: 'median', 'random', 'first', 'last'

    def partition(a: list, left: int, right: int):
        """
        Takes as input an array `a` but operates only on
        the subarray of elements a[left], ..., a[right],
        where `start` and `end` are given parameters.

        Swaps elements of the subarray.

        Returns the final pivot position.
        """
        pivot_index = choose_pivot(left, right)
        pivot = a[pivot_index]

        if verbose:
            print(
                f"Method: {pivot_method},\tPivot index: {pivot_index},\tPivot value: {pivot}"
            )

        while left <= right:
            while a[left] < pivot:
                left += 1
            while a[right] > pivot:
                right -= 1
            if left <= right:
                swap(a, left, right)
                left += 1
                right -= 1
        return left

    def swap(a: list, i: int, j: int):
        if verbose:
            print(f"Swap: {i, j}")
            print(a)
        a[i], a[j] = a[j], a[i]
        if verbose:
            print(a)

    def choose_pivot(start: int, end: int):
        if pivot_method == "median":
            return (start + end) // 2
        elif pivot_method == "random":
            return random.randint(start, end)
        elif pivot_method == "first":
            return start
        elif pivot_method == "last":
            return end - 1
        else:
            return (start + end) // 2

    def quicksort(a: list, left: int, right: int):
        index = partition(a, left, right)

        if verbose:
            print(f"\nQuicksort call interval: {left, right}")

        if left < right - 1:
            quicksort(a, left, index - 1)
        if index < right:
            quicksort(a, index, right)

        return a

    quicksort(a, 0, len(a) - 1)
    return a


def quicksort2low(a_list):
    # Source:
    # https://stackoverflow.com/questions/18262306/quicksort-with-python/20258416
    """Hoare partition scheme, see https://en.wikipedia.org/wiki/Quicksort"""

    def _quicksort(a_list, low, high):
        # must run partition on sections with 2 elements or more
        if low < high:
            p = partition(a_list, low, high)
            _quicksort(a_list, low, p)
            _quicksort(a_list, p + 1, high)

    def partition(a_list, low, high):
        pivot = a_list[low]
        while True:
            while a_list[low] < pivot:
                low += 1
            while a_list[high] > pivot:
                high -= 1
            if low >= high:
                return high
            a_list[low], a_list[high] = a_list[high], a_list[low]
            low += 1
            high -= 1

    _quicksort(a_list, 0, len(a_list) - 1)
    return a_list


def quicksort2high(a_list):
    # Source:
    # https://stackoverflow.com/questions/18262306/quicksort-with-python/20258416
    """Hoare partition scheme, see https://en.wikipedia.org/wiki/Quicksort"""

    def _quicksort(a_list, low, high):
        # must run partition on sections with 2 elements or more
        if low < high:
            p = partition(a_list, low, high)
            _quicksort(a_list, low, p)
            _quicksort(a_list, p + 1, high)

    def partition(a_list, low, high):
        pivot = a_list[high - 1]
        while True:
            while a_list[low] < pivot:
                low += 1
            while a_list[high] > pivot:
                high -= 1
            if low >= high:
                return high
            a_list[low], a_list[high] = a_list[high], a_list[low]
            low += 1
            high -= 1

    _quicksort(a_list, 0, len(a_list) - 1)
    return a_list


def quicksort2median(a_list):
    # Source:
    # https://stackoverflow.com/questions/18262306/quicksort-with-python/20258416
    """Hoare partition scheme, see https://en.wikipedia.org/wiki/Quicksort"""

    def _quicksort(a_list, low, high):
        # must run partition on sections with 2 elements or more
        if low < high:
            p = partition(a_list, low, high)
            _quicksort(a_list, low, p)
            _quicksort(a_list, p + 1, high)

    def partition(a_list, low, high):
        pivot = a_list[(low + high) // 2]
        while True:
            while a_list[low] < pivot:
                low += 1
            while a_list[high] > pivot:
                high -= 1
            if low >= high:
                return high
            a_list[low], a_list[high] = a_list[high], a_list[low]
            low += 1
            high -= 1

    _quicksort(a_list, 0, len(a_list) - 1)
    return a_list


def quicksort2random(a_list):
    # Source:
    # https://stackoverflow.com/questions/18262306/quicksort-with-python/20258416
    """Hoare partition scheme, see https://en.wikipedia.org/wiki/Quicksort"""

    def _quicksort(a_list, low, high):
        # must run partition on sections with 2 elements or more
        if low < high:
            p = partition(a_list, low, high)
            _quicksort(a_list, low, p)
            _quicksort(a_list, p + 1, high)

    def partition(a_list, low, high):
        pivot = a_list[random.randint(low, high)]
        while True:
            while a_list[low] < pivot:
                low += 1
            while a_list[high] > pivot:
                high -= 1
            if low >= high:
                return high
            a_list[low], a_list[high] = a_list[high], a_list[low]
            low += 1
            high -= 1

    _quicksort(a_list, 0, len(a_list) - 1)
    return a_list


def quicksort3(xs):
    # Source:
    # https://stackoverflow.com/questions/18262306/quicksort-with-python/20258416
    return xs and (
        quicksort3([i for i in xs[1:] if i < xs[0]])
        + [xs[0]]
        + quicksort3([i for i in xs[1:] if i >= xs[0]])
    )


def quicksort4(xs, fst, lst):
    """
    Source:
    https://stackoverflow.com/questions/18262306/quicksort-with-python/20258416

    Sort the range xs[fst, lst] in-place with vanilla QuickSort

    :param xs:  the list of numbers to sort
    :param fst: the first index from xs to begin sorting from,
                must be in the range [0, len(xs))
    :param lst: the last index from xs to stop sorting at
                must be in the range [fst, len(xs))
    :return:    nothing, the side effect is that xs[fst, lst] is sorted
    """
    if fst >= lst:
        return

    i, j = fst, lst
    pivot = xs[random.randint(fst, lst)]

    while i <= j:
        while xs[i] < pivot:
            i += 1
        while xs[j] > pivot:
            j -= 1

        if i <= j:
            xs[i], xs[j] = xs[j], xs[i]
            i, j = i + 1, j - 1
    quicksort4(xs, fst, j)
    quicksort4(xs, i, lst)


def quicksort(arr: list) -> list:
    def _quicksort(arr: list, left: int, right: int):
        if left < right:
            p = partition(arr, left, right)
            _quicksort(arr, left, p)
            _quicksort(arr, p+1, right)

    def partition(arr: list, left: int, right: int) -> int:
        pivot = arr[(left + right) // 2]
        while True:
            while arr[left] < pivot:
                left += 1
            while arr[right] > pivot:
                right -= 1
            if left >= right:
                return right
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    _quicksort(arr, 0, len(arr) - 1)
    return arr


if __name__ == "__main__":
    print("\n" + "-" * 60)
    print("Quicksort")
    print("-" * 60)

    test_cases = [
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([8, 7], [7, 8]),
        ([3, 2, 1, 4], [1, 2, 3, 4]),
        ([1, 8, -3, -8, 1, 1], [-8, -3, 1, 1, 1, 8]),
        ([0.1, -0.8, -2, 3.8], [-2, -0.8, 0.1, 3.8]),
        ([-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 1, 1, 1, 1, 1, 0], [0, 1, 1, 1, 1, 1, 1]),
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
        array = [*array]
        string = f"quicksort({str(array)}) = {str(quicksort(array))}"
        string += " " * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == array else "NOT OK"}')
    print()

    case = -2
    arr = test_cases[case][0]
    print(f"\n>>> Verbose example:", arr)
    quicksort1([*arr], verbose=True)

    size = int(5e5)
    print(f"\n\n>>> Performance test - Random array size: {size}")
    arr = [random.randint(0, size) for _ in range(size)]

    t = time.time()
    quicksort1([*arr], pivot_method="random")
    t = time.time() - t
    print(f"Method 1-random:   {t*1e3:>8.0f} ms")

    t = time.time()
    quicksort1([*arr], pivot_method="first")
    t = time.time() - t
    print(f"Method 1-first:    {t*1e3:>8.0f} ms")

    t = time.time()
    quicksort1([*arr], pivot_method="last")
    t = time.time() - t
    print(f"Method 1-last:     {t*1e3:>8.0f} ms")

    t = time.time()
    quicksort1([*arr], pivot_method="median")
    t = time.time() - t
    print(f"Method 1-median:   {t*1e3:>8.0f} ms")

    t = time.time()
    quicksort2low([*arr])
    t = time.time() - t
    print(f"Method 2-low:      {t*1e3:>8.0f} ms")

    t = time.time()
    quicksort2high([*arr])
    t = time.time() - t
    print(f"Method 2-high:     {t*1e3:>8.0f} ms")

    t = time.time()
    quicksort2median([*arr])
    t = time.time() - t
    print(f"Method 2-median:   {t*1e3:>8.0f} ms")

    t = time.time()
    quicksort2random([*arr])
    t = time.time() - t
    print(f"Method 2-random:   {t*1e3:>8.0f} ms")

    t = time.time()
    quicksort3([*arr])
    t = time.time() - t
    print(f"Method 3:          {t*1e3:>8.0f} ms")

    t = time.time()
    quicksort4([*arr], 0, size - 1)
    t = time.time() - t
    print(f"Method 4:          {t*1e3:>8.0f} ms")
