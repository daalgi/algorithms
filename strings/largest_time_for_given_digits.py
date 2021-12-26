"""
https://leetcode.com/problems/largest-time-for-given-digits/

Given an array arr of 4 digits, find the latest 24-hour time that 
can be made using each digit exactly once.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, 
and MM is between 00 and 59. The earliest 24-hour time is 00:00, and 
the latest is 23:59.

Return the latest 24-hour time in "HH:MM" format. If no valid time 
can be made, return an empty string.

Example 1:
Input: arr = [1,2,3,4]
Output: "23:41"
Explanation: The valid 24-hour times are "12:34", "12:43", 
"13:24", "13:42", "14:23", "14:32", "21:34", "21:43", 
"23:14", and "23:41". Of these times, "23:41" is the latest.

Example 2:
Input: arr = [5,5,5,5]
Output: ""
Explanation: There are no valid 24-hour times as "55:55" is not valid.
 
Constraints:
arr.length == 4
0 <= arr[i] <= 9
"""
from typing import List
from collections import Counter
import itertools


def python_permutations(digits: List[int]) -> str:
    # Time complexity: O(1) (n! = 4! = 24)
    # Space complexity: O(1)

    max_time = -1

    for h1, h2, m1, m2 in itertools.permutations(digits):
        # Check if the hour is valid
        hh = h1 * 10 + h2
        if hh >= 24:
            continue

        # Check if the minute is valid
        mm = m1 * 10 + m2
        if mm >= 60:
            continue

        # Compare with the current max
        max_time = max(max_time, hh * 60 + mm)

    # If no valid time, return empty string
    if max_time == -1:
        return ""
    # Format the time string
    return f"{max_time // 60:02d}:{max_time % 60:02d}"


def backtrack(digits: List[int]) -> str:
    # Time complexity: O(1)
    # Space complexity: O(1)

    def is_valid_time(hh: int, mm: int) -> bool:
        if hh >= 24:
            return False
        if mm >= 60:
            return False
        return True

    def dfs(comb: List[int], counter: dict) -> None:

        # Base case
        if len(comb) == 4:
            hh = "".join(str(d) for d in comb[:2])
            mm = "".join(str(d) for d in comb[2:])
            if is_valid_time(int(hh), int(mm)):
                res.append(hh + mm)
            return

        # Loop over the available digits
        for num in counter:
            if counter[num] > 0:
                # Option 1
                comb.append(num)
                counter[num] -= 1
                dfs(comb, counter)

                # Option 2
                comb.pop()
                counter[num] += 1

    # List to store the valid times as strings (without `:`),
    # i.e.: "2315", "0838"
    res = list()
    counter = Counter(digits)
    dfs([], counter)
    if not res:
        # If no valid times obtained
        return ""

    # Maximum of the valid times (compare strings)
    time = max(res)
    return time[:2] + ":" + time[2:]


def backtrack2(digits: List[int]) -> str:
    # Time complexity: O(1)
    # Space complexity: O(1)

    def is_valid_time(hh: int, mm: int) -> bool:
        if hh >= 24:
            return False
        if mm >= 60:
            return False
        return True

    def build_time(digits: List[int]) -> int:
        hh = digits[0] * 10 + digits[1]
        mm = digits[2] * 10 + digits[3]
        if is_valid_time(hh, mm):
            return hh * 60 + mm
        return -1

    def swap(array: List[int], i: int, j: int) -> None:
        if i != j:
            array[i], array[j] = array[j], array[i]

    def permutate(array: List[int], start: int = 0):
        # Base case: `start` pointer reached the end of `array`
        # print('start', start)
        if start == n:
            time = build_time(array)
            if time != -1:
                res.append(time)
            return

        for index in range(start, n):
            # New candidate
            swap(array, index, start)
            # Explore
            permutate(array, start + 1)
            # Remove last candidate
            swap(array, index, start)

        return

    n = len(digits)
    max_time = -1
    res = []
    permutate(digits)
    for time in res:
        if time > max_time:
            max_time = time

    if max_time == -1:
        return ""
    return f"{max_time // 60:02d}:{max_time % 60:02d}"


if __name__ == "__main__":
    print("-" * 60)
    print("Largest time for given digits")
    print("-" * 60)

    test_cases = [
        ([0, 0, 0, 0], "00:00"),
        ([0, 0, 0, 2], "20:00"),
        ([9, 0, 0, 0], "09:00"),
        ([9, 5, 0, 0], "09:50"),
        ([9, 5, 0, 1], "19:50"),
        ([9, 5, 0, 8], "09:58"),
        ([1, 2, 3, 4], "23:41"),
        ([5, 2, 3, 4], "23:54"),
        ([5, 3, 4, 5], ""),
        ([3, 7, 2, 3], "23:37"),
    ]

    for digits, solution in test_cases:

        output = f"Digits: {digits}"
        print(output)

        result = python_permutations(digits)
        output = f"\t  python_permutations = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = backtrack(digits)
        output = f"\t            backtrack = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = backtrack2(digits)
        output = f"\t           backtrack2 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)
        print()
