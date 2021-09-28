"""
https://leetcode.com/problems/move-zeroes/
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""

def suboptimal(nums: list) -> list:
    # O(n), but the number of writes (or swaps) 
    # can be optimized.
    
    # slow pointer `k` indicating the last_non_zero_found_at
    k = 0 
    n = len(nums)
    for i in range(n):
        if k < i and nums[i] != 0:
            nums[k], nums[i] = nums[i], nums[k]
            k += 1
        elif nums[i] != 0:
            k += 1
    return nums

def optimal(nums: list) -> list:
    # O(n) with minimal writes,
    # altough for an array like [0, 0, 0, 0, 1]
    # the number of swaps could be optimized.

    # slow pointer `k` indicating the last_non_zero_found_at
    k = 0 
    n = len(nums)
    for i in range(n):
        if nums[i] != 0:
            nums[k] = nums[i]
            k += 1            

    for i in range(k, n):
        nums[i] = 0
    
    return nums



if __name__ == "__main__":
    print('-' * 60)
    print('Move zeroes')
    print('-' * 60)
    
    test_cases = [
        ([0], [0]),
        ([1], [1]),
        ([0, 0, 0], [0, 0, 0]),
        ([0, 1, 2], [1, 2, 0]),
        ([5, 0, 2], [5, 2, 0]),
        ([5, 1, 0], [5, 1, 0]),
        ([5, 1, 2], [5, 1, 2]),
        ([0, 0, 2], [2, 0, 0]),
        ([0, 2, 0], [2, 0, 0]),
        ([2, 0, 0], [2, 0, 0]),
        ([0, 0, 2, 0, 0], [2, 0, 0, 0, 0]),
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([1, 0, 0, 0, 3, 2], [1, 3, 2, 0, 0, 0]),
    ]
    
    for a, solution in test_cases:
        
        arr_string = str(a)

        result = suboptimal(a)
        string = f'suboptimal{arr_string} = '
        string += ' ' * (30 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = optimal(a)
        string = f'optimal{arr_string} = '
        string += ' ' * (30 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()