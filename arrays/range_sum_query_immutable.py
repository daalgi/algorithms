"""
https://leetcode.com/problems/range-sum-query-immutable/

Given an integer array nums, handle multiple 
queries of the following type:

Calculate the sum of the elements of nums between 
indices left and right inclusive where 
left <= right.

Implement the NumArray class:
- NumArray(int[] nums) Initializes the object with 
the integer array nums.
- int sumRange(int left, int right) Returns the sum 
of the elements of nums between indices left and right 
inclusive 
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Example 1:
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
 

Constraints:
1 <= nums.length <= 10^4
-105 <= nums[i] <= 10^5
0 <= left <= right < nums.length
At most 10^4 calls will be made to sumRange.


Example:
 indices    0  1  2  3   4
 array      1  2  3  2  -1
 prefix sum 1  3  6  8   7
 Ranges:                using prefx_sum array
    [0, 1]: 1 + 2 = 3  = 3 
    [0, 2]: 1 + 2 + 3  = 6
    [1, 2]: 2 + 3 = 5  = 6 - 1
    [1, 3]: 2 + 3 + 2  = 7 = 8 - 1
    [2, 3]: 3 + 2 = 5  = 8 - 3
"""
from typing import List


def prefix_sum(nums: List[int], left: int, right: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    n = len(nums)
    acc = [nums[0]]
    for i in range(1, n):
        acc.append(acc[-1] + nums[i])

    if left == 0:
        return acc[right]
    return acc[right] - acc[left - 1]


def prefix_sum2(nums: List[int], left: int, right: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    acc = [0]
    for num in nums:
        acc.append(acc[-1] + num)

    return acc[right + 1] - acc[left]


if __name__ == "__main__":
    print("-" * 60)
    print("Range sum query - Immutable")
    print("-" * 60)

    test_cases = [
        # (nums, left, right, solution)
        ([-2, 0, 3, -5, 2, -1], 0, 2, 1),
        ([-2, 0, 3, -5, 2, -1], 2, 5, -1),
        ([-2, 0, 3, -5, 2, -1], 0, 5, -3),
        ([-2, 0, 3, -5, 2, -1], 0, 0, -2),
        ([-2, 0, 3, -5, 2, -1], 5, 5, -1),
        ([-2, 0, 3, -5, 2, -1], 1, 4, 0),
    ]

    for i, (nums, left, right, solution) in enumerate(test_cases):

        if i == 0 or test_cases[i][0] != test_cases[i - 1][0]:
            print("Nums:", nums)

        print(f"Range: {left, right}")
        result = prefix_sum(nums, left, right)
        output = "    prefix_sum = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = prefix_sum2(nums, left, right)
        output = "   prefix_sum2 = "
        output += str(result)
        output += " " * (60 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
