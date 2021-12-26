"""
https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

You are given two strings s1 and s2 of equal length. A string swap is an 
operation where you choose two indices in a string (not necessarily 
different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing 
at most one string swap on exactly one of the strings. 
Otherwise, return false.

Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the 
last character of s2 to make "bank".

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string 
swap operation is required.
 
Constraints:
1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""
from typing import List
from collections import Counter


def solution1(s1: str, s2: str) -> str:
    # Time complexity: O(n)
    # Space complexity: O(n)

    count1, count2 = Counter(s1), Counter(s2)
    if count1 != count2:
        return False

    n = len(s1)
    diff = 0
    for i in range(n):
        if s1[i] != s2[i]:
            diff += 1
        if diff > 2:
            return False

    return diff == 0 or diff == 2


if __name__ == "__main__":
    print("-" * 60)
    print("Check if one string swap can make strings equal")
    print("-" * 60)

    test_cases = [
        ("kelb", "belk", True),
        ("kelb", "blek", False),
        ("kelb", "melb", False),
        ("kelb", "kelb", True),
        ("attack", "defend", False),
        ("bank", "kanb", True),
    ]

    for s1, s2, solution in test_cases:

        output = f"String 1: {s1}"
        output += f"\nString 2: {s2}"
        print(output)

        result = solution1(s1, s2)
        output = f"\tsolution1 = "
        output += " " * (10 - len(output))
        test_ok = solution == result
        output += str(result)
        output += " " * (55 - len(output))
        output += f'\t\tTest: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
