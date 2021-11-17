"""
CRACKING THE CODING INTERVIEW
10.3 Search in rotated array.
*Assumption: no repeating values

https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order 
(with distinct values).

Prior to being passed to your function, nums is possibly rotated 
at an unknown pivot index k (1 <= k < nums.length) such that the 
resulting array is 
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and 
become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""


def recursion(nums: list, target: int) -> int:
    # Binary search variation
    # Time complexity: O(logn)
    # Strategy: half of the array must be ordered normally, so
    # we can use this information to determine whether we
    # should search the left or the right half.

    def f(nums: list, left: int, right: int, target: int) -> int:
        # Base cases
        if left > right:
            # Pointers crossed, which indicates that
            # `target` doesn't exist in the array
            return None

        mid = (left + right) // 2
        if nums[mid] == target:
            # Target in the mid pointer
            return mid

        # Select a half to search for the target
        if nums[left] <= nums[mid]:
            # Left side is ordered normally
            # Note that we use "<=" to include the cases
            # of two element arrays, where left = mid
            if nums[left] <= target < nums[mid]:
                # Target in the left side --> search left side
                return f(nums, left, mid - 1, target)
            else:
                # Target in the right side --> search right side
                return f(nums, mid + 1, right, target)

        else:  # elif nums[left] > nums[mid]:
            # Right side is ordered normally
            if nums[mid] < target <= nums[right]:
                # Target in the right side --> search right side
                return f(nums, mid + 1, right, target)
            else:
                # Target in the left side --> search left side
                return f(nums, left, mid - 1, target)

    return f(nums, 0, len(nums) - 1, target)


def iterative(nums: list, target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            # Left half ordered normally
            if nums[left] <= target < nums[mid]:
                # Search in left half
                right = mid - 1
            else:
                # Search in right half
                left = mid + 1
        else:
            # Right half ordered normally
            if nums[mid] < target <= nums[right]:
                # Search in right half
                left = mid + 1
            else:
                # Search in left half
                right = mid - 1

    return None


if __name__ == "__main__":
    print("-" * 60)
    print("Search in rotated sorted array")
    print("-" * 60)

    test_cases = [
        ([1], 1, 0),
        ([1], 5, None),
        ([-1, 0], -1, 0),
        ([-1, 0], 0, 1),
        ([-1, 0], 8, None),
        ([-1, 0, 2], -1, 0),
        ([-1, 0, 2], 0, 1),
        ([-1, 0, 2], 2, 2),
        ([3, 1, 2], 3, 0),
        ([1, -1, 0], 1, 0),
        ([1, -1, 0], -1, 1),
        ([1, -1, 0], 0, 2),
        ([-2, 1, 2, 3], -2, 0),
        ([-2, 1, 2, 3], 1, 1),
        ([-2, 1, 2, 3], 2, 2),
        ([-2, 1, 2, 3], 3, 3),
        ([3, 4, -2, -1, 2], 4, 1),
        ([3, 4, -2, -1, 2], -1, 3),
        ([1, 2, 3, 4, 5, 6, 7, -1, 0], 2, 1),
        ([1, 2, 3, 4, 5, 6, 7, -1, 0], 5, 4),
        ([1, 2, 3, 4, 5, 6, 7, -1, 0], 7, 6),
        ([1, 2, 3, 4, 5, 6, 7, -1, 0], -1, 7),
        ([2, 3, 4, 5, 6, 7, -1, 0, 1], 0, 7),
        ([1, 2, 3, 4, 5, 6, 7, -2, -1, 0], 5, 4),
        ([1, 2, 3, 4, 5, 6, 7, -3, -2, -1, 0], 5, 4),
        ([1, 2, 3, 4, 5, 6, 7, -3, -2, -1, 0], 6, 5),
        ([1, 2, 3, 4, 5, 6, 7, -3, -2, -1, 0], 7, 6),
        ([1, 2, 3, 4, 5, 6, 7, -3, -2, -1, 0], -3, 7),
        ([1, 2, 3, 4, 5, 6, 7, -3, -2, -1, 0], -2, 8),
        ([1, 2, 3, 4, 5, 6, -4, -3, -2, -1, 0], -1, 9),
        ([2, 3, 4, 5, 6, 7, 8, 9, -5, -4, -3, -2, -1], 3, 1),
        ([2, 3, 4, 5, 6, 7, 8, 9, -5, -4, -3, -2, -1], 4, 2),
        ([2, 3, 4, 5, 6, 7, 8, 9, -5, -4, -3, -2, -1], 5, 3),
        ([2, 3, 4, 5, 6, 7, 8, 9, -5, -4, -3, -2, -1], 6, 4),
        ([2, 3, 4, 5, 6, 7, 8, 9, -5, -4, -3, -2, -1], 7, 5),
        ([2, 3, 4, 5, 6, 7, 8, 9, -5, -4, -3, -2, -1], 8, 6),
        ([2, 3, 4, 5, 6, 7, 8, 9, -5, -4, -3, -2, -1], 9, 7),
        ([2, 3, 4, 5, 6, 7, 8, 9, -5, -4, -3, -2, -1], -5, 8),
        ([2, 3, 4, 5, 6, 7, 8, 9, -5, -4, -3, -2, -1], -4, 9),
        ([2, 3, 4, 5, 6, 7, 8, 9, -5, -4, -3, -2, -1], -3, 10),
        ([2, 3, 4, 5, 6, 7, 8, 9, -5, -4, -3, -2, -1], -2, 11),
        ([2, 3, 4, 5, 6, 7, 8, 9, -5, -4, -3, -2, -1], -1, 12),
        ([2, 3, 4, 5, 6, 7, 8, 9, -5, -4, -3, -2, -1], 88, None),
    ]

    for nums, target, solution in test_cases:

        result = recursion(nums, target)
        string = f"recursion{nums, target} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        result = iterative(nums, target)
        string = f"iterative{nums, target} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')

        print()
