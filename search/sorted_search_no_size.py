"""
CRACKING THE CODING INTERVIEW
10.4 Sorted search, no size.

You are given an array-like data structure `Listy` which lacks a size method.
it does, however, have an `elementAt(i)` method that returns the element at
index `i` in O(1) time. If `i` is beyond the bounds of the data structure, it
returns -1. (For this reason, the data structure only supports positive integers).
Given `Listy` which contains sorted, positive integers, find the index at which
an element `x` occurs. If `x` occurs multiple times, you may return any index.
"""
import time
import random
import cProfile


def element_at(array: list, index: int) -> int:
    return array[index] if index < len(array) else -1


def target_interval(array: list, target: int) -> tuple:
    # Assumption: instead of using a `Listy` data structure, we're going
    # to use a list and the method `element_at()`.

    # Store the previous and current indices
    prev, curr = 0, 0

    # Store the current element
    value = element_at(array, curr)

    # Test the boundaries of the array.
    # Loop over until `current` is greater or equal to `target`
    while value < target:

        # Initialize the step to 1 for the current iteration
        step = 1

        # Loop over until we find a boundary of the array or
        # `target` is within the interval [prev, curr]
        # doubling `index` in each iteration
        # print('while 1 start --> index', prev, curr)
        while value > -1 and value < target:
            prev = curr
            curr += step
            value = element_at(array, curr)
            # Double the step
            # print('while 2 indeces', prev, curr, ' ::step', step)
            step *= 2

        # Check if the target is not in the array
        if curr - prev == 1 and value != target:
            # If the difference between `curr` and `prev` is 1
            # and `target` hasn't been found, it means that
            # no matter how small the steps are, it's not possible to
            # find it because it's not in the sorted array
            return None

        # If we've passed the boundary, undo the last iteration
        # to be checked again with more precission (smaller steps)
        if value == -1:
            # Undo the last iteration
            curr = prev
            prev -= step // 4
            value = element_at(array, curr)

    # Return interval as a tuple
    return prev, curr


def binary_search(nums: list, target: int, left: int, right: int) -> int:
    if left > right:
        return -1

    mid = (left + right) // 2
    if nums[mid] == target:
        return mid

    if nums[mid] > target:
        return binary_search(nums, target, left, mid - 1)
    else:
        return binary_search(nums, target, mid + 1, right)


def ssns(nums: list, target: int) -> int:
    # Time complexity: O(logn)
    # Space complexity: O(1)

    # Find the interval
    interval = target_interval(nums, target)

    # Edge case
    if interval is None:
        # If the returned interval is None, `target` is not in `nums`
        return -1

    # Find the target with binary search
    return binary_search(nums, target, *interval)


def ssns2(nums: list, target: int) -> int:
    def binary_search(nums: list, target: int, left: int, right: int) -> int:
        if left > right:
            return -1

        mid = (left + right) // 2
        value = element_at(nums, mid)
        if value == target:
            return mid
        if target < value or value == -1:
            return binary_search(nums, target, left, mid - 1)
        if value < target:
            return binary_search(nums, target, mid + 1, right)

    index = 1
    while element_at(nums, index) != -1 and element_at(nums, index) < target:
        index *= 2

    return binary_search(nums, target, index // 2, index)


if __name__ == "__main__":
    print("-" * 60)
    print("Sorted search, no size")
    print("-" * 60)
    size = 16
    crescendo = [i for i in range(size)]
    test_cases = [
        ([1], 1, 0),
        ([1], 5, -1),
        ([1, 1], 1, 0),
        ([1, 1, 1], 1, 0),  # returns the first occurrence
        ([8, 10, 13, 25, 64, 81], 5, -1),
        ([8, 10, 13, 25, 64, 81], 8, 0),
        ([8, 10, 13, 25, 64, 81], 9, -1),
        ([8, 10, 13, 25, 64, 81], 13, 2),
        ([8, 10, 13, 25, 64, 81], 25, 3),
        *[(crescendo, i, i if i < size else -1) for i in range(size + 2)],
    ]

    for nums, target, solution in test_cases:
        array_string = str(nums)
        if len(array_string) > 20:
            array_string = array_string[:20] + "...]"

        result = ssns(nums, target)
        string = f"sol1{array_string, target} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = ssns2(nums, target)
        string = f"sol2{array_string, target} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()

    # case = 0
    # array = test_cases[case][0]
    # target = 15
    # print(array)
    # # print(target, target_invterval(array, target))
    # for target in range(0, 20):
    #     print(target, target_interval(array, target))

    size = int(1e8)
    iterations = 1000
    print(f"\n>>> Performance test - Array size: {size} - Iterations: {iterations}")
    array = [i for i in range(size)]

    t = time.time()
    for _ in range(iterations):
        target = random.randint(0, size)
        ssns2(array, target)
    t = time.time() - t
    print(f"Method 2: {t*1e3:>8.0f} ms")

    t = time.time()
    for _ in range(iterations):
        target = random.randint(0, size)
        ssns(array, target)
    t = time.time() - t
    print(f"Method 1: {t*1e3:>8.0f} ms")

    target = random.randint(0, size)
    print("\n>>> Method 1")
    cProfile.run("ssns(array,target)")
    print(">>> Method 2")
    cProfile.run("ssns2(array,target)")
