"""
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum 
and return its sum.

A subarray is a contiguous part of an array. 

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

def brute_force(nums: list) -> bool:
    # O(n2)
    n = len(nums)
    current_max = nums[0]
    for i in range(n - 1):
        current_sum = nums[i]
        for j in range(i + 1, n):
            current_sum += nums[j]
            if current_sum > current_max:
                current_max = current_sum
    return current_max

def efficient(nums: list) -> bool:
    # O(n)
    n = len(nums)
    current_sum = nums[0]
    current_max = current_sum
    for i in range(1, n):
        current_sum = max(current_sum + nums[i], nums[i])
        if current_sum > current_max:
            current_max = current_sum
    return current_max

    
if __name__ == "__main__":
    print('-' * 60)
    print('Maximum subarray')
    print('-' * 60)
    
    test_cases = [
        ([1], 1),
        ([1, 1], 2),
        ([5, 4, -1, 7, 8], 23),
        ([-2, 1, -3, 4, -1, 2, 1, -5, 1], 6),
    ]
    
    for arr, solution in test_cases:
        
        result = brute_force(arr)        
        string = f'brute_force{arr} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = efficient(arr)        
        string = f'  efficient{arr} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()