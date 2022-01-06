"""
https://leetcode.com/problems/3sum/
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

"""
from typing import List
from copy import deepcopy


def brute_force(nums: List[int]) -> List[List[int]]:
    # Time complexity: O(n³)
    # Space complexity: O(n)
    pass


def three_pointers(nums: List[int]) -> List[List[int]]:
    # Time complexity: O(n³)
    # Space complexity: O(n)
    n = len(nums)
    if n < 2:
        return []

    triplets = []

    # Sort the numbers to enable a more
    # efficient algorithm
    # (time complexity O(nlogn))
    nums.sort()

    # Auxiliary variables
    ref = 0
    prev_num = None

    # Loop through the negative numbers
    while ref < n - 2 and nums[ref] <= 0:

        # If the reference number is equal to the previous,
        # skip the iteration to avoid duplicate triplets
        if nums[ref] == prev_num:
            ref += 1
            continue

        # Look for the two remaining numbers
        # using two pointers
        left, right = ref + 1, n - 1
        while left < right:
            suma = nums[ref] + nums[left] + nums[right]
            if suma > 0:
                right -= 1
            elif suma < 0:
                left += 1
            else:
                triplets.append([nums[ref], nums[left], nums[right]])
                left += 1
                # Avoid repeated numbers
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

        # print('Update', left, right)
        # Update variables for next iter
        prev_num = nums[ref]
        ref += 1

    return triplets


def three_pointers2(nums: List[int]) -> List[List[int]]:
    # Time complexity: O(n²)
    # Space complexity: O(n)
    # Less efficient version using a hashset to store the triplets

    n = len(nums)
    if n < 3:
        return []

    # Sort the array to be able to use pointers to scan the array
    # to reduce the time complexity
    nums.sort()

    # Result in a set to avoid duplicates (much less efficient!)
    triplets = set()

    # Use three pointers
    left = 0

    # Loop over the negative numbers
    while left < n - 2 and nums[left] <= 0:
        target = -nums[left]
        mid, right = left + 1, n - 1
        while mid < right:
            curr = nums[mid] + nums[right]
            if curr == target:
                triplets.add((nums[left], nums[mid], nums[right]))
                mid += 1
                right -= 1
            elif curr < target:
                mid += 1
            else:
                right -= 1

        left += 1

    return list([list(t) for t in triplets])


if __name__ == "__main__":
    print("-" * 60)
    print("Three sum")
    print("-" * 60)

    test_cases = [
        ([], []),
        ([0], []),
        ([-1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([-3, 3, 4, -3, 1, 2], [[-3, 1, 2]]),
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        (
            [-5, 2, 4, 1, -2, 5, 0, 8, 3, -1],
            [[-5, 0, 5], [-5, 1, 4], [-5, 2, 3], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]],
        ),
        (
            [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4],
            [
                [-4, 0, 4],
                [-4, 1, 3],
                [-3, -1, 4],
                [-3, 0, 3],
                [-3, 1, 2],
                [-2, -1, 3],
                [-2, 0, 2],
                [-1, -1, 2],
                [-1, 0, 1],
            ],
        ),
    ]

    for nums, solution in test_cases:

        print(f"Array: {nums}")

        result = three_pointers(deepcopy(nums))
        output = f"  three_pointers = "
        test_ok = sorted(result) == sorted(solution)
        str_res = str(result)
        if len(str_res) > 35:
            str_res = str_res[:30] + " ...]]"
        output += str_res
        output += " " * (50 - len(output))
        output += f'\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = three_pointers2(deepcopy(nums))
        output = f" three_pointers2 = "
        test_ok = sorted(result) == sorted(solution)
        str_res = str(result)
        if len(str_res) > 35:
            str_res = str_res[:30] + " ...]]"
        output += str_res
        output += " " * (50 - len(output))
        output += f'\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
