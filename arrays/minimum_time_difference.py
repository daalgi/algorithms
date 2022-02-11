"""
https://leetcode.com/problems/minimum-time-difference/

Given a list of 24-hour clock time points in "HH:MM" 
format, return the minimum minutes difference between 
any two time-points in the list.

Example 1:
Input: timePoints = ["23:59","00:00"]
Output: 1

Example 2:
Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

Constraints:
2 <= timePoints.length <= 2 * 10^4
timePoints[i] is in the format "HH:MM".
"""
from typing import List
from copy import deepcopy


def sorting(time_points: List[str]) -> int:
    # Time complexity: O(nlogn)
    # Space complexity: O(n)

    # Convert the times into minutes (integers): hour * 60 + minutes
    # Then sort them in ascending order
    time_points = sorted(int(s[:2]) * 60 + int(s[3:]) for s in time_points)

    # Check the time difference between the last and the first times
    # (23:59 - 00:00 = 1 minute)
    min_diff = abs(time_points[-1] - 1440 - time_points[0])

    # Loop over the sorted list of times comparing `i` with `i-1`
    # and checking if the difference is smaller than the previously
    # smallest difference
    n = len(time_points)
    for i in range(1, n):
        diff = time_points[i] - time_points[i - 1]
        if diff < min_diff:
            min_diff = diff

    return min_diff


if __name__ == "__main__":
    print("-" * 60)
    print("Minimum time difference")
    print("-" * 60)

    test_cases = [
        # (time_points, solution)
        (["00:01", "00:09"], 8),
        (["00:00", "23:59"], 1),
        (["00:00", "23:59", "00:00"], 0),
        (["10:00", "23:59", "09:10"], 50),
    ]

    for time_points, solution in test_cases:

        print("Time points:", time_points)

        result = sorting(deepcopy(time_points))
        output = f"     sorting = "
        output += str(result)
        test_ok = solution == result
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
