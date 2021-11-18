"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Suppose an array of length n sorted in ascending order is rotated 
between 1 and n times. For example, the array 
nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time 
results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, 
return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.

Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

Example 3:
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 
Constraints:
n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""

def sol1(nums: list) -> int:
    # Binary search variation, where the decision
    # of the search direction is adapted to the problem.
    # Time complexity: O(logn)

    # Pointers defining the boundaries of the current subarray
    left, right = 0, len(nums) - 1

    # Check if the array is rotated
    if nums[left] < nums[right]:
        return nums[left]

    while right - left > 1:
        mid = (left + right) // 2
        if nums[mid] > nums[left] and nums[left] > nums[right]:
            left = mid
        else:
            right = mid

    if nums[left] < nums[right]:
        return nums[left]
    return nums[right]

def sol1b(nums: list) -> int:
    # Binary search variation, where the decision
    # of the search direction is adapted to the problem.
    # Time complexity: O(logn)

    # Pointers defining the boundaries of the current subarray
    left, right = 0, len(nums) - 1

    # Check if the array is rotated
    if nums[left] < nums[right]:
        return nums[left]

    while right - left > 1:
        mid = (left + right) // 2
        if nums[mid] > nums[0]:
            left = mid
        else:
            right = mid

    if nums[left] < nums[right]:
        return nums[left]
    return nums[right]

def sol2(nums: list) -> int:
    n = len(nums)
    if n == 1:
        return nums[0]

    # Pointers defining the boundaries of the current subarray
    left, right = 0, n - 1    

    # Check if the array is rotated
    if nums[0] <= nums[right]:
        return nums[0]

    while right > left:
        mid = (left + right) // 2

        # If we are in or next to the minimum,
        # return it
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        elif nums[mid-1] > nums[mid]:
            return nums[mid]

        # Update pointers depending on the current
        # mid value
        if nums[0] < nums[mid]:
            left = mid + 1
        else:
            right = mid - 1


if __name__ == "__main__":
    print('-' * 60)
    print('Find minimum in rotated sorted array')
    print('-' * 60)
    
    test_cases = [
        ([1], 1),
        ([-1, 0], -1),
        ([1, 0], 0),
        ([-1, 0, 2], -1),
        ([1, -1, 0], -1),
        ([0, 1, -4], -4),
        ([-2, 1, 2, 3], -2),
        ([3, -2, 1, 2], -2),
        ([2, 3, -2, 1], -2),
        ([1, 2, 3, -2], -2),
        ([1, 2, 3, 4, 5, 6, 7, 0], 0),
        ([1, 2, 3, 4, 5, 6, 7, -1, 0], -1),
        ([1, 2, 3, 4, 5, 6, 7, -2, -1, 0], -2),
        ([1, 2, 3, 4, 5, 6, 7, -3, -2, -1, 0], -3),
        ([1, 2, 3, 4, 5, 6, -4, -3, -2, -1, 0], -4),
        ([1, 2, 3, 4, 5, -5, -4, -3, -2, -1, 0], -5),
        ([1, 2, 3, 4, -6, -5, -4, -3, -2, -1, 0], -6),
        ([1, 2, 3, -7, -6, -5, -4, -3, -2, -1, 0], -7),
        ([1, 2, -8, -7, -6, -5, -4, -3, -2, -1, 0], -8),
        ([1, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0], -9),
        ([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0], -10),
    ]
    
    for nums, solution in test_cases:
        
        result = sol1(nums)        
        string = f' sol1{nums} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
        
        result = sol1b(nums)        
        string = f'sol1b{nums} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = sol2(nums)        
        string = f' sol2{nums} = '
        string += ' ' * (35 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
        
        print()