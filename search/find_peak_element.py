"""
https://leetcode.com/problems/find-peak-element/

A peak element is an element that is 
strictly greater than its neighbors.

Given an integer array nums, find a peak element, 
and return its index. If the array contains 
multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should 
return the index number 2.

Example 2:
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index 
number 1 where the peak element is 2, or index number 5 
where the peak element is 6.

Constraints:
1 <= nums.length <= 1000
-2^31 <= nums[i] <= 2^31 - 1
nums[i] != nums[i + 1] for all valid i.
"""
from typing import List


def linear_scan(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    # Strategy: starting from index 0, if the next number (i + 1)
    # is less than the current (i), the current number is a peak
    n = len(nums)
    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            return i

    # If peak not found, the last element is a peak
    return n - 1


def binary_search_recursive(nums: List[int]) -> int:
    # Time complexity: O(logn)
    # Space complexity: O(logn)

    def bs(left: int, right: int) -> int:
        # Binary search - Recursive function

        # Base case
        if left == right:
            return right

        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            return bs(left, mid)
        return bs(mid + 1, right)

    return bs(0, len(nums) - 1)


def binary_search_iterative(nums: List[int]) -> int:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    # Strategy: check the slope of the element (mid, mid + 1).
    # If the slope is positive (greater numbers towards the right),
    # there'll be a peak to the right of `mid`;
    # otherwise, there'll be a peak to the left

    # Binary search
    left, right = 0, len(nums) - 1
    while left < right:
        # Middle index (avoids overflow)
        mid = left + (right - left) // 2

        if nums[mid] > nums[mid + 1]:
            # If the slope is negative (number increases
            # towards the left), move the right pointer
            # to the current `mid`
            right = mid
        else:
            # If the slope is positive (number increases
            # towards the right), move the left pointer
            # to `mid + 1`.
            # `+1` to avoid an infinite loop, since `mid` is going
            # to always lean towards the left due to
            # the integer division:
            #   0 1 2 3 4 5
            #   L M   R
            left = mid + 1

    return right


if __name__ == "__main__":
    print("-" * 60)
    print("Find peak element")
    print("-" * 60)

    test_cases = [
        ([3], 0),
        ([3, 2], 0),
        ([3, 2, 1], 0),
        ([1, 2, 3], 2),
        ([1, 2, 3, 1], 2),
        ([1, 2, 1, 3, 5, 6, 4], (1, 5)),
        ([1, 2, 3, 5, 8, 3, 4], (4, 6)),
    ]

    for nums, solution in test_cases:

        print("Array:", nums)

        result = linear_scan(nums)
        output = f"              linear_scan = "
        output += " " * (10 - len(output))
        test_ok = result == solution
        if isinstance(solution, tuple):
            test_ok = result in solution
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = binary_search_recursive(nums)
        output = f"  binary_search_recursive = "
        output += " " * (10 - len(output))
        test_ok = result == solution
        if isinstance(solution, tuple):
            test_ok = result in solution
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = binary_search_iterative(nums)
        output = f"  binary_search_iterative = "
        output += " " * (10 - len(output))
        test_ok = result == solution
        if isinstance(solution, tuple):
            test_ok = result in solution
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
