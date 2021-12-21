"""
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

Given the array of integers nums, you will choose two different indices 
i and j of that array. Return the maximum value of 
(nums[i]-1)*(nums[j]-1).

Example 1:
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), 
you will get the maximum value, that is, 
(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

Example 2:
Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), 
you will get the maximum value of (5-1)*(5-1) = 16.

Example 3:
Input: nums = [3,7]
Output: 12

Constraints:
2 <= nums.length <= 500
1 <= nums[i] <= 10^3
"""
from typing import List
import heapq
import math


def scan(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    # max1 >= max2
    max1 = max2 = -math.inf
    for num in nums:
        if num >= max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    return (max1 - 1) * (max2 - 1)


def heapmax1(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Create an empty list to be used as a heap
    heap = []

    # Push the value items onto the heap, maintaining the heap invariant
    for num in nums:
        heapq.heappush(heap, num)

    # Get the two largest values
    # `heapq.nlargest(k, heap)`
    #   returns a list sorted in descending order of size `k`
    # print(heapq.nlargest(2, heap))
    # max1 = heapq.nlargest(2, heap)[-2]  # max
    # max2 = heapq.nlargest(2, heap)[-1]  # 2nd max
    max1, max2 = heapq.nlargest(2, heap)
    return (max1 - 1) * (max2 - 1)


def heapmax2(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Transform list `nums` into a heap, in-place, in linear time
    heapq.heapify(nums)

    # Get the two largest values
    # `heapq.nlargest(k, heap)`
    #   returns a list sorted in descending order of size `k`
    # print(heapq.nlargest(2, heap))
    # max1 = heapq.nlargest(2, nums)[-2]  # max
    # max2 = heapq.nlargest(2, nums)[-1]  # 2nd max
    max1, max2 = heapq.nlargest(2, nums)
    return (max1 - 1) * (max2 - 1)


if __name__ == "__main__":
    print("-" * 60)
    print("Maximum product of two elements in an array")
    print("-" * 60)

    test_cases = [
        ([1, 2], 0),
        ([3, 7], 12),
        ([3, 4, 5, 2], 12),
        ([1, 5, 4, 5], 16),
        ([1, 5, 4, 8, 13, 25, 3, 2, 5], 12 * 24),
    ]

    for nums, solution in test_cases:

        print("List:", nums)

        result = scan([*nums])
        output = f"\t    scan = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = heapmax1([*nums])
        output = f"\theapmax1 = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = heapmax2([*nums])
        output = f"\theapmax2 = "
        output += " " * (25 - len(output))
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = solution == result
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
