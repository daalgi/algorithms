"""
https://leetcode.com/problems/array-of-doubled-pairs/

Given an integer array of even length arr, 
return true if it is possible to reorder arr such 
that arr[2 * i + 1] = 2 * arr[2 * i] for 
every 0 <= i < len(arr) / 2, or false otherwise.

Example 1:
Input: arr = [3,1,3,6]
Output: false

Example 2:
Input: arr = [2,1,2,6]
Output: false

Example 3:
Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to 
form [-2,-4,2,4] or [2,4,-2,-4].

Constraints:
2 <= arr.length <= 3 * 10^4
arr.length is even.
-10^5 <= arr[i] <= 10^5
"""
from typing import List
from copy import deepcopy
from collections import Counter


def hashmap(arr: List[int]) -> bool:
    # Time complexity: O(nlogn + n) = O(nlogn)
    # Space complexity: O(n)

    # Sort the array, so we can start from the smallest
    # number, so there is only one choice of valid pairs
    # as we loop over the array: only the smallest
    # (or biggest) absolute value has only one possible
    # pair.
    arr.sort()

    # Use a hashmap for O(1) lookups of the available
    # numbers to form a pair { num: count_available }
    available = {}

    pairs_count = 0

    # Loop over the elements of `arr`
    for num in arr:
        double = num * 2
        half = num // 2
        if double in available:
            # If the current number's double is
            # available in the hashmap
            available[double] -= 1
            if available[double] == 0:
                del available[double]
            pairs_count += 1

        elif num & 1 == 0 and half in available:
            # If the current number is even, and its
            # half is in available in the hashmap
            available[half] -= 1
            if available[half] == 0:
                del available[half]
            pairs_count += 1

        else:
            # Add the current number to the hashmap
            available[num] = available.get(num, 0) + 1

    return pairs_count == len(arr) // 2


def hashmap2(arr: List[int]) -> bool:
    # Time complexity: O(nlogn + n) = O(nlogn)
    # Space complexity: O(n)

    # Sort the array by absolute value, so
    # the smallest value will only have one pair
    # Note: faster runtime if done directly in the loop
    # `for num in sorted(arr, key=abs)`
    arr.sort(key=abs)

    counter = Counter(arr)

    for num in arr:
        if counter[num] == 0:
            # Current `num` already forming a pair
            # with `num // 2` (in previous iterations)
            continue

        if counter[2 * num] == 0:
            # If `num` hasn't been paired yet,
            # but `2 * num` doesn't exist
            return False

        # Update the counter
        counter[num] -= 1
        counter[2 * num] -= 1

    return True


if __name__ == "__main__":
    print("-" * 60)
    print("Array of doubled pairs")
    print("-" * 60)

    test_cases = [
        ([1, 2], True),
        ([1, 3], False),
        ([3, 1, 3, 6], False),
        ([2, 1, 2, 6], False),
        ([4, -2, 2, -4], True),
        ([2, 4, 0, 0, 8, 1], True),
        ([2, 1, 2, 1, 1, 1, 2, 2], True),
    ]

    for arr, solution in test_cases:

        print("Array:", arr)

        result = hashmap(deepcopy(arr))
        output = "    hashmap = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap2(deepcopy(arr))
        output = "   hashmap2 = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
