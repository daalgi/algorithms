"""
https://leetcode.com/problems/insert-interval/

You are given an array of non-overlapping intervals intervals 
where intervals[i] = [starti, endi] represent the start and the 
end of the ith interval and intervals is sorted in ascending 
order by starti. You are also given an interval 
newInterval = [start, end] that represents the start and 
end of another interval.

Insert newInterval into intervals such that intervals is still 
sorted in ascending order by starti and intervals still does not 
have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
"""
from typing import List
import heapq
from copy import deepcopy


def sol1(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    # Time complexity: O(n)
    # Space complexity: O(n)

    # Special cases
    if intervals and intervals[0]:
        if new_interval[1] < intervals[0][0]:
            # `new_interval` before the first interval
            return [new_interval, *intervals]
        elif intervals[-1][1] < new_interval[0]:
            # `new_interval` after the last interval
            intervals.append(new_interval)
            return intervals
    else:
        # If no `intervals`, return `new_interval`
        return [new_interval]

    # Loop over the intervals
    res = list()
    for interval in intervals:

        if res and res[-1][1] < new_interval[0] and new_interval[1] < interval[0]:
            # `new_interval` between the last and the current intervals
            res.append(new_interval)

        if new_interval[1] < interval[0] or interval[1] < new_interval[0]:
            # `new_interval` not overlapping with `interval`
            res.append(interval)
        elif interval[0] <= new_interval[0] and new_interval[1] <= interval[1]:
            # `new_interval` completely inside `interval`
            res.append(interval)
        else:
            # `new_interval` overlapping `interval`
            if res and new_interval[0] <= res[-1][1]:
                # `new_interval` overlapping both last and current intervals
                res[-1][1] = max(new_interval[1], interval[1])
            else:
                # `new_interval` overlapping only the current interval
                res.append(
                    [
                        min(new_interval[0], interval[0]),
                        max(new_interval[1], interval[1]),
                    ]
                )

    return res


def sol2(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    # Time complexity: O(n)
    # Space complexity: O(n)

    res = list()
    n = len(intervals)

    # Special case, no intervals
    if n == 1 and not intervals[0]:
        return [new_interval]

    # Pointer to the current interval
    i = 0

    # Add all the interals ending before `new_interval` starts
    while i < n and intervals[i][1] < new_interval[0]:
        res.append(intervals[i])
        i += 1

    # Merge all overlapping intervals with `new_interval`
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval = [
            min(new_interval[0], intervals[i][0]),
            max(new_interval[1], intervals[i][1]),
        ]
        i += 1

    # Add the overlapping intervals
    res.append(new_interval)

    # Add the rest of intervals
    while i < n:
        res.append(intervals[i])
        i += 1

    return res


if __name__ == "__main__":
    print("-" * 60)
    print("Insert interval")
    print("-" * 60)

    test_cases = [
        ([[]], [3, 8], [[3, 8]]),
        ([[2, 3]], [0, 1], [[0, 1], [2, 3]]),
        ([[2, 3]], [0, 2], [[0, 3]]),
        ([[2, 3]], [0, 5], [[0, 5]]),
        ([[2, 3]], [4, 5], [[2, 3], [4, 5]]),
        ([[2, 3]], [4, 5], [[2, 3], [4, 5]]),
        ([[2, 3], [5, 8], [13, 25]], [0, 5], [[0, 8], [13, 25]]),
        ([[2, 3], [5, 8], [13, 25]], [0, 10], [[0, 10], [13, 25]]),
        ([[2, 3], [5, 8], [13, 25]], [0, 13], [[0, 25]]),
        ([[2, 3], [5, 8], [13, 25]], [4, 10], [[2, 3], [4, 10], [13, 25]]),
        ([[2, 3], [5, 8], [13, 25]], [9, 10], [[2, 3], [5, 8], [9, 10], [13, 25]]),
        ([[2, 3], [5, 8], [13, 25]], [30, 50], [[2, 3], [5, 8], [13, 25], [30, 50]]),
    ]

    for intervals, new_interval, solution in test_cases:

        output = f"Intervals: {intervals}"
        output += f"\nNew interval: {new_interval}"
        print(output)

        result = sol1(deepcopy(intervals), new_interval)
        output = f"\t   solution1 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = sol2(deepcopy(intervals), new_interval)
        output = f"\t   solution2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)
        print()
