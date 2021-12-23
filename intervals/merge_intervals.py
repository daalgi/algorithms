"""
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the 
non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
"""
from typing import List
from copy import deepcopy
import heapq


def sorting(intervals: List[List[int]]) -> List[List[int]]:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    # Sort intervals by starting time
    intervals.sort()

    res = [intervals[0]]
    n = len(intervals)
    # Loop over the intervals
    for i in range(1, n):
        if res[-1][1] >= intervals[i][0]:
            # If the current interval start (intervals[i][0])
            # is later than the previous interval end (res[-1][1]),
            # the previous interval overlaps the current one,
            # so update its ending time to contain the current interval.
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            # If the current interval doesn't overlap with the previous one,
            # add it to the resulting list of intervals
            res.append(intervals[i])

    return res


def heap(intervals: List[List[int]]) -> List[List[int]]:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    # Convert the list into a heap
    heap = intervals
    heapq.heapify(heap)

    res = [heapq.heappop(heap)]
    n = len(intervals)
    # Loop over the intervals
    while heap:
        interval = heapq.heappop(heap)
        if res[-1][1] >= interval[0]:
            res[-1][1] = max(res[-1][1], interval[1])
        else:
            res.append(interval)

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Merge intervals")
    print("-" * 60)

    test_cases = [
        ([[1, 2]], [[1, 2]]),
        ([[1, 2], [2, 3]], [[1, 3]]),
        ([[1, 2], [1, 5]], [[1, 5]]),
        ([[1, 2], [3, 5], [2, 5], [1, 5]], [[1, 5]]),
        ([[1, 2], [3, 5], [7, 8], [2, 5], [5, 6]], [[1, 6], [7, 8]]),
        ([[1, 2], [1, 2], [5, 8], [9, 13]], [[1, 2], [5, 8], [9, 13]]),
        ([[1, 2], [2, 9], [3, 4], [0, 1]], [[0, 9]]),
    ]

    for intervals, solution in test_cases:

        output = f"Intervals: {intervals}"
        print(output)

        result = sorting(deepcopy(intervals))
        output = f"\t   sorting = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = heap(deepcopy(intervals))
        output = f"\t      heap = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)
        print()
