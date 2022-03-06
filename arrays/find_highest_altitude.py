"""
https://leetcode.com/problems/find-the-highest-altitude/

There is a biker going on a road trip. The road trip 
consists of n + 1 points at different altitudes. The 
biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where 
gain[i] is the net gain in altitude between points 
i and i + 1 for all (0 <= i < n). 
Return the highest altitude of a point.

Example 1:
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. 
The highest is 1.

Example 2:
Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. 
The highest is 0.

Constraints:
n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100
"""
from typing import List
from itertools import accumulate


def prefix_sum(nums: List[int]) -> int:
    # Time complexity: O(n²)
    # Space complexity: O(n)

    curr_height, n = nums[0], len(nums)
    max_gain = max(curr_height, 0)
    for i in range(1, n):
        curr_height += nums[i]
        max_gain = max(max_gain, curr_height)

    return max_gain


def prefix_sum2(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    return max(max(accumulate(nums)), 0)


if __name__ == "__main__":
    print("-" * 60)
    print("Find the highest altitude")
    print("-" * 60)

    test_cases = [
        # (gain, solution)
        ([1], 1),
        ([-2], 0),
        ([1, 2], 3),
        ([-1, 4, -2, -5, 3], 3),
        ([-5, 1, 5, 0, -7], 1),
        ([-4, -3, -2, -1, 4, 3, 2], 0),
        ([-4, -3, -2, -1, 4, -3, 2], 0),
    ]

    for nums, solution in test_cases:

        print("Gain:", nums)

        result = prefix_sum(nums)
        output = "    prefix_sum = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = prefix_sum2(nums)
        output = "   prefix_sum2 = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        # result = frequencies(nums)
        # output = "   frequencies = "
        # output += str(result)
        # output += " " * (60 - len(output))
        # test_ok = result == solution
        # output += f'Test: {"OK" if test_ok else "NOT OK"}'
        # print(output)

        print()
