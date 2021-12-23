"""
https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the 
rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals 
are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the 
intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since 
they're already non-overlapping.
 
Constraints:
1 <= intervals.length <= 10^5
intervals[i].length == 2
-5 * 10^4 <= starti < endi <= 5 * 10^4
"""
from typing import List
from copy import deepcopy


def greedy(intervals: List[List[int]]) -> int:
    """
    GREEDY ALGORITHMS: repeatedly makes locally best choici/decision,
    ignoring effect on future.

    Greedy properties:
    1 - Optimal substructure:
    Optimal solution to problem incorporates optimal solution
    to subproblems.
    2 - Greedy choice property:
    Locally optimal choices lead to globally optimal solution.
    * every choice is a "sub-problem"

    INTERVAL SCHEDULING PROBLEM (greedy problem)
    Max number of non-overlapping intervals:
    at every step, pick the earliest ending time.
    Max number of non-overlapping intervals == min number of removals
    """
    # Time complexity: O(n)
    # Space complexity: O(1)

    # Sort intervals by ending time
    intervals.sort(key=lambda i: i[1])

    n = len(intervals)
    erased, time = 0, float("-inf")
    for interval in intervals:
        if interval[0] >= time:
            time = interval[1]
        else:
            erased += 1

    return erased


if __name__ == "__main__":
    print("-" * 60)
    print("Non-overlapping intervals")
    print("-" * 60)

    test_cases = [
        ([[1, 2]], 0),
        ([[1, 2], [2, 3]], 0),
        ([[1, 2], [2, 5], [3, 5]], 1),
        ([[1, 2], [3, 5], [2, 5], [1, 5]], 2),
        ([[1, 2], [3, 5], [5, 8], [2, 5], [5, 6]], 2),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
    ]

    for intervals, solution in test_cases:

        output = f"Intervals: {intervals}"
        print(output)

        result = greedy(deepcopy(intervals))
        output = f"\t   greedy = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
