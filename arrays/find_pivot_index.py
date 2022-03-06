"""
https://leetcode.com/problems/find-pivot-index/

Given an array of integers nums, calculate 
the pivot index of this array.

The pivot index is the index where the sum of 
all the numbers strictly to the left of the 
index is equal to the sum of all the numbers 
strictly to the index's right.

If the index is on the left edge of the array, 
then the left sum is 0 because there are no 
elements to the left. This also applies to the 
right edge of the array.

Return the leftmost pivot index. If no such 
index exists, return -1.

Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions 
in the problem statement.

Example 3:
Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

Constraints:
1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
"""
from typing import List


def prefix_sum(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)

    acc = [0]
    for num in nums:
        acc.append(acc[-1] + num)

    n = len(acc)
    for i in range(1, n):
        if acc[i - 1] == acc[-1] - acc[i]:
            return i - 1

    return -1


def prefix_sum2(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    total, leftsum, n = sum(nums), 0, len(nums)

    for i in range(n):

        if leftsum == total - leftsum - nums[i]:
            return i

        leftsum += nums[i]

    return -1


def prefix_sum3(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    left, right, n = 0, sum(nums), len(nums)

    for i in range(n):
        right -= nums[i]
        if left == right:
            return i
        left += nums[i]

    return -1


if __name__ == "__main__":
    print("-" * 60)
    print("Find pivot index")
    print("-" * 60)

    test_cases = [
        # (nums, solution)
        ([0, 0], 0),
        ([1, 7, 3, 6, 5, 6], 3),
        ([1, 2, 3], -1),
        ([2, 1, -1], 0),
        ([-2, 0, 3, -5, 2, -1], 3),
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
