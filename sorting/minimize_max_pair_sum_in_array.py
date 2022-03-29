"""
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

The pair sum of a pair (a,b) is equal to a + b. 
The maximum pair sum is the largest pair sum in a 
list of pairs.
- For example, if we have pairs (1,5), (2,3), and (4,4), 
the maximum pair sum would be 
max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.

Given an array nums of even length n, pair up the 
elements of nums into n / 2 pairs such that:
- Each element of nums is in exactly one pair, and
- The maximum pair sum is minimized.

Return the minimized maximum pair sum after optimally 
pairing up the elements.

Example 1:
Input: nums = [3,5,2,3]
Output: 7
Explanation: The elements can be paired up into pairs 
(3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.

Example 2:
Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: The elements can be paired up into 
pairs (3,5), (4,4), and (6,2).
The maximum pair sum is 
max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.

Constraints:
n == nums.length
2 <= n <= 10^5
n is even.
1 <= nums[i] <= 10^5
"""
from typing import List


def sort_two_pointers(nums: List[int]) -> int:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    nums.sort()

    left, right, max_sum = 0, len(nums) - 1, 0
    while left < right:
        max_sum = max(max_sum, nums[left] + nums[right])
        left += 1
        right -= 1

    return max_sum


if __name__ == "__main__":
    print("-" * 60)
    print("Minimize maximum pair sum in array")
    print("-" * 60)

    test_cases = [
        ([3, 5, 2, 3], 7),
        ([3, 5, 4, 2, 4, 6], 8),
        ([1, 1, 3, 3, 3, 3, 5, 5, 6, 7, 1, 1, 1, 8], 9),
    ]

    for nums, solution in test_cases:

        print("Nums:", nums)

        result = sort_two_pointers([*nums])
        output = f"    sort_two_pointers = "
        output += str(result)
        test_ok = result == solution
        output += " " * (60 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
