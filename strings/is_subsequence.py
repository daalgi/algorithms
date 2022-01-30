"""
https://leetcode.com/problems/is-subsequence/

Given two strings s and t, return true if s is a 
subsequence of t, or false otherwise.

A subsequence of a string is a new string that is 
formed from the original string by deleting some 
(can be none) of the characters without disturbing 
the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" 
while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, 
say s1, s2, ..., sk where k >= 109, and you want 
to check one by one to see if t has its subsequence. 
In this scenario, how would you change your code?
"""
from collections import defaultdict


def two_pointers(source: str, target: str) -> bool:
    # Time compleixty: O(t)
    # Space complexity: O(1)
    # where `t` is the length of `target`

    # Base case: the length of `source` can't
    # be greater than the length of `target`
    s, t = len(source), len(target)
    if s > t:
        return False

    # Loop over the characters of both strings
    i = j = 0
    while i < s and j < t:
        if source[i] == target[j]:
            i += 1
        j += 1
    # If the loop ended because the pointer of
    # `source` reached the end of the string,
    # `source` is subsequence of `target`
    return i == s


def hashmap(source: str, target: str) -> bool:
    # Time complexity: O(t + s)
    # Space complexity: O(t)
    # Solution to the follow-up question:
    # multiple `source` strings for a constant `target`

    s, t = len(source), len(target)
    if s > t:
        return False

    # Store the indices of the chars of `target`
    # in a hashmap, for O(1) look-up
    indices = defaultdict(list)
    for i in range(t):
        indices[target[i]].append(i)

    # Loop over the chars of `source`
    target_pointer = -1
    for i in range(s):
        # Check if the current char is in `target`
        if source[i] not in indices:
            return False

        # If the current char is in `target`,
        # but the largest index in `target` is
        # still smaller than the current `target_pointer`,
        # `source` is not a subsequence of `target`
        current_indices = indices[source[i]]
        if target_pointer >= current_indices[-1]:
            return False

        # Use binary search to optimize the look-up
        # of the left-most next `target_pointer`,
        # that is, find its smallest index which is greater
        # than the current `target_pointer`
        # (subsequence must respect the order in which the
        # characters appear)
        left, right = 0, len(current_indices) - 1
        while left < right:
            mid = (left + right) // 2
            if target_pointer < current_indices[mid]:
                right = mid
            else:
                left = mid + 1
        target_pointer = current_indices[right]

    return True


if __name__ == "__main__":
    print("-" * 60)
    print("Is subsequence")
    print("-" * 60)

    test_cases = [
        # (source, target, solution)
        ("", "", True),
        ("", "a", True),
        ("b", "", False),
        ("bear", "abcdeabrd", True),
        ("hello", "world", False),
        ("abc", "ahbgdc", True),
        ("axc", "ahbgdc", False),
        ("acb", "ahbgdc", False),
        ("aaaaaa", "bbaaaa", False),
    ]

    for source, target, solution in test_cases:

        print("Source:", source)
        print("Target:", target)

        result = two_pointers(source, target)
        output = f"      two_pointers = "
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        result = hashmap(source, target)
        output = f"           hashmap = "
        test_ok = solution == result
        output += str(result)
        output += " " * (50 - len(output))
        output += f'Test: {"OK" if test_ok else "NOT OK"}'
        print(output)

        print()
