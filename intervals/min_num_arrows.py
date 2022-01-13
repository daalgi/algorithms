"""
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

There are some spherical balloons taped onto a flat wall that 
represents the XY-plane. The balloons are represented as 
a 2D integer array points where points[i] = [xstart, xend] 
denotes a balloon whose horizontal diameter stretches between 
xstart and xend. You do not know the exact y-coordinates 
of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) 
from different points along the x-axis. A balloon with xstart 
and xend is burst by an arrow shot at x if xstart <= x <= xend. 
There is no limit to the number of arrows that can be shot. A shot 
arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows 
that must be shot to burst all balloons.

Example 1:
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].

Example 2:
Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon 
for a total of 4 arrows.

Example 3:
Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

Constraints:
1 <= points.length <= 10^5
points[i].length == 2
-2^31 <= xstart < xend <= 2^31 - 1
"""
from typing import List
from copy import deepcopy


def greedy(points: List[List[int]]) -> int:
    # Time complexity: O(nlogn)
    # Space complexity: O(logn)

    # Sort the points by the `x_end` coordinate
    # O(nlogn)
    points.sort(key=lambda p: p[1])

    # Minimum number of needed `arrows`.
    # Initialize it to one, so the first interval is already
    # accounted for
    num_arrows = 1
    # Use two pointers to compare intervals.
    # If the current intervals being compared reference interval `left` and
    # the current `right` are overlapping,
    # we can continue comparing the next interval `right + 1`.
    left, right = 0, 1
    # Loop over the intervals until any pointer reaches the end
    n = len(points)
    while left < n and right < n:
        if points[left][1] < points[right][0]:
            # If the current intervals are not overlapping,
            # we need one more arrow.
            num_arrows += 1
            # Update the pointers to check next intervals
            left, right = right, right + 1
        else:
            # If the current intervals are overlapping,
            # the current reference (`left` pointer) stays
            # the same, and continue to compare it with the
            # next one `right + 1`
            right += 1

    return num_arrows


def greedy2(points: List[List[int]]) -> int:
    # Time complexity: O(nlogn)
    # Space complexity: O(logn)
    points.sort(key=lambda p: p[1])
    num_arrows, end = 0, float("-inf")
    for point in points:
        if end < point[0]:
            num_arrows += 1
            end = point[1]
    return num_arrows


if __name__ == "__main__":
    print("-" * 60)
    print("Minimum number of arrows to burst balloons")
    print("-" * 60)

    test_cases = [
        ([[1, 2]], 1),
        ([[1, 2], [2, 3]], 1),
        ([[1, 2], [1, 5], [1, 5]], 1),
        ([[1, 2], [3, 5], [2, 5], [1, 5]], 2),
        ([[1, 2], [3, 5], [7, 8], [2, 5], [6, 7]], 3),
        ([[1, 2], [2, 4], [5, 8], [9, 13]], 3),
        ([[1, 2], [2, 9], [3, 4], [0, 1]], 2),
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
    ]

    for points, solution in test_cases:

        output = f"Points: {points}"
        if len(output) > 60:
            output = output[:60] + " ...]]"
        print(output)

        result = greedy(deepcopy(points))
        output = f"   greedy = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = greedy2(deepcopy(points))
        output = f"  greedy2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
