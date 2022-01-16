"""
https://leetcode.com/problems/4sum/

Given an array nums of n integers, return an array of all the unique 
quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
- 0 <= a, b, c, d < n
- a, b, c, and d are distinct.
- nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]

Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

Follow-up:
5Sum, 6Sum, ..., kSum.
"""
from typing import List


def recursion(nums: List[int], target: int) -> List[List[int]]:
    # Time complexity: O(n^(k-1))
    # Space complexity: O(n)

    def two_sum(curr_elements: List[int], left: int, right: int, target: int):
        # Two pointer solution to the two-sum problem
        # of a sorted array
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum == target:
                # If reached the `target`, add the quadruplet
                res.append(curr_elements + [nums[left], nums[right]])
                left += 1

                # Skip duplicate values
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

            elif curr_sum < target:
                # If the current sum is less than the target,
                # we need to increase it, and we can only do it
                # by moving the left pointer forward
                left += 1
            else:
                # If the current sum is more than the target,
                # we need to decrease it, and we can only do it
                # by moving the right pointer backward
                right -= 1

    def ksum(start: int, end: int, curr_elements: List[int], k: int, target: int):
        # Recursive function to reduce from `k-sum` to `2-sum`

        # Early stop cases:
        if k < 2:
            return
        average_value = target // k
        if (
            end - start + 1 < k
            or average_value < nums[start]
            or nums[end] < average_value
        ):
            # If there're not enough elements to the right,
            # or the elements to the right can't add up to the
            # current `target` (because we sorted `nums`)
            return

        if k == 2:
            # When `k` has been reduced to `2`,
            # solve the two-sum subproblem
            two_sum(curr_elements=curr_elements, left=start, right=end, target=target)

        while start < n - 1:
            ksum(
                start=start + 1,
                end=end,
                curr_elements=curr_elements + [nums[start]],
                k=k - 1,
                target=target - nums[start],
            )
            start += 1
            # Skip duplicates
            while start < n - 1 and nums[start - 1] == nums[start]:
                start += 1

    n = len(nums)
    # Sort the list to be able to use the two-pointer approach
    nums.sort()
    res = []
    ksum(start=0, end=n - 1, curr_elements=[], k=4, target=target)
    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Four sum (k-sum-ready algorithm)")
    print("-" * 60)

    test_cases = [
        ([], 8, []),
        ([0], 8, []),
        ([0, 1, 2, 3], 8, []),
        ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
        ([1, -2, -5, -4, -3, 3, 3, 5], -11, [[-5, -4, -3, 1]]),
        ([2, 2, 2, 2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
        ([6, 7, 8, 3, 0, 2, 1] + list(range(5, 10)), 6, [[0, 1, 2, 3]]),
        ([6, 7, 8, 3, 0, 2, 1] + list(range(5, 20)), 6, [[0, 1, 2, 3]]),
        ([6, 7, 8, 3, 0, 2, 1] + list(range(5, 5000)), 6, [[0, 1, 2, 3]]),
    ]

    for nums, target, solution in test_cases:

        arr_string = str(nums)
        if len(arr_string) > 60:
            arr_string = arr_string[:55] + " ...]"
        print("Array:", arr_string)
        print("Target:", target)

        res = recursion([*nums], target)
        output = "    recursion = "
        output += str(res)
        output += " " * (70 - len(output))
        output += f'\tTest: {"OK" if res == solution else "NOT OK"}'
        print(output)

        print()
