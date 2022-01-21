"""
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a contiguous non-empty 
subarray within the array that has the largest product, 
and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is 
not a subarray.
 
Constraints:
1 <= nums.length <= 2 * 10^4
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed 
to fit in a 32-bit integer.
"""
from typing import List


def brute_force(nums: List[int]) -> int:
    # Time complexity: O(n²)
    # Space complexity: O(1)
    n = len(nums)
    current_max = nums[0]
    for i in range(n - 1):
        current_prod = nums[i]
        for j in range(i + 1, n):
            current_prod *= nums[j]
            if current_prod > current_max:
                current_max = current_prod
    return current_max


def efficient(nums: List[int]) -> int:
    # Time complexity: O(2n) = O(n)
    # Space complexity: O(1)

    # Maximum individual number: O(n)
    res = max(nums)

    # Loop over the array: O(n)
    cur_max, cur_min = 1, 1
    for num in nums:

        # Edge case
        if num == 0:
            # Re-initialize `cur_max` and `cur_min`,
            # as if computing a different subarray
            cur_max, cur_min = 1, 1
            continue

        # Multiply previous prods by the current number
        temp_max = cur_max * num
        temp_min = cur_min * num

        # Re-evaluate the current max and min
        cur_max = max(temp_max, temp_min, num)
        cur_min = min(temp_max, temp_min, num)

        # Global maximum
        res = max(res, cur_max)

    return res


def efficient2(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Keep track of the maximum
    res = nums[0]

    # Loop over the array: O(n)
    cur_max, cur_min = 1, 1
    for num in nums:

        # Edge case
        if num == 0:
            # Re-initialize `cur_max` and `cur_min`,
            # as if computing a different subarray
            cur_max, cur_min = 1, 1
            res = max(res, num)
            continue

        # Multiply previous prods by the current number
        temp_max = cur_max * num
        temp_min = cur_min * num

        # Re-evaluate the current max and min
        cur_max = max(temp_max, temp_min, num)
        cur_min = min(temp_max, temp_min, num)

        # Global maximum
        res = max(res, cur_max)

    return res


def efficient3(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Keep track of the maximum and minimum so far at each iteration

    res = maxi = mini = nums[0]
    n = len(nums)
    for i in range(1, n):
        curr = nums[i]
        maxi, mini = max(curr, maxi * curr, mini * curr), min(
            curr, maxi * curr, mini * curr
        )
        res = max(res, maxi)

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Maximum product subarray")
    print("-" * 60)

    test_cases = [
        ([1], 1),
        ([1, 1], 1),
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([2, 3, -2, 4, 1, -2], 96),
        ([-1, 2, -1, -3, 3, 5], 90),
        ([-50, 2, -1, -3, 3, 5], 100),
        ([-50, 2, -1, 0, 3, 5], 100),
        ([-50, 0, -1, 0, 3, 5], 15),
    ]

    for arr, solution in test_cases:

        print("Array:", arr)
        result = brute_force(arr)
        string = f"    brute_force = "
        string += str(result)
        string += " " * (50 - len(string))
        print(string, f'Test: {"OK" if solution == result else "NOT OK"}')

        result = efficient(arr)
        string = f"      efficient = "
        string += str(result)
        string += " " * (50 - len(string))
        print(string, f'Test: {"OK" if solution == result else "NOT OK"}')

        result = efficient2(arr)
        string = f"     efficient2 = "
        string += str(result)
        string += " " * (50 - len(string))
        print(string, f'Test: {"OK" if solution == result else "NOT OK"}')

        result = efficient3(arr)
        string = f"     efficient3 = "
        string += str(result)
        string += " " * (50 - len(string))
        print(string, f'Test: {"OK" if solution == result else "NOT OK"}')

        print()
