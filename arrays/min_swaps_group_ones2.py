"""
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/

A swap is defined as taking two distinct positions in an array 
and swapping the values in them.

A circular array is defined as an array where we consider 
the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number 
of swaps required to group all 1's present in the array 
together at any location.

Example 1:
Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.

Example 2:
Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.

Example 3:
Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to 
the circular property of the array.
Thus, the minimum number of swaps required is 0.

Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""
from typing import List
from copy import deepcopy


def sliding_window(nums: List[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    """
    Stragety: sliding window
        0 1 2 3 4 5 6 7 8 (indices)
        0 1 1 1 0 0 1 1 0 (nums --> ones = 5)
        0 1 1 1 0 0 1 1 0 0 1 1 1 0 0 1 1 0 (nums + nums)
        0 1 1 1 0                 --> zeros = 2
          1 1 1 0 0               --> zeros = 2
            1 1 0 0 1             --> zeros = 2
              1 0 0 1 1           --> zeros = 2
                0 0 1 1 0         --> zeros = 3
                  0 1 1 0 0       --> zeros = 3
                    1 1 0 0 1     --> zeros = 2
                      1 0 0 1 1   --> zeros = 2
                        0 0 1 1 1 --> zeros = 2

    """
    # Number of ones in the list, which will define
    # the width of the window
    ones = sum(nums)
    # Number of zeros in the first window (from 0 to `ones`)
    zeros = ones - sum(nums[:ones])
    # Keep track of the min number of zeros
    min_zeros = zeros
    # Loop over the list
    # (concatenated with itself to account for the
    # "circular array" property)
    two_n = 2 * len(nums)
    nums += nums
    for i in range(ones, two_n):

        if nums[i] == nums[i - ones]:
            # The new number is equal to the number that was
            # just popped out of the sliding window, so there's
            # no change in the current number of zeros
            continue

        # If the new number and the last popped out are different
        if nums[i] == 0:
            # The new number is a 0,
            # then the popped number was a 1,
            # so the number of zeros increases
            zeros += 1
        else:
            # The new number is a 1,
            # then the popped number was a 0,
            # so the number of zeros decreases
            zeros -= 1

        # If the current number of zeros is less than
        # the minimum registered so far, update it
        if zeros < min_zeros:
            min_zeros = zeros

    return min_zeros


if __name__ == "__main__":
    print("-" * 60)
    print("Minimum swaps to group all 1's together II")
    print("-" * 60)

    test_cases = [
        # (list, solution)
        ([0], 0),
        ([1], 0),
        ([0, 1, 1], 0),
        ([0, 1, 0, 1], 1),
        ([0, 1, 0, 0, 1], 1),
        ([1, 1, 0, 0, 1], 0),
        ([0, 1, 0, 1, 1, 0, 0], 1),
        ([0, 1, 1, 1, 0, 0, 1, 1, 0], 2),
    ]

    for nums, solution in test_cases:

        print("List:", nums)

        result = sliding_window(deepcopy(nums))
        output = f"   sliding_window = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
