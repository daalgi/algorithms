"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in 
non-decreasing order, find the starting and ending 
position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""
from typing import List
from bisect import bisect_left, bisect_right


def binary_search_bisect(nums: List[int], target: int) -> List[int]:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    if not nums:
        return [-1, -1]
    left = bisect_left(nums, target)
    right = bisect_right(nums, target, lo=left) - 1
    if left == len(nums) or nums[left] != target:
        return [-1, -1]
    return [left, right]


def binary_search(nums: List[int], target: int) -> List[int]:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    if not nums:
        return [-1, -1]

    n = len(nums)

    # Binary search to find the first element
    lo, hi = 0, n - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1

    # Check if `target` was found
    left = lo
    if left == n or nums[left] != target:
        return [-1, -1]

    # Binary search to find the last element
    # Use previous `lo` as the left pointer
    hi = n - 1
    while lo < hi:
        # Force `mid` to tend towards the right,
        # so we can update `lo = mid` and `hi = mid - 1`
        # to find the rightmost element equal to `target`
        mid = (lo + hi + 1) // 2
        if nums[mid] <= target:
            lo = mid
        else:
            hi = mid - 1

    return [left, hi]


def binary_search2(nums: List[int], target: int) -> List[int]:
    # Time complexity: O(logn)
    # Space complexity: O(1)
    if not nums:
        return [-1, -1]

    n = len(nums)

    # Binary search to find the first element
    lo, hi = 0, n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    left = lo

    # Binary search to find the last element
    hi = n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] <= target:
            lo = mid + 1
        else:
            hi = mid - 1
    
    return [left, hi] if left <= hi else [-1, -1]



if __name__ == "__main__":
    print("-" * 60)
    print("Find first and last position of element in sorted array")
    print("-" * 60)

    test_cases = [
        # (nums, target, solution)
        ([], 6, [-1, -1]),
        ([1, 2, 3, 4, 5, 6], 5, [4, 4]),
        ([1, 2, 3, 4, 5, 6], 6, [5, 5]),
        ([1, 2, 3, 4, 5, 6], 7, [-1, -1]),
        ([1, 1, 1, 1, 5, 6], 1, [0, 3]),
        ([1, 1, 1, 1, 5, 6, 6, 6], 6, [5, 7]),
    ]

    for nums, target, solution in test_cases:

        print("Nums:", nums)
        print("Target:", target)

        result = binary_search(nums, target)
        output = f"          binary_search = "
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = binary_search2(nums, target)
        output = f"         binary_search2 = "
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = binary_search_bisect(nums, target)
        output = f"   binary_search_bisect = "
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
