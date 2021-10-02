"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the 
index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Example 4:
Input: nums = [1,3,5,6], target = 0
Output: 0

Example 5:
Input: nums = [1], target = 0
Output: 0 

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

def prev(nums: list, target: int) -> int:
    # Binary search O(logn)
    
    # Keep track of the min and max indeces 
    # of the considered array
    # (may change in each iteration)
    start = 0
    end = len(nums)
    
    # Base cases
    if target <= nums[0]:
        return 0
    elif target > nums[end - 1]:
        return end

    # Current index
    i = end // 2

    # Loop until found (always returns a value)
    # print(nums)
    while True:
        # print('-->', start, end, i, '-->', nums[i])
        if nums[i] == target:
            return i
        elif end - start == 1:
            if nums[i] < target:
                return i + 1
            return i
        elif nums[i] > target:
            end = i
            i = (start + end) // 2
        else:
            start = i
            i += (end - start) // 2


def iterative(nums: list, target: int) -> int:
    # Binary search O(logn)
    
    # Keep track of the min and max indeces 
    # of the considered array
    # (may change in each iteration)
    left = 0
    right = len(nums) - 1
    
    # Base cases
    if target <= nums[0]:
        return 0
    elif target == nums[right]:
        return right
    elif target > nums[right]:
        return right + 1

    # Loop until `left` and `right` cross
    while left <= right:
        # print('-->', start, end, i, '-->', nums[i])
        # Current index (subarray midpoint)
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left
    

def recursive(nums: int, target: int, left: int = 0, right: int = None) -> int:
    if right is None:
        right = len(nums) - 1
    
    # When the `left` pointer passes the `right` one,
    # means that the number doesn't exist in the array,
    # and in case of it were to be added to the sorted array,
    # its index would be equal to `left`.
    if left > right:
        return left

    # Mid point
    mid = (right + left) // 2

    # print(left, right, mid)
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return recursive(nums, target, mid + 1, right)
    return recursive(nums, target, left, mid - 1)
    

if __name__ == "__main__":
    print('-' * 60)
    print('Search insert position')
    print('-' * 60)
    
    test_cases = [
        ([1], 0, 0),
        ([1], 2, 1),
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1, 4, 6, 7, 8, 9], 6, 2),
        ([3, 6, 7, 8, 10], 5, 1),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 0, 0),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 1, 0),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 2, 1),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 3, 1),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 4, 2),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 5, 2),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 6, 3),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 7, 3),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 8, 4),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 9, 4),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 10, 5),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 11, 5),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 12, 6),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 13, 6),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 14, 7),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 15, 7),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 16, 8),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 17, 8),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17], 18, 9),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 0, 0),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 1, 0),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 3, 1),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 4, 1),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 5, 1),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 6, 2),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 7, 2),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 8, 2),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 9, 2),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 10, 3),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 11, 3),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 12, 3),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 13, 3),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 14, 4),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 15, 4),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 16, 4),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 17, 4),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 18, 5),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 19, 5),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 20, 5),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 21, 5),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 22, 6),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 23, 6),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 24, 6),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 25, 6),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 26, 7),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 27, 7),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 28, 7),
        ([1, 5, 9, 13, 17, 21, 25, 29, 33], 29, 7),
    ]
    
    for a, b, solution in test_cases:
        
        result = iterative(a, b)
        string = f'iterative{a, b} = '
        string += ' ' * (30 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = recursive(a, b)
        string = f'recursive{a, b} = '
        string += ' ' * (30 - len(string))
        string += str(result)
        string += ' ' * (70 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()