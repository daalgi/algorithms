"""
https://leetcode.com/problems/find-the-middle-index-in-array/

Given a 0-indexed integer array nums, find the 
leftmost middleIndex (i.e., the smallest amongst 
all the possible ones).

A middleIndex is an index where 
nums[0] + nums[1] + ... + nums[middleIndex-1] 
    == nums[middleIndex+1] + nums[middleIndex+2] 
        + ... + nums[nums.length-1].

If middleIndex == 0, the left side sum is considered 
to be 0. Similarly, if middleIndex == nums.length - 1, 
the right side sum is considered to be 0.

Return the leftmost middleIndex that satisfies the 
condition, or -1 if there is no such index.

Example 1:
Input: nums = [2,3,-1,8,4]
Output: 3
Explanation: The sum of the numbers before index 3 is: 
2 + 3 + -1 = 4
The sum of the numbers after index 3 is: 4 = 4

Example 2:
Input: nums = [1,-1,4]
Output: 2
Explanation: The sum of the numbers before index 2 is: 
1 + -1 = 0
The sum of the numbers after index 2 is: 0

Example 3:
Input: nums = [2,5]
Output: -1
Explanation: There is no valid middleIndex.

Constraints:
1 <= nums.length <= 100
-1000 <= nums[i] <= 1000
"""
from typing import List


def prefix_sum(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    n = len(nums)
    acc = [nums[0]]
    for i in range(1, n):
        acc.append(acc[-1] + nums[i])

    # Check the first index
    if acc[-1] - nums[0] == 0:
        return 0

    # Check the rest of indices
    for i in range(n):
        if acc[i - 1] == acc[-1] - acc[i]:
            return i

    # Index doesn't exist
    return -1


def prefix_sum2(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Keep track of the sums of the elements
    # to the left and to the right of the current index
    leftsum, rightsum, n = 0, sum(nums), len(nums)

    for i in range(n):
        # Subtract the current index from the `rightsum`
        # (`leftsum` still not taking it into accout)
        rightsum -= nums[i]

        if leftsum == rightsum:
            return i

        # Update `leftsum` for next iteration
        leftsum += nums[i]

    # Not found
    return -1


if __name__ == "__main__":
    print("-" * 60)
    print("Find the middle index in array")
    print("-" * 60)

    test_cases = [
        # (nums, solution)
        ([2, 3, -1, 8, 4], 3),
        ([1, -1, 4], 2),
        ([1, -1, 1], 0),
        ([2, 5], -1),
    ]

    for nums, solution in test_cases:

        print("Nums:", nums)

        result = prefix_sum(nums)
        output = "      prefix_sum = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = prefix_sum2(nums)
        output = "     prefix_sum2 = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
