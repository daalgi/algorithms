"""
https://leetcode.com/problems/teemo-attacking/

Our hero Teemo is attacking an enemy Ashe with 
poison attacks! When Teemo attacks Ashe, Ashe gets 
poisoned for a exactly duration seconds. More 
formally, an attack at second t will mean Ashe is 
poisoned during the inclusive time interval 
[t, t + duration - 1]. If Teemo attacks again before 
the poison effect ends, the timer for it is reset, 
and the poison effect will end duration seconds 
after the new attack.

You are given a non-decreasing integer array timeSeries, 
where timeSeries[i] denotes that Teemo attacks Ashe at 
second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.

Example 1:
Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.

Example 2:
Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer. 
Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.
 

Constraints:
1 <= timeSeries.length <= 10^4
0 <= timeSeries[i], duration <= 10^7
timeSeries is sorted in non-decreasing order.
"""
from time import time
from typing import List


def one_scan(time_series: List[int], duration: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    total = 0
    prev = curr = -1
    for t in time_series:
        if t >= prev:
            total += duration
            if curr >= t:
                total -= curr - t + 1
            curr = t + duration - 1
            prev = t
    return total


def one_scan2(time_series: List[int], duration: int) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)

    if duration == 0:
        return 0

    n, total = len(time_series), 0
    for i in range(n - 1):
        total += min(time_series[i + 1] - time_series[i], duration)

    return total + duration


if __name__ == "__main__":
    print("-" * 60)
    print("Can place flowers")
    print("-" * 60)

    test_cases = [
        # (time_series, duration, solution)
        ([1], 2, 2),
        ([1, 4], 2, 4),
        ([1, 1, 2], 2, 3),
        ([0, 0, 2, 2, 2, 2, 2, 3, 15, 17, 19], 4, 15),
    ]

    for time_series, duration, solution in test_cases:

        print("Time series:", time_series)
        print("Duration:", duration)

        result = one_scan(time_series, duration)
        output = f"     one_scan = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = one_scan2(time_series, duration)
        output = f"    one_scan2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
