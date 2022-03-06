"""
https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/

You are given a 2D integer array ranges and two 
integers left and right. Each 
ranges[i] = [starti, endi] represents an inclusive 
interval between starti and endi.

Return true if each integer in the inclusive 
range [left, right] is covered by at least one 
interval in ranges. Return false otherwise.

An integer x is covered by an interval 
ranges[i] = [starti, endi] if starti <= x <= endi.

Example 1:
Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
Output: true
Explanation: Every integer between 2 and 5 is covered:
- 2 is covered by the first range.
- 3 and 4 are covered by the second range.
- 5 is covered by the third range.

Example 2:
Input: ranges = [[1,10],[10,20]], left = 21, right = 21
Output: false
Explanation: 21 is not covered by any range.

Constraints:
1 <= ranges.length <= 50
1 <= starti <= endi <= 50
1 <= left <= right <= 50
"""
from typing import List


def brute_force(ranges: List[List[int]], left: int, right: int) -> bool:
    # Time complexity: O(nm)
    # Space complexity: O(1)

    for i in range(left, right + 1):
        if not any(start <= i <= end for start, end in ranges):
            return False
    return True


def brute_force2(ranges: List[List[int]], left: int, right: int) -> bool:
    # Time complexity: O(nm)
    # Space complexity: O(1)
    return all(
        any(start <= i <= end for start, end in ranges) for i in range(left, right + 1)
    )


def constant_range_updates(ranges: List[List[int]], left: int, right: int) -> bool:
    # Time complexity: O(m+n)
    # Space complexity: O(n)
    # where `m` is the length of `ranges`
    # and `n` is `right - left`
    max_size = 52
    seen = [0] * max_size
    for start, end in ranges:
        seen[start] += 1
        seen[end + 1] -= 1

    for i in range(1, max_size):
        seen[i] += seen[i - 1]

    for i in range(left, right + 1):
        if not seen[i]:
            return False

    return True


if __name__ == "__main__":
    print("-" * 60)
    print("Check if all the integers in a range are covered")
    print("-" * 60)

    test_cases = [
        # (ranges, left, right, solution)
        ([[1, 2], [3, 4], [5, 6]], 2, 5, True),
        ([[1, 2], [3, 4], [5, 6], [8, 20]], 2, 7, False),
        ([[1, 2], [3, 4], [5, 6], [8, 20]], 7, 21, False),
        ([[1, 2], [3, 4], [5, 6], [8, 20]], 8, 20, True),
        ([[1, 10], [10, 20]], 21, 21, False),
    ]

    for i, (ranges, left, right, solution) in enumerate(test_cases):

        if not i or ranges != test_cases[i - 1][0]:
            print("Ranges:", ranges)
        print(f"Integers between {left} and {right}")

        result = brute_force(ranges, left, right)
        output = "              brute_force = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = brute_force2(ranges, left, right)
        output = "             brute_force2 = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = constant_range_updates(ranges, left, right)
        output = "   constant_range_updates = "
        output += str(result)
        output += " " * (50 - len(output))
        test_ok = result == solution
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
