"""
CRACKING THE CODING INTERVIEW
10.3 Search in rotated array.
*Actual CTCI and LeetCode equivalents 
(although LeetCode question is about existance rather than returning the index)

https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

There is an integer array nums sorted in non-decreasing order 
(not necessarily with distinct values).

Before being passed to your function, nums is rotated at an 
unknown pivot index k (0 <= k < nums.length) such that the resulting 
array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] 
(0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 
and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if 
target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
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
        if nums[left] < nums[mid]:
            # Left side is ordered normally
            # Note that we can't use "<=" here to include the cases
            # of two element arrays, where left = mid
            if nums[left] <= target < nums[mid]:
                # Target in the left side --> search left side
                return f(nums, left, mid - 1, target)
            else:
                # Target in the right side --> search right side
                return f(nums, mid + 1, right, target)

        elif nums[left] > nums[mid]:
            # Right side is ordered normally
            if nums[mid] < target <= nums[right]:
                # Target in the right side --> search right side
                return f(nums, mid + 1, right, target)
            else:
                # Target in the left side --> search left side
                return f(nums, left, mid - 1, target)

        elif nums[left] == nums[mid]:
            # There are repeated numbers in the whole left or right side
            if nums[mid] != nums[right]:
                # If right is different, search it
                return f(nums, mid + 1, right, target)
            else:
                # Else, we have to search both halves

                # Left half
                result = f(nums, left, mid - 1, target)
                if result is None:
                    # If not found in the left half, search the right half
                    return f(nums, mid + 1, right, target)
                # If found in the left half, return the result
                return result

    return f(nums, 0, len(nums) - 1, target)


if __name__ == "__main__":
    print("-" * 60)
    print("Search in rotated sorted array II")
    print("-" * 60)

    test_cases = [
        ([1], 1, 0),
        ([1], 5, None),
        ([1, 1], 1, 0),
        ([1, 1, 1], 1, 1),  # returns the first `mid`
        ([1, 1, 1, 1], 1, 1),
        ([1, 1, 1, 1, 1], 1, 2),
        ([1, 1, 1, 2, 3], 2, 3),
        ([5, 2, 3, 3, 3, 4], 5, 0),
        ([5, 2, 3, 3, 3, 4], 2, 1),
        ([5, 2, 3, 3, 3, 4], 4, 5),
        ([4, 5, 6, 1, 1, 1, 2, 3], 4, 0),
        ([4, 5, 6, 1, 1, 1, 2, 3], 5, 1),
        ([4, 5, 6, 1, 1, 1, 2, 3], 6, 2),
        ([4, 5, 6, 1, 1, 1, 2, 3], 1, 3),
        ([4, 5, 6, 1, 1, 1, 2, 3], 2, 6),
        ([4, 5, 6, 1, 1, 1, 2, 3], 3, 7),
        ([2, 5, 6, 0, 0, 1, 2], 0, 3),
        ([3, 1, 1], 3, 0),
        ([1, 0, 1, 1, 1], 1, 2),
        ([1, 0, 1, 1, 1], 0, 1),
        ([1, 3, 4, 5, 6, 0, 1, 1, 1], 0, 5),
        ([1, 3, 4, 5, 6, 0, 1, 1, 1], 1, 0),
        ([1, 3, 4, 5, 6, 0, 1, 1, 1], 2, None),
        ([1, 3, 4, 5, 6, 0, 1, 1, 1], 3, 1),
        ([1, 3, 4, 5, 6, 0, 1, 1, 1], 4, 2),
        ([1, 3, 4, 5, 6, 0, 1, 1, 1], 5, 3),
        ([1, 3, 4, 5, 6, 0, 1, 1, 1], 6, 4),
    ]

    for nums, target, solution in test_cases:

        result = recursion(nums, target)
        string = f"recursion{nums, target} = "
        string += " " * (35 - len(string))
        string += str(result)
        string += " " * (60 - len(string))
        print(string, f'\t\tTest: {"OK" if solution == result else "NOT OK"}')
