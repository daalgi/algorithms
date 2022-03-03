"""
https://leetcode.com/problems/valid-mountain-array/

Given an array of integers arr, return true if 
and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 
Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true

Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 10^4
"""
from typing import List


def one_pass(nums: List[int]) -> bool:
    # Time complexity: O(n)
    # Space complexity: O(1)

    n = len(nums)
    if n < 3:
        return False

    i = 1

    # Strictly increasing elements
    while i < n and nums[i] > nums[i - 1]:
        i += 1

    if i == n or i == 1:
        # If i == n --> no decreasing elements
        # If i == 1 --> no increasing elements
        return False

    # Strictly decreasing elements
    while i < n and nums[i] < nums[i - 1]:
        i += 1

    # True if we've reached the end of the array
    return i == n


if __name__ == "__main__":
    print("-" * 60)
    print("Valid mountain array")
    print("-" * 60)

    test_cases = [
        ([1, 2], False),
        ([1, 2, 3, 4, 5], False),
        ([1, 2, 3, 4, 5, 3], True),
        ([1, 2, 3, 4, 5, 3, 2, 3], False),
        ([1, 2, 3, 3, 2], False),
        ([11, 9, 3, 2, 1], False),
        ([1, 11, 9, 3, 2, 1], True),
    ]

    for nums, solution in test_cases:

        print("Nums:", nums)

        result = one_pass(nums)
        output = "    one_pass = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
