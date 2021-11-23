"""
https://leetcode.com/problems/missing-number/

Given an array nums containing n distinct numbers in the 
range [0, n], return the only number in the range that 
is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, 
so all numbers are in the range [0,3]. 2 is the missing 
number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, 
so all numbers are in the range [0,2]. 2 is the missing 
number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, 
so all numbers are in the range [0,9]. 8 is the missing 
number in the range since it does not appear in nums.

Example 4:
Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, 
so all numbers are in the range [0,1]. 1 is the missing 
number in the range since it does not appear in nums.

Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
"""


def missing_number(nums: list) -> int:
    # Time complexity: O(n)
    # a ^ a = 0
    # a ^ 0 = a
    # a ^ b ^ b = a
    # a ^ b ^ c ^ d ^ b ^ c ^ d  = a
    n = len(nums)
    res = n
    for i in range(n):
        res ^= i ^ nums[i]

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Missing number")
    print("-" * 60)

    test_cases = [
        ([0, 1, 3, 4], 2),
        ([0, 4, 3, 2], 1),
        ([0, 4, 1, 2], 3),
        ([3, 4, 1, 2], 0),
    ]

    for nums, solution in test_cases:

        string = f"missing_number({nums}) = "
        string += " " * (35 - len(string))
        result = missing_number(nums)
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
