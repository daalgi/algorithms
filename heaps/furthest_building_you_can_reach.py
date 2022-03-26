"""
https://leetcode.com/problems/furthest-building-you-can-reach/

You are given an integer array heights representing the 
heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the 
next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),
- If the current building's height is greater than or equal 
to the next building's height, you do not need a ladder or bricks.
- If the current building's height is less than the next 
building's height, you can either use one ladder or 
(h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can 
reach if you use the given ladders and bricks optimally.

Example 1:
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or 
ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either 
bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have 
any more bricks or ladders.

Example 2:
Input: heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
Output: 7

Example 3:
Input: heights = [14,3,19,3], bricks = 17, ladders = 0
Output: 3

Constraints:
1 <= heights.length <= 10^5
1 <= heights[i] <= 10^6
0 <= bricks <= 10^9
0 <= ladders <= heights.length
"""
from functools import lru_cache
from typing import List
import heapq


def dp_recursion(heights: List[int], bricks: int, ladders: int) -> int:
    # Time complexity: O(n²)
    # Space complexity: O(n)
    # Leetcode: memory limit exceeded

    @lru_cache(maxsize=None)
    def dfs(i: int, bricks: int, ladders: int) -> int:
        # Base case: reached the end
        if i == n - 1 and bricks >= 0 and ladders >= 0:
            return i

        # Base case: not enough `bricks` or `ladders`,
        # couldn't reach the current building `i`
        if bricks < 0 or ladders < 0:
            return i - 1

        # Check the next height difference
        diff = heights[i + 1] - heights[i]

        # If the next building is smaller or equally higher,
        # just jump
        if diff <= 0:
            return dfs(i + 1, bricks, ladders)

        # If the next building is taller,
        # explore the possible paths
        return max(
            # Option 1: use bricks
            dfs(i + 1, bricks - diff, ladders),
            # Option 2: use a ladder
            dfs(i + 1, bricks, ladders - 1),
        )

    n = len(heights)
    return dfs(0, bricks, ladders)


def heapmin(heights: List[int], bricks: int, ladders: int) -> int:
    # Time complexity: O(nlogk)
    # Space complexity: O(n)
    # We want to use the ladders for the largest height differences,
    # and if there're not enough, use bricks.

    # min-heap to track the current minimum difference.
    heap = []
    n = len(heights)
    for i in range(n - 1):
        # Current height difference
        diff = heights[i + 1] - heights[i]

        if diff > 0:
            # If positive, add the height difference
            # to the heap
            heapq.heappush(heap, diff)
            if ladders < len(heap):
                # If there're not enough ladders to jump
                # into the higher buildings, use bricks
                # for the current smallest one
                bricks -= heapq.heappop(heap)
                if bricks < 0:
                    # If there're not enough bricks,
                    # we can't go any further
                    return i

    # Reached the last building
    return n - 1


if __name__ == "__main__":
    print("-" * 60)
    print("Furthest building you can reach")
    print("-" * 60)

    test_cases = [
        # (heights, bricks, ladders, solution)
        ([4, 2, 7, 6, 9, 14, 12], 5, 1, 4),
        ([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2, 7),
        ([14, 3, 19, 3], 17, 0, 3),
        (
            [40, 200, 70, 69, 99, 114, 112, 102, 40, 210, 32, 4, 45, 6, 5, 34, 43],
            50,
            3,
            14,
        ),
    ]

    for heights, bricks, ladders, solution in test_cases:

        print("Heights:", heights)
        print("Bricks:", bricks)
        print("Ladders:", ladders)

        result = dp_recursion(heights, bricks, ladders)
        output = f"      dp_recursion = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = heapmin(heights, bricks, ladders)
        output = f"           heapmin = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = solution == result
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
