"""
https://leetcode.com/problems/contains-duplicate/
Given an integer array nums, return true if any value appears at 
least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

def solve(nums: list) -> bool:
    # Define a hash set for linear lookups
    s = set()
    # Loop over the list O(n)
    for n in nums:
        if n in s:
            return True
        s.add(n)
    return False    


if __name__ == "__main__":
    print('-' * 60)
    print('Contains duplicate')
    print('-' * 60)
    
    test_cases = [
        ([1], False),
        ([1, 1], True),
        ([1, 0], False),
        ([1, 2], False),
        ([7, 1, 5, 3, 6, 4], False),
        [[7, 6, 4, 3, 7], True],
    ]
    
    for arr, solution in test_cases:
        
        result = solve(arr)        
        string = f'solve{arr} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')