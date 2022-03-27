"""
https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

You are given an integer array nums. In one move, you 
can choose one element of nums and change it by any value.

Return the minimum difference between the largest 
and smallest value of nums after performing at most 
three moves.

Example 1:
Input: nums = [5,3,2,4]
Output: 0
Explanation: Change the array [5,3,2,4] to [2,2,2,2].
The difference between the maximum and minimum is 2-2 = 0.

Example 2:
Input: nums = [1,5,0,10,14]
Output: 1
Explanation: Change the array [1,5,0,10,14] to [1,1,0,1,1]. 
The difference between the maximum and minimum is 1-0 = 1.

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List
from copy import deepcopy
import heapq


def sorting(nums: List[int]) -> int:
    # Time complexity: O(nlogn)
    # Space complexity: O(logn)
    # Strategy: sort the list and explore which removals
    # will produce the smallest `max - min`

    def dfs(left: int, right: int, moves: int) -> int:
        # Depth First Search - Recursive

        # Base case
        if moves == 0:
            # No moves left, so return max - min
            return nums[right] - nums[left]

        # Explore the most favourable next move
        moves -= 1
        return min(
            # Option 1: remove the number at `left`
            dfs(left + 1, right, moves),
            # Option 2: remove the number at `right`
            dfs(left, right - 1, moves),
        )

    n = len(nums)
    # If the length of the list is 4 or less,
    # we can always achieve a min difference of 0
    if n < 5:
        return 0

    # Sort the list
    nums.sort()
    moves = 3
    # Use two pointers to indicate the first and last
    # non-discarded elements in the list
    left, right = 0, n - 1
    return dfs(left, right, moves)


def sorting2(nums: List[int]) -> int:
    # Time complexity: O(nlogn)
    # Space complexity: O(logn)
    n = len(nums)
    if n < 5:
        return 0

    nums.sort()
    # After "removing" 3 elements, we can find
    # the minimum difference `max - min` by comparing
    # the elements at indices:
    #   0 and n - 3
    #   1 and n - 2
    #   2 and n - 1
    # i.e., given the list:
    #   0 10 20 30 ... 100 1000 2000 2001
    # the comparisons to be made:
    #   100 - 0   =  100 --> minimum
    #   1000 - 10 =  990
    #   2000 - 20 = 1980
    #   2001 - 30 = 1971
    moves = 3
    return min(
        right - left for left, right in zip(nums[: moves + 1], nums[-moves - 1 :])
    )


def heaps(nums: List[int]) -> int:
    # Time complexity: O(nlogk)
    # Space complexity: O(logk)
    # where `k` is the number of moves
    # Strategy: partially sort `nums` by means of heaps
    # to improve the time complexity.
    # `heapq.nsmallest` returns the `k` smallest numbers in a list in O(nlogk)
    # `heapq.nlargest` returns the `k` largest numbers in a list in O(nlogk)
    """
    Example:
       k        1   5   6  13  14  15  16  17
       0        17 - 1 = 16
       1    min(17 - 5, 16 - 1) = 12
       2    min(17 - 6, 16 - 5, 15 - 1) = 11
       3    min(17 - 13, 16 - 6, 15 - 5, 14 - 1) = 4

    Equivalent to minimize the maximum amplitude (difference)
    after removing `k` elements in the list.
    """
    n = len(nums)
    if n < 5:
        return 0

    return min(
        right - left
        for left, right in zip(
            # 4 smallest numbers in increasing order
            # (heap-min reversed)
            heapq.nsmallest(4, nums)[::-1],
            # 4 largest numbers in increasing order
            # (heap-max)
            heapq.nlargest(4, nums),
        )
    )


if __name__ == "__main__":
    print("-" * 60)
    print("Minimum difference between largest and smallest value in three moves")
    print("-" * 60)

    test_cases = [
        ([0, 8], 0),
        ([0, 8, 9, 10], 0),
        ([0, 8, 9, 10], 0),
        ([0, 1, 8, 9, 10], 1),
        ([0, 1, 9, 18, 19, 20], 2),
        ([1, 5, 6, 13, 14, 15, 16, 17], 4),
        ([0, 10, 20] + list(range(100, 1000)) + [8000, 9000, 9001, 9002], 8000),
        ([0, 10, 20] + list(range(100, 1000)) + [9000, 9000, 9001, 9002], 8902),
    ]

    for nums, solution in test_cases:

        nums_str = str(nums)
        if len(nums_str) > 60:
            nums_str = nums_str[:55] + " ...]"
        print("nums:", nums_str)

        result = sorting(deepcopy(nums))
        output = f"      sorting = "
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sorting2(deepcopy(nums))
        output = f"     sorting2 = "
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = heaps(deepcopy(nums))
        output = f"        heaps = "
        output += str(result)
        test_ok = solution == result
        output += " " * (50 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
