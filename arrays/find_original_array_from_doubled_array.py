"""
https://leetcode.com/problems/find-original-array-from-doubled-array/

An integer array original is transformed into a 
doubled array changed by appending twice the value 
of every element in original, and then randomly 
shuffling the resulting array.

Given an array changed, return original if changed 
is a doubled array. If changed is not a doubled array, 
return an empty array. The elements in original may 
be returned in any order.

Example 1:
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].

Example 2:
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:
Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.

Constraints:
1 <= changed.length <= 10^5
0 <= changed[i] <= 10^5
"""
from typing import List
from copy import deepcopy
from collections import Counter


def sorting1(changed: List[int]) -> List[int]:
    # Time complexity: O(n + klogk)
    # Space complexity: O(n)
    # where `n` is the number of elements in the input
    # array, and `k` is the number of unique elements.

    # Sort the elements of the array, and start from
    # the first element to check whether its double
    # exists. Use a hashmap for O(1) lookups.

    count = Counter(changed)
    original = []
    for num in sorted(changed):
        double = num * 2

        # If the current number's counter
        # is zero, it was a double from a previous
        # number, so skip it
        if count[num] == 0:
            continue

        # If the array doesn't have the double of
        # the current number, not valid array
        if count[double] == 0:
            return []

        # Edge case: if `num` is zero, but
        # the counter doesn't have two zeros,
        # invalid array
        if num == 0 and count[num] <= 1:
            return []

        # `num` and `double` exist on the counter,
        # so add `num` to the `original` array
        original.append(num)

        # Decrease the counter for both `num` and `double`
        count[num] -= 1
        count[double] -= 1

    return original


def sorting2(changed: List[int]) -> List[int]:
    # Time complexity: O(n + klogk)
    # Space complexity: O(n)
    # where `n` is the number of elements in the input
    # array, and `k` is the number of unique elements.

    count = Counter(changed)
    for num in sorted(count):
        double = num * 2

        # If there're not enough `double` for
        # `num`, not valid array
        if count[num] > count[double]:
            return []

        # Edge case: `num` is zero and
        # the count of zero is odd
        if num == 0 and count[num] & 1:
            return []

        # Update the count
        count[double] -= count[num] if num else count[num] // 2

    return list(count.elements())


if __name__ == "__main__":
    print("-" * 60)
    print("Find original array from doubled array")
    print("-" * 60)

    test_cases = [
        # (doubled_array, solution)
        ([1], []),
        ([1, 2], [1]),
        ([1, 0], []),
        ([0, 0], [0]),
        ([1, 3, 4, 2, 6, 8], [1, 3, 4]),
        ([6, 3, 0, 1], []),
        ([6, 3, 0, 0], [3, 0]),
        ([4, 4, 16, 20, 8, 8, 2, 10], [2, 4, 8, 10]),
        ([1, 4, 5, 2, 8, 10, 4, 16, 20], []),
    ]

    for doubled_array, solution in test_cases:

        print("Doubled array:", doubled_array)

        result = sorting1(deepcopy(doubled_array))
        output = f"         sorting1 = "
        output += str(result)
        test_ok = sorted(solution) == sorted(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sorting2(deepcopy(doubled_array))
        output = f"         sorting2 = "
        output += str(result)
        test_ok = sorted(solution) == sorted(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
