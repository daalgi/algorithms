"""
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

Given an array of integers nums, you start with 
an initial positive value startValue.

In each iteration, you calculate the step by 
step sum of startValue plus elements in nums 
(from left to right).

Return the minimum positive value of startValue 
such that the step by step sum is never less than 1.

Example 1:
Input: nums = [-3,2,-3,4,2]
Output: 5
Explanation: If you choose startValue = 4, in 
the third iteration your step by step sum is 
less than 1.

step by step sum
startValue = 4 | startValue = 5 | nums
  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
  (4 +2 ) = 6  | (5 +2 ) = 7    |   2

Example 2:
Input: nums = [1,2]
Output: 1
Explanation: Minimum start value should be positive. 

Example 3:
Input: nums = [1,-2,-3]
Output: 5

Constraints:
1 <= nums.length <= 100
-100 <= nums[i] <= 100
"""
from typing import List
from itertools import accumulate


def prefix_sum(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    prefix_sum = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)

    return max(-min(prefix_sum), 0) + 1


def prefix_sum2(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    min_step, curr = float("inf"), 0
    for num in nums:
        curr += num
        if curr < min_step:
            min_step = curr

    return max(-min_step, 0) + 1


def prefix_sum3(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    return max(-min(accumulate(nums)), 0) + 1


if __name__ == "__main__":
    print("-" * 60)
    print("Minimum value to get positive step by step sum")
    print("-" * 60)

    test_cases = [
        # (nums, solution)
        ([0, 0], 1),
        ([1, 7, 3, 6, 5, 6], 1),
        ([-3, 2, -3, 4, 2], 5),
        ([2, 1, -1], 1),
        ([-2, 0, 3, -5, 2, -1], 5),
        ([1, 2, 3, -3, 2, -6, 3, -4, -8, -86], 97),
    ]

    for nums, solution in test_cases:

        print("Nums:", nums)

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

        result = prefix_sum3(nums)
        output = "   prefix_sum3 = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
